from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming', '0003_full_india_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous Farmer', max_length=200)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('crop', models.CharField(blank=True, default='', max_length=200)),
                ('category', models.CharField(
                    choices=[('question','Question'),('tip','Tip / Experience'),('success','Success Story'),('warning','Warning / Alert'),('photo','Photo Post')],
                    default='question', max_length=20
                )),
                ('content', models.TextField()),
                ('photo_description', models.CharField(blank=True, default='', max_length=500)),
                ('likes', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
