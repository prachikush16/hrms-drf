from django.db import models

# Create your models here.

class BaseModel(models.Model):
    '''Base model with common fields.'''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(BaseModel):
    '''Model representing an employee.'''
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    
class Attendance(BaseModel):
    '''Model representing attendance records for employees.'''
    STATUS_CHOICES=[
        ('Present','Present'),
        ('Absent','Absent'),
        ('Leave','Leave'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('employee', 'date')
        
    def __str__(self):
        return f"{self.employee.full_name} - {self.date} - {self.status}"
