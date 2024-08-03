
from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, PasswordsChangeView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home" ),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like-post'),
    #path('1/password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('1/password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password_success'),
    

]