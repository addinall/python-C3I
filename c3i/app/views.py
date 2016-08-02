# from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world - You are in the Python version of C3I")

