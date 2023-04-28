from django.shortcuts import render
from eventos.models import Certificado

def meus_certificados(request):
    # Filtra todos os certificados do participante logado
    certificados = Certificado.objects.filter(participante=request.user)
    
    # Renderiza o template 'meus_certificados.html' com os certificados do participante
    return render(request, 'meus_certificados.html', {'certificados': certificados})
