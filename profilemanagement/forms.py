from django import forms
from .models import Customer, Wallet, Order, CartItem
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['balance', 'transaction_history']

class RentalForm(forms.Form):
    today = timezone.now().date()  # Default start date as today's date
    next_day = today + timedelta(days=1)  # Default end date as the day after today

    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=today
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=next_day
    )
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }



class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_pic', 'address', 'mobile']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)