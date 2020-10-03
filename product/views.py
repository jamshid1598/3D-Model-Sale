from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.views import View
from django.core.paginator import Paginator
from django.views.generic import (
    
)

# from django.contrib.auth.forms import  AuthenticationForm  # Now we can use 'LoginForm' instead of 'AuthenticationForm'
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError

from .models import (
    Category_3D,
    Info_Modul_3D,
    Modul_Format_3D,
)


# Create your views here.


class Info_Modul_3D_ListView(List)