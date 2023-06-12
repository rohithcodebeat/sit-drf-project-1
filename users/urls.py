from django.urls import path 
from .views import dummy_api, DummyRestAPIView, DummyRestAPIIDView

urlpatterns = [
    path("dummy-api/", dummy_api, name="dummy_api"),
    path("dummy-rest-api/", DummyRestAPIView.as_view(), name="dummy_rest_api"),
    path("dummy-rest-api/<id>/", DummyRestAPIIDView.as_view(), name="dummy_rest_api"),
]


