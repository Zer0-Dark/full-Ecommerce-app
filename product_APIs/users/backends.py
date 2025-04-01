from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q # for complex queries using "OR"



class MultiFieldAuthBackend(ModelBackend):
    # override the authenticate method to allow email and phone number
    def authenticate(self, request, identifier=None, password=None, **kwargs):
        UserModel = get_user_model()
        # username here is misleading it is for whatever the user inputted during login 
        try:
            # iexact (case insensitive) is used here for user convenience and according to standard practices.
            user = UserModel.objects.get(
                Q(email__iexact=identifier) |
                Q(username__iexact=identifier) |
                Q(phone_number__iexact=identifier)
            )
            
        except UserModel.DoesNotExist:
            return None
        else:
            # Reject users with is_active=False 
            # currently my custom user model doesn't have it but it is best to have it for the future 
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
