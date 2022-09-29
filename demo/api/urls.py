from django.urls import path
from . import views

urlpatterns = [

    path('all/', views.apiOverview, name="api-overview"),
    path('list/', views.blogList, name="list"),
    path('detail/<str:pk>/', views.blogDetail, name="detail"),
    path('latest/', views.blogLatest, name="Blog Latest"),
    path('astroCurr/', views.astroCurr, name="Astro Current"),
    path('makepost/', views.makeBlog, name="Make Post"),
]