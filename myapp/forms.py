from django import forms

# ModelForm: MenuForm
class MenuForm(forms.Form):
    item_name = forms.CharField(max_length = 200)
    category = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000)
    price = forms.DecimalField(max_digits = 10, decimal_places = 2)
