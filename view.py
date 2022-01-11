# this is created by sadhana
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
   # return HttpResponse("I love magiee home page")

def analyze(request):
    #get the text
    djtext= request.POST.get('text','default')

    #check checkbox values
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    countletter=request.POST.get('countletter', 'off')

    if removepunc == "on":
        #analyzed=djtext
         punctuations=''' !()-[]{};:'"\,<>./?@#$%^&?*_~ '''
         analyzed = ""
         for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char


         params={'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
         djtext = analyzed
        #analaze the text
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params={'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if(char != '\n' and char !='\r'):
                analyzed = analyzed + char

        params = {'purpose': 'Line remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (countletter == "on"):
        count=0;
        for char in djtext:
            if(char.isalpha()):
                count=count+1;

        params = {'purpose': 'to count the letter', 'analyzed_text': count}
        return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and countletter !="on"):
        return HttpResponse("Please select the operation ")         #for text

    return render(request, 'analyze.html', params)