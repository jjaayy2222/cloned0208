'''
from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['recipient', 'subject', 'body']

    def clean_recipient(self):
        recipient = self.cleaned_data.get('recipient')
        if not recipient or '@' not in recipient:
            raise forms.ValidationError('Invalid email address')  # 이메일 주소 유효성 검사
        return recipient
        '''
        
from django import forms
from .models import Email
from django.contrib.auth.models import User


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['recipient', 'subject', 'body']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter message'}),
        }

    # recipient를 ModelChoiceField로 수정하여 사용자만 선택할 수 있도록
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_recipient(self):
        recipient = self.cleaned_data.get('recipient')
        if not recipient or recipient == self.instance.sender:
            raise forms.ValidationError('You cannot send an email to yourself.')
        return recipient
