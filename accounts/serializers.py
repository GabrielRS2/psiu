from rest_framework import serializers
from .models import Account
class AccountSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
                "id",
                "password",
                "email",
                "first_name",
                "last_name",
                "joined_date",
            ]