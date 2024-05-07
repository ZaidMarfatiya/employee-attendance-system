from datetime import date
from django import forms
from core_app.models import Employee, Attendance


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'department']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'is_present']
        widgets = {
            'employee': forms.HiddenInput(),
            'date': forms.DateInput(format='%Y-%m-%d')
        }

