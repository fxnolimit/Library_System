document.addEventListener("DOMContentLoaded", function (event) {
    var addBookbtn = document.getElementById('addBookBtn');
    addBookbtn.addEventListener('click', function(){
        window.location.href = "/create";
    });

    var listBooksBtn = document.getElementById('listBooksBtn');
    listBooksBtn.addEventListener('click', function(){
        window.location.href = "/list_all";
    });
});