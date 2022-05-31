from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from app_bank.forms import MyForm, QuestionForm
from app_bank.models import BankTestModel, UserAnswer


class AnotherLoginView(LoginView):
    """
    Класс-контроллер для авторизации пользователя
    """
    template_name = 'users/login.html'
    next_page = '/'


class AnotherLogoutView(LogoutView):
    """
    Класс-контроллер для выхода из аккаунта пользователя
    """
    template_name = 'users/logout.html'


class SignUpView(CreateView):
    """
    Класс-контроллер регистрации аккаунта пользователя
    """
    form_class = MyForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def home_view(request):
    """
    Класс-контроллер главной страницы
    """
    return render(request, 'bank_testing/home.html')


def bank_testing_view(request):
    """
    Класс-контроллер страницы тестирования и вывода результата тестирования. Содержит метоы GET и POST.
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            index = 0
            for elem in form:
                for i_objects in BankTestModel.objects.all():
                    if i_objects.question == elem.label:
                        user_answer = UserAnswer()
                        user_answer.user = request.user
                        user_answer.question = i_objects.question
                        user_answer.answer = elem.data
                        if i_objects.correct_answer == elem.data:
                            index += 1
                            user_answer.status = 'корректный'
                        else:
                            user_answer.status = 'не корректный'
                        user_answer.save()
            percent = index * 10
            if percent == 100:
                result_text = 'Отличный результат! Вы мастер своего дела!'
            elif percent >= 70:
                result_text = 'Хороший результат! Есть недочёты.'
            elif percent >= 40:
                result_text = 'Много ошибок. Надо подтянуть теорию'
            else:
                result_text = 'Не позволительный результат. Вы плохо разбираетесь в современной безопасности'
            context = {'percent': percent, 'result_text': result_text}
            return render(request, 'bank_testing/result.html', context)
    else:
        form = QuestionForm
        questions = BankTestModel.objects.all()
        content = {'form': form, 'question': questions}
        return render(request, 'bank_testing/bank_testing.html', content)
