from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginp,name='login'),
    path('register/',views.register,name='register'),
    path('dash/',views.dash,name='dash'),
    path('udetail/',views.udetail,name='udetail'),
    path('recommend/',views.rec,name='rec'),
    path('logout/',views.logoutUser,name='logout'),
    path('about',views.about,name="about"),
    path('aboutl',views.aboutl,name="aboutl"),
]
