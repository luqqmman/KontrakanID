# Generated by Django 4.1.5 on 2023-05-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Laki-laki'), ('Female', 'Perempuan')], max_length=10),
        ),
    ]
