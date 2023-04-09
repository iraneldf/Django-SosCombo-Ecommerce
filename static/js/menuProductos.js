const btnMenuFiltrar = document.querySelector('.btn-menu-filtrar');
const menuFiltrar = document.querySelector('.menu-filtrar');
const btnMenuFiltrarCategoria1 = document.querySelector('.btn-filtrar__menu-producto1');
const btnMenuFiltrarCategoria2 = document.querySelector('.btn-filtrar__menu-producto2');
const menuFiltrarCategoria = document.querySelector('.menu-filtrar-categoria');
const filtroMenuContenedor = document.querySelector('.filtro-menu');


btnMenuFiltrar.addEventListener('click', () => {
    menuFiltrar.classList.toggle('filtrar-activo');
    btnMenuFiltrar.classList.toggle('invertir')
});


btnMenuFiltrarCategoria1.addEventListener('click', () => {
    menuFiltrarCategoria.classList.toggle('categoria-activo');
    filtroMenuContenedor.classList.toggle('filtro-menu-activo');
    btnMenuFiltrarCategoria1.classList.toggle('ocultar-btn');
    btnMenuFiltrarCategoria2.classList.toggle('ocultar-btn');
});
btnMenuFiltrarCategoria2.addEventListener('click', () => {
    menuFiltrarCategoria.classList.toggle('categoria-activo');
    filtroMenuContenedor.classList.toggle('filtro-menu-activo');
    btnMenuFiltrarCategoria1.classList.toggle('ocultar-btn');
    btnMenuFiltrarCategoria2.classList.toggle('ocultar-btn');
});
