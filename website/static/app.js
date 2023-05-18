// dom elements
var itemForm = document.querySelector('.popup-content')
var itemList = document.querySelector('.item')

var titleInput = document.querySelector('.title')
var descInput = document.querySelector('.description')
var priceInput = document.querySelector('.price')


let items = JSON.parse(localStorage.getItem('items')) || [] 

if (localStorage.getItem('items')){
    items.map((item) => {
        createItem(item)
    })
}
// submit form
itemForm.addEventListener('submit', (e)=>{
    e.preventDefault()

    const titleValue = titleInput.value
    const descValue = descInput.value
    const priceValue = priceInput.value

    if (titleValue == ''){
        return
    }

    const item = {
        id: new Date().getTime(),
        title: titleValue,
        description: descValue,
        price: priceValue
    }

    
    items.push(item)
    localStorage.setItem('items', JSON.stringify(items))

    createItem(item)
    itemForm.reset()

    titleInput.focus()
    descInput.focus()
    priceInput.focus()

})

itemList.addEventListener('click' , (e)=>{
    if(e.target.classList.contains('remove-task')){
        const itemid = e.target.closest('li').id
        removeItem(itemid)
    }
})

// create item
function createItem(item){
    const itemEl = document.createElement('li')
    itemEl.setAttribute('id', item.id)
    
    const itemElMarkup = `

        <div>
            <h6>${item.title}</h6>
            <p>${item.price}</p>
        </div>
        <div>
            <p>${item.description}</p>
            <img src="../src/close.png" alt="" class = "remove-task">
        </div>
    `
itemEl.innerHTML = itemElMarkup

itemList.appendChild(itemEl)
}

function removeItem(itemid){
    items = items.filter((item)=> item.id != parseInt(itemid))
    localStorage.setItem('items', JSON.stringify(items))
    document.getElementById(itemid).remove()
}

// functionality to pop-up the filds for input

document.getElementById("btn").addEventListener("click", function(){
    document.querySelector(".pop-up").style.display = "flex"
})
document.querySelector(".close").addEventListener("click", function(){
    document.querySelector(".pop-up").style.display = "none"
})