from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',views.CustomerView.as_view(),name='customer_get_post'),
    path('<int:pk>/',views.CustomerView.as_view(),name='customer_put_delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)
