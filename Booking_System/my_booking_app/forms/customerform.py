from django import forms
from my_booking_app.models.customermodel import Customer

# Customer
class Customer_Signup_Form(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = "__all__"

