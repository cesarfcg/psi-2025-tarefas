from django.shortcuts import render,get_object_or_404
from . models import Postagem
# Create your views here.
def index(request):
    postagem = Postagem.objects.all()
    context = {"postagem":postagem}
    return render(request,'blog/index.html',context)
def noticia(request, id_post):
    postagem = get_object_or_404(Postagem, id=id_post)
    context = {"postagem":postagem}
    return render(request,'blog/noticia.html',context)
