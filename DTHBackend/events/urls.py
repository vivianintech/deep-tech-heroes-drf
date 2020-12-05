from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.EventList.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('events/new/', views.EventList.as_view()),
    path('events/keynote/', views.NeedKeyNoteEventList.as_view()),
    path('events/facilitator/', views.NeedFacilitatorEventList.as_view()),
    path('events/mentor/', views.NeedMentorEventList.as_view()),
    path('events/expert/', views.NeedExpertEventList.as_view()),
    path('events/enthusiast/', views.NeedEnthusiastEventList.as_view()),
    path('events/intimate/', views.SizeIntimateEventList.as_view()),
    path('events/small/', views.SizeSmallEventList.as_view()),
    path('events/medium/', views.SizeMediumEventList.as_view()),
    path('events/large/', views.SizeLargeEventList.as_view()),
    path('events/verylarge/', views.SizeVeryLargeEventList.as_view()),
    path('events/huge/', views.SizeHugeEventList.as_view()),
    path('applications/', views.ApplicationList.as_view()),
    path('applications/<int:pk>/', views.ApplicationDetail.as_view()),
    path('events/<applications>/applications/', views.EventApplicationList.as_view()),
    path('applications/<int:pk>/assess/', views.AssessApplication.as_view()),
    path('applications/assessed/', views.AssessedApplicationsList.as_view()),
    path('applications/notassessed/', views.NotAssessedApplicationsList.as_view()),
    path('applications/accepted/', views.AcceptedApplicationsList.as_view()),
    path('applications/notaccepted/', views.NotAcceptedApplicationsList.as_view()),
    path('events/apply/', views.ApplicationList.as_view()),
    path('events/<int:pk>/applications/', views.ApplicationDetail.as_view()),
    path('events/newreview/', views.ReviewEventList.as_view()),
    path('events/editreview/', views.ReviewEventDetail.as_view()),
    path('events/reviews/', views.ReviewEventList.as_view()),
    path('applications/assessment/', views.ReviewApplicationList.as_view()),
    path('applications/editassessment/', views.ReviewApplicationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)