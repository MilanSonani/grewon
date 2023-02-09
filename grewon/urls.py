from .views import CheckUserAvailibity
from django.urls import path
urlpatterns = [
    path('', CheckUserAvailibity.as_view())
]