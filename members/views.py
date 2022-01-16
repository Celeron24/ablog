from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from myblog.models import UserProfile
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm


class CreateProfilePageView(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/UserProfile.html'

    def get_context_data(self, *args, **kwargs):
        # users = UserProfile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    # from_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, **kwargs):
        return self.request.user


# class EditProfilePageView(generic.UpdateView):
#     model = UserProfile
#     template_name = 'registration/edit_profile_page.html'
#     fields = ['bio', 'profile_pic', 'website_url', 'instagram_url', 'facebook_url', 'linkedin_url']
