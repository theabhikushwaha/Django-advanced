from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentSubmissionTests(TestCase):
    def test_valid_submission_saves_student(self):
        response = self.client.post(
            reverse("student_list"),
            {
                "name": "Ada Lovelace",
                "age": 20,
                "email": "ada@example.com",
                "student_id": "S123",
                "major": "Mathematics",
            },
        )

        self.assertRedirects(response, reverse("student_list"))
        self.assertEqual(Student.objects.count(), 1)
        student = Student.objects.get()
        self.assertEqual(student.name, "Ada Lovelace")
        self.assertEqual(student.student_id, "S123")

    def test_invalid_submission_does_not_save_student(self):
        response = self.client.post(
            reverse("student_list"),
            {
                "name": "Ada Lovelace",
                "age": "not-an-age",
                "email": "not-an-email",
                "student_id": "S123",
                "major": "Mathematics",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a whole number")
        self.assertEqual(Student.objects.count(), 0)
