document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#movetotop').onclick = () => {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    };

    window.onscroll = () => {
        if (document.body.scrollTop > 15 || document.documentElement.scrollTop > 15 ) {
            document.getElementById("movetotop").style.display = "block";
        } else {
            document.getElementById("movetotop").style.display = "none";
        };
    };    
});
