from django import forms
from .models import Cliente, Menu, Order, OrderDetail

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'correo']

class BuscarClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nombre', 'descripcion', 'precio']

class BuscarMenuForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['cliente', 'estado']

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['menu', 'cantidad']

class BuscarOrderForm(forms.Form):
    cliente = forms.CharField(max_length=100, required=False)
 