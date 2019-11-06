# Generated by Django 2.0.13 on 2019-09-29 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_coursecontent_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontent',
            name='ClassAvailability',
        ),
        migrations.RemoveField(
            model_name='coursecontent',
            name='CourseDuration',
        ),
        migrations.RemoveField(
            model_name='coursecontent',
            name='DemoClass',
        ),
        migrations.RemoveField(
            model_name='coursecontent',
            name='Overview',
        ),
        migrations.RemoveField(
            model_name='coursecontent',
            name='TrainingMethodology',
        ),
        migrations.AddField(
            model_name='coursecontent',
            name='heading',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='coursename',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.SubCourse'),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
