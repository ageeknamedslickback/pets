"""Pet app URL conf dispatcher."""

from django.urls import path

from pets.views import PetCreateView, PetListView

urlpatterns = [
    path("", PetListView.as_view(), name="pets"),
    path("add/", PetCreateView.as_view(), name="create"),
]
