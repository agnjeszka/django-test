from django import forms

from .models import Zamowienie

class ZamowienieForm(forms.ModelForm):
    class Meta:
        model = Zamowienie
        fields = ['l1', 'l2']

    def clean_listwa1(self):
        print(self.cleaned_data.get('l1'))
        return "666"
