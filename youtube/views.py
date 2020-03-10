from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from forms import LoginForm
# Create your views here.
class HomeView(View):

    template_name = 'homeView.html'

    def get(self,request):
        variableA = "some text here"
                                                        #context variable
        return render(request,self.template_name,{'variableA':variableA})
# form class를 html로 보여주기 위해서 인스턴싱하여
class LoginView(View):
    template_name = 'login.html'
    form = LoginForm()
    def get(self,request):                          #렌더의 인자로 넘겨준다.
        return render(request,self.template_name,{'form':self.form})
                                                    #html template가 form이라는 context variable을 받도록 되어있으니 'form':form의 인스턴스 이렇게 해서 넘겨주면 form class가 그려지게 되는것이다.

"""You don't have implicit access to attributes inside methods, in Python.
A bare name like currentid in the line:
del connections[currentid]
always looks up a name in the local function scope, then in each enclosing function scope, before trying the global module scope (and then looks at built-ins as a last resort).
currentid is a class attribute, which won't be found in any of those scopes.
To look up an attribute in Python you always need to specify an object in which to look.
Though the lookup protocol means the object need not necessarily have the attribute itself;
attribute lookup will fall back to the class of the object you specified (and the base classes, if inheritance is involved)."""
#한마디로 클래스 안의 this(여기선 self)가 생략이 안되므로 명시해줘야 찾는단다..


class NewVideo(View):

    template_name = 'new_video.html'

    def get(self,request):
        variableA = 'new_video'
        return render(request,self.template_name,{'variableA':variableA})



