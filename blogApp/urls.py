from django.urls import path,include
from . import views

urlpatterns = [
   
    
    path('',views.blog_list,name="home") , 
    path('singleBlog/<int:pk>',views.blog_detail,name="singleBlog") , 
    path('createBlog/',views.create_blog_post,name="createBlog") , 
]
