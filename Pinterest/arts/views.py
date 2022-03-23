from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View, RedirectView
from django.views.generic.list import MultipleObjectMixin
from arts.models import Art
from accounts.models import User
from reviews.models import Review
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .decorators import art_ownership_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import art_form
from django.urls import reverse_lazy
from django.urls import reverse
from accounts import mixins as user_mixins
from django.http import Http404, JsonResponse
from django.views.generic.edit import FormMixin
from reviews.forms import review_form
from django.contrib import messages

class HomeView(ListView):
    model = Art
    paginate_by = 30
    paginate_orphans = 5
    ordering = ['title']
    template_name = 'arts/photo_list.html'

    context_object_name = 'arts'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArtCreateView(CreateView):
    model = Art
    form_class = art_form
    template_name = 'arts/photo_create.html'

    def form_valid(self, form):
        new_art = form.save(commit=False)
        new_art.artist = self.request.user
        print(new_art)
        new_art.save()
        return super().form_valid(form)

    # 성공시 내가 보재고자 하는 URL과 필요한 데이터를 넘겨준다.
    def get_success_url(self) -> str:
        return reverse("arts:viewDetail", kwargs = {"id":self.object.pk})

class ArtDetailView(DetailView, FormMixin):
    model = Art
    pk_url_kwarg = 'id'
    form_class = review_form
    template_name = 'arts/photo_detail.html'
    context_object_name = 'target_art_work'
    
    # def get_context_data(self, **kwargs):
        # object_list = Review.objects.filter(art=self.get_object(), user=self.request.user)
        # print(object_list)
        # return super(ArtDetailView, self).get_context_data(object_list=object_list, **kwargs)

class ArtUpdateView(UpdateView):
    model = Art
    pk_url_kwarg = 'id'
    # UpdateView를 사용하려면 form클래스가 필수인듯?
    form_class = art_form
    template_name = 'arts/photo_update.html'
    context_object_name = 'target_art_work'

    def get_success_url(self) -> str:
        return reverse("arts:viewDetail", kwargs = {"id":self.object.pk})

class ArtDeleteView(DeleteView):
    model = Art
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("core:CoreHomeView")
    template_name = 'arts/photo_delete.html'
    context_object_name = 'target_art_work'

class ArtshotosView(DetailView, MultipleObjectMixin):
    """
    내가 가지고 있는 작품 리스트
    """
    model = User
    template_name = "arts/art_llist.html"
    context_object_name = 'arts'

    def get_context_data(self, **kwargs):
        object_list = Art.objects.filter(artist=self.get_object())
        return super(ArtshotosView, self).get_context_data(object_list=object_list, **kwargs)


def likes(request, id):
    art = get_object_or_404(Art, pk=id)
    if request.user.is_authenticated:
        if request.user in art.like_users.all():
            art.like_users.remove(request.user)
        else:
            art.like_users.add(request.user)
        return redirect('arts:viewDetail', art.pk)

    return redirect('accounts:login')
