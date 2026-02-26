from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farming', '0004_community_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitypost',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='community/'),
        ),
        migrations.AlterField(
            model_name='farmerquery',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='farmerquery',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='farmerquery',
            name='category',
            field=models.CharField(default='pest', max_length=20, choices=[('wildlife', 'Wildlife'), ('pest', 'Pest & Insect'), ('weed', 'Weed')]),
        ),
    ]
