# Generated by Django 3.2.5 on 2021-08-23 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20210823_0149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
