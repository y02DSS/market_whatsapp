from django.shortcuts import render

from .models import MainAdmin
from .forms import CreatePost

from datetime import datetime
import os
import shutil
from zipfile import ZipFile

def index(request):
    all_info = MainAdmin.objects.all()
    return render(request, "main.html", {"all_info": all_info})


def page_folder(request, name_page):
    info_json = MainAdmin.objects.get(name=name_page)
    info_all_temp = []
    for item in info_json.info["posts"]:
        info_temp = []
        info_temp.append(item["name"])
        info_temp.append(item["time"])
        info_all_temp.append(info_temp)

    info_all_temp.reverse()
    info_all = []
    temp_name = []
    for temp_item in info_all_temp:
        if temp_item[0] not in temp_name:
            temp_name.append(temp_item[0])
            info_all.append(temp_item)

    if len(info_all) == 0:
        info_all = "Записи не найдены"
    return render(request, "page_folder.html", {"info": info_all, "name_page": name_page})


def page_folder_human(request, name_page, name_human):
    info_json = MainAdmin.objects.get(name=name_page)
    info_all_temp = []
    for item in info_json.info["posts"]:
        info_temp = []
        if item["name"] == name_human:
            info_temp.append(item["img"])
            info_temp.append(item["description"])
            info_temp.append(item["time"])
            info_temp.append(f'./static/uploads/zip/{item["name"]}-{item["time"].replace(":", "-").replace("/", "-")}.zip'[1:])
            info_all_temp.append(info_temp)
    return render(request, "page_folder_human.html", {"name_page": name_page, "name_human": name_human, "info": info_all_temp})


def create(request):
    all_info = MainAdmin.objects.all()
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            objects = form.cleaned_data["objects"]
            message = form.cleaned_data["message"]
            photos = request.FILES.getlist('photos')
            dir = 'static\\uploads\\Main\\'
            if not os.path.exists(os.path.dirname(dir)):
                os.makedirs(os.path.dirname(dir))
            for f in photos:
                with open(dir + str(f), 'wb') as dest:
                    for chunk in f.chunks():
                        dest.write(chunk)

            time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            all_photos = []
            for photo in photos:
                all_photos.append(str(photo.name)) 

            with ZipFile(f"{name}.zip", "w") as newzip:
                for one_photo in all_photos:
                    newzip.write(f"./static/uploads/Main/{one_photo}")

            shutil.move(f'./{name}.zip', f'./static/uploads/zip/{name}-{time.replace(":", "-").replace("/", "-")}.zip')

            entry = [
                {
                "name": name,
                "img": all_photos,
                "description": message,
                "time": time
                }
            ]
            data = MainAdmin.objects.filter(name=objects)[0].info
            data["posts"] += entry
            MainAdmin.objects.filter(name=objects).update(info=data)
    else:
        form = CreatePost()
    
    return render(request, "create.html", {"all_info": all_info, 'form': form})