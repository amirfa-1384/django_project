from django.urls import path
from .views import BlogComent, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailViewComment, LikeView

urlpatterns = [
    path('like/<int:pk>', LikeView,name="like_post"),
    path('post/<int:pk>/comments/', BlogDetailViewComment.as_view(), name='Comment_detail'),
    path('post/<int:pk>/comment/', BlogComent.as_view(), name='Post_Comment'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    
]