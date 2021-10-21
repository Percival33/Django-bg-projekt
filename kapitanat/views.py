from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView 
)
from .models import Jacht

def home(request):
    context = {
        'jachty': Jacht.objects.all()
    }
    return render(request, 'kapitanat/home.html', context)

class JachtListView(ListView):
    model = Jacht
    template_name = 'kapitanat/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'jachty'
    ordering = ['-data_dodania']
    paginate_by = 5

class UserJachtListView(ListView):
    model = Jacht
    template_name = 'kapitanat/user_jachty.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'jachty'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Jacht.objects.filter(autor=user).order_by('-data_dodania')

class JachtDetailView(DetailView):
    model = Jacht

class JachtCreateView(LoginRequiredMixin, CreateView):
    model = Jacht
    fields = ['nazwa', 'model', 'opis']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class JachtUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jacht
    fields = ['nazwa', 'model', 'opis']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
 
    def test_func(self):
        jacht = self.get_object()
        if self.request.user == jacht.autor:
            return True
        return False


class JachtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jacht
    success_url = '/'

    def test_func(self):
        jacht = self.get_object()
        if self.request.user == jacht.autor:
            return True
        return False


def about(request):
    return render(request, 'kapitanat/about.html', {'title' : 'about'})
    # return HttpResponse('<h4>Bocianie gowno</h4>')

