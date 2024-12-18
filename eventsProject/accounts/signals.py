from django.contrib.auth import get_user_model, user_logged_in
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from eventsProject.accounts.models import UserProfile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# TODO: make a check in templates if a user is set to inactive and display appropriate msg
@receiver(user_logged_in)
def reactivate_user_profile(sender, request, user, **kwargs):
    # Check if the user is active and if their profile is inactive
    if user.is_active:
        try:
            profile = UserProfile.objects.get(user=user)
            if not profile.is_active:
                # Reactivate the profile if it's inactive
                profile.is_active = True
                profile.save()

                # Optionally, you can also trigger user reactivation (if needed)
                user.is_active = True
                user.save()

                # Log or notify that the profile was reactivated (optional)
                print(f"Profile for {user.email} has been reactivated.")
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=user)