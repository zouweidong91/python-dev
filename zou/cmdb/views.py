from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

''' http://127.0.0.1:8000/login '''
# def home(request):
#     return HttpResponse('<h1>CMDBSS</h1>')

def login(request):
    print(request.method)
    error_msg = ''
    if request.method == 'POST':
        # 获取用户通过post提交过来的数据
        pwd = request.POST['pwd']
        user = request.POST['user']
        print(user, pwd)
        if user == 'root' and pwd == '123':
            return redirect('/home')
        else:
            error_msg = '错误'

    return render(request, 'login.html', {'error_msg': error_msg})

user_list = []
for index in range(2):
    tem_dict = {"username": 'zou'+str(index), "email":'dfcfedf', "gender":'mail'}
    user_list.append(tem_dict)


def home(request):
    if request.method == 'POST':
        # 获取用户提交的数据
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username':u, 'email':e, 'gender':g}
        user_list.append(temp)
        
    return render(request, 'home.html', {"user_list": user_list})