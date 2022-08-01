from django.http import Http404
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import *
from .serializers import *
from rest_framework import viewsets

 # Create your views here. 
    
class StudentView(APIView):  
    def get(self, request, format = None):  
        result = Students.objects.all()  
        serializers = StudentSerializer(result, many=True)  
        return Response(serializers.data)  
      
    def post(self, request, format = None):  
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():  
            serializer.save()
            student_id = serializer.data["id"]
            FullDetail.objects.create(student_id = student_id)
           
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get_object(self,pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        data=self.get_object(pk)
        serializer = StudentSerializer(data)  
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        data=self.get_object(pk)
        serializer=StudentSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        data=self.get_object(pk)
        serializer=StudentSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        data=self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MarkView(APIView):  
    def get(self, request,format=None):  
        result = Marks.objects.all()  
        serializers = MarkSerializer(result, many=True)  
        return Response(serializers.data)  
      
    def post(self, request,format=None):  
        serializer = MarkSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save() 
            mark_id = serializer.data["id"]
            student_id = serializer.data["student_name"]
            result = FullDetail.objects.get(student_id = student_id)
            result.mark_id = mark_id
            result.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkDetailView(APIView):
    def get_object(self,pk):
        try:
            return Marks.objects.get(pk=pk)
        except Marks.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        data=self.get_object(pk)
        serializer = MarkSerializer(data)  
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        data=self.get_object(pk)
        serializer=MarkSerializer(data,data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        data=self.get_object(pk)
        serializer=MarkSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data=self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FullDetailView(APIView):
    def get(self, request, format=None):  
        detail = FullDetail.objects.all()
        serializers = DetailSerializer(detail, many = True) 
        return Response(serializers.data)

class DetailView(APIView):
    def get_object(self,pk):
        try:
            return FullDetail.objects.get(student_id=pk)
        except FullDetail.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = DetailSerializer(data) 
        student_id = serializer.data['student_id']
        student_detail = Students.objects.get(id = student_id)
        student_name = student_detail.id
        mark_detail = Marks.objects.get(student_name = student_name)
        context = {
            "student_name" : student_detail.first_name+" "+student_detail.last_name,
            "phy_mark" : mark_detail.phy_mark,
            "chem_mark" : mark_detail.chem_mark,
            "bio_mark" : mark_detail.bio_mark
        }
        return Response(context)