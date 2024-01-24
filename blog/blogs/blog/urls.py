from django.urls import include, path


from djoser.views import UserViewSet as DjoserUserViewSet
from djoser.urls import authtoken
from .views import ArticleCreateView, ArticleDeleteView, ArticleUpdateView, ListeArticlesAPI

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/posts/', ListeArticlesAPI.as_view(), name='liste_articles_api'),
    path('api/posts/create/', ArticleCreateView.as_view(), name='create-article'),
    path('api/posts/<int:pk>/update/', ArticleUpdateView.as_view(), name='update-article'),
    path('api/posts/<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete-article')
]
