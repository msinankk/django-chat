# Generated by Django 4.1.2 on 2023-07-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_alter_chatroom_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]