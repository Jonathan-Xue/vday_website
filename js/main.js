var video = document.querySelector("#webcam #video");
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