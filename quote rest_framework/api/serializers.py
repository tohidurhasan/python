from rest_framework import serializers

from quote.models import Quote
from quote.models import QuoteCategory

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote' , 'author']


class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory
        fields = ('__all__')

