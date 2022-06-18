// file: render.js

function renderFromTemplate() {
  fetch(
    "https://raw.githubusercontent.com/bids-standard/bids-methods/main/templates/func.mustache"
  )
    .then((response) => response.text())
    .then((template) => {
      var rendered = Mustache.render(template, { duration: "30" });
      document.getElementById("target").innerHTML = rendered;
    });
  var metadata = readJson();
  console.log(metadata);
}

function readJson() {
  // http://localhost:8080
  fetch(
    "https://raw.githubusercontent.com/bids-standard/bids-methods/main/demos/data/ds000117/task-facerecognition_bold.json"
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("HTTP error " + response.status);
      }
      return response.json();
    })
    .then((json) => {
      this.metadata = json;
      return this.metadata;
    })
    .catch(function () {
      this.dataError = true;
    });
}
