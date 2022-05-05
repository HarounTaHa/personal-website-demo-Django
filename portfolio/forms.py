from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'email'})
        self.fields['message'].widget.attrs.update({'class': 'form-control mb-3', 'placeholder': 'message'})

