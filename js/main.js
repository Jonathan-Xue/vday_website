// Typewriter
const text = "It'd be a shame for a girl like you to spend it alone. :("
const typingDelay = 75;

let textSpan = document.querySelector(".typewriter .typewriter-text");
let charIndex = 0;
function type() {
  if (charIndex < text.length) {
    textSpan.textContent += text.charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  }
}
type();

// Webcam
let video = document.querySelector("#webcam #video");
if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
    })
    .catch(function (err) {
      console.log(err);
    });
}

document.querySelector("#webcam #overlay").addEventListener("click", () => {
  document.querySelector("#webcam #overlay").style.visibility = "hidden";
  document.querySelector("#webcam-caption").style.visibility = "visible";
});