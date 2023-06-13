from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import views , status






data = {
    "name" : "First API",
    "format" : "Json",
    "category" : "http",
    "framework" : "django"
}

# Create your views here.
def dummy_api(request):
    if request.method == "POST":
        pass
    elif request.method == "PUT":
        pass 
    elif request.method == "DELETE":
        pass 
    else:
        return JsonResponse(data)



class DummyRestAPIView(views.APIView):
    # Read
    def get(self, request):
        return Response(data, status=status.HTTP_200_OK)
    # Create
    def post(self, request):
        req_data = request.data
        return Response(req_data, status=status.HTTP_200_OK)
    # Update
    def put(self, request):
        req_data = request.data
        return Response(req_data, status=status.HTTP_200_OK)
    # Delete
    def delete(self, request):
        return Response({"message" : "Id is deleted"})

    
# 200_OK & 400_BAD_REQUEST
    


class DummyRestAPIIDView(views.APIView):

    def get(self, request, id):
        return Response({"id" : id})



