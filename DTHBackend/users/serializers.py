from rest_framework import serializers
from .models import CustomUser, HostUser, HeroUser
from django.utils import timezone


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    is_hero = serializers.BooleanField(default=False)
    is_host = serializers.BooleanField(default=False)
    rec_newsletter = serializers.BooleanField(default=True)
    date_updated = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class HeroUserSerializer(CustomUserSerializer):
    is_hero = serializers.BooleanField(default=True)
    year_of_birth = serializers.IntegerField(min_value=1900)
    hero_phone = serializers.CharField(max_length=10)
    hero_location = serializers.CharField(max_length=100)
    hero_image = serializers.URLField(default="https://res.cloudinary.com/flifree/image/upload/v1605350476/Deep%20Tech%20Heroes/DTH_2_cahr8o.png")
    linkedin_url = serializers.URLField(default="https://www.linkedin.com/feed/")
    hero_bio = serializers.CharField(max_length=5000, default="")
    gender = serializers.ChoiceField(
        choices=('transgender', 'cisgender', 'agender', 'genderqueer', 'feminine', 'masculine', 'prefer not to say'),
        default='prefer not to say',
        label='gender identity'
    )
    pref_pronoun = serializers.ChoiceField(
        choices=('they/them', 'she/her', 'he/him', 'ze/zem', 'prefer not to say'),
        default='prefer not to say',
        label='preferred pronoun'
    )
    has_bluecard = serializers.BooleanField(default=False)
    has_yellowcard = serializers.BooleanField(default=False)
    is_virtual_accepted = serializers.BooleanField(default=False)
    is_paid_preferred = serializers.BooleanField(default=False)
    culture = serializers.CharField(max_length=250)
    hero_language = serializers.CharField(max_length=200, default="English")
    hero_disability = serializers.BooleanField(default=False)
    badge_keynote = serializers.BooleanField(default=False)
    badge_facilitator = serializers.BooleanField(default=False)
    badge_mentor = serializers.BooleanField(default=False)
    badge_expert = serializers.BooleanField(default=False)
    badge_enthusiast = serializers.BooleanField(default=False)
    date_updated = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        return HeroUser.objects.create_user(**validated_data)

    class Meta:
        model = HeroUser
        fields = '__all__'


class HostUserSerializer(CustomUserSerializer):
    is_host = serializers.BooleanField(default=True)
    organisation_name = serializers.CharField(max_length=100)
    organisation_logo = serializers.URLField(default="https://res.cloudinary.com/flifree/image/upload/v1605350477/Deep%20Tech%20Heroes/DTH_8_pqsldv.png")
    host_phone = serializers.CharField(max_length=10)
    date_updated = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        return HostUser.objects.create_user(**validated_data)

    class Meta:
        model = HostUser
        fields = '__all__'



class CustomUserDetailSerializer(CustomUserSerializer):
    herousers = HeroUserSerializer(many=True, read_only=True)
    hostusers = HostUserSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_hero = validated_data.get('is_hero', instance.is_hero)
        instance.is_host = validated_data.get('is_host', instance.is_host)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class HeroUserDetailSerializer(HeroUserSerializer):

    def update(self, instance, validated_data):
        instance.year_of_birth = validated_data.get('year_of_birth', instance.year_of_birth)
        instance.hero_phone = validated_data.get('hero_phone', instance.hero_phone)
        instance.hero_location = validated_data.get('hero_location', instance.hero_location)
        instance.hero_image = validated_data.get('hero_image', instance.hero_image)
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.hero_bio = validated_data.get('hero_bio', instance.hero_bio)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.pref_pronoun = validated_data.get('pref_pronoun', instance.pref_pronoun)
        instance.has_bluecard = validated_data.get('has_bluecard', instance.has_bluecard)
        instance.has_yellowcard = validated_data.get('has_yellowcard', instance.has_yellowcard)
        instance.is_virtual_accepted = validated_data.get('is_virtual_accepted', instance.is_virtual_accepted)
        instance.is_paid_preferred = validated_data.get('is_paid_preferred', instance.is_paid_preferred)
        instance.culture = validated_data.get('culture', instance.culture)
        instance.hero_language = validated_data.get('hero_language', instance.hero_language)
        instance.hero_disability = validated_data.get('hero_disability', instance.hero_disability)
        instance.badge_keynote = validated_data.get('badge_keynote', instance.badge_keynote)
        instance.badge_facilitator = validated_data.get('badge_facilitator', instance.badge_facilitator)
        instance.badge_mentor = validated_data.get('badge_mentor', instance.badge_mentor)
        instance.badge_expert = validated_data.get('badge_expert', instance.badge_expert)
        instance.badge_enthusiast = validated_data.get('badge_enthusiast', instance.badge_enthusiast)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class HostUserDetailSerializer(HostUserSerializer):

    def update(self, instance, validated_data):
        instance.organisation_name = validated_data.get('organisation_name', instance.organisation_name)
        instance.organisation_logo = validated_data.get('organisation_logo', instance.organisation_logo)
        instance.host_phone = validated_data.get('host_phone', instance.host_phone)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance


class HeroUpgradeSerializer(serializers.Serializer):
    is_hero = serializers.BooleanField(default=True)
    year_of_birth = serializers.IntegerField(min_value=1900)
    hero_phone = serializers.CharField(max_length=10)
    hero_location = serializers.CharField(max_length=100)
    hero_image = serializers.URLField(default="https://res.cloudinary.com/flifree/image/upload/v1605350476/Deep%20Tech%20Heroes/DTH_2_cahr8o.png")
    linkedin_url = serializers.URLField(required=False)
    hero_bio = serializers.CharField(max_length=5000, default="")
    gender = serializers.ChoiceField(
        choices=('transgender', 'cisgender', 'agender', 'genderqueer', 'feminine', 'masculine', 'prefer not to say'),
        default='prefer not to say',
        label='gender identity'
    )
    pref_pronoun = serializers.ChoiceField(
        choices=('they/them', 'she/her', 'he/him', 'ze/zem', 'prefer not to say'),
        default='prefer not to say',
        label='preferred pronoun'
    )
    has_bluecard = serializers.BooleanField(default=False)
    has_yellowcard = serializers.BooleanField(default=False)
    is_virtual_accepted = serializers.BooleanField(default=False)
    is_paid_preferred = serializers.BooleanField(default=False)
    culture = serializers.CharField(max_length=250)
    hero_language = serializers.CharField(max_length=200, default="English")
    hero_disability = serializers.BooleanField(default=False)
    badge_keynote = serializers.BooleanField(default=False)
    badge_facilitator = serializers.BooleanField(default=False)
    badge_mentor = serializers.BooleanField(default=False)
    badge_expert = serializers.BooleanField(default=False)
    badge_enthusiast = serializers.BooleanField(default=False)
    date_updated = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        user = self.context.get('user')
        return HeroUser.objects.create(**validated_data, customuser_ptr=user, username=user.username, password=user.password, email=user.email, first_name=user.first_name, last_name=user.last_name, is_host=user.is_host, rec_newsletter=user.rec_newsletter)


class HostUpgradeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    is_host = serializers.BooleanField(default=True)
    organisation_name = serializers.CharField(max_length=100)
    organisation_logo = serializers.URLField(default="https://res.cloudinary.com/flifree/image/upload/v1605350477/Deep%20Tech%20Heroes/DTH_8_pqsldv.png")
    host_phone = serializers.CharField(max_length=10)
    date_updated = serializers.DateTimeField(default=timezone.now)

    def create(self, validated_data):
        user = self.context.get('user')
        return HostUser.objects.create(**validated_data, customuser_ptr=user, username=user.username, password=user.password, email=user.email, first_name=user.first_name, last_name=user.last_name, is_hero=user.is_hero, rec_newsletter=user.rec_newsletter)

