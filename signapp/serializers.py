from rest_framework import serializers
from .models import Custumuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Custumuser
        fields=['id','username','email','password']

        