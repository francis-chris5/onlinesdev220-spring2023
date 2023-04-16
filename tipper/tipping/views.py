from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Greeting(request):
	page = "<html><body><h1>Hello World</h1></body></html>"
	return HttpResponse(page)


def otherGreeting(request):
	return render(request, "greet.html", {"title": "greetings", "message": "hello world"})



def calculateTip(request):
	return render(request, "tipInput.html")


def displayTip(request):
	price = float(request.GET["price"])
	service = float(request.GET["service"])
	service /= 100
	amount = price + price * service
	return render(request, "tipOutput.html", {"amount": format(amount, ".2f")})

















	 #### white space 