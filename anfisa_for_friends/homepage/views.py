from django.shortcuts import render

from ice_cream.models import IceCream

from django.db.models import Q


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        is_published=True,
        is_on_main=True,
        category__is_published=True
    )
    # template = 'homepage/index.html'
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'description', 'wrapper__title'
    # ).filter(is_on_main=True, is_published=True).order_by('title')

    #                   IceCream.objects.values(
    #     'id', 'title', 'description'
    # ).filter(
    #     # Q(is_on_main=True)
    #     # & Q(is_published=True)
    #     # | Q(title__contains='пломбир')
    #     # & Q(is_published=True)
    #     is_published=True, is_on_main=True
    # ).order_by('title')[:3]

    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
