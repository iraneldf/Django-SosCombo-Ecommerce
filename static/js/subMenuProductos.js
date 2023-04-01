
// Menu escritorio

const btnA  = document.querySelector('.btn-aseo__categorias-escritorio');
const btnC  = document.querySelector('.btn__categorias-escritorio');

function setCategoryMenu(btn,classOfButton){
    document.querySelector(classOfButton).classList.toggle('ocultar');
    btn.classList.toggle('invertir');
}


btnA.addEventListener('click', ()=> setCategoryMenu(btnA, '.aseo__categorias-escritorio'));

