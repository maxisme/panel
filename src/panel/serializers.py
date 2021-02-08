from rest_framework import serializers


class MessageSerializer(serializers.Serializer):  # type: ignore[misc]
    text = serializers.CharField(max_length=300)
    priority = serializers.ChoiceField(
        (
            ("high",) * 2,
            ("default",) * 2,
            ("low",) * 2,
        ),
        default="default",
    )
    font = serializers.CharField(default="LCD_FONT")
