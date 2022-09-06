from django.urls import path
from . import views

urlpatterns = [
    path("", views.ELV.as_view(), name="entry-list"),
    path("entry/<int:pk>",views.EDV.as_view(),name="entry-detail"),
    path("create", views.ECV.as_view(), name="entry-create"),
    path("entry/<int:pk>/update", views.EUV.as_view(), name="entry-update",),
    path("entry/<int:pk>/delete", views.EntryDeleteView.as_view(), name="entry-delete",),
]