from django.http import HttpResponse
from django.shortcuts import render

from fahanda.models import Index, New, Project, Product, About, Contact 

def index(request):
	my_index = Index.objects.all()
	context = {'my_index':my_index}
	return render(request, 'fahanda/index.html', context)

def new(request):
	news_title = New.objects.get(pk=1)
	news_text = New.objects.get(pk=2)
	return HttpResponse(news_title,news_text)

def project(request):
	current_projects = Project.objects.all()
	return HttpResponse(current_projects)

def products(request):
	list_products = Product.objects.order_by("created")[:5]
	context = {'list_products':list_products}
	return render(request, 'fahanda/products.html', context)

def about(request):
	about = About.objects.all()
	return HttpResponse(about)

def contact(request):
	contacts = Contact.objects.all()
	return HttpResponse(contacts)