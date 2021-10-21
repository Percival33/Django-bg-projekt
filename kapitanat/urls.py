from django.urls import path
from .views import (
    JachtListView,
    JachtDetailView,
    JachtCreateView,
    JachtUpdateView,
    JachtDeleteView,
    UserJachtListView
)
from . import views

urlpatterns = [
    path('', JachtListView.as_view(), name='kapitanat-home'),
    path('user/<str:username>', UserJachtListView.as_view(), name='user-jachty'),
    path('jacht/<int:pk>/', JachtDetailView.as_view(), name='jacht-detail'),
    path('jacht/nowy/', JachtCreateView.as_view(), name='jacht-create'),
    path('jacht/<int:pk>/update/', JachtUpdateView.as_view(), name='jacht-update'),
    path('jacht/<int:pk>/delete/', JachtDeleteView.as_view(), name='jacht-delete'),
    path('about/', views.about, name='kapitanat-about'),
]

