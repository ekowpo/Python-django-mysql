from django import forms
from .models import Semester

SEMESTER_TYPE = (
    ('F', 'Fall'),
    ("S1", 'Summer 1'),
    ("S2", 'Summer 2'),
    ('W', 'Winter'),
)
class SemesterCreateForm(forms.Form):
    semester= forms.ChoiceField(choices=SEMESTER_TYPE, required=True)
    startDate = forms.CharField(max_length=4, required=True)
    endDate = forms.CharField(max_length=4, required=True)
    dne = forms.DateField(('%d-%m-%Y', '%Y-%m-%d'))

class SemesterModelForm(forms.ModelForm):
    class Meta:
        model=Semester
        fields =[
            'semesterType',
            'startDate',
            'endDate',
            'dne',
        ]