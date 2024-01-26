let availablekeywords = [
    "django",
    "python",
    "Java",
    "csharp",
];

const resultBox = document.getElementById("box-result");
const filteredlist = document.getElementById("filteredlist");
const inputBox = document.getElementById("input-box");

inputBox.onkeyup = function(){
    let result = [];
    let input = inputBox.value;
    // console.log(availablekeywords);
    // console.log(input);
    if(input.length != 0){
        result = availablekeywords.filter((keyword)=>{
            filteredlist.innerHTML ="";
            return keyword.toLowerCase().includes(input.toLowerCase());
        });
        // console.log(result);
       
    }
    display(result);

    if(!result.length){
        resultBox.innerHTML = '';
    }
}

function display(result){
    
    resultBox.appendChild(filteredlist);
    result.forEach(element => {
        var li = document.createElement('li');
        li.innerText = element; 
        filteredlist.appendChild(li);
        
    });

    // const content = result.map((list)=>{
    //     var li = document.createElement('ul');
    //     li.innerText = list;
    //     resultBox.appendChild(li);
        // return `<li onclick=selectInput(this)> + ${list} + </li>`;
    // });

    // resultBox.innerHTML = `<ul> + content.join('') + </ul>`;
    
}

function selectInput(list){
    inputBox.value = list.innerHTML;
    resultBox.innerHTML = '';
    
}

