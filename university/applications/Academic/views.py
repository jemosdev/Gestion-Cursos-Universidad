from django.shortcuts import render
from .models import Curso

# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListados})