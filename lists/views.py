from django.shortcuts import redirect, render
from django.http import HttpResponse

from lists.models import Item

def home_page(request):

    # todo enable for multiple users & more than one list

    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/single-list/')