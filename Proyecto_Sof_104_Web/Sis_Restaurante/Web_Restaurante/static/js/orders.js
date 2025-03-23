document.getElementById('add-platillo').addEventListener('click', function() {
    const platillosDiv = document.getElementById('order-platillos');
    const newPlatillo = platillosDiv.children[0].cloneNode(true);
    newPlatillo.querySelector('input[name="cantidad"]').value = 1;
    platillosDiv.appendChild(newPlatillo);
});

document.addEventListener('click', function(e) {
    if (e.target && e.target.className == 'remove-platillo') {
        const platillosDiv = document.getElementById('order-platillos');
        if (platillosDiv.children.length > 1) {
            e.target.parentElement.remove();
        } else {
            alert("No se puede eliminar el último platillo.");
        }
    }
});

document.getElementById('create-invoice').addEventListener('click', function() {
    const orderId = document.getElementById('order_id').value;
    if (orderId) {
        window.open(`/home/orders/crear_factura/${orderId}/`, '_blank');
    } else {
        alert("Seleccione un pedido para crear la factura.");
    }
});

document.getElementById('order_cliente').addEventListener('change', function() {
    const clienteId = this.value;
    if (clienteId === 'todos') {
        window.location.href = '/home/orders/';  // Aquí asumimos que /orders es la URL que muestra todos los pedidos
    } else {
        document.getElementsByName('buscar')[1].click();
    }
});