from django.urls import path

from ecommerce import views

urlpatterns =[
    path('find_by_category/',views.FindProductByCategory.as_view()),
    path('find_by_name/',views.FindProductByCategory.as_view()),
    path('add_to_cart/',views.AddItemToCart.as_view()),
    path('remove_from_cart/',views.RemoveItemFromCart.as_view())
]