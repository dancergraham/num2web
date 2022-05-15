async function getWords() {
    let data = {
        number: document.getElementById("number").value,
        language: document.getElementById("language").value
        };
    if (data.language == ""){return;}
    let r = await fetch("http://localhost:5000/num2words/",
    {
        method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data),
    });
    let words = await r.text();
    document.getElementById("words").innerHTML = words;
}