from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
