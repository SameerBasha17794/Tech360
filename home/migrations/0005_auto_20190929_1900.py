# Generated by Django 2.0.13 on 2019-09-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseimage',
            field=models.ImageField(default='', upload_to='CourseImages/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='content',
            field=models.CharField(default='', max_length=1000000000000),
            preserve_default=False,
        ),
    ]
