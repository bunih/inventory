from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        labels = {
            'user': '',
            'weapon': '',
            'site': '',
            'status': '',
            'start_time': '',
            'end_time': ''
        }
        widgets = {
            'user': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Title...",
                    "style": "border-radius:50px",
                }
            ),
            'weapon': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Title...",
                    "style": "border-radius:50px",
                }
            ),
        }
