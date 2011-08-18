from django.shortcuts import render_to_response

def home(request):
    return render_to_response("root/home.tpl", {})

def about(request):
    return render_to_response("root/about.tpl", {})
