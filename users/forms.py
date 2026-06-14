from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'username', 'phone_number', 'country', 'avatar', 'password1', 'password2']
