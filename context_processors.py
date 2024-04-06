from django.shortcuts import redirect
from django.urls import reverse

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if request.META.get('QUERY_STRING'):
            path = path + '?' + request.META.get('QUERY_STRING')
        if '?currency=' in path:
            print('path true== ', path)
            try:
                request.session['currency'] = request.META.get('QUERY_STRING').split('=')[1]
            except:
                request.session['currency'] = request.META.get('QUERY_STRING')
    
            return redirect('{}'.format(path.split('?')[0])) 