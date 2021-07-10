from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.UplaodTextAPIView.as_view()),

]
