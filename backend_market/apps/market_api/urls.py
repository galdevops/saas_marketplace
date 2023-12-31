from django.urls import re_path,path
from .views import *

app_name = "market_api"

market_api_urlpatterns = [
    
    # re_path(r'^api/v1/kuery/limited/', viewt, name="viewt"),
    # re_path(r'^api/v1/kuery/test/', kuery_test, name="kuery_test"),
    # re_path('api/v1/kuery/', query_request_generator, name="query_request"),
    # path('api/v1/queries/', call_queries, name="call_queries"),
    # path('api/v1/add_segment/', add_segment, name="add_segment"),
    # path('api/v1/edit_segment/', edit_segment, name="edit_segment"),
    # path('api/v1/segments/', segments, name="segments"),
    # path('api/v1/modifiers/', modifiers, name="modifiers"),
    # path('api/v1/query_content/', query_content, name="query_content"),
    # path('status/check', health_check, name="healthcheck")
    path('api/v1/sellers/', SellerListView.as_view(), name="seller_list"),
    path('api/v1/buyers/', BuyerListView.as_view(), name="buyer_list"),
    path('api/v1/gigs/', GigListView.as_view(), name="gig_list"),
    path('api/v1/orders/', OrderListView.as_view(), name="order_list"),
    path('api/v1/reviews/', ReviewListView.as_view(), name="review_list"),
    # path('api/v1/reviews/<slug:link>/', ReviewDetailView.as_view(), name="review_detail"),
    path('api/v1/orders/<slug:link>/', OrderDetailView.as_view(), name="order_detail"),
    path('api/v1/gigs/<slug:link>/', GigDetailView.as_view(), name="gig_detail"),
    path('api/v1/sellers/<slug:link>/', SellerDetailView.as_view(), name="seller_detail"),
    path('api/v1/buyers/<slug:link>/', BuyerDetailView.as_view(), name="buyer_detail"),
    path('api/v1/accounts/<int:pk>/', UserDetailView.as_view(), name="user_detail"),
    # path('api/v1/products/<slug:link>/', ProductDetailView.as_view(), name="product_detail"),
    # path('api/v1/bids/<int:pk>/', BidDetailView.as_view(), name="bid_detail"),
    path('api/v1/root/', market_api_root, name="digisouq_api_root")
    
]