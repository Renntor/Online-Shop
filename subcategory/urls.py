from django.urls import path
from subcategory.apps import SubcategoryConfig
from subcategory.views import SubcategoryListCreateAPIView, SubcategoryRetrieveUpdateDestroyAPIView

app_name = SubcategoryConfig.name

urlpatterns = [
    path('<slug:slug>/', SubcategoryListCreateAPIView.as_view(), name='list_create_subcategory'),
    path('', SubcategoryRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_subcategory'),
]