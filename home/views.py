from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

def get_quotes():
    response=requests.get("https://goquotes-api.herokuapp.com/api/v1/random?count=1")
    json_file=json.loads(response.text)
    qut=json_file['quotes'][0]['text']
    aut=json_file['quotes'][0]['author']
    return {'quote':qut, 'author':aut}

# Create your views here.
def hello(request):
    return render(request, 'home/index.html', get_quotes())