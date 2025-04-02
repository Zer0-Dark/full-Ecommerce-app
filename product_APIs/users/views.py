from rest_framework import generics, status
from .serializers import RegistrationSerializer, LoginSerializer, CustomUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken 



class RegistrationAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh":str(token),
                          "access":str(token.access_token)}
        return Response(data= data, status=status.HTTP_201_CREATED )
    

class LoginAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data
        data = CustomUserSerializer(user).data
        token = RefreshToken.for_user(user)
        # Retrieve or create a token for the authenticated user.
        data["tokens"] = {"refresh":str(token),
                        "access":str(token.access_token)}
        return Response(data= data, status=status.HTTP_200_OK )