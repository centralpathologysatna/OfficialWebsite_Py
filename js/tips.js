const tips = [
"Drink enough water before urine tests.",
"Fasting blood sugar requires 8–10 hours fasting.",
"Avoid heavy exercise before lipid profile test.",
"Carry previous reports for better diagnosis.",
"Stay hydrated before sample collection.",
"Do not consume alcohol 24 hours before liver function tests.",
"Morning samples are preferred for hormone tests.",
"Inform the lab about medicines you are taking."
];

let i = 0;

const tipElement = document.getElementById("tipText");

if (tipElement) {

tipElement.classList.add("fade-tip");

setInterval(() => {

tipElement.classList.add("fade-out");

setTimeout(() => {

i = (i + 1) % tips.length;

tipElement.textContent = tips[i];

tipElement.classList.remove("fade-out");

}, 800);

}, 6000);

}
