   window.addEventListener('click', (e) => {
                if (e.composedPath()[0].classList[0] === 'btn-contar') {
                    const botonAnnadir = document.querySelector(`#btn${e.composedPath()[0].id}`);
                    const botonAnnadirP = document.querySelector(`#pbtn${e.composedPath()[0].id}`);
                    const contenedor = document.querySelector(`.${e.composedPath()[0].id}`);

                    botonAnnadir.classList.remove('ocultar');
                    botonAnnadirP.classList.remove('ocultar');

                    if (e.composedPath()[0].classList[1] === 'restar') {
                        if (contenedor.textContent == 1 || contenedor.textContent == 0) {
                            botonAnnadir.classList.add('ocultar')
                            botonAnnadirP.classList.add('ocultar')
                        }
                    } else if (e.composedPath()[0].classList[1] === 'sumar') {
                        if (contenedor.textContent != 0) {
                            botonAnnadir.classList.remove('ocultar')
                            botonAnnadirP.classList.remove('ocultar')
                        }
                    }


                }
            }
        )
        ;