from django.shortcuts import render
from .models import Tarefa
from datetime import date
# Create your views here.
def index(request):
    tarefa = Tarefa.objects.all()
    context = {"tarefa":tarefa}
    context['hoje'] = date.today()

    return render(request,'tarefas/index.html',context)