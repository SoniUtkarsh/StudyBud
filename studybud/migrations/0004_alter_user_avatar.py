# Generated by Django 5.0.6 on 2024-05-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybud', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/images/avatar.svg', null=True, upload_to=''),
        ),
    ]
