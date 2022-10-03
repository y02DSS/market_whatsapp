const openFolder = document.getElementsByClassName("open-folder")

for (let i = 0; i < openFolder.length; i++) {
    openFolder[i].addEventListener('click', function() {
        var name_folder = openFolder[i].name
        var name_element = document.getElementById(name_folder)
        if (name_element.style.display == 'flex'){
            name_element.style.display = 'none'
        }else{
            name_element.style.display = 'flex'
        }
    });
}

