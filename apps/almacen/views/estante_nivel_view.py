from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from ..models.EstanteNivel import EstanteNivel
from ..forms.estante_nivel_form import EstanteNivelForm

class ListadoEstanteNivel(ListView):
    model = EstanteNivel
    template_name = 'estante_nivel/listar_estante_nivel.html'

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
        
class RegistrarEstanteNivel(CreateView):
    model = EstanteNivel
    form_class = EstanteNivelForm
    template_name = 'estante_nivel/crear_estante_nivel.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if form.is_valid():
                nuevo_estante_nivel = EstanteNivel(
                    estante=form.cleaned_data['estante'],
                    nivel=form.cleaned_data['nivel'],
                    estado=form.cleaned_data['estado']
                )
                nuevo_estante_nivel.save()
                return JsonResponse({'mensaje': 'Nivel de Estante creado correctamente.'})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        else:
            return redirect('listar_estante_nivel')
