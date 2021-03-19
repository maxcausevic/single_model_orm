from django.shortcuts import render,redirect
from .models import User

def index(request):
    context = {
        "users_app_DB":User.objects.all()
    }
    return render(request, "index.html", context)
def users(request):
    print("Got Post Info....................")
    User.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email_address = request.POST["email"], age = request.POST['age'],belt = request.POST['beltrank'], academy_name = request.POST['academy_name'])
    return redirect("/")


