from django.shortcuts import render, HttpResponse, redirect
import os
# Create your views here.
def index(request):
    return HttpResponse('index')

# def login(request):
#     if request.method == 'GET': 
#         return render(request, 'login.html')
#     elif request.method == 'POST': 
#         u = request.POST.get('user')
#         p = request.POST.get('pwd')
#         v = request.POST.get('gender')
#         print(v)
#         obj = request.FILES.get('fafafa')
#         print(obj)
#         file_path = os.path.join('upload', obj.name)
#         f = open(file_path, 'wb')
#         for item in obj.chunks():
#             f.write(item)
#         f.close

#         if u == 'zou' and p == '123':
#             return redirect('/index/')
#         else:
#             return render(request, 'login.html')
#         pass
#     else:
#         return redirect('/index/')



# def detail(request):
#     nid = request.GET.get('nnid')
#     detail_info = user_dict[nid]
#     return render(request, 'detail.html', {'detail_info': detail_info})

def detail(request, nid):
    detail_info = user_dict[nid]
    return render(request, 'detail.html', {'detail_info': detail_info})
    # print(nid)
    # return HttpResponse(nid)


from app01 import models

def login(request):
    models.UserGroup.objects.create(caption='DBA')
    if request.method == 'GET': 
        return render(request, 'login.html')
    elif request.method == 'POST': 
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        # count = models.UserInfo.objects.filter(username=u, password=p).count()
        print(obj)
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request, 'login.html')
    else:
        return redirect('/index/')

def index(request):
    return render(request, 'index.html')

def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html', {'user_list':user_list, 'group_list':group_list})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u, password=p)
        return redirect('/cmdb/user_info/')

def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request, 'user_detail.html', {'obj':obj})

def user_del(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')

def user_edit(request, nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p)
        return redirect('/cmdb/user_info/')

def orm(request):
    # 创建
    # dic = {'username':'zouweidong', 'password':'123'}
    # models.UserInfo.objects.create(**dic)

    # 查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(id=2)

    # 删
    # result = models.UserInfo.objects.filter(id=2).delete()

    # 更新
    # result = models.UserInfo.objects.filter(id=2).update(password='6669')
    # result = models.UserInfo.objects.filter(id=2)

    '''result 为列表类型'''
    # print(result)
    # for row in result:
    #     print(row.id, row.username, row.password)
    # models.UserInfo.objects.create(
    #     username='root1',
    #     password='123',
    #     email='decd',
    #     test='dwdc',
    #     user_group=models.UserGroup.objects.filter(id=1).first()

    # )
    models.UserInfo.objects.create(
        username='root1',
        password='123',
        email='decd',
        user_group_id=1

    )
    return HttpResponse('orm')