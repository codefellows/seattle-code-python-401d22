from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('', MovieListView.as_view(), name='list_view'),
    path('<int:pk>', MovieDetailView.as_view(), name='detail_view'),
    path('new', MovieCreateView.as_view(), name='create_view'),
    path('<int:pk>/edit', MovieUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', MovieDeleteView.as_view(), name='delete_view'),
]
