from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from ..models import Customer
from django.views import View
# Create your views here.

class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        data = request.POST
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        phone = data.get('phone')
        email = data.get('email')
        password = data.get('password')

        error = None
        values = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email
        }
        if not first_name:
            error = "First Name is Required"
        if not last_name:
            error = "last_name is Required"
        if not phone:
            error = "phone is Required"
        if not email:
            error = "email  is Required"
        if not password:
            error = "password is Required"

        if error:
            data = {
                "values": values,
                "error": error
            }
            return render(request, "signup.html", data)
        else:
            ob = Customer(first_name=first_name, last_name=last_name, phone=phone,
                          email=email, password=password)
            ob.password = make_password(password)
            ob.save()
            return redirect("indexpage")

