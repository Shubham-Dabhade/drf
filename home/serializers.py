from rest_framework import serializers
from .models import Person,Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    country = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = "__all__"

    def get_country(self,obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color_name':color_obj.color_name}

    def validate(self,data):
        if data['age'] <18:
            raise serializers.ValidationError("age should be greater than 18")
        return data