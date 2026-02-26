from django.db import models
import os


class ThreatCategory(models.TextChoices):
    WILDLIFE = 'wildlife', 'Wildlife'
    PEST = 'pest', 'Pest & Insect'
    WEED = 'weed', 'Weed'


class Threat(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=ThreatCategory.choices)
    description = models.TextField()
    affected_crops = models.CharField(max_length=500)
    prevention_methods = models.TextField()
    treatment = models.TextField()
    season = models.CharField(max_length=100, default='All seasons')
    severity = models.CharField(max_length=20, choices=[
        ('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')
    ], default='medium')
    icon = models.CharField(max_length=10, default='🐛')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['category', 'name']


class CropTip(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    crop_type = models.CharField(max_length=100)
    season = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class FarmerQuery(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    crop = models.CharField(max_length=200)
    problem = models.TextField()
    category = models.CharField(max_length=20, choices=ThreatCategory.choices, default='pest')
    answered = models.BooleanField(default=False)
    answer = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.crop}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Farmer Queries'


def community_photo_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f'community/{instance.pk or "new"}_{filename}'


class CommunityPost(models.Model):
    CATEGORY_CHOICES = [
        ('question', 'Question'),
        ('tip', 'Tip / Experience'),
        ('success', 'Success Story'),
        ('warning', 'Warning / Alert'),
        ('photo', 'Photo Post'),
    ]
    name = models.CharField(max_length=200, default='Anonymous Farmer')
    state = models.CharField(max_length=100, blank=True, default='')
    crop = models.CharField(max_length=200, blank=True, default='')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='question')
    content = models.TextField()
    photo = models.ImageField(upload_to='community/', blank=True, null=True)
    photo_description = models.CharField(max_length=500, blank=True, default='')
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.category} ({self.created_at.date()})"


class FarmerProfile(models.Model):
    """Registered farmers who can receive SMS alerts"""
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, unique=True)
    state = models.CharField(max_length=100, blank=True, default='')
    crop = models.CharField(max_length=200, blank=True, default='')
    village = models.CharField(max_length=200, blank=True, default='')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        ordering = ['-created_at']


class ChatRoom(models.Model):
    """Direct 1-to-1 chat session between farmer and expert"""
    farmer_name = models.CharField(max_length=200)
    farmer_phone = models.CharField(max_length=15, blank=True, default='')
    expert_name = models.CharField(max_length=200, default='Agricultural Expert')
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Chat: {self.farmer_name} ({self.created_at.date()})"

    class Meta:
        ordering = ['-created_at']


class ChatMessage(models.Model):
    SENDER_CHOICES = [('farmer', 'Farmer'), ('expert', 'Expert')]
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    sender_name = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender_name}: {self.message[:50]}"

    class Meta:
        ordering = ['created_at']


class SMSAlert(models.Model):
    """SMS alerts sent by admin/expert to registered farmers"""
    STATUS_CHOICES = [('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')]
    title = models.CharField(max_length=200)
    message = models.TextField()
    sent_by = models.CharField(max_length=200, default='Agricultural Expert')
    target = models.CharField(max_length=50, default='all',
        help_text='all / state:Punjab / crop:wheat')
    recipients_count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.status})"

    class Meta:
        ordering = ['-created_at']


class PostComment(models.Model):
    """Comments on community posts"""
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, default='Anonymous Farmer')
    state = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    is_expert = models.BooleanField(default=False)  # True if posted by verified expert
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.name} on post {self.post_id}"
