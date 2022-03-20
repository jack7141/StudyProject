from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

class HomeView(View):
    def get(self, request):
        return render(request, "arts/art_list.html")
        # return render(request, "base.html")