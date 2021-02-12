from rest_framework import serializers

MAX_LEN_WITHOUT_SLIDE = 10

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
    timeout = serializers.IntegerField(default=4)
    font = serializers.CharField(default="LCD_FONT")
