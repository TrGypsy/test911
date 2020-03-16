//Slider expansion selector

const menuNav = document.querySelector(".menu-nav");

//Hamburger animation selector

const menuBarTop = document.querySelector(".top");
const menuBarMiddle = document.querySelector(".middle");
const menuBarBottom = document.querySelector(".bottom");

// CLICK EVENT ON HAMBURGER

const menuBtn = document.querySelector(".hamburger");

menuBtn.addEventListener("click", () => {
  //Expansion
  menuNav.classList.toggle("expanded")
  //Animation
  menuBtn.classList.toggle("hamburger-animate")
  menuBarMiddle.classList.toggle("middle-animate");
  menuBarTop.classList.toggle("top-animate");
  menuBarBottom.classList.toggle("bottom-animate");
});