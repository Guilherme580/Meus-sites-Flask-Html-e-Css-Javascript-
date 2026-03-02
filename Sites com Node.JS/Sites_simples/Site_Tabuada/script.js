function tabuada() {
    var numb = parseInt(document.getElementById('numb').value)
    var tab = document.getElementById('tab')


    if (isNaN(numb)){
        alert('Por favor, digite um número!');
    }else{
        let cont = 1;
        tab.innerHTML = ''
        do{
            let opt = document.createElement('option');
            opt.text = `${numb} x ${cont} = ${numb * cont}`;
            opt.value = `tab${cont}`

            tab.appendChild(opt)
            cont++
        }while (cont <= 10)
    }
}
