function fillForm(id, nombre, descripcion, precio) {
    document.getElementById('dish_id').value = id;
    document.getElementById('dish_name').value = nombre;
    document.getElementById('dish_description').value = descripcion;
    document.getElementById('dish_price').value = precio;
}

document.getElementById('show-all-clients').addEventListener('click', function() {
    window.location.href = '/home/menu/';
});