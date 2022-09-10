from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("summary/", login_required(views.ELV.as_view()), name="entry-list"),
    path("entry/<int:pk>",login_required(views.EDV.as_view()),name="entry-detail"),
    path("create", login_required(views.ECV.as_view()), name="entry-create"),
    path("entry/<int:pk>/update", login_required(views.EUV.as_view()), name="entry-update",),
    path("entry/<int:pk>/delete", login_required(views.EntryDeleteView.as_view()), name="entry-delete",),
    path("about/", views.About, name="about-page"),
]
