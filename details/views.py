from django.http import Http404
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Students  
from .serializers import StudentSerializer  

 # Create your views here.  
      
class StudentView(APIView):  
    def get(self, request,format=None):  
        result = Students.objects.all()  
        serializers = StudentSerializer(result, many=True)  
        return Response(serializers.data)  
      
    def post(self, request,fromat=None):  
        serializer = StudentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
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