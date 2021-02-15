from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Product, id=self.kwargs['pk'])
        liked = False
        if likes_connected.like.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.likeCount()
        data['post_is_liked'] = liked
        return data


def ProductLike(request, pk):
    post = get_object_or_404(Product, id=request.POST.get('product_id'))
    if post.like.filter(id=request.user.id).exists():
        print('remove')
        post.like.remove(request.user)
    else:
        print('add')
        post.like.add(request.user)

    return HttpResponseRedirect(reverse('productDetail', args=[str(pk)]))


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
