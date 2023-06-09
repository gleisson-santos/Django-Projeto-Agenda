from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato

from django.db.models import Q, Value
from django.db.models.functions import  Concat
from django.contrib import messages

# Create your views here.
def index(request):


    contatos = Contato.objects.order_by('id') #Pode usar o Filtro ao invez de fazer o If no Html indez :)

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


def busca(request):
    termo = request.GET.get('termo')

    #se não estiver termo ou o termo estiver vazio
    if termo is None or not termo:
        #raise  Http404()
        messages.add_message(request, messages.ERROR, 'Campo de pesquisa não pode ficar vazio')
        return redirect ('index')


    campos = Concat('nome', Value(' '), 'sobrenome')#Valeu vai simular um campo/espaço vazio

    #para utilizar busca considerando duas colunas separadas
    contatos = Contato.objects.annotate(nome_completo = campos).filter(
       Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    # #Pode usar o Filtro ao invez de fazer o If no Html index  / Criando o filtro de itens Q = OR
    # contatos = Contato.objects.order_by('-id').filter(
    #     Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
    #     mostrar=True
    # )

    #Configurção de paginação.
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {  'contatos' : contatos  })