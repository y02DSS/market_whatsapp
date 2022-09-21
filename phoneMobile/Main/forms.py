from django import forms

from .models import MainAdmin

class CreatePost(forms.Form):
    name = forms.ChoiceField(label='Кто публикует?', choices=(("Рюмин А", "Рюмин А"), ("Калиненко В", "Калиненко В"), 
                                                            ("Маликов В", "Маликов В"), ("Бабаев Д", "Бабаев Д"),
                                                            ("Краснецов С", "Краснецов С"), ("Лучин М", "Лучин М"),
                                                            ("Донских А", "Донских А"), ("Мишин П", "Мишин П"),
                                                            ("Волков С", "Волков С"), ("Шелофастов А", "Шелофастов А"),
                                                            ("Ровба О", "Ровба О"), ("Чащин А", "Чащин А"),
                                                            ("Фёдоров К", "Ровба О"), ("Чепитов Ю", "Чепитов Ю"),
                                                            ("Князев С", "Князев С")))
    objects = forms.ChoiceField(label='Выбрать объект', choices=[])
    message = forms.CharField(label='Добавьте описание', widget=forms.Textarea, required=False)
    photos = forms.FileField(label='Добавьте фотографии', 
                            widget=forms.ClearableFileInput(attrs={'multiple': True}), 
                            required=False)


    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
        self.fields['objects'].choices = [(c.name, c.name) for c in MainAdmin.objects.all()]


    def clean_field(self):
        data = self.cleaned_data['message']
        if not data:
            data = ' '
        return data