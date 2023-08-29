//this have to launch when the document has been loaded
(function(){

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm("¿Seguro que quieres eliminar el curso?");
            if (!confirmacion) {
                //preventDefault prevent the default behavior, in this case, the click event
                e.preventDefault()
            }
        });
    });

})();