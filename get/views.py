from django.shortcuts import render_to_response
from django.shortcuts import redirect

from models import DownloadLink

def index(request):
    links = DownloadLink.objects.all()
    context = {'links': list(links)}
    return render_to_response('get/listing.tpl', context)
