from rest_framework import serializers
from employee.models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        
class AttendanceSerialize4r(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
        validators = [] 
    
    def validate(self, data):
        if not self.instance:
            if Attendance.objects.filter(
                employee=data["employee"],
                date=data["date"]).exists():
                raise serializers.ValidationError(
                    {"detail": "Attendance already marked for this date."}
                )
        return data
    