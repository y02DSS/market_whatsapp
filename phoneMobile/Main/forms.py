from django import forms

from .models import NameObject

class CreatePost(forms.Form):
    name = forms.ChoiceField(label='Кто публикует?', choices=(("Рюмин А", "Рюмин А"), ("Калиненко В", "Калиненко В"), 
                                                            ("Маликов В", "Маликов В"), ("Бабаев Д", "Бабаев Д"),
                                                            ("Краснецов С", "Краснецов С"), ("Лучин М", "Лучин М"),
                                                            ("Донских А", "Донских А"), ("Мишин П", "Мишин П"),
                                                            ("Волков С", "Волков С"), ("Шелофастов А", "Шелофастов А"),
                                                            ("Ровба О", "Ровба О"), ("Чащин А", "Чащин А"),
                                                            ("Фёдоров К", "Фёдоров К"), ("Чепитов Ю", "Чепитов Ю"),
                                                            ("Князев С", "Князев С"), ("Софронова М", "Софронова М"),
                                                            ("Адиатулина В", "Адиатулина В"), ("Коноплева Е", "Коноплева Е")
                                                            ))
    objects_all = forms.ChoiceField(label='Выбрать раздел', error_messages={'required': 'Это поле обязательно к заполнению'}, choices=[])
    objects = forms.ChoiceField(label='Выбрать объект', error_messages={'required': 'Это поле обязательно к заполнению'}, choices=[])
    message = forms.CharField(label='Добавьте описание', widget=forms.Textarea, required=False)
    photos = forms.FileField(label='Добавьте фотографии', 
                            widget=forms.ClearableFileInput(attrs={'multiple': True}), 
                            required=False)

    def sortByHome(self):
        all_info = NameObject.objects.all()
        list_without_home = []
        dict_home = {}
        temp_name_list_home = set()
        for info in all_info:
            list_without_home.append(info)
            if info.group_home:
                list_without_home.remove(info)
                temp_name_home = info.group_home
                if temp_name_home not in temp_name_list_home:
                    temp_name_list_home.add(temp_name_home)
                    temp_list_home = []
                    for name_home in all_info:
                        if name_home.group_home == temp_name_home:
                            temp_list_home.append(name_home)
                    dict_home[temp_name_home]=(temp_list_home)
        return list_without_home, dict_home.items()

    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
        list_without_home, dict_home = self.sortByHome()
        complete_without_home = []
        for item in list_without_home:
            complete_without_home.append(item)
        self.fields['objects_all'].choices = [(str(';'.join([val.name for val in value])), key) for key, value in dict_home] + [((str(';'.join([item.name for item in complete_without_home]))), "Без раздела")]
        self.fields['objects'].choices = [(c.name, c.name) for c in NameObject.objects.all()]


    def clean_field(self):
        data = self.cleaned_data['message']
        if not data:
            data = ' '
        return data