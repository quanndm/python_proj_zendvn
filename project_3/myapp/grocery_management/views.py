from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Product
# Create your views here.
def create_product(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        price_purchase = float(request.POST.get('purchase_price'))
        price_sale = float( request.POST.get('selling_price'))
        quantity = request.POST.get('quantity')

        product = Product(name=name, price_purchase=price_purchase, price_sale=price_sale, quantity=quantity)
        product.save()

        messages.success(request, 'Sản phẩm tạo mới thành công!')
        return redirect('/products/list/')
    
    return render(request, 'create.html', {})

def list_products(request: HttpRequest):
    products = Product.objects.all()

    total_revenue = sum(product.price_sale * product.quantity_sold for product in products)
    total_profit = sum((product.price_sale - product.price_purchase) * product.quantity_sold for product in products)


    return render(request, 'list.html', {
        'products': products,
        'total_revenue': total_revenue,
        'total_profit': total_profit
    })

def update_product(request: HttpRequest, product_id: int):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price_purchase = float(request.POST.get('purchase_price'))
        product.price_sale = float( request.POST.get('selling_price'))
        product.quantity = request.POST.get('quantity')
        product.save()

        messages.success(request, 'Sản phẩm cập nhật thành công!')
        return redirect('/products/list/')
    return render(request, 'update.html', {
        'product': product
    })

def delete_product(request: HttpRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    product.delete()

    messages.success(request, 'Sản phẩm xóa thành công!')
    return redirect('/products/list/')

def sell_product(request: HttpRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    quantity_sold = request.GET.get('quantity')
        
    if int(quantity_sold) > product.quantity:
        messages.error(request, 'Số lượng bán ra không được lớn hơn số lượng tồn kho!')
        return redirect('/products/list/')
    
    product.quantity_sold += int(quantity_sold)
    product.quantity -= int(quantity_sold)
    product.save()

    messages.success(request, 'Sản phẩm bán thành công!')
    return redirect('/products/list/')