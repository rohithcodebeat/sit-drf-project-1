from rest_framework import serializers
from .models import StudentDetailModel

# create a serializer that converts a models objects into json objects 
# GET
class StudentDetailModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        # fields = ["id","name", "roll_no", "date_of_birth", "branch", "year_of_joining"]
        # fields = "__all__"
        exclude = ("id",)

class StudentDetailModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        # fields = ["id","name", "roll_no", "date_of_birth", "branch", "year_of_joining"]
        # fields = "__all__"
        exclude = ("id","created_at")
    
    def validate(self, data):
        if StudentDetailModel.objects.filter(roll_no=data["roll_no"]).exists():
            return serializers.ValidationError({"message" : "student with this roll no is already exists"})
        return data


class StudentDetailModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        # fields = ["id","name", "roll_no", "date_of_birth", "branch", "year_of_joining"]
        # fields = "__all__"
        exclude = ("id","created_at")
    
   



