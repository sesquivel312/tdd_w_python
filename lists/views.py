from django.shortcuts import redirect, render
from django.http import HttpResponse

from lists.models import Item

def home_page(request):

    # todo enable for multiple users & more than one list

    if request.method == 'POST':  # I assume as opposed to the GET resulting from just visiting the page
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/single-list')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})