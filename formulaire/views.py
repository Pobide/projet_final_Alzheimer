from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
import csv
import os

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # Vérifiez si le formulaire est valide
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            newsletter = form.cleaned_data['newsletter']
    
    # Enregistrement des données dans un fichier CSV
            with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([name, email, message, phone, age, gender, newsletter])


            # Rediriger ou afficher un message de succès
            return render(request, 'thank_you.html', {'name': name})
        
        else:
            # Si le formulaire n'est pas valide
            print("Formulaire invalide")
            print(form.errors)  # Affiche les erreurs dans le terminal pour débogage

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

