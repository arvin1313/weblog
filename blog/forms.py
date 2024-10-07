from django import forms
from .models import Message


# class ContactUsForm(forms.Form):
#     username = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(max_length=100, required=True)
#     message = forms.CharField(widget=forms.Textarea)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
