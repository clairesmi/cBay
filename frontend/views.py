import os
from django.shortcuts import render
# Create your views here.
from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound

# Home view opens the index.html file located in the dist folder and sends it back to the client
class Home(View):
    def get(self, _request): # underscore - request can still be passed to the function even if it is not used
        with open(os.path.join(os.path.dirname(__file__), 'dist', 'index.html')) as file:
            return HttpResponse(file.read())


# The Assets view attempts to find the requested file in the dist folder. 
# If found it will send it back to the client, if not a 404 response will be sent
class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'dist', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read())
        return HttpResponseNotFound
