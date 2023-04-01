

window.addEventListener('click', (e) => {
    if(e.composedPath()[0].classList[1] == 'tarjeta1'){
        document.getElementById('tarjeta1').checked = true
        document.getElementById('tarjeta2').checked = false;
        document.getElementById('tarjeta3').checked = false;
        document.getElementById('tarjeta4').checked = false;

        // document.getElementById('selectorTarjeta1').hidden = false;
        // document.getElementById('selectorTarjeta2').hidden = true;
        // document.getElementById('selectorTarjeta3').hidden = true;
        // document.getElementById('selectorTarjeta4').hidden = true;
    }
    if(e.composedPath()[0].classList[1] == 'tarjeta2'){
        document.getElementById('tarjeta2').checked = true
        document.getElementById('tarjeta1').checked = false;
        document.getElementById('tarjeta3').checked = false;
        document.getElementById('tarjeta4').checked = false;

        // document.getElementById('selectorTarjeta2').hidden = false;
        // document.getElementById('selectorTarjeta1').hidden = true;
        // document.getElementById('selectorTarjeta3').hidden = true;
        // document.getElementById('selectorTarjeta4').hidden = true;
    }
    if(e.composedPath()[0].classList[1] == 'tarjeta3'){
        document.getElementById('tarjeta3').checked = true
        document.getElementById('tarjeta2').checked = false;
        document.getElementById('tarjeta1').checked = false;
        document.getElementById('tarjeta4').checked = false;

        // document.getElementById('selectorTarjeta3').hidden = false;
        // document.getElementById('selectorTarjeta2').hidden = true;
        // document.getElementById('selectorTarjeta1').hidden = true;
        // document.getElementById('selectorTarjeta4').hidden = true;
    }
    if(e.composedPath()[0].classList[1] == 'tarjeta4'){
        document.getElementById('tarjeta4').checked = true
        document.getElementById('tarjeta2').checked = false;
        document.getElementById('tarjeta3').checked = false;
        document.getElementById('tarjeta1').checked = false;

        // document.getElementById('selectorTarjeta4').hidden = false;
        // document.getElementById('selectorTarjeta2').hidden = true;
        // document.getElementById('selectorTarjeta3').hidden = true;
        // document.getElementById('selectorTarjeta1').hidden = true;
    }

    
    document.getElementById('tarjeta1').checked ? document.getElementById('selectorTarjeta1').removeAttribute('hidden') : document.getElementById('selectorTarjeta1').setAttribute('hidden', 'true');

    document.getElementById('tarjeta2').checked ? document.getElementById('selectorTarjeta2').removeAttribute('hidden') : document.getElementById('selectorTarjeta2').setAttribute('hidden', 'true');

    document.getElementById('tarjeta3').checked ? document.getElementById('selectorTarjeta3').removeAttribute('hidden') : document.getElementById('selectorTarjeta3').setAttribute('hidden', 'true');

    document.getElementById('tarjeta4').checked ? document.getElementById('selectorTarjeta4').removeAttribute('hidden') : document.getElementById('selectorTarjeta4').setAttribute('hidden', 'true');
    
    
});
