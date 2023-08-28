from django import forms

class AdvertsForm(forms.Form):
            title = forms.CharField(max_length=64,
            widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg'}))
            content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control form-control-lg'}))  
            photo= forms.ImageField(widget=forms.FileInput(attrs={'class' : 'form-control form-control-lg'}))
            price = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}))
            category = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}))
            location= forms.CharField( max_length=255, widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg'})) 
            auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class' : 'form-cgeck-input'}))
   