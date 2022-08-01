from dataclasses import fields
from typing_extensions import Required
from rest_framework import serializers  
from details.models import *
  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Marks
        fields = ["id", "phy_mark", "chem_mark", "bio_mark", "student_name"]
        depth = 1


# class DetailSerializer(serializers.ModelSerializer):
#     student_id = serializers.PrimaryKeyRelatedField(
#         queryset=Students.objects.all(),
#         required=True,
#         source='students',
#     )
#     mark_id = serializers.PrimaryKeyRelatedField(
#         queryset=Marks.objects.all(),
#         allow_null=True,
#         required=False,
#         source='marks',
#     )
#     class Meta:
#         model = FullDetail
#         fields = ("student_id", "mark_id")

class DetailSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(required = True)
    mark_id = serializers.IntegerField(required = False)
    class Meta:
        model = FullDetail
        fields = ("student_id", "mark_id")


