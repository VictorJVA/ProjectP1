'use strict';

const jquery = require("jquery");

let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
btn.onclick = function () {
  sidebar.classList.toggle("active");
};

var $ = jquery.noConflict();
function abrir_modal_crear(url){
  $('#crear').load(url,function(){
    $(this).modal('show');
  });
};

// // Definir la función en el ámbito global
// window.abrir_modal_crear = function(url) {
//   $('#crear').load(url,function(){
//     $(this).modal('show');
//   });
// };

// jQuery(document).ready(function($) {
//   // Otras operaciones que puedas tener dentro de tu función jQuery(document).ready()
// });
