# Generated by Django 3.2 on 2021-04-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='\\static\\image\x0cood_default.jpg', max_length=500),
        ),
    ]