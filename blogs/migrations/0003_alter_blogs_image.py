# Generated by Django 5.1 on 2024-09-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='blogs/static/blogs/uploads'),
        ),
    ]
