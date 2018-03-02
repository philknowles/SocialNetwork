from django.views.generic import TemplateView
from django.shortcuts import render
from home.forms import HomeForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})