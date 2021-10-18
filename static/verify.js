// Se leen las variables de Iconos y los textos a desplazar
var check1 = document.getElementById('check1');
var check2 = document.getElementById('check2');
var check3 = document.getElementById('check3');
var check4 = document.getElementById('check4');
var check5 = document.getElementById('check5');
var check6 = document.getElementById('check6');
var error1 = document.getElementById('error1');
var error2 = document.getElementById('error2');
var error3 = document.getElementById('error3');
var error4 = document.getElementById('error4');
var error5 = document.getElementById('error5');
var error6 = document.getElementById('error6');
var text1 = document.getElementById('text1');
var text2 = document.getElementById('text2');
var text3 = document.getElementById('text3');
var text4 = document.getElementById('text4');
var text5 = document.getElementById('text5');
var text6 = document.getElementById('text6');

// Se validan los diferentes campos
function validarnombre(){
    var name = document.getElementById('name');
    if(!(name == null || name.length == 0 )){
        check1.style.display='inline';
        error1.style.display='none'; 
        name.style.border='3px solid green';
        return true;
    }else if(name.value.length == 0){
        name.style.border='3px solid red';
        check1.style.display='none';
        error1.style.display='none';
        return false;
    }else {
        check1.style.display='none';
        error1.style.display='inline'; 
        name.style.border='3px solid red'    
        return false;   
    }
}
function validarapellido(){
    var lastname = document.getElementById('lastname');
    if(!(lastname == null || lastname.length == 0 )){
        check6.style.display='inline';
        error6.style.display='none'; 
        lastname.style.border='3px solid green';
        return true;
    }else if(lastname.value.length == 0){
        lastname.style.border='3px solid red';
        check6.style.display='none';
        error6.style.display='none';
        return false;
    }else {
        check6.style.display='none';
        error6.style.display='inline'; 
        lastname.style.border='3px solid red'    
        return false;   
    }
}
function validaremail(){
    var email = document.getElementById('email');
    if(/\S+@\S+\.\S+/.test(email.value)){
        check2.style.display='inline';
        error2.style.display='none'; 
        email.style.border='3px solid green';
        return true;
    } else if(email.value.length == 0){
        email.style.border='3px solid red';
        check2.style.display='none';
        error2.style.display='none';
        return false;
    } else {
        check2.style.display='none';
        error2.style.display='inline'; 
        email.style.border='3px solid red'       
        return false;
    }
    
}
function validarcel(){
    var tel = document.getElementById('tel');
    if(/^\(?(\d{3})\)?[-]?(\d{3})[-]?(\d{4})$/.test(tel.value)){
        check3.style.display='inline';
        error3.style.display='none'; 
        tel.style.border='3px solid green';
        return true;
    }else if(tel.value.length == 0){
        tel.style.border='3px solid red';
        check3.style.display='none';
        error3.style.display='none';
        return false;
    } else {
        check3.style.display='none';
        error3.style.display='inline'; 
        tel.style.border='3px solid red'       
        return false;
    }
    
}
function validarpass(){
        // La contrasena debe tener entre 8 y 16 caracteres, al menos una mayuscula, una minuscula y un numero
        // No debe contener caracteres especiales
        var pass1 = document.getElementById('pass1');
        if(/^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/.test(pass1.value)){
            check4.style.display='inline';
            error4.style.display='none'; 
            pass1.style.border='3px solid green';
            return true;
        }else if(pass1.value.length == 0){
            pass1.style.border='3px solid red';
            check4.style.display='none';
            error4.style.display='none';
            return false;
        } else {
            check4.style.display='none';
            error4.style.display='inline'; 
            pass1.style.border='3px solid red';
            return false;
        }
    }
function compararpass(){
    // Se comprueba que las contrasenas coincidan
    var pass1 = document.getElementById('pass1');
    var pass2 = document.getElementById('pass2');
    if(pass1.value == pass2.value){
        check5.style.display='inline';
        error5.style.display='none'; 
        pass2.style.border='3px solid green';
        return true;
    }else if(pass2.value.length == 0){
        pass2.style.border='3px solid red';
        check5.style.display='none';
        error5.style.display='none';
        return false;
    } else {
        check5.style.display='none';
        error5.style.display='inline'; 
        pass2.style.border='3px solid red'       
        return false;
    }
}
function someBug(n){
    if(n == 1){
        validarnombre();
    } else if (n == 7){
        validarapellido();
    } else if (n == 2){
        validaremail();
    } else if (n == 3){
        validarcel();
    } else if (n == 4){
        validarpass();
    } else if (n == 5){
        compararpass();
    }else if (n == 6){
        var p1 = validarnombre();
        if(p1 == true){
            var p2 = validaremail();
            if(p2 == true){
                var p3 = validarcel();
                if(p3 == true){
                    var p4 = validarpass();
                    if(p4 == true){
                        var p5 = compararpass();
                        if(p5 == true){
                            return true;  
                        }else{return false;}
                    }else{return false;}
                }else{return false;}
            }else{return false;}
        }else{return false;}

    }
}
// Se desplazan los textos de los inputs
function labelsup(text){
    text.style.transform='translate(0,-19px)';
    text.style.transition='all 0.5s';
}