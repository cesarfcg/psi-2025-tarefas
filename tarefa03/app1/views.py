from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def usuarios(request):
    meus_usuarios = [
        {"nome":"Nico Delasexo","matricula":1,"cidade":"Montevidéu","idade":"33"},
        {"nome":"Chico Pereira","matricula":2,"cidade":"São Pedro","idade":"67"},
        {"nome":"Zé Briolo","matricula":3,"cidade":"Curicaca","idade":"87"},
        {"nome":"Manoel Lopes","matricula":4,"cidade":"Arisco de Condessa","idade":"91"},
        {"nome":"Alfreu Nobrega","matricula":5,"cidade":"Pau dos Ferros","idade":"76"}
    ]
    context = {"usuarios": meus_usuarios,}
    return render(request,"usuarios.html",context)
# Create your views here.
