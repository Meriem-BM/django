# Generated by Django 3.2.8 on 2021-12-21 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to='templates/blogs/', validators=[django.core.validators.FileExtensionValidator(['html'])]),
        ),
    ]