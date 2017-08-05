from django.shortcuts import render, get_object_or_404
from .models import DemoCategory, Demo, Message

def index(request):
	return render(request, 'main/index.html')

def academia(request):
	return render(request, 'main/academia.html')

def dev(request):
	categories = DemoCategory.objects.all()
	context = {'categories': categories,}
	return render(request, 'main/dev.html', context)

def demo(request, demo_id):
	demo = get_object_or_404(Demo,pk=demo_id)
	context = {'demo':demo,}
	return render(request, 'main/demo.html', context)

def fun(request):
	return render(request, 'main/fun.html')

def contact(request):
	return render(request, 'main/contact.html')

def message(request):
	msg = Message(sender=request.POST.get('sender', 'anon'), contact_info=request.POST.get('contact_info','anon'), content=request.POST.get('content','empty'))
	msg.save()
	return render(request, 'main/contact.html', {'sent': True,})