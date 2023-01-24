from django.shortcuts import render
from Employee.models import Employee
# Create your views here.
def register(request):
    return render(request, 'register.html')

def addEmployee(request):
    if request.method == 'POST':
        firstName = request.POST.get("firstName") 
        lastName = request.POST.get("lastName")
        emailAddress = request.POST.get("emailAddress") 
        address = request.POST.get("address")
        department = request.POST.get("department") 
        position = request.POST.get("position")
        img = request.POST.get("img")
        background = request.POST.get("background")
        phoneNumber = request.POST.get("phoneNumber")
        data = Employee(firstName=firstName,lastName=lastName,email=emailAddress,address=address,department=department,position=position,background=background,image=img, phoneNumber=phoneNumber)
        data.save()
    return render(request, 'update.html')

def showEmployee(request):
    employee = Employee.objects.all()
    return render(request, 'result.html', {'employeeDetails': employee})