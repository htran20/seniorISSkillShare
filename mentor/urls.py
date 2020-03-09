from django.urls import path
from .views import HomeView, MentorDetailView, SearchResultsView1, OrderSummaryView
app_name = 'mentor'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<slug>/', MentorDetailView.as_view(), name='detail'),
    path('search/', SearchResultsView1.as_view(), name='search'),
    path('user-profile/', OrderSummaryView.as_view(), name='user-profile')
]