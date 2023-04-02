const btnProvincia = document.querySelector('.btn-provincia');
const btnMunicipio = document.querySelector('.btn-municipio');





btnProvincia.addEventListener('click', () => {
    document.querySelector('.ubicacion-provincia-modal').classList.toggle('ocultar-sub-modal');
});

// btnMunicipio.addEventListener('click', () => {
//     document.querySelector('.ubicacion-municipio-modal').classList.toggle('ocultar-sub-modal');
// });


