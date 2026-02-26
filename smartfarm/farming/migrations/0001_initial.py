from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('wildlife', 'Wildlife'), ('pest', 'Pest & Insect'), ('weed', 'Weed')], max_length=20)),
                ('description', models.TextField()),
                ('affected_crops', models.CharField(max_length=500)),
                ('prevention_methods', models.TextField()),
                ('treatment', models.TextField()),
                ('season', models.CharField(default='All seasons', max_length=100)),
                ('severity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], default='medium', max_length=20)),
                ('icon', models.CharField(default='🐛', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['category', 'name']},
        ),
        migrations.CreateModel(
            name='CropTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('crop_type', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='FarmerQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField()),
                ('crop', models.CharField(max_length=200)),
                ('problem', models.TextField()),
                ('category', models.CharField(choices=[('wildlife', 'Wildlife'), ('pest', 'Pest & Insect'), ('weed', 'Weed')], max_length=20)),
                ('answered', models.BooleanField(default=False)),
                ('answer', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Farmer Queries'},
        ),
    ]
