from django.urls import path
from . import views
urlpatterns = [
	path('recruiter/', views.register_recruiter, name="reg_recruiter"),
	path('partner/', views.register_partner, name="reg_partner"),
	path('worker/', views.register_worker, name="reg_worker"),
	path('home/', views.home, name="home"),
    ]