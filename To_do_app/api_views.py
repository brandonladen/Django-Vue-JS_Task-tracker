from rest_framework import viewsets
from .serializers import toDoListSerializer
from rest_framework.pagination import PageNumberPagination 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from .models import To_Do_List

class CustomPageNumberPagination(PageNumberPagination): 
    page_size = 100
    page_size_query_param = 'page_size' 
    max_page_size = 100 
    
class todoViewset(viewsets.ModelViewSet):
    queryset = To_Do_List.objects.all()
    serializer_class = toDoListSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    