let availablekeywords = [
    "django",
    "python",
    "Java",
    "csharp",
];

const resultBox = document.querySelector(".result-box");
const inputBox = document.getElementById("SearchBar");

inputBox.onkeyup = function(){
    let result = [];
    let input = inputBox.value;
    if(input.lenght){
        result = availablekeywords.filter((keyword)=>{
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        console.log(result);
    }
    display(result);

    if(result.length){
        resultBox.innerHTML = '';
    }
}

function display(result){
    const content = result.map((list)=>{
        return "<ul onclick=selectInput(this)>" + list + "</ul>";
    });

    resultBox.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function selectInput(list){
    inputBox.value = liat.innerHTML;
    resultBox.innerHTML = '';
}