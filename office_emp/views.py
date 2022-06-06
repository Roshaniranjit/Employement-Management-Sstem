from django.shortcuts import render,HttpResponse
from .models import Department, Role, Employee
from .forms import EmployeeForm,DepartmentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all() 
    context ={
        'emps': emps
        
    }
    print(context)
    return render(request, 'all_emp.html',context)


def add_emp(request):
    if request.method =='POST':
                forms = EmployeeForm(request.POST)
                
                
                
                if forms.is_valid():
                    
                    forms.save()
                    return HttpResponse('Employee added Sucessfully')
       
    forms = EmployeeForm()
    return render(request,'add_emp.html',{"forms": forms})

    

def remove_emp(request):

    emp_id = request.GET.get("employee_id", None) #function
    if  emp_id != None:
        
        emps = Employee.objects.get(id = emp_id)
        emps.delete()
        return HttpResponse("Employee has bee deleted")
    emps = Employee.objects.all()
    context ={
        'emps' : emps
            
    }
    return render(request, 'remove_emp.html',context)

def search_emp(request):
    return render(request, 'search_emp.html')




