from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
        return HttpResponse('Данные успешно отправлены')
    else:
        return render(request, 'contacts.html')
