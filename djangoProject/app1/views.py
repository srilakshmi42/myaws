from django.shortcuts import render,redirect
from app1.models import ProductModel

def showIndex(request):
    return render(request,"index.html")

def saveProduct(request):
    if request.method == "POST":

        name = request.POST.get("product_name")
        price = request.POST.get("product_price")
        photo = request.FILES["product_photo"]

        ProductModel(name=name,price=price,photo=photo).save()
        return redirect('main')

def viewProduct(request):
    return render(request, "index.html", {"product":ProductModel.objects.all()})

def delete(request,id):
    product_details = ProductModel.objects.get(number=id)
    if request.method == "POST":
        product_details.delete()
        return render(request, "index.html", {"product":ProductModel.objects.all()})
    else:
        return render(request, "delete.html", {"product_info": product_details})

