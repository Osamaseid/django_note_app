from django.contrib.auth.models import User
from rest_framework import serializers 

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        etra_kwargs = {'password': {'write_only':True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
