from django.db import models

from services.models_services import pkgen
from subscribe.managers import SubscriberManager


class Subscriber(models.Model):
    '''
    Модель подписчика
    '''
    class SubscriberStatuses(models.TextChoices):
        ACTIVE = 'ON', 'Активен'
        ARCHIVE = 'OFF', 'В архиве'

    id = models.CharField(max_length=10, unique=True, primary_key=True, default=pkgen)
    first_name = models.CharField(max_length=512, verbose_name='Имя')
    last_name = models.CharField(max_length=512, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email адрес')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    status = models.CharField(max_length=5, default='ON', choices=SubscriberStatuses.choices, verbose_name='Статус')

    active = SubscriberManager()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        db_table = 'subscriber'
        indexes = [
            models.Index(fields=['email']),
        ]
