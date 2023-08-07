import "./style.css";

const sourceTextLang = document.querySelector(
  "#source-text"
) as HTMLInputElement;
const targetTextLang = document.querySelector(
  "#target-text"
) as HTMLParagraphElement;

export function translate() {
  const query = sourceTextLang.value.trim().toLowerCase();

  if (query.trim() === "") {
    targetTextLang.textContent = "";
    return;
  }

  fetch("words.json")
    .then((response) => {
      if (!response.ok) {
        throw new Error("HTTP error " + response.status);
      }
      return response.json();
    })
    .then((data) => {
      let targetData = data["papua-id"];
      let isFound = false;

      for (let key in targetData) {
        if (key.toLowerCase().startsWith(query)) {
          targetTextLang.textContent = key + " = " + targetData[key];
          isFound = true;
          break;
        }
      }

      if (!isFound) {
        targetTextLang.textContent = "Kata yang dicari tidak ditemukan";
      }
    })
    .catch((error) => {
      console.log("Failed to fetch dictionary:", error);
    });
}

sourceTextLang.addEventListener("input", translate);
