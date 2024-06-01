from django.urls import path, include
from .views import view_task, create_task, delete_task, edit_task
from rest_framework.routers import DefaultRouter 
from .api_views import todoViewset


router = DefaultRouter() 
router.register(r'view', todoViewset) 

urlpatterns = [
    # path('', view_task, name='home'),
    # path('create/', create_task, name='create'),
    # path('<int:task_id>/', delete_task, name='delete'),
    # path('edit/<int:taskid>/', edit_task, name='edit'),
    
    
    path('app/', include(router.urls)), 
]