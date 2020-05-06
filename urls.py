from django.urls import path , include
from django.contrib.auth import views as auth_views
from authentication import urls as authentication_urls
from .views import authentication, my_logout, signup, update_profile, psi_confirmado
from django.conf.urls import url

urlpatterns = [
    path('', authentication, name = "url_authentication"),
    path('logout/', my_logout, name='url_logout'),
    path('login/', auth_views.LoginView.as_view(), name='url_login'),
    path('signup/', signup, name='url_signup'),
    path('psi_confirmado/', psi_confirmado, name='url_psi_confirmado'),
    path('update_profile/', update_profile, name='url_update_profile'),

]