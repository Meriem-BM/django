# Generated by Django 3.2.8 on 2022-01-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='field',
            field=models.IntegerField(choices=[('frontend_design', 'Frontend Design'), ('python_programmes', 'Python Programmes'), ('django_pevelopment', 'Django Development'), ('Article', 'Article')], default=0),
        ),
    ]
