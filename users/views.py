from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework.decorators import action 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from users.models import User
from users.serializers import UserSerializer
from users.filters import UserFilter
from users.permissions import IsAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = UserFilter
    search_fields = ['first_name','last_name','rented_date']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        refresh = RefreshToken.for_user(serializer.instance)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        
    @action(methods=["get"], detail=False)
    def verified(self, request):
        queryset = self.queryset.filter(cash_verified=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
