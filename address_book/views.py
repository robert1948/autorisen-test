from django.shortcuts import render

def add_address(request):
    return render(request, 'add_address.html', {})

