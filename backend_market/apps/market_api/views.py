from django.http import Http404
from rest_framework.response import Response 
from rest_framework import generics 
from rest_framework.reverse import reverse 
from django.conf import settings
#Import the Market app's models and API Serializers
from .models import *
from .serializers import *
from ..accounts.serializers import UserCustomSerializer
from ..accounts.models import User
# https://github.com/techbuktu/DigiSouq/blob/master/
#Import the Authentication and Permission classes to control access to certain
# API endpoints/data
from rest_framework.decorators import (api_view, authentication_classes)
from rest_framework.authentication import (
    BasicAuthentication, SessionAuthentication, TokenAuthentication
)
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
)

from rest_framework import filters
import datetime


@api_view(['GET'])
def market_api_root(request, format=None):
    """
    Root/home page of the DigiSouq APIs
    """
    return Response({
        'users': reverse('market_api:user_list', request=request, format=format),
        'sellers': reverse('market_api:seller_list', request=request, format=format),
        'buyers': reverse('market_api:buyer_list', request=request, format=format),
        'products': reverse('market_api:product_list', request=request, format=format),
        'bids': reverse('market_api:bid_list', request=request, format=format),
        'Obtain Auth Token': reverse('market_api:auth_token', request=request, format=format), 
    })



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Performs GET (one), PUT and DELETE operations on the User API.
    """
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    lookup_field = "pk"
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class SellerListView(generics.ListCreateAPIView):
    """
    Performs GET (all) and POST actions on the SellerSerializer.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return self.create(request, *args, **kwargs)


class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Makes GET (one), PUT and DELETE requests against the Seller API.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]



class BuyerListView(generics.ListCreateAPIView):
    """
    Makes GET (all) and POST requests against the Buyer API endpoint
    """
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return self.create(request, *args, **kwargs)



class BuyerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Makes GET, PUT and DELETE requests a single Buyer API endpoint
    """
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]



class GigListView(generics.ListCreateAPIView):
    """
    Performs GET (all) and POST actions on the SellerSerializer.
    """
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        seller, created = Seller.objects.get_or_create(user=request.user)
        request.data['seller'] = seller.id
        return self.create(request, *args, **kwargs)


class GigDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Makes GET, PUT and DELETE requests a single Buyer API endpoint
    """
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]



class OrderListView(generics.ListCreateAPIView):
    """
    Performs GET (all) and POST actions on the SellerSerializer.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        buyer, created = Buyer.objects.get_or_create(user=request.user)
        giged = Gig.objects.get(link=request.data['gig'])
        request.data['gig'] = giged.id
        request.data['total_cost'] =  request.data['amount'] * giged.delivery_time
        request.data['due_date'] =  datetime.datetime.now() + datetime.timedelta(days=giged.delivery_time)
        request.data['buyer'] = buyer.id
        return self.create(request, *args, **kwargs)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Makes GET, PUT and DELETE requests a single Buyer API endpoint
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]



class ReviewListView(generics.ListCreateAPIView):
    """
    Performs GET (all) and POST actions on the SellerSerializer.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "link"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        request.data['order'] = Order.objects.get(link='1690907620galdevops').id
        return self.create(request, *args, **kwargs)


# class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Makes GET, PUT and DELETE requests a single Buyer API endpoint
#     """
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     lookup_field = "link"
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]