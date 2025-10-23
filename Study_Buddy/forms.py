from django import forms

from Study_Buddy.models import Assignment

class StudentForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"

    def clean_title(self):
        return self.cleaned_data['title'].strip()