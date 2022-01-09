import logging

from django.core.mail import send_mail
from django.template.loader import get_template

from project_config.celery import app


@app.task
def send_offers_mail(subject: str, recipient_list: list, template_name: str, context: dict = None) -> None:
    '''
    Отправка рассылки с рекламными предложениями
    '''
    try:
        send_mail(
            subject=subject, message=None, from_email=None, recipient_list=recipient_list, fail_silently=True,
            html_message=get_template(template_name=template_name).render(context)
        )
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.info(e)


@app.task
def send_birthday_mail(subject: str, recipient_list: list, template_name: str, context: dict) -> None:
    '''
    Отправка сообщения с поздравлением на день рождения

    Note: список должен состоять из 1-го адреса
    '''
    try:
        send_mail(
            subject=subject, message=None, from_email=None, recipient_list=recipient_list, fail_silently=True,
            html_message=get_template(template_name=template_name).render(context)
        )
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.info(e)
