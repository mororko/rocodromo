from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import Notice

def _active_notices():
    now = timezone.now()
    return (Notice.objects
            .filter(is_active=True, start_at__lte=now)
            .filter(end_at__isnull=True) | Notice.objects
                    .filter(is_active=True, start_at__lte=now, end_at__gte=now))
    


def _ctx():
    now = timezone.now()
    active_notice = (
        Notice.objects
        .filter(is_active=True, start_at__lte=now)
        .filter(Q(end_at__isnull=True) | Q(end_at__gte=now))
        .order_by("-start_at")
        .first()
    )
    return {"active_notice": active_notice}
        
# Create your views here.
def home(request):
    return render(request, 'core/home.html', _ctx())

def instalaciones(request):
    return render(request, "core/instalaciones.html", _ctx())

def horarios(request):
    return render(request, "core/horarios.html", _ctx())

def precios(request):
    return render(request, "core/precios.html", _ctx())

def contacto(request):
    return render(request, "core/contacto.html", _ctx())

def reservar(request):
    return render(request, "core/reservar.html", _ctx())