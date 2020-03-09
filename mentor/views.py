from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import MentorProfile, UserMentorProfile
from django.views.generic import TemplateView
from django.db.models import Q

from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            userProfile = UserMentorProfile.objects.get(user=self.request.user)
            context = {
                'object': userProfile
            }
            return render(self.request, 'userprofile.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

class HomeView(ListView):
    model = MentorProfile
    paginate_by = 4
    template_name = "home2.html"

class MentorDetailView(DetailView):
    model = MentorProfile
    template_name = "product2.html"

class SearchResultsView1(ListView):
    model = MentorProfile
    template_name = 'search_page.html'
    paginate_by = 8

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