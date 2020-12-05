from .sub_models.Category import Category

def categories(request):
    category_list = Category.objects.filter()
    return {"categories":category_list}
