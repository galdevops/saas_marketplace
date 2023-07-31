from rest_framework import serializers
#Import models to serialize
from .models import Seller, Buyer



class SellerSerializer(serializers.ModelSerializer):
    """
    API Serializer for the market.Seller model. Returns JSON as default data format.
    """

    class Meta:
        model = Seller 
        fields = ['user', 'description','skills', 'link']

class BuyerSerializer(serializers.ModelSerializer):
    """
    Serializes the market.Buyer model inot various data formats. JSON is the default.
    """

    class Meta:
        model = Buyer 
        fields = ['user','link']

# class ProductSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     Serializes the market.Product model various data format. JSON is the default.
#     """
#     seller = serializers.HyperlinkedRelatedField(
#         queryset = Seller.objects.all(),
#         view_name = "market_api:seller_detail",
#         lookup_field = "link",
#     )
#     bids = serializers.HyperlinkedRelatedField(
#         #queryset = Bid.objects.all(),
#         many = True,
#         view_name = "market_api:bid_detail",
#         lookup_field = "pk",
#         read_only = True
#     )
#     link = serializers.SlugField(allow_blank=True, read_only=True)

#     class Meta:
#         model = Product 
#         fields = ['seller','bids','name','desc','quantity','price','link']

# class BidSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     market.Bid model serializer. Returns various data formats. JSON is default.
#     """
#     buyer = serializers.HyperlinkedRelatedField(
#         queryset = Buyer.objects.all(),
#         view_name = "market_api:buyer_detail",
#         lookup_field = "link"
#     )
#     gig = serializers.HyperlinkedRelatedField(
#         queryset = GigRequest.objects.all(),
#         view_name = "market_api:gigrequest_detail",
#         lookup_field = "link",
#     )

#     bid_date = serializers.DateTimeField(read_only=True)
#     class Meta:
#         model = Bid
#         fields = ['pk','buyer','product','amount','bid_date','accepted']


