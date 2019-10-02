from django.shortcuts import render, HttpResponse, redirect
import os
# Create your views here.
def index(request):
    return HttpResponse('index')

def login(request):
    if request.method == 'GET': 
        return render(request, 'login.html')
    elif request.method == 'POST': 
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        v = request.POST.get('gender')
        print(v)
        obj = request.FILES.get('fafafa')
        print(obj)
        file_path = os.path.join('upload', obj.name)
        f = open(file_path, 'wb')
        for item in obj.chunks():
            f.write(item)
        f.close

        if u == 'zou' and p == '123':
            return redirect('/index/')
        else:
            return render(request, 'login.html')
        pass
    else:
        return redirect('/index/')

user_dict = {
    '1':{'name':'root1'},
    '2':{'name':'root2'},
    '3':{'name':'root3'},
    '4':{'name':'root4'},
}
def index(request):
    return render(request, 'index.html', {'user_dict': user_dict})

# def detail(request):
#     nid = request.GET.get('nnid')
#     detail_info = user_dict[nid]
#     return render(request, 'detail.html', {'detail_info': detail_info})

def detail(request, nid):
    detail_info = user_dict[nid]
    return render(request, 'detail.html', {'detail_info': detail_info})
    # print(nid)
    # return HttpResponse(nid)