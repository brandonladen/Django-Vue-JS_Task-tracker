from rest_framework import serializers
from .models import To_Do_List

class toDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = To_Do_List
        fields = '__all__'