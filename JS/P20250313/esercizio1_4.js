const e = (x) =>{

    if(typeof x === 'number'){
        return true;
    }else{
        return false;
    }
}

let numstring = "50";

console.log(numstring + " " + typeof numstring);

let ris = e(numstring);

console.log(ris);

numstring = 50;

console.log(numstring + " " + typeof numstring);

ris = e(numstring);

console.log(ris);