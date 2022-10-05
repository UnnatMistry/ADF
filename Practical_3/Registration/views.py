from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy

class ContactCreate(CreateView):
    model = Contact
    fields=('first_name','last_name','username','email','password','contact','age')
    template_name="contact_create.html"