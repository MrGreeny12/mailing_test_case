from django.db import models

from mailer.managers import MailTemplateManager, MailingManager
from services.models_services import pkgen
from subscribe.models import Subscriber


class MailTemplate(models.Model):
    '''
    Модель хранения шаблонов
    '''
    class TemplateStatuses(models.TextChoices):
        ACTIVE = 'ON', 'Активен'
        ARCHIVE = 'OFF', 'В архиве'

    class MailTypes(models.IntegerChoices):
        BIRTHDAY = 1, 'Birthday'
        OFFERS = 2, 'Offers'

    id = models.CharField(max_length=10, unique=True, primary_key=True, default=pkgen)
    title = models.CharField(max_length=1024, verbose_name='Название шаблона')
    template_path = models.TextField(verbose_name='Путь к шаблону', help_text='Нужно внести путь к шаблону. Пример:'
                                                                              '"mailer/mail_templates/hello.html"')
    status = models.CharField(max_length=5, default='ON', choices=TemplateStatuses.choices, verbose_name='Статус')
    mail_type = models.IntegerField(default=1, choices=MailTypes.choices, verbose_name='Тип')

    active = MailTemplateManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Шаблон письма'
        verbose_name_plural = 'Шаблоны писем'
        db_table = 'male_templates'
        indexes = [
            models.Index(fields=['title']),
        ]


class Mailing(models.Model):
    '''
    Модель рассылки
    '''
    class MailingStatuses(models.TextChoices):
        CREATE = 'CREATE', 'Создана'
        SENDING = 'SENDING', 'Отправлена'
        RECEIVED = 'RECEIVED', 'Получена'

    id = models.CharField(max_length=10, unique=True, primary_key=True, default=pkgen)
    template = models.ForeignKey(
        MailTemplate,
        on_delete=models.CASCADE,
        related_name='mailings',
        verbose_name='Шаблон'
    )
    subscribers = models.ManyToManyField(
        Subscriber,
        verbose_name='Подписчики'
    )
    send_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, default='CREATE', choices=MailingStatuses.choices, verbose_name='Статус')

    active = MailingManager()

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
