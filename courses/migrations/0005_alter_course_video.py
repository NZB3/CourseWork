# Generated by Django 4.1.5 on 2023-01-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
