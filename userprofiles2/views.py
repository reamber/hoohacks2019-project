from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import UserProfile, Pill
from .forms import IdentiteForm, PillForm


class ProfileHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofiles2/home.html'
    user_check_failure_path = reverse_lazy("account_signup")

    def check_user(self, user):
        if user.is_active:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(ProfileHomeView, self).get_context_data(**kwargs)
        profile = UserProfile.objects.get_or_create(user=self.request.user)[0]
        context['profile'] = profile
        return context


class ProfileIdentite(LoginRequiredMixin, UpdateView):
    template_name = "userprofiles2/identity_form.html"
    form_class = IdentiteForm
    user_check_failure_path = reverse_lazy("account_signup")
    success_url = reverse_lazy("profile-home")

    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset

    def form_valid(self, form, **kwargs):
        super(ProfileIdentite, self).form_valid(form)
        profile = form.save(commit=False)
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        profile.gender = form.cleaned_data['gender']
        profile.phone = form.cleaned_data['phone']
        profile.personal_info_is_completed = True
        profile.completion_level = profile.get_completion_level()
        profile.save()
        return HttpResponseRedirect(self.get_success_url())


class PillView(generic.ListView):
    model = Pill
    template_name = 'userprofiles2/list.html'

    def get_queryset(self):
        return Pill.objects.all()


def get_pill(request):
    if request.method == 'POST':
        form = PillForm(request.POST)
        if form.is_valid():
            pill = form.save()
            return HttpResponseRedirect(reverse('pill-list'))
    else:
        form = PillForm()
    return render(request, 'userprofiles2/pill_form.html', {'form': form})
