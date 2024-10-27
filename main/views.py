from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from  .models import AdvUser
from  .forms import ProfileEditForm

def index(request):
    return render(request, 'main/index.html')


# Create your views here.
def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
class BBLoginView(LoginView):
    template_name = "main/login.html"
@login_required
def profile(request):
    return render(request, "main/profile.html")
class BBLogoutView(LogoutView):
    pass
class ProfileEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = "main/profile_edit.html"
    form_class = ProfileEditForm
    success_url = reverse_lazy("main:profile")
    success_message = "Данные пользователя изменены"

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request)
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

