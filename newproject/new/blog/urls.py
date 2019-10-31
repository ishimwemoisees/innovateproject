from django.urls import path


from . import views
urlpatterns = [
      path('', views.pome, name='blog-pome'),
      path('abot/', views.abot, name='blog-abot'),
]
