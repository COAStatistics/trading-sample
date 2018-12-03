from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

import requests

# Create your views here.

@xframe_options_exempt
def trade(request):
    return render(request, 'trade.html')

def sample(request):
    url = 'https://tableau.mlozo.com/trusted'
    data = {
        'username': 'viewer'
    }
    ticket = []
    res = requests.post(url, data=data, verify=False)
    ticket.append(res.text)
    res = requests.post(url, data=data, verify=False)
    ticket.append(res.text)

    return render(request, 'sample.html', locals())
