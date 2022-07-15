from django.shortcuts import render


def user_history(request):
    context = {
        'user': request.user
    }
    return render(request, 'history.html', context)
