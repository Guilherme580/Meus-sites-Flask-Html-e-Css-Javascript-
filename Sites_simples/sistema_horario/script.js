function carregar() {
    // horario do sistema
    var agora = new Date()
    var horario = agora.getHours()
    var minutos = agora.getMinutes()
    // espaços a seren modificados
    var corpo = document.getElementById("corpo")
    var msg = document.getElementById("msg")
    var img = document.getElementById("img")

    msg.innerHTML = `<p>Nesse exato momento são ${horario} horas! e ${minutos} minutos</p>`
    if(horario >= 5 && horario < 12) {
        corpo.style.backgroundColor = "#3D5C78"
        img.src = "imgs/manhã.jpg"
        addEventListener()

    }else if(horario >= 12 && horario < 18) {
        corpo.style.backgroundColor = "#8F9DB8"
        img.src = "imgs/tarde.jpg"
    }
    else if(horario >= 18 && horario < 24 || horario >= 0 && horario < 5 ) {
        corpo.style.backgroundColor = "#3F5064"
        img.src = "imgs/noite.jpg"

    }
}