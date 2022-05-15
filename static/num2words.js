async function getWords() {
    let number = document.getElementById("number").value;
    let language_selector = document.getElementById("language");
    let language = language_selector.value;
    let r = await fetch("http://localhost:5000/" + language + "/" + number, {mode: 'no-cors'});
    let words = await r.text();
    document.getElementById("words").innerHTML = words;
}