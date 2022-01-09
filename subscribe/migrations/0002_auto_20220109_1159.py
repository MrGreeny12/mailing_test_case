# Generated by Django 3.2.7 on 2022-01-09 11:59

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='subscriber',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='subscriber',
            name='status',
            field=models.CharField(choices=[('ON', 'Активен'), ('OFF', 'В архиве')], default='ON', max_length=5, verbose_name='Статус'),
        ),
    ]
