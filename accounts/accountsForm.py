from django.forms import ModelForm
from django import forms
from .models import CustomUser


class AccountsForm(ModelForm):
    class Meta:

        model = CustomUser

        fields =  ['username', 'first_name', 'last_name', 'email', 'phone_number', 'age', 'password']


    def clean(self):
        super(AccountsForm, self).clean()

        username = self.cleaned_data.get('username') 
        first_name = self.cleaned_data.get('first_name') 
        last_name = self.cleaned_data.get('last_name') 
        email = self.cleaned_data.get('email') 
        phone_number = self.cleaned_data.get('phone_number') 
        age = self.cleaned_data.get('age') 
        password = self.cleaned_data.get('password')
        
        if len(username) < 5:
            self._errors['fname'] = self.error_class(['Min length 5 '])

        if len(first_name) < 5:

            self._errors['first_name'] = self.error_class(['Min length 5 '])
        
        if len(last_name) < 5:

            self._errors['first_name'] = self.error_class(['Min length 5 '])

        if not('@' in email and ('.com' in email or '.uz' in email or '.ru' in email or '.org' in email)):
            self._errors['email'] = self.error_class(['Email '])
        
        if len(phone_number) < 8:
            self._errors['phone_nnumber'] = self.error_class(['Phone number '])
        
        if int(age)  < 8:
            self._errors['age'] = self.error_class(['You hav to 8 age'])
        
        if len(password) < 8:
            
            self._errors['password'] = self.error_class(['password min length 8'])

        
        return self.cleaned_data
        
