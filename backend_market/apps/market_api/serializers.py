from rest_framework import serializers
#Import models to serialize
from .models import *



class SellerSerializer(serializers.ModelSerializer):
    """
    API Serializer for the market_api.Seller model. Returns JSON as default data format.
    """

    class Meta:
        model = Seller 
        fields = ['user', 'description','skills', 'link']



class BuyerSerializer(serializers.ModelSerializer):
    """
    Serializes the market_api.Buyer model inot various data formats. JSON is the default.
    """

    class Meta:
        model = Buyer 
        fields = ['user','link']



class GigSerializer(serializers.ModelSerializer):
    """
    Serializes the market_api.Gig model inot various data formats. JSON is the default.
    """

    class Meta:
        model = Gig 
        fields = ['title','description', 'seller', 'price', 'status', 'link']



class OrderSerializer(serializers.ModelSerializer):
    """
    Serializes the market_api.Order model inot various data formats. JSON is the default.
    """

    class Meta:
        model = Order 
        fields = ['due_date','order_date', 'buyer', 'gig', 'total_cost', 'amount', 'status', 'link']

    
class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializes the market_api.Review model inot various data formats. JSON is the default.
    """

    class Meta:
        model = Review 
        fields = ['delivery_rating', 'expectations_rating', 'needs_rating','public_review', 'seller_rating', 'order']


