from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#we are going to include model so that view can use those models
from .models import Product, Sale
#We are going to include our filter so that can be  used our by views
from .filters import Product_filter

#iclude modelform created in the form file
from .forms import Addform, SaleForm
#Handlling redirection after deletion
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
################################################################################

#################################################################################
# Create your views here.
@login_required
def index(request):
    products = Product.objects.all().order_by('-id')
    products_filter = Product_filter(request.GET, queryset = products)
    products = products_filter.qs 
    return render(request, 'products/index.html', {'products':products,'products_filter': products_filter})

@login_required
def home(request):
    return render(request, 'products/aboutDrkalimunda.html')

@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def issued_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)

    if request.method == 'POST':
        #check if required input is as is supposed to be
        if sales_form.is_valid():
            new_sales = sales_form.save(commit = False)
            new_sales.item = issued_item
            new_sales.unit_price = issued_item.unit_price
            new_sales.save()
            #to keep track of remainding stock aftr sale
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)

            return redirect('reciept')
    return render(request, 'products/issued_item.html', {'sales_form': sales_form})
@login_required
def reciept(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'products/reciept.html', {'sales': sales})


@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id = pk)
    form = Addform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            add_quantity = int(request.POST['recieved_quantity'])
            issued_item.total_quantity += add_quantity
            issued_item.save()
            #to add to the remaining stock as quantity is reducing
            print(add_quantity)
            print(issued_item.total_quantity)
            return redirect('index')
        messages.success(request, "You Have added to stock!")
    return render(request, 'products/add_to_stock.html',{'form':form})



@login_required
def all_sales(request, user_id):
    sales = Sale.objects.all()
    total = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    vat = round((total * 0.18) * 100, 2)
    user = User.objects.get(id = user_id)
    return render(request, 'products/all_sales.html', {
        'sales':sales,
        'total': total,
        'change': change,
        'net':net,
        'vat':vat,
        'user':user
    })


@login_required
def reciept_detail(request, reciept_id):
    reciept = Sale.objects.get(id = reciept_id)
    date = Sale.objects.all().order_by()
    return render(request, 'products/reciept_detail.html', {'reciept': reciept, 'date':date})


@login_required
def delete_item(request, product_id):
    delete = Product.objects.get(id = product_id)
    delete.delete()
    messages.success(request, "Deleted successfully")
    return HttpResponseRedirect(reverse('index', messages))