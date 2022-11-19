function open_add_item_modal(){
let modal = document.getElementById('add_item_Modal')
let mymodal = new bootstrap.Modal(modal)
mymodal.show()
}

function open_edit_item_modal(){
   
let edit = document.getElementById('edit_item_Modal')
let edit_modal = new bootstrap.Modal(edit)
edit_modal.show()
}

function form_submit(){
    document.querySelector(".submit").submit();
    
    console.log('ok')
}

function form_update(){
    document.querySelector(".update").submit();
    
    console.log('ok')
}




