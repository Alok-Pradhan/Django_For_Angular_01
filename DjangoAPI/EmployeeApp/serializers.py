from django.db.models import fields
from rest_framework import serializers
from EmployeeApp.models import Departments,Employees

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                     'DepartmentName')

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                    'EmployeeName',
                    'Department', 
                    'DateOfJoining',
                    'PhotoFileName')