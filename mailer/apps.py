from django.apps import AppConfig


class MailerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Отправка писем'
    name = 'mailer'
