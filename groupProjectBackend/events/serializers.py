from rest_framework import serializers
from .models import Event, Application, ReviewEvent, ReviewApplication
from django.utils import timezone


# To enable the Host to leave a comment on an Application for the Hero
class ReviewApplicationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    application_id = serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.id')
    comment = serializers.CharField(max_length=2000)
    assessor = serializers.SerializerMethodField('get_username_from_owner')

    def create(self, validated_data):
        return ReviewApplication.objects.create(**validated_data)

    def get_username_from_owner(self, review_application):
        username = review_application.owner.full_name
        return username

    class Meta:
        model = ReviewApplication
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    reason_apply = serializers.CharField(max_length=1000)
    is_assessed = serializers.BooleanField(default=False)
    is_accepted = serializers.BooleanField(default=False)
    apply_keynote = serializers.BooleanField(default=False)
    apply_facilitator = serializers.BooleanField(default=False)
    apply_mentor = serializers.BooleanField(default=False)
    apply_expert = serializers.BooleanField(default=False)
    apply_enthusiast = serializers.BooleanField(default=False)
    is_anon = serializers.BooleanField(default=False)
    date_created = serializers.DateTimeField(label='application created', default=timezone.now)
    date_updated = serializers.DateTimeField(label="application last amended on", default=timezone.now)
    owner = serializers.ReadOnlyField(source='owner.id')
    event_id = serializers.IntegerField()
    applicant_name = serializers.SerializerMethodField('get_username_from_owner')
    applicant_email = serializers.SerializerMethodField('get_email_from_owner')

    def create(self, validated_data):
        return Application.objects.create(**validated_data)

    def get_username_from_owner(self, application):
        username = application.owner.full_name
        return username

    def get_email_from_owner(self, application):
        email = application.owner.email
        return email

    class Meta:
        model = Application
        fields = '__all__'



# To enable the Hero to leave a review and rating of the Event
class ReviewEventSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    event_id = serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.id')
    comment = serializers.CharField(max_length=2000)
    rating = serializers.IntegerField()
    reviewer = serializers.SerializerMethodField('get_username_from_owner')

    def create(self, validated_data):
        return ReviewEvent.objects.create(**validated_data)

    def get_username_from_owner(self, review_event):
        username = review_event.owner.full_name
        return username

    class Meta:
        model = ReviewEvent
        fields = '__all__'


class EventSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    event_name = serializers.CharField(label='event')
    event_description = serializers.CharField(label='event details', default="Describe the events purpose and the expected audience.")
    event_location = serializers.CharField(label="city or Region")
    event_date = serializers.DateField(label='event date')
    event_time = serializers.TimeField(label='event time')
    event_ticket = serializers.CharField(label='get event ticket')
    skills_keynote = serializers.BooleanField(default=False)
    skills_facilitator = serializers.BooleanField(default=False)
    skills_mentor = serializers.BooleanField(default=False)
    skills_expert = serializers.BooleanField(default=False)
    skills_enthusiast = serializers.BooleanField(default=False)
    event_size = serializers.IntegerField(default=1)
    is_paid = serializers.BooleanField(default=False)
    date_created = serializers.DateTimeField(label='event created', default=timezone.now)
    date_updated = serializers.DateTimeField(label="event last amended on", default=timezone.now)
    image = serializers.URLField(label='event image', default="https://res.cloudinary.com/flifree/image/upload/v1605350477/Deep%20Tech%20Heroes/DTH_10_cwdfqx.png")
    owner = serializers.ReadOnlyField(source='owner.id')
    event_host = serializers.SerializerMethodField('get_name_from_owner')
    host_username = serializers.SerializerMethodField('get_username_from_owner')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def get_name_from_owner(self, event):
        name = event.owner.full_name
        return name

    def get_username_from_owner(self, event):
        username = event.owner.username
        return username


class EventDetailSerializer(EventSerializer):
    applications = ApplicationSerializer(many=True, read_only=True)
    review_event = ReviewEventSerializer(many=True, read_only=True)


    def update(self, instance, validated_data):
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.event_description = validated_data.get('event_description', instance.event_description)
        instance.event_location = validated_data.get('event_location', instance.event_location)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.event_time = validated_data.get('event_time', instance.event_time)
        instance.event_ticket = validated_data.get('event_ticket', instance.event_ticket)
        instance.skills_keynote = validated_data.get('skills_keynote', instance.skills_keynote)
        instance.skills_facilitator = validated_data.get('skills_facilitator', instance.skills_facilitator)
        instance.skills_mentor = validated_data.get('skills_mentor', instance.skills_mentor)
        instance.skills_expert = validated_data.get('skills_expert', instance.skills_expert)
        instance.skills_enthusiast = validated_data.get('skills_enthusiast', instance.skills_enthusiast)        
        instance.event_size = validated_data.get('event_size', instance.event_size)
        instance.is_paid = validated_data.get('is_paid', instance.is_paid)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


#Edit Application details except is_assessed or is_accepted - for Applicant(Hero)
class ApplicationDetailSerializer(ApplicationSerializer):
    review_application = ReviewApplicationSerializer(many=True, read_only=True)


    def update(self, instance, validated_data):
        instance.reason_apply = validated_data.get('reason_apply', instance.reason_apply )
        instance.apply_keynote = validated_data.get('apply_keynote', instance.apply_keynote)
        instance.apply_facilitator = validated_data.get('apply_facilitator', instance.apply_facilitator)
        instance.apply_mentor = validated_data.get('apply_mentor', instance.apply_mentor)
        instance.apply_expert = validated_data.get('apply_expert', instance.apply_expert)
        instance.apply_enthusiast = validated_data.get('apply_enthusiast', instance.apply_enthusiast)   
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.event = validated_data.get('event', instance.event)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.is_anon = validated_data.get('is_anon', instance.is_anon)
        instance.save()
        return instance


# Edit is_assessed and is_accepted field of Application only - for Event Host
class AssessApplicationSerializer(ApplicationSerializer):

    def update(self, instance, validated_data):
        instance.is_assessed = validated_data.get('is_assessed', instance.is_assessed)
        instance.is_accepted = validated_data.get('is_accepted', instance.is_accepted)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance

# Edit comments left on an Application by an Event Host
class ReviewApplicationDetailSerializer(ReviewApplicationSerializer):

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance


# Edit comment or rating left on an Event by a Hero
class ReviewEventDetailSerializer(ReviewApplicationSerializer):

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance


# To enable view of Applications related to a specific event, without the event details being list - for Event Host
class EventApplicationSerializer(ApplicationSerializer):

    def read(self, validated_data):
        return Application.objects.all(**validated_data)

# To enable view of Event Reviews related to a specific event, without the event details being listed
class EventReviewsSerializer(ReviewEventSerializer):

    def read(self, validated_data):
        return ReviewEvent.objects.all(**validated_data)