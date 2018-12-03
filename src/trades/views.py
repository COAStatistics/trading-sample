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
    res = requests.post(url, data=data, verify=False)
    ticket = res.text

    return render(request, 'sample.html', locals())
