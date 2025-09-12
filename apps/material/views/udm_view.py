from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import UdM

@login_required
def udm_create(request):
    return render(request, "udm/_form_udm.html")

@login_required
def udm_update(request, pk):
    udm = get_object_or_404(UdM, pk=pk)
    return render(request, "udm/_form_udm.html", {"udm": udm})

@login_required
def udm_delete(request, pk):
    udm = get_object_or_404(UdM, pk=pk)
    udm.delete()
    udms = UdM.objects.all()
    return render(request, "udm/_tabla.html", {"udms": udms})
