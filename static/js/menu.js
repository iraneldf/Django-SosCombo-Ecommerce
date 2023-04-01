const btnBuscar = document.querySelector('.buscar-icono');
const btnAbrirMenu = document.querySelector('.btn-menu');
const menu = document.getElementById('menu-principal');
const btnCerrarMenu = document.querySelector('.btn-cerrar-menu');
// const ingles = document.querySelector('.ingles');
// const espannol = document.querySelector('.espannol');

const btnMenuFiltrar = document.querySelector('.btn-menu-filtrar');
const menuFiltrar = document.querySelector('.menu-filtrar');
const btnMenuFiltrarCategoria1 = document.querySelector('.btn-filtrar__menu-producto1');
const btnMenuFiltrarCategoria2 = document.querySelector('.btn-filtrar__menu-producto2');
const menuFiltrarCategoria = document.querySelector('.menu-filtrar-categoria');
const filtroMenuContenedor = document.querySelector('.filtro-menu');

const subMenuAseo = document.querySelector('.aseo__categoria');
const btnMenuAseo = document.querySelector('.btn-filtrar__aseo');

const categorias = document.querySelectorAll('.categoria')
const subcategorias = document.querySelectorAll('.subcategoria')
const btnMenuCat = document.querySelectorAll('.btn-filtrar');

console.log(categorias.forEach((categoria,key)=>categoria.addEventListener("click", ()=>{
    btnMenuCat[key].classList.toggle('invertir');
    subcategorias[key].classList.toggle("subcategoria-oculta")
})))

/* btnMenuComidasBebidas.addEventListener('click', () => {
    subMenuComidasBebidas.classList.toggle('comidas-bebidas-oculto');
    btnMenuComidasBebidas.classList.toggle('invertir');
}); */
/* btnMenuAseo.addEventListener('click', () => {
    subMenuAseo.classList.toggle('aseo-oculto');
    btnMenuAseo.classList.toggle('invertir');
}); */





btnBuscar.addEventListener('click', () =>{
    document.querySelector('.barra-buscar').focus();
});


btnAbrirMenu.addEventListener('click', () => {
    menu.classList.toggle('activo');
});

btnCerrarMenu.addEventListener('click', () => {
    menu.classList.toggle('activo');
    
});

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




if (window.screen.width < 700) {
    document.getElementById('barra-escritorio').style.display = 'none';
}
else document.getElementById('barra-responsive').style.display = 'none';



