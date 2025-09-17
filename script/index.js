import DATA from "./data.js";

document.addEventListener("DOMContentLoaded", () => {
  const carsSection = document.querySelector("#our-cars");
  const carousel = document.getElementById("carsCarousel");

  if (!carousel || !carsSection) return;

  const carouselInner = document.querySelector(".carousel-inner");
  const items = [];

  DATA.Cars.forEach((item, index) => {
    const { name, mode, image, bgImg, specs } = item;
    items.push(corouselCars(bgImg, image, name, mode, specs, index === 0));
  });

  carouselInner.innerHTML = items.join("");
});

function corouselCars(bg, img, name, modelNo, specs, isActive) {
  const all_specs = Object.entries(specs);
  const html = all_specs
    .map(([key, value]) => `<li>${key.replaceAll("_", " ")}: ${value}</li>`)
    .join("");

  return `
    <div class="carousel-item ${isActive ? "active" : ""}" data-bg="${bg}">
      <div class="row align-items-center">
        <div class="col-md-6">
          <img src="${img}" class="d-block w-100 rounded" alt="${name}" />
        </div>

        <div class="col-md-6 text-white text-center p-4">
          <h3 class="car-name">${name}</h3>
          <p class="car-model">Model: ${modelNo}</p>
          <ul class="list-unstyled">
            ${html}
          </ul>
          <a href="https://wa.me/8184888828/?text=$I want to book ${name}" class="btn btn-outline-warning" style="border-radius: 10px;">Book Now</a>
        </div>
      </div>
    </div>
  `;
}
