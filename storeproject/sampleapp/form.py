from django import forms
from .models import detail

class detailform(forms.ModelForm):
    class Meta:
        model = detail
        fields = ['name', 'dob', 'age','gender','phone' ,'email', 'address','department','course','purpose','materials']