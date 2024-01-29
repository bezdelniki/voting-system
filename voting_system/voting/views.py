from django.shortcuts import render, redirect
from .models import *

def sign_up(request):
    data = {}

    if (request.method == 'POST'):
        passw = request.POST.get('passw')

        is_user_exists = VotingProcess.objects.filter(enter_code=passw)
        if is_user_exists.exists():
            data['error_message'] = ''
            return redirect('/voting')
        else:
            data['error_message'] = 'NotExist'

    return render(request, 'sign-up.html', { 'data': data })

def vote(request):
    return render(request, 'voting.html')
