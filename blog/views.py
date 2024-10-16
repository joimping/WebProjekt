import xml.etree.ElementTree as ET
from django.shortcuts import render

# Create your views here.

def blog(reqest):
    


    if reqest.method == 'POST':
       print('Empfangen' , 'Name: ',reqest.POST['name'],'Text: ' , reqest.POST['text']) 
    return render(reqest, 'blogs.html')
