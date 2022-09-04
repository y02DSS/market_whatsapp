from django import forms

from .models import MainAdmin

class CreatePost(forms.Form):
    name = forms.ChoiceField(label='Кто публикует?', choices=(("Наташа", "Наташа"), ("Миша", "Миша"), ("Юра", "Юра")))
    objects = forms.ChoiceField(label='Выбрать объект', choices=[])
    message = forms.CharField(label='Добавьте описание', widget=forms.Textarea)
    photos = forms.FileField(label='Добавьте фотографии', widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
        self.fields['objects'].choices = [(c.name, c.name) for c in MainAdmin.objects.all()]
