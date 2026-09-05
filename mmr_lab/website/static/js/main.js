const topButton = document.getElementById("topBtn");


window.onscroll = function(){

    if (
        document.body.scrollTop > 300 ||
        document.documentElement.scrollTop > 300
    ){

        topButton.style.display = "block";

    }

    else{

        topButton.style.display = "none";

    }

};



topButton.onclick = function(){

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

};