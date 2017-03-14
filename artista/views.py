from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import *
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import json
import urllib2


from artista.models import ArtistaFavorit
# Create your views here.
@login_required
def veure_artistes(request):
    artistes = ArtistaFavorit.objects.filter(usuari=request.user)
    return render(request, 'artista/index.html', {'artistes': artistes})

@login_required
def intro_edit_artistes(request, id_artista=None):
    es_modificacio =(id_artista!=None)
    artistaForm =modelform_factory(ArtistaFavorit, exclude=('usuari', ))
    if es_modificacio:
        artista = get_object_or_404(ArtistaFavorit, id_producte=id_artista)
    else:
        artista=ArtistaFavorit(usuari=request.user)
    if request.method == 'POST':
        form = artistaForm(request.POST,request.FILES,instance=artista)
        if form.is_valid():
            artista = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, "L'artista ha sigut modificat correctament")
            else:
                messages.add_message(request, messages.SUCCESS, "L'artista nou ha sigut creat correctament")
            return HttpResponseRedirect(reverse('artista:veure_artistes'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, "Error en modificar a l'artista")
            else:
                messages.add_message(request, messages.ERROR, "Error en modificar a l'artista nou")
    else:
        form = artistaForm(instance=artista)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-9'
    form.helper.add_input(Submit('submit', 'Guardar'))
    return render(request, 'artista/formulariArtista.html', {'form': form, 'artistes':artista})

def rebreDadesArtista(request):
    q = request.GET.get('query', '')
    url = 'http://ws.audioscrobbler.com/2.0/?method=artist.search&artist='+ q +'&api_key=593ff784c9b080040b22ebc449a9a444&format=json'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    ep = json.load(response)


    artistes = list()
    for a in ep['results']['artistmatches']['artist']:
        artistes.append(a['name'])

    values = json.dumps(artistes)

    return HttpResponse(values, content_type='application/json')