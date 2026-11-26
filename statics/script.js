const resumeInput = document.querySelector("#resume");
const fileName = document.querySelector("#file-name");
const uploadBox = document.querySelector(".upload-box");
const form = document.querySelector("#analysis-form");

if (resumeInput && fileName) {
    resumeInput.addEventListener("change", () => {
        const file = resumeInput.files[0];
        fileName.textContent = file ? file.name : "Choose a PDF or DOCX file";
    });

    ["dragenter", "dragover"].forEach((eventName) => {
        uploadBox.addEventListener(eventName, (event) => {
            event.preventDefault();
            uploadBox.classList.add("dragging");
        });
    });

    ["dragleave", "drop"].forEach((eventName) => {
        uploadBox.addEventListener(eventName, () => {
            uploadBox.classList.remove("dragging");
        });
    });

    uploadBox.addEventListener("drop", (event) => {
        if (event.dataTransfer.files.length) {
            resumeInput.files = event.dataTransfer.files;
            fileName.textContent = event.dataTransfer.files[0].name;
        }
    });
}

if (form) {
    form.addEventListener("submit", () => {
        const button = form.querySelector("button[type='submit']");
        button.classList.add("loading");
        button.querySelector("span").textContent = "Analyzing...";
        button.disabled = true;
    });
}