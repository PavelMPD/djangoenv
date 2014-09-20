from django import forms
from filepicker.models import TestModel


class TestModelForm(forms.ModelForm):
    class Meta:
        model = TestModel