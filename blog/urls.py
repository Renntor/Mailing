from blog.apps import BlogConfig
from django.urls import path
from blog.views import BlogDeleteView, BlogCreateView, BlogDetailView, BlogListView

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog')

]

