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
from .models import MentorProfile
from django.views.generic import TemplateView
from django.db.models import Q

from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

class HomeView(ListView):
    model = MentorProfile
    paginate_by = 3
    template_name = "home2.html"

class MentorDetailView(DetailView):
    model = MentorProfile
    template_name = "product2.html"

class SearchResultsView1(ListView):
    model = MentorProfile
    template_name = 'search_page.html'
    paginate_by = 2

    def get_queryset(self):
        query_name = self.request.GET.get('name')
        query_city = self.request.GET.get('city')
        query_school = self.request.GET.get('school')
        if query_name:
            object_list = MentorProfile.objects.filter(
                Q(name__icontains=query_name)
            )
        elif query_city:
            object_list = MentorProfile.objects.filter(
                Q(address__city__icontains=query_city)
            )
        elif query_school:
            object_list = MentorProfile.objects.filter(
                Q(school__icontains=query_school)
            )
        else:
            object_list = MentorProfile.objects.all()
        return object_list