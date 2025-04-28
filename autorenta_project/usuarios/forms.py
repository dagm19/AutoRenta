from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm 
from .models import UserCustom

class CustomUserCreationForm(AdminUserCreationForm): 
    class Meta:
        model = UserCustom
        fields = ("username", "email", "rol") 

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserCustom
        fields = ("username", "email", "is_active", "rol")
