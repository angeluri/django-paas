from django.http import HttpResponse

def home(request):
    return HttpResponse("App Django publicada con PaaS correctamente ✅")
