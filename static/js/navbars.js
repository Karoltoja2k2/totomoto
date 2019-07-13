let scrollpos = window.scrollY;
const header = document.querySelector(".navbar");
const headerHeight = header.offsetHeight / 2;

console.log(headerHeight / 2);

window.addEventListener('scroll', function () {
    scrollpos = window.scrollY;
    if (scrollpos >= headerHeight) {
        header.classList.add("white");
    } else {
        header.classList.remove("white");
    }
    console.log(scrollpos);
});