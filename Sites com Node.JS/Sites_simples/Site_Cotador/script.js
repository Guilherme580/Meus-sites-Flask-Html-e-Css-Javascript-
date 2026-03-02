function contar(){   
    var inicio = parseInt(document.getElementsByName("inicio")[0].value)
    var fim = parseInt(document.getElementsByName("fim")[0].value)
    var passo = parseInt(document.getElementsByName("passo")[0].value)
    var resultado = document.getElementById("resultado")
    
    if(isNaN(inicio) || isNaN(fim)){
        resultado.innerHTML = "Impossível contar! Faltam dados."
        return 
    } 
    
    if(isNaN(passo)){
        alert('Passo inválido! Considerando PASSO 1');
        passo = 1;
    }

    resultado.innerHTML = ` `
    if(inicio < fim){
        for(let i = inicio ;i <= fim; i += passo){
            resultado.innerHTML += `${i} 👉 `
        }   
    }else{
        for(let i = inicio ;i >= fim; i -= passo){
            resultado.innerHTML += `${i} 👉 `
        }
    }
    bandeira()
}


function bandeira(){
    var num = Math.floor(Math.random() * 4) + 1
    switch (num) {
        case 1:
            resultado.innerHTML += "🏴"
            break;
        case 2:
            resultado.innerHTML += "🚩"
            break;
        case 3:
            resultado.innerHTML += "🏴‍☠️"
            break;
        case 4:
            resultado.innerHTML += "🏳‍🌈"
            break;
    }
}
