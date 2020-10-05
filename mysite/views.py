# i have created this file.
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1>Hello!</h1> <a href="https://www.facebook.com/"> ClickforFacebook</a>''')
# def about(request):
#     return HttpResponse("Howdy?")
def index2(request):
    return render(request, 'index2.html')
    # return HttpResponse("Home")
def cottage(request):
    return render(request, "cottage.html")
def ex1(request):
    s ='''<h1>Navigation Bar</h1>
    <a href ="https://www.facebook.com/">Facebook</a><br>
    <a href = "https://www.youtube.com/">Youtube</a><br>'''
    return HttpResponse(s)
def newlineremover(request):
    return HttpResponse("NewLineRemover")

def spaceremover(request):
    return HttpResponse("spaceremover")

def analyze(request):
    djtext = request.POST.get('text', 'None')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    print(djtext)
    print(removepunc)
    if removepunc=="on":
        punctuatios = ''':/[-[\]{}()*+?.,\\^$|#'\]/, ";"\\$&"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuatios:
                analyzed = analyzed + char
        params = {'Purpose': 'Removed punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'Purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
             analyzed = analyzed + char
        params = {'Purpose': 'New Line Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(spaceremover=="on"):
        analyzed = ""
        for index, char  in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'Purpose': 'Space Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first <a href='/'> Back</a>")
