# Generated by Django 3.2.8 on 2022-01-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field',
            field=models.IntegerField(choices=[('Frontend Design', 'Frontend Design'), ('Python Programmes', 'Python Programmes'), ('Django Development', 'Django Development'), ('Article', 'Article')], default=0),
        ),
    ]
