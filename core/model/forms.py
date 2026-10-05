from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "email", "student_id", "major"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter name"}),
            "age": forms.NumberInput(attrs={"placeholder": "Enter age"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter email"}),
            "student_id": forms.TextInput(
                attrs={"placeholder": "Enter student ID"}
            ),
            "major": forms.TextInput(attrs={"placeholder": "Enter major"}),
        }
