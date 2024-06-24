from django.contrib import admin
from django.urls import path
from myapp.views import MsgList,MsgDetail

urlpatterns = [
    path('api/msgs',MsgList.as_view()),
    path('api/msgs/<int:pk>',MsgDetail.as_view()),
    path('admin/', admin.site.urls),

]