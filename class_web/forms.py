from django import forms
from .models import MessageBox,ClassActive,ClassNews,ClassNote
class MessForm(forms.ModelForm):
    class Meta:
        model=MessageBox
        fields=['name','text']
        labels={'text':'','name':''}
        #widgets={'text':forms.Textarea(attrs={'cols':80})}

class NoteForm(forms.ModelForm):
    class Meta:
        model=ClassNote
        fields=['otitle','otext']
        labels={'otitle':'','otext':''}

class NewsForm(forms.ModelForm):
    class Meta:
        model=ClassNews
        fields=['ntitle','ntext']
        labels={'ntitle':'','ntext':''}

class ActiveForm(forms.ModelForm):
    class Meta:
        model=ClassActive
        fields=['atitle','atext']
        labels={'atitle':'','atext':''}