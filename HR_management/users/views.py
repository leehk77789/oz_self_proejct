from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from users.forms import SignupForm  # 사용자 등록 폼을 import합니다.

# 사용자 모델을 가져옵니다.
User = get_user_model()

# 로그인 뷰
def login_view(request):
    if request.method == 'POST':
        # POST 요청이 들어왔을 때, 사용자가 입력한 username과 password를 가져옵니다.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 사용자 인증을 수행합니다.
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 사용자가 인증되면 로그인을 수행하고 목록 페이지로 리디렉션합니다.
            login(request, user)
            return redirect('/list') 
        else:
            # 인증에 실패하면 다시 로그인 페이지로 리디렉션합니다.
            return redirect('/')
    # GET 요청이 들어왔을 때는 로그인 페이지를 렌더링합니다.
    return render(request, 'login.html')

# 회원가입 뷰
def register_view(request):
    if request.method == 'POST':
        # POST 요청이 들어왔을 때, 회원가입 폼을 생성하고 유효성을 검사합니다.
        form = SignupForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 사용자를 저장하고 홈 페이지로 리디렉션합니다.
            form.save()
            return redirect('/')
    else:
        # GET 요청이 들어왔을 때는 빈 회원가입 폼을 생성합니다.
        form = UserCreationForm()
    # 회원가입 페이지를 렌더링하고 폼을 템플릿에 전달합니다.
    return render(request, 'register.html', {'form': form})

# 사용자 목록 뷰
@login_required
def user_list(request):
    # 모든 사용자를 가져와서 사용자 목록 페이지를 렌더링합니다.
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
