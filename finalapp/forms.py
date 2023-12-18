from django import forms
from finalapp.models  import Attendance, Student,Course, Notice,Fee,QuestionPaper,AnswerSheet, Result, Subject, Userdata,Userdata1,TeacherJob,StudentFeedback,TeacherFeedback,StudentLeave,TeacherLeave,Contact,StudentForm,Teacher
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentData(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class Userform(forms.ModelForm):
    class Meta:
        model=Userdata
        fields=['Username','Email','Password']

class Userform1(forms.ModelForm):
    class Meta:
        model=Userdata1
        fields=['Username','Email','Password']

class StudentFeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = ['feedback_text']

class TeacherFeedbackForm(forms.ModelForm):
    class Meta:
        model = TeacherFeedback
        fields = ['feedback_text']


class StudentLeaveForm(forms.ModelForm):
    class Meta:
        model = StudentLeave
        fields = ['student','reason', 'start_date', 'end_date']


from django import forms
from .models import TeacherLeave

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = TeacherLeave
        fields = ['teacher', 'reason', 'start_date', 'end_date']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class StudentAdmissionRequestForm(forms.ModelForm):
    class Meta:
        model = StudentForm
        fields = '__all__'


class TeacherJobApplicationForm(forms.ModelForm):
    class Meta:
        model = TeacherJob
        fields = ['first_name', 'last_name', 'enter_email', 'phone_num', 'resume']
        
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content' ]

class QuestionPaperUploadForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['title', 'file']

class AnswerSheetUploadForm(forms.ModelForm):
    class Meta:
        model = AnswerSheet
        fields = ['question_paper', 'file']

class FeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['class_name', 'amount']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

# forms.py
from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'is_present', 'present_status']
class AskDateForm(forms.Form):
    date=forms.DateField()
    
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['class_name', 'result_file']

# forms.py
from django import forms

class DateSelectionForm(forms.Form):
    attendance_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

