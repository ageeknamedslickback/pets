from django.views.generic import CreateView, ListView

from pets.models import Pet


class PetListView(ListView):
    """View all pets in the database."""

    model = Pet


class PetCreateView(CreateView):
    """View to create a pet."""

    model = Pet
    fields = ["name", "species", "year_of_birth"]
