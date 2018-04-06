from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def profile(request, pk=None):
    if pk:   #pk = id  pk ist unabhaengiger vom eigentlichen Primaerschluesselfeld, d. h. man muss sich nicht darum kuemmern, ob das Primaerschluesselfeld "id" oder "object_id" oder was auch immer heisst.
        user = User.object.get(pk=pk)
    else:
        user = request.user
    args = {'user': user} 
    return render(request, ('benutzeraccounts/profile.html'), args)
