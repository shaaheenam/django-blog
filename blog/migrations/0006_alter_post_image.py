# Generated by Django 4.1.5 on 2023-01-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post-default.jpg', upload_to='post_images'),
        ),
    ]
