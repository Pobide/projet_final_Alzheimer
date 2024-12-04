from django import forms

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    message = forms.CharField(
        label="Message", 
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=True
    )
    # Champs supplémentaires
    phone = forms.CharField(label="Téléphone", max_length=15, required=False)
    age = forms.IntegerField(label="Âge", required=False)
    gender = forms.ChoiceField(
        label="Genre",
        choices=[('M', 'Masculin'), ('F', 'Féminin'), ('O', 'Autre')],
        required=False
    )
    newsletter = forms.BooleanField(
        label="Souhaitez-vous recevoir notre newsletter ?",
        required=False
    )
