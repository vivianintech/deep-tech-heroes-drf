from django.http import Http404, HttpResponse
from rest_framework import status, viewsets, permissions, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, Application, ReviewEvent, ReviewApplication
from .serializers import EventSerializer, EventDetailSerializer, ApplicationSerializer, ApplicationDetailSerializer, AssessApplicationSerializer, EventApplicationSerializer, ReviewEventSerializer, ReviewEventDetailSerializer, ReviewApplicationSerializer, ReviewApplicationDetailSerializer
from .permissions import IsOwnerOrReadOnly
from django.db.models import Count, Sum
from users.models import CustomUser

class EventList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

class EventDetail(APIView):
    permissions_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self,pk):
        try:
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        data = request.data
        serializer = EventDetailSerializer(
            instance=event,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response (
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response (
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApplicationList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
    def get(self, request):
        application = Application.objects.all()
        serializer = ApplicationSerializer(application, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
              serializer.data,
              status=status.HTTP_201_CREATED
            )
        return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
        )

class ApplicationDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            application = Application.objects.get(pk=pk)
            self.check_object_permissions(self.request, application)
            return application
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = ApplicationDetailSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk):
        application = self.get_object(pk)
        data = request.data
        serializer = ApplicationDetailSerializer(
            instance=application,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response (
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response (
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Amend is_accepted for Application - ideally only accessible via page/button which can be viewed by the Event Host
class AssessApplication(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            application = Application.objects.get(pk=pk)
            self.check_object_permissions(self.request, application)
            return application
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = AssessApplicationSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk):
        application = self.get_object(pk)
        data = request.data
        serializer = AssessApplicationSerializer(
            instance=application,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response (
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response (
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# Create and view Reviews for Events
class ReviewEventList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
    def get(self, request):
        review = ReviewEvent.objects.all()
        serializer = ReviewEventSerializer(application, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ReviewEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
              serializer.data,
              status=status.HTTP_201_CREATED
            )
        return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
        )

# Edit Reviews for Events
class ReviewEventDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            review = ReviewEvent.objects.get(pk=pk)
            self.check_object_permissions(self.request, review)
            return application
        except ReviewEvent.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewEventDetailSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk):
        review = self.get_object(pk)
        data = request.data
        serializer = ReviewEventDetailSerializer(
            instance=review,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response (
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response (
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create a written response to an Application - ideally by Host
class ReviewApplicationList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
    def get(self, request):
        feedback = ReviewApplication.objects.all()
        serializer = ReviewApplicationSerializer(feedback, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ReviewApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
              serializer.data,
              status=status.HTTP_201_CREATED
            )
        return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
        )

# Edit a written response to an Application - ideally by a Host
class ReviewApplicationDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            application = ReviewApplication.objects.get(pk=pk)
            self.check_object_permissions(self.request, application)
            return application
        except ReviewApplication.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = ReviewApplicationDetailSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk):
        application = self.get_object(pk)
        data = request.data
        serializer = ReviewApplicationDetailSerializer(
            instance=application,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response (
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response (
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Display a list of Events that need a Keynote Speaker
class NeedKeyNoteEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        keynote = Event.objects.filter(skills_keynote=True)
        return keynote

# Display a list of Events that need a Workshop Facilitator
class NeedFacilitatorEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        facilitator = Event.objects.filter(skills_facilitator=True)
        return facilitator

# Display a list of Events that need a Mentor
class NeedMentorEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        mentor = Event.objects.filter(skills_mentor=True)
        return mentor

# Display a list of Events that need an Expert
class NeedExpertEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        expert = Event.objects.filter(skills_expert=True)
        return expert

# Display a list of Events that need an Enthusiast
class NeedEnthusiastEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        enthusiast = Event.objects.filter(skills_enthusiast=True)
        return enthusiast

# Display a list of Events that are Intimate Size
class SizeIntimateEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        intimate = Event.objects.filter(event_size=1)
        return intimate

# Display a list of Events that are Small Size
class SizeSmallEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        small = Event.objects.filter(event_size=2)
        return small

# Display a list of Events that are Medium Size
class SizeMediumEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        medium = Event.objects.filter(event_size=3)            
        return medium

# Display a list of Events that are Large Size
class SizeLargeEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        large = Event.objects.filter(event_size=4)
        return large

# Display a list of Events that are VeryLarge Size
class SizeVeryLargeEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        verylarge = Event.objects.filter(event_size=5)
        return verylarge

# Display a list of Events that are Huge Size
class SizeHugeEventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        huge = Event.objects.filter(event_size=6)
        return huge



# Display a list of Applications for a specific Event
class EventApplicationList(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        applicationsfor = self.kwargs['applications']
        return Application.objects.filter(event_id=applicationsfor)

# Display a list of Applications that have been Assessed
class AssessedApplicationsList(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        assessed = Application.objects.filter(is_assessed=True)
        return assessed

# Display a list of Applications that have not been Assessed
class NotAssessedApplicationsList(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        not_assessed = Application.objects.filter(is_assessed=False)
        return not_assessed

# Display a list of Applications that have been Accepted
class AcceptedApplicationsList(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        accepted = Application.objects.filter(is_accepted=True)
        return accepted

# Display a list of Applications that have not been Accepted
class NotAcceptedApplicationsList(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        not_accepted = Application.objects.filter(is_accepted=False)
        return not_accepted