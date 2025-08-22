from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','comments']
        widgets = {
            'comments':forms.Textarea(attrs={'rows':4,'placeholder':'Enter your feedback..'}),
        }