from django.views.generic import TemplateView, ListView, DetailView

from app.models import Product, Tag

itemPerPages = 3

class IndexView(ListView):
    template_name = "Product/list.html"
    paginate_by = itemPerPages

    def get_queryset(self):
        return Product.objects.all().order_by('-id')  # order_by('tags__name')


class ProductView(DetailView):
    template_name = "product/detail.html"
    model = Product


class LikeView(ListView):
    template_name = "Product/list.html"
    paginate_by = itemPerPages

    def get_queryset(self):
        return Product.objects.all().order_by('-like')  # order_by('tags__name')


class CroissantView(ListView):
    template_name = "Product/list.html"
    paginate_by = itemPerPages

    def get_queryset(self):
        return Product.objects.all().order_by('price')


class DecroissantView(ListView):
    template_name = "Product/list.html"
    paginate_by = itemPerPages

    def get_queryset(self):
        return Product.objects.all().order_by('-price')

class GamingView(ListView):
    template_name = "Product/list.html"
    paginate_by = itemPerPages
    tag = Tag.objects.create(name='Gaming')

    def get_queryset(self):
        return Product.objects.all().filter('tags__id__in=[1]').values_list('id', flat=True)
