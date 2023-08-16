from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
def number(request):
    urls = request.GET.getlist('url')
    resp = {}
    numbers_list = []
    for url in urls:
        response = requests.get(url)
        if response.status_code==200:
            data = response.json()
            print(data)
            numbers_list.extend(data.get('numbers' , []))
    numbers_list = sorted(set(numbers_list))
    resp = {"numbers" : numbers_list}
    return JsonResponse(resp)
