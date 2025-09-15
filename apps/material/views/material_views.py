from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from ..models.Material import Material
from ..forms.material_form import MaterialForm

class ListadoMaterial(ListView):
    model = Material
    template_name = 'material/listar_material.html'
    
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
            
class RegistrarMaterial(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/crear_material.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if form.is_valid():
                nuevo_material = Material(
                    material=form.cleaned_data['material'],
                    partida=form.cleaned_data['partida'],
                    unidad_medida=form.cleaned_data['unidad_medida'],
                    nivel_minimo=form.cleaned_data['nivel_minimo'],
                    cantidad_existente=form.cleaned_data['cantidad_existente'],
                    estado=form.cleaned_data['estado']
                )
                nuevo_material.save()
                return JsonResponse({'mensaje': 'Material agregado correctamente.'})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        else:
            return redirect('listar_material')
