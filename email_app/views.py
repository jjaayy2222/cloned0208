'''
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Email
from .forms import EmailForm
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q

@login_required
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user  # 발신자 설정

            # 이메일 수신자가 User 모델일 경우
            if isinstance(email.recipient, str):  
                messages.error(request, "Invalid recipient. Please enter a valid email.")
                return render(request, 'email_app/send_email.html', {'form': form})

            email.save()
            try:
                send_mail(
                    email.subject,
                    email.body,
                    email.sender.email if email.sender.email else "no-reply@example.com",  # 이메일이 없을 경우 기본값 설정
                    [email.recipient.email],  
                    fail_silently=False,
                )
                messages.success(request, 'Email sent successfully!')
                return redirect('email_list')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
        else:
            messages.error(request, 'Form is not valid. Please check your inputs.')
    else:
        form = EmailForm()
    
    return render(request, 'email_app/send_email.html', {'form': form})

@login_required
def email_list(request):
    received_emails = Email.objects.filter(recipient=request.user)
    sent_emails = Email.objects.filter(sender=request.user)
    
    return render(request, 'email_app/email_list.html', {
        'received_emails': received_emails,
        'sent_emails': sent_emails,
    })

@login_required
def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id, Q(recipient=request.user) | Q(sender=request.user))
    
    return render(request, 'email_app/email_detail.html', {'email': email})
'''

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .forms import EmailForm
from .models import Email
import logging

# 로깅 설정
logger = logging.getLogger(__name__)

@login_required
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user  # 발신자 설정

            # 이메일 저장
            email.save()

            try:
                # 이메일 전송
                send_mail(
                    email.subject,
                    email.body,
                    email.sender.email if email.sender.email else "no-reply@example.com",  # 발신자 이메일이 없을 경우 기본값
                    [email.recipient.email],
                    fail_silently=False,
                )

                messages.success(request, 'Email sent successfully!')
                return redirect('email_list')  # 이메일 목록 페이지로 리다이렉션
            except Exception as e:
                # 로깅과 에러 처리
                logger.error(f'Error sending email: {e}')
                messages.error(request, f'Error sending email: {e}')
        else:
            messages.error(request, 'Form is not valid. Please check your inputs.')
    else:
        form = EmailForm()

    return render(request, 'email_app/send_email.html', {'form': form})

@login_required
def email_list(request):
    received_emails = Email.objects.filter(recipient=request.user)
    sent_emails = Email.objects.filter(sender=request.user)

    return render(request, 'email_app/email_list.html', {
        'received_emails': received_emails,
        'sent_emails': sent_emails,
    })

@login_required
def email_detail(request, email_id):
    email = get_object_or_404(Email, id=email_id, recipient=request.user)

    return render(request, 'email_app/email_detail.html', {'email': email})
