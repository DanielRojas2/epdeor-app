from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from ..models.Contrato import Contrato
from ..forms.contrato_form import ContratoForm

class ListadoContrato(ListView):
    model = Contrato
    template_name = 'cuentas/contratos/listar_contrato.html'

    def get_queryset(self):
        return self.model.objects.filter(estado='activo')
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponse(
                serialize('json', self.get_queryset()), 'application/json'
            )
        else:
            return render(
                request, self.template_name, {'object_list': self.get_queryset()}
            )
        
class RegistrarContrato(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'cuentas/contratos/crear_contrato.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if form.is_valid():
                nuevo_personal = Contrato(
                    nro_contrato=form.cleaned_data['nro_contrato'],
                    fecha_inicio=form.cleaned_data['fecha_inicio'],
                    fecha_fin=form.cleaned_data['fecha_fin'],
                    estado=form.cleaned_data['estado'],
                    cargo=form.cleaned_data['cargo'],
                    personal=form.cleaned_data['personal'],
                    usuario=form.cleaned_data['usuario']
                )
                nuevo_personal.save()
                return JsonResponse({'mensaje': 'Contrato registrado correctamente.'})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        else:
            return redirect('contratos')
