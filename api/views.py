from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class EmployeeListCreateView(APIView):
      def get(self,request,*args,**kwargs):
            return Response(data={"message":"listing employee"})
      
      def post(self,request,*args,**kwargs):
            return Response(data={"message":"creating employee"})
      
class EmployeemixinView(APIView):
      
       def get(self,request,*args,**kwargs):
            return Response(data={"message":"retrieving sepcific emp detail"})
       
       def put(self,request,*args,**kwargs):
            return Response(data={"message":"editing emp detail"})
       
       def delete(self,request,*args,**kwargs):
            return Response(data={"message":"deleting emp detail"})

      