from django import forms

from mailer.models import Mailing


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('template', 'subscribers', 'send_date')
        labels = {
            'template': 'Шаблон',
            'subscribers': 'Подписчики',
            'send_date': 'Дата отправки',
        }
        widgets = {
            'template': forms.Select(attrs={
                'class': 'form-select'
            }),
            'subscribers': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'send_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пример: 12.10.2022 17:00 (оставь пустым, чтобы отправить прямо сейчас)'
            }),
        }
