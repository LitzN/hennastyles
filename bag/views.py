from django.shortcuts import render, redirect, reverse, HttpResponse, \
     get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ View to return shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']

    bag = request.session.get('bag', {})

    if colour:
        if item_id in list(bag.keys()):
            if colour in bag[item_id]['items_by_colour'].keys():
                bag[item_id]['items_by_colour'][colour] += quantity
                messages.success(request, f'Updated {colour} {product.name} \
                    quantity of your bag!')
            else:
                bag[item_id]['items_by_colour'][colour] = quantity
                messages.success(request, f'Added {colour}-{product.name} \
                     to your bag')
        else:
            bag[item_id] = {'items_by_colour': {colour: quantity}}
            messages.success(request, f'Added {colour}-{product.name} \
                to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity \
                 to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']

    bag = request.session.get('bag', {})

    if colour:
        if quantity > 0:
            bag[item_id]['items_by_colour'][colour] = quantity
            messages.success(request, f'Updated {colour} {product.name} \
                quantity of your bag!')
        else:
            del bag[item_id]['items_by_colour'][colour]
            if not bag[item_id]['items_by_colour']:
                bag.pop(item_id)
            messages.success(request, f'Removed {colour}-{product.name} from \
                 your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} \
                quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ """
    try:
        product = get_object_or_404(Product, pk=item_id)
        colour = None
        if 'product_colour' in request.POST:
            colour = request.POST['product_colour']

        bag = request.session.get('bag', {})

        if colour:
            del bag[item_id]['items_by_colour'][colour]
            if not bag[item_id]['items_by_colour']:
                bag.pop(item_id)
            messages.success(request, f'Removed {colour}-{product.name} from \
                 your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
