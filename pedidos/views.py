from django.shortcuts import render
from django.http import HttpResponse
from pedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def busqueda_productos(request):

    return render(request, "busq_pructos.html")


def buscad(request):

    if request.GET["prd"]:

        #mensaje="Articulo: %r" %request.GET["prd"]
        produc=request.GET["prd"]

        if  len(produc)>40:
            mensaje="La cadena de texto es muy extensa"
        else:
            arti=articulos.objects.filter(name__icontains=produc)
            return render(request, "resultado_busqueda.html", {"articulos":arti, "query":produc})

    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)


def contacto(request):

    if request.method=="POST":

        subject=request.POST["subject"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=['kjjzhor@gmail.com']
        send_mail(subject, message, email_from, recipient_list)

        return render(request, "thanks.html")

    return render(request, "mail.html")

esto es una prueba para git 
