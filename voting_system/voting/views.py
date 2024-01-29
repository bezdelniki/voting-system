from django.shortcuts import render

def sign_up(request):
    if (request.method == 'POST'):
        passw = request.POST.get('passw')
        print(passw)

    data = []

    return render(request, 'sign-up.html', { 'data': data })