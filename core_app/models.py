from django.db import models


class Department(models.TextChoices):
    DEVELOPMENT = 'DEV', 'Development'
    TESTING = 'TEST', 'Testing'
    HR = 'HR', 'Human Resources'


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    department = models.CharField(max_length=20, choices=Department.choices)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

