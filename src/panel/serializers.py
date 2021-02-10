from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    priority = serializers.ChoiceField(
        (
            ('high', 'high'),
            ('default', 'default'),
            ('low', 'low'),
        ),
        default='low'
    )
    slide = serializers.BooleanField(default=True)
    timeout = serializers.IntegerField(default=10)
