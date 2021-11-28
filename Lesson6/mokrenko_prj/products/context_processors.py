from .models import Category

def get_category_list(request):

    items = Category.objects.all()
    print('ITEMS=', items)
    context = {
        'categoryobjects': items
    }
    print('КОНТЕКСТ=', context)
    return context