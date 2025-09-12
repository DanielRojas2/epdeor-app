from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Partida

@login_required
def partida_create(request):
    return render(request, "partida/_form_partida.html")

@login_required
def partida_update(request, pk):
    partida = get_object_or_404(Partida, pk=pk)
    return render(request, "partida/_form_partida.html", {"partida": partida})

@login_required
def partida_delete(request, pk):
    partida = get_object_or_404(Partida, pk=pk)
    partida.delete()
    partidas = Partida.objects.all()
    return render(request, "partida/_tabla.html", {"partidas": partidas})
