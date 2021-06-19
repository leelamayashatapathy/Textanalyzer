#i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def analyze(request):
    djtext=(request.GET.get("text","default"))
    removepunc = (request.GET.get("removepunc", "off"))
    captext= (request.GET.get("captext", "off"))
    newlineremover = (request.GET.get("newlineremover", "off"))
    extraspaceremover = (request.GET.get("extraspaceremover", "off"))
    charcounter = (request.GET.get("charcounter", "off"))
    print(removepunc)
    print(djtext)
    if removepunc=="on":
    #analyzed=djtext
        punctuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        params={'purpose':'removed punctuation','analyzed_text':analyzed}
        return render(request,"analyze.html",params)
    elif (captext=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)
    elif (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="/n":
                analyzed=analyzed+char
        params = {'purpose': 'remove newline', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)
    elif (extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate (djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        return render(request, "analyze.html", params)
    elif (charcounter=="on"):
        count=0
        for i in range (0,len(djtext)):
            if (djtext[i] !=" "):
                count=count+1
        params = {'purpose': 'character counter', 'analyzed_text': str(count)}
        return render(request, "analyze.html", params)

    else:
        return HttpResponse("Error")


#def capitalfirst(request):
    #return HttpResponse("capitalize first")
#def newlineremove(request):
   # return HttpResponse("newlineremove")
#def spaceremove(request):
    #return HttpResponse("space remove")
#def charcounter(request):
    #return HttpResponse("charcount")
