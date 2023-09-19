from rest_framework import serializers
from .models import Counter


class CounterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = "__all__"


class CounterUpdateSerializer(serializers.Serializer):
    counter = serializers.IntegerField(required=True)
    action = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        instance.counter = validated_data.get("counter", instance.counter)
        instance.action = validated_data.get("action", instance.action)
        return instance
