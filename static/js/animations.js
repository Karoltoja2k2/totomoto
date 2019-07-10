const description = document.querySelector(".offers-description");


description.addEventListener('mouseover', e => {
    const title = document.querySelector(".offers-title");
    title.classList.toggle("small");
});

description.addEventListener('mouseout', e => {
    const title = document.querySelector(".offers-title");
    title.classList.toggle("small");
});

const navbar = document.querySelector("nav");
window.onscroll = () => {
    "use strict";
    if
}