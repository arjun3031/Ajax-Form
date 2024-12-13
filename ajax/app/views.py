from django.shortcuts import render
from .models import Student
from django.http import JsonResponse

# Create your views here.
def forms(request):
    return render(request,'form.html')

def add_item(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        mail=request.POST.get('email')
        s=Student(name=name,age=age,email=mail)
        s.save()
        return JsonResponse({'success':True})
    
def get_items(request):
    items=Student.objects.all()
    data=[{'id':item.id,'name':item.name,'age':item.age,'email':item.email} for item in items]
    return JsonResponse(data,safe=False)

def edit_item(request):
    item_id=request.GET.get('id')
    item=Student.objects.get(id=item_id)
    data={'id':item.id,'name':item.name,'age':item.age,'email':item.email}
    return JsonResponse(data,safe=False)

def update_item(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        mail=request.POST.get('email')
        item_id=request.POST.get('id')
        st=Student.objects.get(id=item_id)
        st.name=name
        st.age=age
        st.email=mail
        st.save()
        return JsonResponse({'success':True})
    else:
        return JsonResponse({'success':False,'error':'Invalid Request Method'})
    
def delete_item(request):
    if request.method == 'POST':
        item_id=request.POST.get('id')
        stud=Student.objects.get(id=item_id)
        stud.delete()
        return JsonResponse({'success':True})
