# Generated by Django 3.1.3 on 2021-01-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AlterField(
            model_name='image',
            name='link',
            field=models.FileField(upload_to='uploads/image'),
        ),
    ]
