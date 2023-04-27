from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
# from django.contrib.auth.models import User
from .models import User
# import models.User as bar

def login_view(request,id):
    print(id)
    nameee='Nooo'
    isStaff=False
    if id==2:
        nameee='Patient'
        isStaff=False
    else:
        nameee='Doctor'
        isStaff=True
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # account_type = request.POST.get('account-type')

        # Authenticate user
        # user = authenticate(request, email=email, password=password)
        userrr=User.objects.get(email=email,password=password)
        print(userrr.first_name)
        if userrr is not None:
            if userrr.userType == id:
                # Login user
                # login(request, userrr)
                return redirect('/dashboard/'+str(userrr.id)) # replace with your dashboard URL
            else:
                # Display error message
                message = "Invalid account type."
        else:
            # Display error message
            message = "Invalid email or password."

        return render(request, 'login.html', {'nameee':nameee,'id':id})

    else:
        return render(request, 'login.html',{'nameee':nameee,'id':id})

def signup(request,id):
    print(id)
    nameee='Nooo'
    isStaff=False
    if id==2:
        nameee='Patient'
        isStaff=False
    else:
        nameee='Doctor'
        isStaff=True
    if request.method == 'POST':
        # Retrieve the form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_picture = request.FILES.get('profile-picture')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address_line1 = request.POST.get('address_line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        userType=id
        # Create a new user object and save it to the database
        user = User(first_name=first_name, last_name=last_name, profile_picture=profile_picture, username=username,
                    email=email, password=password, address_line1=address_line1, city=city, state=state, pincode=pincode,userType=userType)
        user.save()

        # myuser=User.objects.create_user(username,email,password) 
        # myuser.first_name=first_name
        # myuser.last_name=last_name
        # myuser.is_staff=isStaff
        # myuser.save()
        # Redirect to the dashboard page with the user's data
        return redirect('/login/'+str(id))

    return render(request, 'signup.html',{'nameee':nameee})


def select(request):
   return render(request,'select.html')

def dashboard(request,id):
    if request.method == 'GET':
        userrr=User.objects.get(id=id)

        # Retrieve user data entered in the signup form
        first_name =  userrr.first_name
        last_name = userrr.last_name
        profile_picture = userrr.profile_picture
        username = userrr.username
        email = userrr.email
        password = userrr.password
        confirm_password =userrr.password
        address_line1 = userrr.address_line1
        city = userrr.city
        state = userrr.state
        pincode = userrr.pincode

        # Pass user data as context to dashboard.html template
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'profile_picture': profile_picture,
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'address_line1': address_line1,
            'city': city,
            'state': state,
            'pincode': pincode,
        }

        return render(request, 'dashboard.html', context)

    else:
        return HttpResponse('Invalid Request')
