# I have create this file - SJ

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("SJs First Django Site")


def home(request):
    return render(request, 'home.html')


def process_text(request):
    input_text = request.GET.get('text', 'default')
    removespace = request.GET.get('removespace', 'off')
    charcount = request.GET.get('charcount', 'off')
    capitialize = request.GET.get('capitialize', 'off')


    if(removespace == 'on'):
        processed_text = input_text.replace(' ', '')
        params = {'purpose': 'Remove Space', 'processed_text': processed_text}
        return render(request, 'process.html', params)
    elif(charcount == 'on'):
        processed_text = len(input_text)
        params = {'purpose': 'Count Characters', 'processed_text': processed_text}
        return render(request, 'process.html', params)
    elif(capitialize == 'on'):
        processed_text = ''
        for char in input_text:
            processed_text = processed_text + char.upper()
        params = {'purpose': 'Capitialize Characters', 'processed_text': processed_text}
        return render(request, 'process.html', params)
    else:
        return HttpResponse("Something Is Not Right.....<a href = '/'>Back To Home</a>")
