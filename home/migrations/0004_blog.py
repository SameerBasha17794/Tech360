# Generated by Django 2.0.13 on 2019-09-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_coursecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Blogs/')),
                ('author', models.CharField(max_length=1000)),
                ('published_on', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('News', 'News'), ('Business', 'Business'), ('Python', 'Python'), ('Java', 'Java'), ('Startup', 'Startup')], default='News', max_length=1000)),
                ('description', models.CharField(max_length=1000000000)),
                ('title', models.CharField(max_length=100000)),
            ],
        ),
    ]
