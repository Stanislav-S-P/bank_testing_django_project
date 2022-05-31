from typing import List
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BankTestModel


def choices_method() -> List:
    """Функция - создает список кортежей для choices, полей формы ChoiceField"""
    object_list = []
    models = BankTestModel.objects.all()
    index = 0
    for i_object in models:
        if index == 10:
            break
        else:
            object_list.append((
                (i_object.first_answer, i_object.first_answer),
                (i_object.second_answer, i_object.second_answer),
                (i_object.third_answer, i_object.third_answer)
            ))
        index += 1
    return object_list


def label_method():
    """Функция - создает список для label, полей формы ChoiceField"""
    object_list = []
    models = BankTestModel.objects.all()
    index = 0
    for i_object in models:
        if index == 10:
            break
        else:
            object_list.append(i_object.question)
        index += 1
    return object_list


class MyForm(UserCreationForm):
    """
    Класс - переопределяющий стандартный класс django UserCreationForm.
    Форма регистрации пользователя.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Только буквы, цифры и @/./+/-/_.'
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password1'].help_text = '<ul class="list-reset"><li>Пароль не должен быть похож' \
                                             ' на личную информацию.</li><li>Пароль должен' \
                                             ' содержать не менее 8 символов.</li><li>Пароль не может быть' \
                                             ' часто используемым паролем.</li><li>Пароль не может быть' \
                                             ' полностью числовым.</li></ul>'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].help_text = 'Повторите пароль'
        self.fields['password2'].label = 'Подтверждение пароля'


class QuestionForm(forms.Form):
    """
    Класс -  форма тестирования пользователей. Содержит 10 полей с вопросами, тип поля ChoiceField
    """
    one = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[0], label=label_method()[0])
    two = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[1], label=label_method()[1])
    three = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[2], label=label_method()[2])
    four = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[3], label=label_method()[3])
    five = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[4], label=label_method()[4])
    six = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[5], label=label_method()[5])
    seven = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[6], label=label_method()[6])
    eight = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[7], label=label_method()[7])
    nine = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[8], label=label_method()[8])
    ten = forms.ChoiceField(widget=forms.RadioSelect(), choices=choices_method()[9], label=label_method()[9])
