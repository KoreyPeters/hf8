from django.urls import path
from . import views

urlpatterns = [
    path("", views.polium_root, name="polium"),
    path("candidates/", views.candidates_list, name="polium_candidates_list"),
    path(
        "candidates/<str:sqid>",
        views.candidates_detail,
        name="polium_candidates_detail",
    ),
    path("elections/", views.elections_list, name="polium_elections_list"),
    path(
        "elections/<str:sqid>", views.elections_detail, name="polium_elections_detail"
    ),
    path("politicians/", views.politicians_list, name="polium_politicians_list"),
    path(
        "politicians/<str:sqid>",
        views.politicians_detail,
        name="polium_politicians_detail",
    ),
]
