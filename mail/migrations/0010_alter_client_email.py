# Generated by Django 4.2.4 on 2023-09-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0009_alter_settingmail_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='почта'),
        ),
    ]
