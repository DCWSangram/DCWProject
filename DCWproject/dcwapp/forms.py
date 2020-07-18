from django import forms
from re import fullmatch
def validate(mobile):
    regex = "[6-9][0-9]{9}"
    match = fullmatch(regex,mobile)
    if match:
        return True
    else:
        return False
class SignupForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())
    cpassword = forms.CharField(widget = forms.PasswordInput())
    mobile_number = forms.CharField(max_length=10)
    gender = forms.CharField(widget=
    forms.RadioSelect(choices=[('male','Male'),('Female','Female'),('transgender','Transgender')]))
    bot = forms.CharField(widget=forms.HiddenInput(),required=False)

    def clean(self):
        cd = super().clean()
        pwd1 = cd['password']
        pwd2 = cd['cpassword']
        bot = cd['bot']
        mobile = cd['mobile_number']
        if bot:
            raise forms.ValidationError("Thanks bot")
        if pwd1 != pwd2:
            raise forms.ValidationError("Password shoud be matched...")
        if len(pwd1) < 6:
            raise forms.ValidationError("Password shoud contain atleast 6 charcters...")
        if validate(mobile):
            pass
        else:
            raise forms.ValidationError("Invalid mobile number...Mobile Number should starts with either 6 or 7 or 8 or 9")
        
