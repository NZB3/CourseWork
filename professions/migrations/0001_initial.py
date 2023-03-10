# Generated by Django 4.1.5 on 2023-01-22 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professions', to='directions.direction')),
            ],
            options={
                'verbose_name': 'Profession',
                'verbose_name_plural': 'Profession',
                'ordering': ['-title'],
            },
        ),
    ]
