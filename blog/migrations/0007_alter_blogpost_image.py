# Generated by Django 4.1.1 on 2022-10-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpost_dislikes_blogpost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
