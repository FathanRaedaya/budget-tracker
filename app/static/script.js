function toggleEditMode(tableId) {
    const editButton = document.querySelector('.btn-secondary');
    const inputFields = document.querySelectorAll(`#${tableId} input`);
    if (editButton.innerText === "Edit Mode") {
        editButton.innerText = "Read Mode";
        inputFields.forEach(field => field.removeAttribute('readonly'));
    } else {
        editButton.innerText = "Edit Mode";
        inputFields.forEach(field => field.setAttribute('readonly', 'true'));    
    } 
}

document.addEventListener('DOMContentLoaded', function() {
    let flashMessages = document.querySelectorAll('.flash-message');

    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.remove();
        }, 3500); 
    });
});