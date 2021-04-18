from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('',views.index, name="index"),
    path('<int:item_id>',views.details, name="details"),
    path('add_item',views.add_item, name="additem"),
    path('update_item/<int:item_id>',views.update_item, name="updateitem"),
    path('delete_item/<int:item_id>',views.delete_item, name="deleteitem"),
]