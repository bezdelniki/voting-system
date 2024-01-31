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


@register.filter
def accept_id(i):
    return (i + 1) * 2 - 1


@register.filter
def cancel_id(i):
    return (i + 1) * 2


@register.filter
def generate_var_name(i):
    return f'var{i}'


def sign_up(request):
    data = {}

    if (request.method == 'POST'):
        passw = request.POST.get('passw')

        user_with_password = VotingProcess.objects.filter(enter_code=passw)

        if user_with_password.exists():
            voting_id = user_with_password.first().voting_id

            voting_details = Voting.objects.filter(id=voting_id)
            start_date = voting_details.first().start_date
            finish_date = voting_details.first().finish_date

            date = timezone.now()

            if start_date <= date <= finish_date:
                is_submitted = user_with_password.first().is_submitted

                if not is_submitted:
                    data['error_message'] = ''
                    user = user_with_password.first()
                    user.is_entered = True
                    user.save()

                    request.session['voting_id'] = voting_id
                    request.session['user_id'] = user.id

                    return redirect('/voting')
                else:
                    data['error_message'] = 'AlreadyVoted'
            else:
                data['error_message'] = 'VotingFinished'
        else:
            data['error_message'] = 'NotExist'

    return render(request, 'sign-up.html', {'data': data})


def vote(request):
    data = {
        'names': [],
        'surnames': [],
        'birth': [],
        'role': [],
        'position': []
    }

    user_id = request.session.get('user_id')
    voting_id = request.session.get('voting_id')

    user_fullname = Users.objects.filter(id=user_id).first().full_name
    data['user_fullname'] = user_fullname

    all_candidates = list(Candidate.objects.filter(voting_id=voting_id).all())
    for candidate in all_candidates:
        data['names'].append(candidate.names)
        data['surnames'].append(candidate.surnames)
        data['birth'].append(candidate.birth)
        data['role'].append(candidate.role)
        data['position'].append(candidate.position)

    data['data_length'] = len(data['names'])

    if request.method == 'POST':
        email = request.POST.get('email')
        choices_list = request.POST.get('choices')
        print(choices_list)

        pass
        # print(checkes)
        # return render(request, 'sign-up.html', {'data': data})

    return render(
        request,
        'voting.html',
        context=data
    )
