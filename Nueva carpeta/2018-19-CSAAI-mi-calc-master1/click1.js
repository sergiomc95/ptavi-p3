function main() {

  console.log("empiezaaaa")
  var boton = document.getElementById('boton')

  boton.onclick = () => {
    console.log("Click");

    var display = document.getElementById('display')
    display.innerHTML = "NUEVO TEXTOOO"
  }
}
