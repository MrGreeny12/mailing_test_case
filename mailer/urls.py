from django.urls import path

from mailer.views import CreateMailingView

urlpatterns = [
    path('create_mailing/', CreateMailingView.as_view(), name='create_mailing'),
]
