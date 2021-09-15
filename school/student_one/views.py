from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def happy(request):
    my_dict = {'import_text':'this is about institution'}
    return render(request,"student_one/happy.html",context=my_dict)
def home(request):
    return render(request,"student_one/home.html")
    
def information(request):
    return render(request,"student_one/information.html")
def trainee(request):
    return render(request,"student_one/trainee.html")



def mail(request):
    web_list=trainer.objects.order_by('total_fee')
    date_dict={'access_records':web_list}
    return render(request,'student_one/mail.html',context=date_dict)
