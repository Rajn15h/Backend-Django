from rest_framework import serializers
from app.models import info
class infoserializer(serializers.ModelSerializer):
    class Meta:
        model=info
        fields='__all__'