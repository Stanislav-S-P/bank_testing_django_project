from django.urls import path
from app_bank.views import AnotherLoginView, AnotherLogoutView, SignUpView, home_view, bank_testing_view

urlpatterns = [
    path('login/', AnotherLoginView.as_view(), name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home_view, name='home'),
    path('bank_testing/', bank_testing_view, name='bank_testing'),
]