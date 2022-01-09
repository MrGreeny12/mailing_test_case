from django.contrib import admin

from mailer.models import MailTemplate, Mailing


@admin.register(MailTemplate)
class MailTemplateModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')


@admin.register(Mailing)
class MailingModelAdmin(admin.ModelAdmin):
    list_display = ('template', 'status')
