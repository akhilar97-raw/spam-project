async function checkSpam() {
    let msg = document.getElementById("msg").value;

    let response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
    });

    let data = await response.json();

    let resultText = document.getElementById("result");
    resultText.innerText = data.result;

    if (data.result === "Spam") {
        resultText.className = "spam";
    } else {
        resultText.className = "not-spam";
    }
}