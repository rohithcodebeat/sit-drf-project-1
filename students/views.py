from django.shortcuts import render
from .models import StudentDetailModel
from .serializers import StudentDetailModelListSerializer, StudentDetailModelCreateSerializer, StudentDetailModelUpdateSerializer
from rest_framework import views, status, generics, permissions, authentication
from rest_framework.response import Response
from rest_framework import mixins, generics
# Create your views here.

# url -> normal -> [GET, POST] -> api/student-details/ 
# url -> dynamic -> [GET, PUT, DELET] -> api/student-details/<id>/

class StudentDetailModelReadView(views.APIView):
    def get(self, request):
        queryset = StudentDetailModel.objects.all()
        data = []
        for query in queryset:
            data.append({
                "id" : query.id,
                "name" : query.name,
                "roll_no" : query.roll_no,
                "date_of_birth" : query.date_of_birth,
                "branch" : query.branch,
                "year_of_joining" : query.year_of_joining
            }) 
        return Response({"data" : data})

    def post(self, request):
        if StudentDetailModel.objects.filter(roll_no=request.data["roll_no"]).exists():
            return Response({"message" : "Student with this roll no already exists"}, status=status.HTTP_400_BAD_REQUEST)
        StudentDetailModel.objects.create(
            **request.data 
        )
        return Response({"message" : "okay"})


class SingleStudentDetailModelReadView(views.APIView):
    def get(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            data = {
                    "id" : query.id,
                    "name" : query.name,
                    "roll_no" : query.roll_no,
                    "date_of_birth" : query.date_of_birth,
                    "branch" : query.branch,
                    "year_of_joining" : query.year_of_joining
                }
            return Response(data)
        except Exception as e:
            return Response({"message" : f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        data = request.data
        query = StudentDetailModel.objects.get(id=id)
        query.name = data["name"]
        query.roll_no = data["roll_no"]
        query.date_of_birth = data["date_of_birth"]
        query.branch = data["branch"]
        query.year_of_joining = data["year_of_joining"]
        query.save()
        return Response({"message" : "data was updated"})
    
    def delete(self, request, id):
        StudentDetailModel.objects.get(id=id).delete()
        return Response({"message" : "query was deleted"}, status=status.HTTP_200_OK)

"""

APIVIEW

"""

# Serialization -> Python obj's -> Json
# DeSerialization -> Json -> Python obj's
class StudentDetailModelReadRestAPIView(views.APIView):
    def get(self, request):
        queryset = StudentDetailModel.objects.all()
        # all, filter -> [] -> many = True
        # get -> {} -> many = False
        serializer = StudentDetailModelListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentDetailModelCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "data Added Successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class StudentDetialModelUpdateRestAPIView(views.APIView):
    def get(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            serializer = StudentDetailModelListSerializer(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error" : f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            serializer = StudentDetailModelUpdateSerializer(
                data=request.data, 
                instance=query)
            # 
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "data Updated Successfully"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error" : f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            StudentDetailModel.objects.get(id=id).delete()
            return Response({"message" : "query is deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error" : f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
    


"""

GENETIC API VIEWS

"""

class StudentDetailModelReadRestGenericAPIView(generics.GenericAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    # IsAuthenticated IsAdminUser
    authenticate_class = [authentication.BaseAuthentication]

    def get(self, request):
        queryset = StudentDetailModel.objects.all()
        # all, filter -> [] -> many = True
        # get -> {} -> many = False
        serializer = StudentDetailModelListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentDetailModelCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "data Added Successfully"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class StudentDetialModelUpdateGenericAPIView(generics.GenericAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelUpdateSerializer

    def get(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            serializer = StudentDetailModelListSerializer(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error" : f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        try:
            query = StudentDetailModel.objects.get(id=id)
            serializer = StudentDetailModelUpdateSerializer(
                data=request.data, 
                instance=query)
            # 
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "data Updated Successfully"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error" : f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            StudentDetailModel.objects.get(id=id).delete()
            return Response({"message" : "query is deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error" : f"Something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)


"""
LISTAPIVIEW
CREATEAPIVIEW
LISTCREATEAPIVIEW
"""

class StudentDetailModelListAPIView(generics.ListAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelListSerializer

class StudentDetailModelCreateAPIView(generics.CreateAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelCreateSerializer

class StudentDetailModelListCreateAPIView(generics.ListAPIView, generics.CreateAPIView):
    queryset = StudentDetailModel.objects.all()
    serializer_class = StudentDetailModelCreateSerializer



"""
mixins
"""

# Mixin for list and create functionality
# class MyModelListCreateMixin(mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

# # Mixin for retrieve, update and delete functionality
# class MyModelRetrieveUpdateDeleteMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

# # API view using the mixins
# class MyModelListCreateAPIView(MyModelListCreateMixin, generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class MyModelRetrieveUpdateDeleteAPIView(MyModelRetrieveUpdateDeleteMixin, generics.GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
