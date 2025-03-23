from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación

    def __str__(self):
        return self.nombre
    
class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

class Order(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Listo', 'Listo'),
        ('Cancelado', 'Cancelado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    platillos = models.ManyToManyField(Menu, through='OrderDetail')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Fecha y hora de actualización

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()