from django.urls import path
from django.urls.resolvers import URLPattern
from .views import TitleDetailView, TitleListView , TitleCreateView, TitleUpdateView, TitleDeleteView


urlpatterns = [
    path("", TitleListView.as_view(), name="title_list"),
    path("<int:pk>/", TitleDetailView.as_view(), name="title_detail"),
    path("new/", TitleCreateView.as_view(), name="title_create"),
    path("<int:pk>/update/", TitleUpdateView.as_view(), name="title_update"),
    path("<int:pk>/delete/", TitleDeleteView.as_view(), name="title_delete"),
]