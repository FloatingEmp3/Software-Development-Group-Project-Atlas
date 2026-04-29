from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user, status='inbox').order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def sent(request):
    messages = Message.objects.filter(sender=request.user, status='sent').order_by('-timestamp')
    return render(request, 'messaging/sent.html', {'messages': messages})

@login_required
def drafts(request):
    messages = Message.objects.filter(sender=request.user, status='draft').order_by('-timestamp')
    return render(request, 'messaging/drafts.html', {'messages': messages})

@login_required
def new_message(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        action = request.POST.get('action')
        recipient = get_object_or_404(User, id=recipient_id)
        status = 'sent' if action == 'send' else 'draft'
        Message.objects.create(
            sender=request.user,
            recipient=recipient,
            subject=subject,
            body=body,
            status=status
        )
        if status == 'sent':
            Message.objects.create(
                sender=request.user,
                recipient=recipient,
                subject=subject,
                body=body,
                status='inbox'
            )
        return redirect('inbox')
    return render(request, 'messaging/new_message.html', {'users': users})

@login_required
def view_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.is_read = True
    message.save()
    return render(request, 'messaging/view_message.html', {'message': message})