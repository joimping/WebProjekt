import xml.etree.ElementTree as ET
from django.shortcuts import render

# Create your views here.

def blog(reqest):

   # XML-Datei parsen
   tree = ET.parse('xml/data_copy.xml')
   root = tree.getroot()

   # Daten extrahieren
   blog_daten = []
   for auto in root:
      auto_daten = {}
      auto_daten['marke'] = auto.find('Automarke').text
      auto_daten['bezeichnung'] = auto.find('Autobezeichnung').text
      technische_details = auto.find('Technische_Details')
      auto_daten['leistung'] = technische_details.find('Leistung').text
      auto_daten['drehmoment'] = technische_details.find('max_Drehmomemt').text
      blog_daten.append(auto_daten)

   # Daten ausgeben
   #print((blog_daten[1]) ['marke']) 



   if reqest.method == 'POST':
      print('Empfangen' , 'Name: ',reqest.POST['name'],'Text: ' , reqest.POST['text']) 
   return render(reqest, 'blogs.html', {'blog_daten': blog_daten})
