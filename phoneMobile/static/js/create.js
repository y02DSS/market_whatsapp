const id_objects = document.getElementById("id_objects")

const id_objects_all = document.getElementById("id_objects_all")

id_objects_all.addEventListener('click', function() {
    const new_pre_list = id_objects_all.options[id_objects_all.selectedIndex].value
    const new_list = new_pre_list.split(';')
    while (id_objects.firstChild) {
        id_objects.removeChild(id_objects.firstChild);
    }
    for (let i = 0; i < new_list.length; i++) {
        var new_option = document.createElement("option")
        new_option.innerHTML = new_list[i]
        new_option.value = new_list[i]
        id_objects.appendChild(new_option)
    }
})
