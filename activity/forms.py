from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        # labels = {
        #     'user': '',
        #     'weapon': '',
        #     'site': '',
        #     'status': '',
        #     'start_time': '',
        #     'end_time': ''
        # }
        widgets = {
            'user': forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter  user...",
                    "style": "border-radius:50px",
                }
            ),
            'weapon': forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your weapon...",
                    "style": "border-radius:50px",
                }),
            'end_time': forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter  end time...",
                    "style": "border-radius:50px",
                }),
           'site':forms.Select(
                attrs={
                'class':"form-control",
                'placeholder':"Select groups",
                }
            ),
        }
