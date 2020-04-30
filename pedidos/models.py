from django.db import models

# Create your models here.

class clientes(models.Model):
    """docstring for clientes."""

    name = models.CharField(max_length = 30)
    addres = models.CharField(max_length = 50, verbose_name="Dir.")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length = 12)

    def __str__(self):

        return '%s' %(self.name) 

class articulos(models.Model):
    """docstring for articulos."""

    name = models.CharField(max_length = 30)
    seccion = models.CharField(max_length =30)
    precio = models.FloatField()

    def __str__(self):

        return 'Servico %s | Seccion %s | Precio %s |' %(self.name, self.seccion,self.precio)

class pedidos(models.Model):
    """docstring for pedidos."""

    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()
