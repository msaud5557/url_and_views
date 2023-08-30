from django.urls import path
from django.contrib import admin

from  .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name="home_view"),
    path('about/',views.about_view,name="about_view"),
    path('profile/<username>/',views.user_profile_view,name="user_profile_view"),
    path('profile_redirect/<username>/',views.profile_redirect),
    path('html/<username>/<bootcamp>/',views.html),
    # path('home_file/',views.home_file),
    path('stu_dynamic/', views.student_list),
    
    
    
]