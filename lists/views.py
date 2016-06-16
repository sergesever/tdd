from django.shortcuts import redirect, render
# from django.http import HttpResponse
from lists.models import Item
# import pdb


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(
        request,
        'list.html',
        {'items': items},
    )


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    # pdb.set_trace()
    return redirect('/lists/test_list/')
