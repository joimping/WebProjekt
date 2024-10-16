from django.shortcuts import render

# Create your views here.

def blog(reqest):
    if reqest.method == 'POST':
       print('Empfangen', reqest.POST['itemName']) 
    return render(reqest, 'blogs.html')
