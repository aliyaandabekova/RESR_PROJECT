from rest_framework import  serializers
from rest_framework.exceptions import ValidationError

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_sum(self,obj):
        total_sum = obj.product.price * obj.quantity
        if obj.payment_method == 'wallet' and obj.profile.wallet >= total_sum:
            obj.profile.wallet -= total_sum
            obj.profile.order_count += 1
            obj.profile.save()
        else:
            raise ValidationError
        if obj.profile.sale:
            total_sum = total_sum - (total_sum * obj.profile.sale)
        obj.total_sum = total_sum
        obj.save()
        return total_sum