from django.shortcuts import render
from .models import StudentDetailModel
from rest_framework import views, status 
from rest_framework.response import Response
# Create your views here.

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
        # request.data.pop("id")
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



