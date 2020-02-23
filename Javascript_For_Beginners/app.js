const text = document.querySelector(".title");
const changeColor = document.querySelector(".changeColor");

changeColor.addEventListener("click", function(){
    text.classList.add('change');
})

const userList = document.querySelector(".name-list");
const listInput = document.querySelector(".list-input");
const addListBtn = document.querySelector(".addListBtn");

addListBtn.addEventListener("click", function() {
    // Create on Li out of thin air
    const newli = document.createElement('LI');
    const liContent = document.createTextNode('sdf');
    // Add the input value inside that new Li
    newli.appendChild(liContent);
    // Attaching the Li to the user list
    userList.appendChild(newLi);
});

for(user of userList){
    user.addEventListener('click', function(){
    this.style.color - "red";
    });
}

