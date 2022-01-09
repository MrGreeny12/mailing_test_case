import datetime
import json

from django.db.models import QuerySet
from django.core.exceptions import BadRequest
from django_celery_beat.models import PeriodicTask, ClockedSchedule

from mailer.models import MailTemplate, Mailing
from subscribe.models import Subscriber
from .tasks import send_offers_mail


def sending_router(template: MailTemplate, subscribers: QuerySet, send_date=None):
    '''
    Определяет тип письма и создаёт соответствующую задачу
    '''
    if template.mail_type == 0:
        if len(subscribers) == 1:
            subscribe: Subscriber = subscribers[0]
            recipient_list = list()
            now = datetime.datetime.now()
            age = now - subscribe.birthday
            recipient_list.append(subscribe.email)
            context = {
                'first_name': subscribe.first_name,
                'last_name': subscribe.last_name,
                'age': age.year
            }
            PeriodicTask.objects.create(
                clocked=ClockedSchedule.objects.create(clocked_time=subscribe.birthday),
                name=f'Mailing: Birthday, {template.title} - {subscribe.birthday}',
                task='mailing.tasks.send_birthday_mail',
                args=json.dumps([template.title, recipient_list, template.template_path, context]),
                one_off=True
            )
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=subscribe.birthday,
                status='SENDING'
            )
        else:
            raise BadRequest
    elif template.mail_type == 1:
        if send_date:
            for subscriber in subscribers:
                recipient_list = list()
                recipient_list.append(subscriber.email)
                PeriodicTask.objects.create(
                    clocked=ClockedSchedule.objects.create(clocked_time=send_date),
                    name=f'Mailing: Offer, {template.title} - {send_date}',
                    task='mailing.tasks.send_offers_mail',
                    args=json.dumps([template.title, recipient_list, template.template_path]),
                    one_off=True
                )
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=send_date,
                status='SENDING'
            )
        else:
            for subscriber in subscribers:
                recipient_list = list()
                recipient_list.append(subscriber.email)
                send_offers_mail.delay(
                    subject=template.title,
                    recipient_list=recipient_list,
                    template_name=template.template_path,
                )
            Mailing.active.create(
                template=template,
                subscribers=subscribers,
                send_date=send_date,
                status='SENDING'
            )
