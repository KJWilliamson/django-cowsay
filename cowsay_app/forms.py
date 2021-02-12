# from cowsay_app.models import Cowsay
# from django import forms
#
#
# class CowsayForm(forms.Form):
#     model = Cowsay
#     cowsays = forms.CharField(max_length=200)

from cowsay_app.models import Cowsay
from django import forms

class CowsayForm(forms.ModelForm):
    class Meta:
        model = Cowsay
        fields = '__all__'
