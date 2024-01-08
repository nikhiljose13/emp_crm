from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from crm.models import Employees
from api.serializers import EmployeeSerializers
from rest_framework.viewsets import ViewSet
# Create your views here.

class EmployeeListCreateView(APIView):
      def get(self,request,*args,**kwargs):
            qs=Employees.objects.all()
            Serializers=EmployeeSerializers(qs,many=True)
            return Response(data=Serializers.data)
      
      def post(self,request,*args,**kwargs):
            Serializers=EmployeeSerializers(data=request.data)
            if Serializers.is_valid():
                  Serializers.save()
                  return Response(data=Serializers.data)
            else:
                  return  Response(data=Serializers.errors)
          
class EmployeemixinView(APIView):
      
       def get(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            qs=Employees.objects.get(id=id)
            Serializers=EmployeeSerializers(qs,many=False)
            return Response(data=Serializers.data)
       
       def put(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            employee_object=Employees.objects.get(id=id)
            Serializers=EmployeeSerializers(data=request.data,instance=employee_object)
            if Serializers.is_valid():
                  Serializers.save()
                  return Response(data=Serializers.data)
            else:
                  return  Response(data=Serializers.errors)
          
       
       def delete(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            Employees.objects.get(id=id).delete()
            return Response(data={"message":"deleting emp detail"})

# ______________ViewSet___________
       

class EmployeesViewSetView(ViewSet):
      def list(self,request,*args,**kwargs):