from django.shortcuts import render, HttpResponse
import wikipedia
# Create your views here.
def index(request):
    if request.method == 'POST':
        search = request.POST['search']
        try:
            result = wikipedia.summary(search,sentences = 100) #No of sentences that you want as output
        except:
            return HttpResponse("Wrong Input")
        return render(request,"index.html",{"result":result})
    return render(request,"index.html")