from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):

    response_string = b'<html><title>To-Do lists</title><body>hooray</body></html>'

    response = HttpResponse()
    response.content = response_string

    return response
