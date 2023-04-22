from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.order_by('nome') #Pode usar o Filtro ao invez de fazer o If no Html indez :)

    #Configurção de paginação.
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {  'contatos' : contatos  })


def ver_contato(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    #gerando a pagina de erro 404 com o Http404
    contato = get_object_or_404(Contato, id=contato_id)

    #Impede que o ID seja mostrado de forma manual na view
    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {  'contato' : contato })
