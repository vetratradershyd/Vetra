const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {

    navMenu.classList.toggle("active");

});



const contactForm = document.querySelector("#contact-form");

if (contactForm) {

    contactForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        const formData = new FormData(contactForm);

        try {

            const response = await fetch(
                contactForm.action || window.location.href,
                {
                    method: "POST",
                    body: formData
                }
            );

            if (response.ok) {

                contactForm.reset();

                const message = document.createElement("div");

                message.className = "success-message";

                message.innerHTML =
                    '<i class="bi bi-check-circle-fill"></i> ' +
                    'Request sent successfully!';

                contactForm.parentNode.insertBefore(
                    message,
                    contactForm
                );

            }

        } catch (error) {

            console.error("Form submission error:", error);

        }

    });

}