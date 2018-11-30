from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

@xframe_options_exempt
def trade(request):
    return render(request, 'trade.html')
