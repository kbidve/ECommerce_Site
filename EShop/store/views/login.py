from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from ..models import Customer
from django.views import View
# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        data = request.POST
        email = data.get("email")
        password = data.get("password")
        try:
            cust = Customer.objects.get(email=email)
            if check_password(password, cust.password):
                return redirect("indexpage")
        except:
            return render(request, "login.html", {"error": "Either Email or Password is invalid"})