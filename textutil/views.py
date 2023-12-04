# i have created this file self

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    text1=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    
    print(removepunc)
    print(text1)
    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in text1:
            if char not in punctuations:
                analyzed=analyzed+char
        abdul1={'purpose':'remove punctuation','analyzed_text':analyzed}
        analyzed=text1
       
    if(fullcaps=='on'):
        analyzed=""
        for char in text1:
            analyzed=analyzed+char.upper()
        abdul1={'purpose':'Change to uppercase','analyzed_text':analyzed}
        analyzed=text1
       
    if(newlineremover=='on'):
        analyzed=""
        for char in text1:
            if char !="\n" and char!="\r":
               analyzed=analyzed+char
        abdul1={'purpose':'Remove NewLines','analyzed_text':analyzed}
        analyzed=text1
        
    if(extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate (text1):
            if not (text1[index] == '' and text1[index+1]==''):
               analyzed=analyzed+char
        abdul1={'purpose':'Remove NewLines','analyzed_text':analyzed}
        analyzed=text1
       
    if(charcount=='on'):
        # analyzed="the total number of character is "+str(len(text1))
        analyzed=""
        total = 0
        for char in text1:
           if char == " ":
               continue
           total+=1
        analyzed=analyzed+char
        analyzed=total
        abdul1={'purpose':'the total number of character is ','analyzed_text':analyzed}
        
    if (removepunc !="on" and fullcaps !="on" and newlineremover !="on" and extraspaceremover !="on" and charcount !="on"):
        return HttpResponse("please select atleast one of them ")
    return render (request,'analyze.html',abdul1)
    