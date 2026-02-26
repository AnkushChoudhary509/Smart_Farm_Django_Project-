from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_expert(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    # Create expert user with hashed password
    if not User.objects.filter(username='AnkushChoudhary').exists():
        User.objects.create(
            username='AnkushChoudhary',
            password=make_password('Jatts23@aR'),
            first_name='Ankush',
            last_name='Choudhary',
            email='expert@smartfarm.in',
            is_staff=False,
            is_active=True,
        )

def reverse_expert(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='AnkushChoudhary').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('farming', '0007_post_comment'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]
    operations = [
        migrations.RunPython(create_expert, reverse_expert),
    ]
