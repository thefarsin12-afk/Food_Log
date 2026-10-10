from django.contrib.auth.models import User

from rest_framework import serializers

from food_log.models import MealRecordModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class MealRecordSerializer(serializers.ModelSerializer):  

    class Meta:

        model = MealRecordModel

        fields = '__all__'

        read_only_fields = ["id","owner","created_at"]

