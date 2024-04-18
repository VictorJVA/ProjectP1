// Definir la función en el ámbito global
window.abrir_modal_crear = function(url) {
  $('#crear').load(url,function(){
    $(this).modal('show');
  });
};

jQuery(document).ready(function($) {
  // Otras operaciones que puedas tener dentro de tu función jQuery(document).ready()
  
});
