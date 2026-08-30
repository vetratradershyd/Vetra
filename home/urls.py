from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path(
            "products/<slug:slug>/",
            views.product_detail,
            name="product_detail",
        ),
    path('contact/',views.contact,name='contact')
]



