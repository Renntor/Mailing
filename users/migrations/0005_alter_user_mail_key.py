# Generated by Django 4.2.4 on 2023-09-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_mail_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail_key',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='key'),
        ),
    ]