from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from ..models.Personal import Personal
from ..forms.personal_form import PersonalForm

class ListadoPersonal(ListView):
    model = Personal
    template_name = 'cuentas/personal/listar_personal.html'

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
        
class RegistrarPersonal(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'cuentas/personal/crear_personal.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if form.is_valid():
                nuevo_personal = Personal(
                    nombre_personal=form.cleaned_data['nombre_personal'],
                    apellido_paterno=form.cleaned_data['apellido_paterno'],
                    apellido_materno=form.cleaned_data['apellido_materno'],
                    estado=form.cleaned_data['estado']
                )
                nuevo_personal.save()
                return JsonResponse({'mensaje': 'Personal creado correctamente.'})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        else:
            return redirect('listar_personal')
