from django.http import JsonResponse

def home(req):
    res = {
        'message': 'Hello from Django response',
        'success': True,
        "data":[1,2,3,4,5]
    }
    return JsonResponse(res)
