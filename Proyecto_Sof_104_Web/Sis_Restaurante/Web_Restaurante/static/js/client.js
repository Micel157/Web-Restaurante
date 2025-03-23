function fillForm(id, nombre, telefono, correo) {
    document.getElementById('cliente_id').value = id;
    document.getElementById('name_client').value = nombre;
    document.getElementById('tel_client').value = telefono;
    document.getElementById('email_client').value = correo;
}
document.getElementById('show-all-clients').addEventListener('click', function() {
    window.location.href = '/home/client/';
});