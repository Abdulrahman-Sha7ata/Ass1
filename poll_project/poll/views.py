from django.shortcuts import render
from .models import Poll
# Create your views here.

def list_polls(request):

    polls = Poll.objects.filter(status=1)
    context = {
        'polls': polls  
    }

    return render(request, 'polls.html', context)