from django.shortcuts import render

# Create your views here.

def blog(reqest):
    if reqest.method == 'POST':
       print('Empfangen' , 'Name: ',reqest.POST['name'],'Text: ' , reqest.POST['text']) #Hier XML Anbindung
    return render(reqest, 'blogs.html')
