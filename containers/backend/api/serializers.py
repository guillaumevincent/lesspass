from api import models
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Password
        fields = (
            "id",
            "login",
            "site",
            "lowercase",
            "uppercase",
            "symbols",
            "numbers",
            "counter",
            "length",
            "version",
            "created",
            "modified",
        )
        read_only_fields = ("created", "modified")

    def create(self, validated_data):
        user = self.context["request"].user
        return models.Password.objects.create(user=user, **validated_data)


class EncryptedPasswordProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EncryptedPasswordProfiles
        fields = (
            "id",
            "password_profile",
            "created",
            "modified",
        )
        read_only_fields = ("created", "modified")

    def create(self, validated_data):
        user = self.context["request"].user
        return models.EncryptedPasswordProfiles.objects.create(user=user, **validated_data)


class BackwardCompatibleTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({"token": data["access"]})
        return data
