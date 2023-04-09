const btnBuscar = document.querySelector('.buscar-icono');
const btnAbrirMenu = document.querySelector('.btn-menu');
const menu = document.getElementById('menu-principal');
const btnCerrarMenu = document.querySelector('.btn-cerrar-menu');

const categorias = document.querySelectorAll('.categoria')
const subcategorias = document.querySelectorAll('.subcategoria')
const btnMenuCat = document.querySelectorAll('.btn-filtrar');

categorias.forEach((categoria, key) => categoria.addEventListener("click", () => {
    btnMenuCat[key].classList.toggle('invertir');
    subcategorias[key].classList.toggle("subcategoria-oculta")
}))


btnBuscar.addEventListener('click', () => {
    document.querySelector('.barra-buscar').focus();
});


btnAbrirMenu.addEventListener('click', () => {
    menu.classList.toggle('activo');
});

btnCerrarMenu.addEventListener('click', () => {
    menu.classList.toggle('activo');

});



