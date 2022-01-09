from django.db.models import Manager


class SubscriberManager(Manager):

    def get_all(self):
        return self.filter(status='ON')
