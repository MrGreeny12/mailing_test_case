# Generated by Django 3.2.7 on 2022-01-09 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaleTemplate',
            new_name='MailTemplate',
        ),
    ]