from django.shortcuts import render
from django.views import View

from mailer.forms import MailingForm
from mailer.services import sending_router


class CreateMailingView(View):
    '''
    Представление для выбора шаблона
    '''
    def get(self, request):
        form = MailingForm()
        context = {
            'form': form,
        }

        return render(request, 'mailer/base_templates/create_mailing.html', context)

    def post(self, request):
        form = MailingForm(request.POST or None)
        if form.is_valid():
            sending_router(
                template=form.cleaned_data.get('template'),
                subscribers=form.cleaned_data.get('subscribers'),
                send_date=form.cleaned_data.get('send_date') or None
            )

            return render(request, 'mailer/base_templates/success_create.html')
        else:
            form = MailingForm()
            context = {
                'form': form,
            }

            return render(request, 'mailer/base_templates/create_mailing.html', context)
