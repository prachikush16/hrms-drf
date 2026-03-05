from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from employee.models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerialize4r

class EmployeeViewSet(viewsets.ModelViewSet):
    '''ViewSet for managing Employee records.'''
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['employee_id', 'full_name', 'email', 'department']
    search_fields = ['employee_id', 'full_name', 'email']
    ordering_fields = ['created_at', 'updated_at']

class AttendanceViewSet(viewsets.ModelViewSet):
    '''ViewSet for managing Attendance records.'''
    queryset = Attendance.objects.all().order_by('-created_at')
    serializer_class = AttendanceSerialize4r
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['employee', 'date', 'status']
    search_fields = ['employee__full_name']
    ordering_fields = ['date']
    
    def get_queryset(self):
        queryset=super().get_queryset()
        employee_id=self.request.query_params.get("employee")
        
        if employee_id:
            queryset=queryset.filter(employee_id=employee_id)
            
        return queryset