from django.http import JsonResponse


def ping(request):
    data = {'ai': 'vitinhuu!'}
    return JsonResponse(data)
