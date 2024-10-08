from django import forms
from django.forms import BooleanField, ModelForm

from mailings.models import Client, Message, Newsletter


class StyleFormMixin:
    """
     Форма для стализации
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)


class NewsletterForm(StyleFormMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].queryset = Message.objects.filter(owner=self.instance.owner)
        self.fields['client'].queryset = Client.objects.filter(owner=self.instance.owner)

    class Meta:
        model = Newsletter
        fields = ["name", "start_time", "end_time", "periodicity", "status", "message", "client"]
        widgets = {
            'start_time': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'periodicity': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.SelectMultiple(attrs={'class': 'form-control', 'multiple': True}),
        }


class NewsletterModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        fields = ('status',)
