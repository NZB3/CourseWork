# Generated by Django 4.1.5 on 2023-01-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Direction',
                'verbose_name_plural': 'Directions',
                'ordering': ['-title'],
            },
        ),
    ]
