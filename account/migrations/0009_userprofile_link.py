# Generated by Django 4.1.5 on 2023-05-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_userprofile_gender_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='link',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
