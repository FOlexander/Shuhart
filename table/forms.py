from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from table.models import Tables

User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1')


class TableDownload(ModelForm):
    class Meta:
        model = Tables
        fields = ('user_table',)