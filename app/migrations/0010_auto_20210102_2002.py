# Generated by Django 3.1.3 on 2021-01-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210102_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(default='oui', upload_to='app/static/uploads/image'),
        ),
    ]