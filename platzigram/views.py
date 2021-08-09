
#Django
from django.http import HttpResponse


#Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greating"""
    return HttpResponse("""Hello, this is the begin.
        If you can go to admin please put /admin on url. :)
        """
    )

def now_time(request):
    """return the time"""
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse(f'the time is: {now}')

def sorted_numbers(request):
    """Return sorted numbers"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sortes_ints = sorted(numbers)
    #import pdb; pdb.set_trace()

    data ={
        'status': 'ok',
        'numbers': sortes_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type = 'application/json'
    )

def say_hi(request, name, age):
    """Retur a greatting."""

    if age <= 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hi {name}, welcome to platzigram'

    return HttpResponse(message)