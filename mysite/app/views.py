from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"api": api})


def user(request):
    if request.method == 'POST':
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/" + user)
        user_name = json.loads(user_request.content)
        return render(request, 'user.html', {'user': user, 'user_name': user_name})

    else:
        notfound = '请输入搜索内容'
        return render(request, 'user.html', {'notfound': notfound})
