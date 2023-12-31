"""VIEWS APPCITAS"""
"""Django"""
from django.http import HttpResponse
from datetime import datetime
import json

#utilities
def hello_world(request):
    
    return HttpResponse('Current server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sort_integers(request):
    """Return a JSON response with sorted integers"""
    
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfuly.'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to appcitas '.format(name)
        
    return HttpResponse(message)
