from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser, MultiPartParser

from django.db.models import Q
from django.contrib.auth.hashers import make_password



class CustomAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.resolver_match.url_name == 'docs' or request.resolver_match.url_name == 'api_schema':
            return True
        return super().has_permission(request, view)
    

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomAuthenticated]

    def get_object(self):
        return self.request.user



class UserCreateView(APIView):
    serializer_class = UserSerializer
    parser_classes = [JSONParser, MultiPartParser]
    
    def post(self, request, *args, **kwargs):
        data = request.data

        user_serializer = self.serializer_class(data={
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
            'email': data.get('email'),
            'is_active': True
        })

        if user_serializer.is_valid():
            user = user_serializer.save(password=make_password(data.get('password')))
            image = request.FILES.get('image')
            if image:
                user.image = image
                user.save()

            return Response({
                "data":None,
                "status":True,
                "message":"User Registered Successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


