from django.contrib import admin

from subscribe.models import Subscriber


@admin.register(Subscriber)
class SubscriberModelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
