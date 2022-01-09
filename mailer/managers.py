from django.db.models import Manager


class MailTemplateManager(Manager):

    def get_all(self):
        return self.filter(status='ON')


class MailingManager(Manager):
    ...
