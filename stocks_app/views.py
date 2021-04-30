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
        # user_stock: stock linked by the buy order
            #dislpays on html if owned is True
        # user_sale: sales linked to User
        # follows: linked by Stock to User
        # other keys will = math done by related classes
    }
    return render(request, 'user_account.html', context)

def display_stock_page(request):
    # contexts will = stock info
    return render(request, 'stock_page.html')

def buy_page(request):
    context = {
        'shares': request.POST['shares']
        # context = neccessary stock info
    }
    return render(request, 'buy_page.html', context)

# def buy(request, stock_id):
#   Buy.objects.create(
#   ...create buy_order
#   assign one to manys to user_id and stock_id
#   )
# redirects to user_account page

def sell_page(request):
    context = {
        'shares': request.POST['shares']
        # context will = all active buy orders accosiated with this stock
    }
    return render(request, 'sell_page.html', context)

# def sell(request, buy_order_id):
#   if checks to make sure the buy order does not go below 0
#   create sell order...
#   if user sells all stock in buy order owned = False
#   buy_order.current_value - shares * current price
#   save()

# def follow(request, stock_id):
#   user_id assignt to stock.follow

