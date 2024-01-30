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
            votind_id = is_user_exists.first().voting_id
            date = timezone.localtime()
            voting_details = Voting.objects.filter(id=votind_id).first()

            request.session['variants'] = voting_details.variants
            start_date = voting_details.start_date
            finish_date = voting_details.finish_date

            # check with datetime
            if start_date <= date <= finish_date:
                data['error_message'] = ''
                return redirect('/voting')
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

    data['data_size'] = len(req) - 1

    print(data)

    return render(
                    request,
        'voting.html',
                    context=data
                  )
