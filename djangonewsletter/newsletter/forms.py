from django import forms
from .models import NewsletterSignup


class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        """Uses the Signup model."""
        model = NewsletterSignup
        fields = ('full_name', 'email', 'postcode',)

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name*',
            'email': 'Email Address*',
            'postcode': 'Postal Code*'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
