from django.shortcuts import render, redirect
from django.utils import timezone
from django.template.defaulttags import register

from .models import *


@register.filter
def get_range(value):
    return range(value)

@register.filter
def hash(h, key):
    return h[key]

def sign_up(request):
    data = {}

    if (request.method == 'POST'):
        passw = request.POST.get('passw')

        is_user_exists = VotingProcess.objects.filter(enter_code=passw)
        if is_user_exists.exists():
            voting_id = is_user_exists.first().voting_id
            user_id = is_user_exists.first().user_id

            date = timezone.localtime()
            voting_details = Voting.objects.filter(id=voting_id).first()
            user_fullname = Users.objects.filter(id=user_id).first()

            request.session['variants'] = voting_details.variants
            request.session['fullname'] = user_fullname.full_name

            start_date = voting_details.start_date
            finish_date = voting_details.finish_date

            # check with datetime
            if start_date <= date <= finish_date:
                voting_details_process = VotingProcess.objects.filter(user_id=user_id, voting_id=voting_id).first()
                chosen = voting_details_process.chosen

                if not chosen:
                    data['error_message'] = ''
                    return redirect('/voting')
                else:
                    data['error_message'] = 'HasVoted'
            else:
                data['error_message'] = 'VotingFinished'
        else:
            data['error_message'] = 'NotExist'

    return render(request, 'sign-up.html', {'data': data})


def vote(request):
    data = {}

    req = request.session['variants']
    for key in req.keys():
        data[key] = req[key]

    data['data_size'] = len(req["surnames"])
    data['user_fullname'] = request.session['fullname']

    return render(
                    request,
        'voting.html',
                    context=data
                  )
