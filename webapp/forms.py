from django import forms
from .models import Task

STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
]

class TaskForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    due_date = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    details = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Task
        fields = ['description', 'details', 'status', 'due_date']

