from api import models, serializers
from api.permissions import IsOwner

from rest_framework import permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView


class PasswordViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PasswordSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )
    search_fields = (
        "site",
        "email",
    )
    ordering_fields = ("site", "email", "created")

    def get_queryset(self):
        return models.Password.objects.filter(user=self.request.user)


class EncryptedPasswordProfilesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EncryptedPasswordProfilesSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )

    def get_queryset(self):
        return models.EncryptedPasswordProfiles.objects.filter(user=self.request.user)


class BackwardCompatibleTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.BackwardCompatibleTokenObtainPairSerializer

    token_obtain_pair = TokenObtainPairView.as_view()
