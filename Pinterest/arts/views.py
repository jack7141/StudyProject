from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, UpdateView, CreateView
from arts.models import Art
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import art_ownership_required
from django.shortcuts import render, redirect
from .forms import art_form
from django.urls import reverse_lazy
from django.urls import reverse

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

# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
class ArtDetailView(DetailView):
    model = Art
    pk_url_kwarg = 'id'
    template_name = 'arts/photo_detail.html'
    context_object_name = 'target_art_work'

class ArtUpdateView(UpdateView):
    model = Art
    pk_url_kwarg = 'id'
    # UpdateView를 사용하려면 form클래스가 필수인듯?
    form_class = art_form
    template_name = 'arts/photo_update.html'
    context_object_name = 'target_art_work'

    def get_success_url(self) -> str:
        return reverse("arts:viewDetail", kwargs = {"id":self.object.pk})