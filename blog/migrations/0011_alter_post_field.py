# Generated by Django 3.2.8 on 2022-01-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field',
            field=models.IntegerField(choices=[(0, 'Frontend Design'), (1, 'Python Programmes'), (2, 'Django Development'), (3, 'Article')], default=0),
        ),
    ]
