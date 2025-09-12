from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Material, Partida, UdM

@login_required
def material_list(request):
    materiales = Material.objects.select_related('partida', 'unidad_medida').all()
    return render(request, 'material/listado.html', {'materiales': materiales})

@login_required
def material_create(request):
    partidas = Partida.objects.all()
    udms = UdM.objects.all()
    return render(request, "material/_form.html", {"partidas": partidas, "udms": udms})

@login_required
def material_update(request, pk):
    material = get_object_or_404(Material, pk=pk)
    partidas = Partida.objects.all()
    udms = UdM.objects.all()
    return render(request, "material/_form.html", {"material": material, "partidas": partidas, "udms": udms})

@login_required
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    materiales = Material.objects.select_related('partida', 'unidad_medida').all()
    return render(request, "material/_tabla.html", {"materiales": materiales})
