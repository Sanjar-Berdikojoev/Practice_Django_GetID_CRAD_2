from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic
from .models import PC_Details

def mainpage_all(request):
    post = models.PC_Details.objects.all()
    return render(request, 'index.html',{'post':post})

def detail(request, id):
    post = models.PC_Details.objects.get(id=id)
    return render(request, 'index2.html', {'post': post})

class Post(generic.ListView):
    template_name = 'Post.html'
    queryset = models.PC_Details.objects.all()

    def get_queryset(self):
        return models.PC_Details.objects.all()

class PostDetail(generic.DetailView):
    template_name = 'PostDetail.html'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.PC_Details, id=post_id)

class PostCreate(generic.CreateView):
    template_name = 'PostCreate.html'
    form_class = forms.PostForm
    queryset = models.PC_Details.objects.all()
    success_url = '/post/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PostCreate, self).form_valid(form=form)

class PostUpdate(generic.UpdateView):
    template_name = 'PostUpdate.html'
    form_class = forms.PostForm
    success_url = '/post/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.PC_Details, id=post_id)

    def form_valid(self, form):
        return super(PostUpdate, self).form_valid(form=form)

class PostDelete(generic.DeleteView):
    template_name = 'PostDelete.html'
    success_url = '/post/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.PC_Details, id=post_id)

# Create your views here.
