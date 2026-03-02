function verificar(){
    var agora = new Date() 
    var ano_atual = agora.getFullYear()
    var ano_nascimento = Number(document.getElementById("txt_nascimento").value)
    var resul = document.getElementById("resultado")
    

    if(ano_nascimento == 0 || ano_nascimento > ano_atual){
        alert("[ERRO]Tente de novo");
    }else{
        var sexo = document.getElementsByName("sexo")
        var idade = (ano_atual - ano_nascimento) 
        var genero = ""
        var img = document.createElement("img")
        img.setAttribute("id", "foto")

        if(sexo[0].checked){
            genero = "Homem"
            if(idade >= 0 && idade < 10){
                img.setAttribute("src", "img/bebê_homem.jpg")
            }else if(idade >= 10 && idade < 21){
                img.setAttribute("src", "img/jovem_homem.jpg")
            }else if(idade >= 21 && idade < 50){
                img.setAttribute("src", "img/adulto_homem.jpg")
            }else{
                img.setAttribute("src", "img/velho_homem.jpg")
            }
        }else if(sexo[1].checked){
            genero = "Mulher"
            if(idade >=0 && idade < 10){
                img.setAttribute("src", "img/bebê_mulher.jpg")
            }else if(idade >= 10 && idade < 21){
                img.setAttribute("src", "img/jovem_mulher.jpg")
            }else if(idade >= 21 && idade < 50){
                img.setAttribute("src", "img/adulta_mulher.jpg")
            }else{
                img.setAttribute("src", "img/velha_mulher.jpg")
            }
        }
        resul.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        resul.appendChild(img)
    }
}