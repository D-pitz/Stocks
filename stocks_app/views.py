from django.shortcuts import render, redirect
from login_app.models import User
from django.contrib import messages


def index(request):
    if 'user_id' in request.session:
        context={
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')

def display_user_account(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'user_account.html', context)

def display_stock_page(request):
    return render(request, 'stock_page.html')

