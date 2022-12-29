const btnSwitch = document.querySelector('#switch');

function switching(){
	if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark')
    }
}

function crearURL(slug) {
        
        // Reemplaza los carácteres especiales | simbolos con un espacio 
        slug = slug.replace(/[`~!@#$%^&*()_\-+=\[\]{};:'"\\|\/,.<>?\s]/g, ' ').toLowerCase();
        
        // Corta los espacios al inicio y al final del sluging 
        slug = slug.replace(/^\s+|\s+$/gm,'');
        
        // Reemplaza el espacio con guión  
        slug = slug.replace(/\s+/g, '-');

        // Creo la URL en el campo de texto 'url'
        var input = document.getElementById('url');
        input.value = slug;  

        // Creo la URL en el elemento span 'texto-url' 
        document.getElementById("texto-url").innerHTML= slug;
        
      } 