from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django import template

from .models import Allegato, Categoria, Dettaglio, Lavoro

#def index(request):
#    return HttpResponse("Hello, world. Benvenuto!")

def index(request):
    lavori_list = Lavoro.objects.order_by('-data_lavoro')[:5]
    context = {'lavori_list': lavori_list}
    return render(request, 'lista.html', context)

def lavori(request, lavoro_id):
    try:
        lavoro = Lavoro.objects.get(pk=lavoro_id)
        dettaglio = Dettaglio.objects.filter(lavoro_dettaglio=lavoro)
        allegato = Allegato.objects.all()

        fotoallegate = []
        for detail in dettaglio:
            for att in allegato:
                if att.dettaglio_id == detail.id:
                    fotoallegate.append(att.foto_allegato)

        print (fotoallegate)
        #for d in dettaglio:
        #    allegato = Allegato.objects.filter(dettaglio_id=d.id)

    except Lavoro.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'dettaglio.html', {'lavoro': lavoro, 'dettaglio': dettaglio, 'allegato': allegato, 'fotoallegate': fotoallegate})

def categorie(request, lavoro_id):
    lavoro = Lavoro.objects.get(pk=lavoro_id)
    categoria = Categoria.objects.filter(titolo_categoria=lavoro.categoria)
    context = {'categoria': categoria}
    return render(request, 'categorie.html', context)
