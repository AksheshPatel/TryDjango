# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import UserForm
# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()

	# if request.method == "POST":
	# 	print "title" + request.POST.get("content")
	# 	print request.POST.get("title")
	# 	#Post.objects.create(title=title)
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
#	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	context={
	"title":"Detail"
	}
	return render(request,"index.html",context)

def post_list(request):
	if request.user.is_authenticated():
		context={
				"title":" User List"
				}
	else:
		context={
				"title":"Not List"
				}
	return render(request,"index.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
