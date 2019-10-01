from django.shortcuts import render, HttpResponse, redirect
# Create your views here.


# def home(request):
#     return HttpResponse('<h1>CMDBSS</h1>')

def login(request):
    print(request.method)
    # string = """
    # <form>
    #     <input type='text' />
    # </form>
    # """
    # f = open('templates/login.html', 'r', encoding='utf8')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)
    error_msg = ''
    if request.method == 'POST':
        # 获取用户通过post提交过来的数据
        pwd = request.POST['pwd']
        user = request.POST['user']
        
        print(user, pwd)
        if user == 'root' and pwd == '123':
            return redirect('/hoe')
        else:
            error_msg = '错误'

    return render(request, 'login.html', {'error_msg': error_msg})

def home(request):
    return render(request, 'home.html')