from django.urls import path, include


urlpatterns = [
    path('', include('product.urls')),
    path('api/v1/', include('product.api.urls')),
]
