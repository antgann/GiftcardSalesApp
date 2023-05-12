from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('giftcardbalance/', views.gift_card_balance_view, name='giftcardbalance-view'),
    path('sellingprice/', views.selling_price_view, name='sellingprice-view'),
    path('network/', views.network_view, name='network-view'),
    path('postaladdress/', views.postal_address_view, name='postaladdress-view'),
    path('emailaddress/', views.email_address_view, name='emailaddress-view'),
    path('thankyou/', views.thank_you_view, name='thankyou-view'),
    path('results/', views.results_view, name='results-view')
]
