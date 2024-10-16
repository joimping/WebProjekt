import xml.etree.ElementTree as ET
from django.shortcuts import render

# Create your views here.

def blog(reqest):

   # XML-Datei parsen
   tree = ET.parse('xml/data.xml')
   root = tree.getroot()

   # Daten extrahieren
   daten = []
   for auto in root:
      auto_daten = {}
      auto_daten['marke'] = auto.find('Automarke').text
      auto_daten['bezeichnung'] = auto.find('Autobezeichnung').text
      technische_details = auto.find('Technische_Details')
      auto_daten['leistung'] = technische_details.find('Leistung').text
      auto_daten['drehmoment'] = technische_details.find('max_Drehmomemt').text
      daten.append(auto_daten)

   # Daten ausgeben
   print(daten)

   if reqest.method == 'POST':
      print('Empfangen' , 'Name: ',reqest.POST['name'],'Text: ' , reqest.POST['text']) 
   return render(reqest, 'blogs.html')
