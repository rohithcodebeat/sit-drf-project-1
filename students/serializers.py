from rest_framework import serializers
from .models import StudentDetailModel, AddressDetailModel


class AddressDetailModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetailModel
        fields = "__all__"

# create a serializer that converts a models objects into json objects 
# GET
class StudentDetailModelListSerializer(serializers.ModelSerializer):
    address_detail = serializers.SerializerMethodField()
    class Meta:
        model = StudentDetailModel
        # fields = ["id","name", "roll_no", "date_of_birth", "branch", "year_of_joining"]
        # fields = "__all__"
        exclude = ("id",)
    
    def get_address_detail(self, obj):
        try:
            data = AddressDetailModelListSerializer(obj.address, many=False).data 
        except:
            data = {}
        return data 

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
    
   



