from django.shortcuts import redirect, render
# from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        # new_item_text = request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/test_list/')
    return render(request, 'home.html')

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()


def view_list(request):
    items = Item.objects.all()
    return render(
        request,
        'list.html',
        {'items': items},
    )
