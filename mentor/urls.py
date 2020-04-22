from django.urls import path
from .views import UserDetailView, UserUpdate, HomeView, MentorDetailView, SearchResultsView1, AboutView, EssayCounselorView, InsiderView, TutorView
app_name = 'mentor'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<slug>/', MentorDetailView.as_view(), name='detail'),
    path('search/', SearchResultsView1.as_view(), name='search'),
    path('user-profile/', UserDetailView.as_view(), name='user-profile'),
    path('about', AboutView.as_view(), name='about'),
    path('essay-counselor', EssayCounselorView.as_view(), name='essay-counselor'),
    path('insider', InsiderView.as_view(), name='insider'),
    path('tutor', TutorView.as_view(), name='tutor'),
]