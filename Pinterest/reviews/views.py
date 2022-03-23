from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from .models import Review
from arts.models import Art
from .forms import review_form
from django.urls import reverse
from django.contrib import messages

# class review_create_view(CreateView):
#     model = Review
#     form_class = review_form
#     template_name = 'reviews/review_create.html'
#     def form_valid(self, form):
#         new_review = form.save(commit=False)
#         new_review.art = Art.objects.get(id=self.request.POST['art_pk'])
#         new_review.user = self.request.user
#         new_review.save()
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse("arts:viewDetail", kwargs = {"id":self.object.art.pk})

def review_create_view(request, id):
    if request.method == "POST":
        # Form을 커스텀 하려면 name과 내가 만든 Modle의 명을 맞춰줘야함;;
        form = review_form(request.POST)
        art_title = Art.objects.get(pk=id)
        if not art_title:
            return redirect(reverse("core:CoreHomeView"))
        if form.is_valid():
            review = form.save()
            review.art = art_title
            review.user = request.user
            review.save()
            messages.success(request, f"{art_title} reviewed")
            return redirect(reverse("arts:viewDetail", kwargs={"id": art_title.pk}))
    messages.error(request, f"{art_title} reviewed Fail")
    return redirect(reverse("arts:viewDetail", kwargs={"id": art_title.pk}))