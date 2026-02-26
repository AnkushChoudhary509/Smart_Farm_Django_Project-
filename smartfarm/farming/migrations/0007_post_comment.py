from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('farming', '0006_chat_farmer_sms'),
    ]
    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='farming.communitypost')),
                ('name', models.CharField(default='Anonymous Farmer', max_length=200)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('content', models.TextField()),
                ('is_expert', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='farming.postcomment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={'ordering': ['created_at']},
        ),
    ]
