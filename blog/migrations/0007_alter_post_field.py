# Generated by Django 3.2.8 on 2022-01-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220114_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field',
            field=models.IntegerField(choices=[('Frontend Design', 'Frontend Design'), ('Python Programmes', 'Python Programmes'), ('Django Development', 'Django Development'), ('Article', 'Article')], default=0),
        ),
    ]
