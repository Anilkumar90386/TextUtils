from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'ind.html')
def analyze(request):
    text1=request.GET.get('text','default')
    punctuations='''!{}-[;;:]"/'''
    analyzed=""
    remove=request.GET.get('removepunc','off')
    #convert_to_upper1=request.GET.get('convert_to_upper','off')

    if remove=='on':
        for char in text1:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Swithced")
def convert(request):
    if convert_to_upper1=="on":
        if text1.islower():
            for char in text1:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': 'removed Punctuations', 'analyzed_text': analyzed.upper()}
            return render(request, 'analyze.html', params)
        else:
            params = {'purpose': 'removed Punctuations', 'analyzed_text': 'Already in upper'}
            return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Switch the button")



