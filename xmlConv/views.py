from django.shortcuts import render, get_object_or_404
from .models import Customers, Orders, Files
from django.views.generic import CreateView

import xml.etree.ElementTree as ET
from collections import defaultdict

# Create your views here.

#class to get the xml file
class XMLtoTable(CreateView):
    model = Files
    template_name = 'xmlConv/xmltopdf.html'
    fields = ['xmlfile']


#class to convert xml to defaultdict

#