from django.urls import path , include
from authentication import urls as authentication_urls
from .views import authentication, my_logout

urlpatterns = [
    path('', authentication, name = "url_authentication"),
    path('logout/', my_logout, name='url_logout'),

]