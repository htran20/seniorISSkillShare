from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic.base import TemplateView
# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import MentorProfile, UserMentorProfile
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.db.models import Q

from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
import data.RCengine as RCengine
import pickle
from .forms import ProfileUpdateForm

class UserDetailView(LoginRequiredMixin, View):
    template_name = 'userprofile.html'

    def get(self, request, *args, **kwargs):
        try:
            userProfile = UserMentorProfile.objects.get(user=self.request.user)
            profile_form = ProfileUpdateForm(instance=userProfile)
            context = {
                'object': userProfile,
                'p_form': profile_form
            }
            return render(self.request, self.template_name, context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You have not logged in")
            return redirect("/")

    def post(self, request, *args, **kwarg):
        try:
            userProfile = UserMentorProfile.objects.get(user=self.request.user)
            profile_form = ProfileUpdateForm(request.POST, instance=userProfile)
            context = {
                'object': userProfile,
                'p_form': profile_form
            }
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, f'Your profile has been updated!')
                return redirect('mentor:user-profile')
            return render(self.request, self.template_name, context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You have not logged in")
            return redirect("/")

class UserUpdate(UpdateView):
    model = UserMentorProfile
    fields = ['first_name']

class HomeView(ListView):
    model = MentorProfile
    paginate_by = 4
    template_name = "home2.html"
    filename = './data/users_model.sav'
    users = pickle.load(open(filename, 'rb'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            userProfile = UserMentorProfile.objects.get(user=self.request.user)
            rc_mentors_email = RCengine.get_recommendations(userProfile.major, self.users)
            context['recommend_list'] = MentorProfile.objects.filter(
                email__in=rc_mentors_email
            )

        else:
            context['recommend_list'] = []
        return context

class MentorDetailView(DetailView):
    model = MentorProfile
    template_name = "product2.html"


class SearchResultsView1(ListView):
    model = MentorProfile
    template_name = 'search_page.html'
    paginate_by = 4

    def get_queryset(self):
        query_name = self.request.GET.get('name')
        query_major = self.request.GET.get('major')
        query_state = self.request.GET.get('state')
        query_school = self.request.GET.get('school')
        if query_name:
            object_list = MentorProfile.objects.filter(
                Q(name__icontains=query_name)
            )
        elif query_major:
            object_list = MentorProfile.objects.filter(
                Q(major__icontains=query_major)
            )
        elif query_state:
            object_list = MentorProfile.objects.filter(
                Q(address__state__icontains=query_state)
            )
        elif query_school:
            object_list = MentorProfile.objects.filter(
                Q(school__icontains=query_school)
            )
        else:
            object_list = MentorProfile.objects.all()
        return object_list


class AboutView(TemplateView):
    template_name = 'about.html'

class EssayCounselorView(TemplateView):
    template_name = 'essay_counselor.html'

class InsiderView(TemplateView):
    template_name = 'insider.html'

class TutorView(TemplateView):
    template_name = 'tutor.html'