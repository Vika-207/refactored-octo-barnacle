from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

from django.shortcuts import render
from .models import Team

def index(request):
list_teams = Team.objects.filter(team_level__exact="U09")
context = {'youngest_teams': list_teams}
return render(request, '/best/index.html', context)
from django.shortcuts import render

from . import util

def index(request):
return render(request, "encyclopedia/index.html", {
"entries": util.list_entries()
})
from django.shortcuts import render
from django.http import HttpResponce

Create your views here.
def index (request):
return HttpResponce("Hello World")
