from django.conf import settings

from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    priority = serializers.ChoiceField(
        (
            ('default', 'default'),
            ('low', 'low'),
            ('high', 'high'),
        ),
        default='low'
    )
