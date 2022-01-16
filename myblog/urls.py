from django.urls import path
# from . import views
from . views import HomeView, ArticleDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, category_view, category_list_view, like_view, AddCommentView
urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='Edit_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='Delete_post'),
    path('category/<str:cats>/', category_view, name='category'),
    path('category-list/', category_list_view, name='category-list'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('article/<int:pk>/Comment/', AddCommentView.as_view(), name='add_comment'),

]
