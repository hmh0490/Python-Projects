from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE

# list type if pages
class Menulist(generic.ListView):
    # items on the menu ordered reversed
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    # get_context_data is a method of .ListView that we will overwrite
    def get_context_data(self, **kwargs):
        # instead of starting with empty dictinoary, we start with standard
        # dict of ListView class
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context

# when we want to check the individual items
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
