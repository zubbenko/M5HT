from movie_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movie', views.movie_api_view),
    path('api/v1/director', views.director_api_view),
    path('api/v1/review', views.review_api_view),

]
