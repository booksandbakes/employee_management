import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Employee_Form, Dept_Form, search_form, update_form
from .models import Employee, Department


def register(request):
    emp_form = Employee_Form(request.POST or None)
    dept_form = Dept_Form(request.POST or None)
    if emp_form.is_valid():
        new_dept_id = request.POST['depart_ment']
        print(new_dept_id, request.POST['Department_name'])
        if request.POST['depart_ment'] == '8' and request.POST['Department_name']:
            dept_data = Department(dept_name  = request.POST['Department_name'])
            dept_data.save()
            new_dept_id = list(Department.objects.filter(dept_name = request.POST['Department_name']).values_list('dept_id', flat=True))[0]
            
        emp_data = Employee(first_name = request.POST['first_name'], last_name = request.POST['last_name'],
                        email= request.POST['email'],  phone_no = request.POST['phone_no'],salary=request.POST['salary'],
                             depart_ment = Department.objects.get(dept_id = new_dept_id))
        emp_data.save()
        return redirect('/display')

    context = {
        'form1': emp_form,
        'form2':dept_form,
    }
    return render(request, 'register.html', context)

def display(request):
    form = search_form(request.POST or None)
    if form.is_valid():
        search_option = request.POST['optionfield']
        search_data = request.POST['searchfield']
        if search_option == '3':
            emp_data = Employee.objects.select_related().filter(email__icontains = search_data).order_by('first_name')
    
        elif search_option == '2':
            emp_data = Employee.objects.select_related().filter(depart_ment__dept_name__icontains = search_data).order_by('first_name')
        
        else:
            emp_data = Employee.objects.select_related().filter(first_name__icontains = search_data).order_by('first_name')

    else:
        emp_data = Employee.objects.select_related().order_by('first_name')
    context = {'list_data': emp_data,'form': form,}
    return render(request, 'output.html', context)


def update_dept(request,emp_id):
    form = update_form(request.POST or None)
    name_ = Employee.objects.filter(e_id = emp_id )
    name_ = [i.first_name for i in name_]
    if form.is_valid():
        print('\n\n',request.POST['depart_ment'])
        update_db = Employee.objects.get(e_id = emp_id)
        update_db.depart_ment=Department.objects.get(dept_id = request.POST['depart_ment'])
        update_db.save()
        return redirect('/display')
    return render(request,'popup.html', context={'form': form,'name':name_[0]})



