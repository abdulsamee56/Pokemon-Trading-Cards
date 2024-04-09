document.addEventListener("DOMContentLoaded", function () {
    var imagePaths = ["../pic/project2pic/01.png", "../pic/project2pic/02.png","../pic/project2pic/03.png","../pic/project2pic/04.png", "../pic/project2pic/05.png",
        "../pic/project2pic/06.png", "../pic/project2pic/07.png", "../pic/project2pic/08.png", "../pic/project2pic/09.png", "../pic/project2pic/10.png",
        "../pic/project2pic/11.png", "../pic/project2pic/12.png", "../pic/project2pic/13.png", "../pic/project2pic/14.png", "../pic/project2pic/15.png",
        "../pic/project2pic/16.png", "../pic/project2pic/17.png", "../pic/project2pic/18.png", "../pic/project2pic/19.png", "../pic/project2pic/20.png"];

    var container = document.getElementById("raindrop-container");

    function createRaindrop() {
        var raindrop = document.createElement("div");
        raindrop.classList.add("raindrop");

        var randomImagePath = imagePaths[Math.floor(Math.random() * imagePaths.length)];
        raindrop.style.backgroundImage = "url('" + randomImagePath + "')";

        raindrop.style.left = Math.random() * window.innerWidth + "px";
        raindrop.style.top = "-30px";

        container.appendChild(raindrop);

        var animationDuration = Math.random() * 6 + 1;
        raindrop.style.animation = "fallAnimation " + animationDuration + "s linear infinite";

        setTimeout(function () {
            container.removeChild(raindrop);
        }, animationDuration * 1000);
    }

    var rainInterval = setInterval(createRaindrop, 200);
});


