from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import CreateView, UpdateView, ListView
from administracion.helpers import obtener_coordenadas
from administracion.user_tests import user_is_visitant
from empresas.models import Empresa
from empresas.forms import FormEmpresaUpdate
from usuarios.models import TipoUsuario
from django.db.models import Q


class EmpresaSolicitud(UserPassesTestMixin, CreateView):
    model = Empresa
    form_class = FormEmpresaUpdate
    template_name = "vinculacion/formulario_empresa.html"
    extra_context = {"formulario_archivos": True, 'accion': 'Nueva'}

    def test_func(self):
        return user_is_visitant(self.request.user)

    def form_valid(self, form):
        empresa = form.save(commit=False)
        empresa.encargado = self.request.user
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(EmpresaSolicitud, self).form_invalid(form)

        # empresa.latitud = coordenadas.latitud
        # empresa.longitud = coordenadas.longitud
        empresa.encargado.tipo_usuario = TipoUsuario.objects.get(
            tipo="Empresa")

        empresa.save()
        empresa.encargado.save()
        form.save_m2m()

        messages.success(self.request, "Solicitud registrada correctamente")
        return redirect('vinculacion:perfil')


class EmpresaActualizar(LoginRequiredMixin, UpdateView):
    model = Empresa
    form_class = FormEmpresaUpdate
    template_name = "vinculacion/formulario_empresa.html"
    extra_context = {"formulario_archivos": True, 'accion': 'Actualizar'}

    def get_object(self):
        return get_object_or_404(Empresa, encargado=self.request.user)

    def form_valid(self, form):
        empresa = form.save(commit=False)
        coordenadas = obtener_coordenadas(form.cleaned_data)

        if not coordenadas:
            messages.error(
                self.request,
                "Error al obtener los datos de ubicación, por favor" +
                " verifique que los datos de dirección" +
                " ingresados son correctos.")
            return super(EmpresaActualizar, self).form_invalid(form)

        # empresa.latitud = coordenadas.latitud
        # empresa.longitud = coordenadas.longitud

        empresa.save()
        form.save_m2m()

        messages.success(self.request, "Perfil actualizado correctamente")
        return redirect('vinculacion:perfil')


class EmpresaLista(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Empresa
    template_name = "vinculacion/empresas_lista.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        base_queryset = Empresa.objects.filter(encargado__aprobado=True)
        if query:
            base_queryset = base_queryset.filter(
                Q(nombre_empresa__icontains=query) |
                Q(especialidades__nombre__icontains=query)
            ).distinct()
        return base_queryset
