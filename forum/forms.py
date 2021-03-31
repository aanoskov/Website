from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
   # blog_title = forms.CharField(label='Blog Title', max_length=80)
    username = forms.CharField(label='Username', max_length=64)
    email = forms.EmailField(label='E-mail', max_length=128)
   # phone = forms.CharField(label='Phone number', min_length=7, max_length=15)
    password = forms.CharField(label='Password', min_length=3, max_length=128, widget=forms.PasswordInput)
    password_again = forms.CharField(label='Password again', min_length=3, max_length=128, widget=forms.PasswordInput)


create_choices =(
    (True, "opened"),
    (False, "closed")
)
class CreatingSection(forms.Form):
    blog_title = forms.CharField(label='Blog Title', max_length=80)
    opened = forms.ChoiceField(choices=create_choices)
    password = forms.CharField(label='Password', min_length=3, max_length=128, widget=forms.PasswordInput)
    

class CreatingPost(forms.Form):
    subject = forms.CharField(label="Post Subject", max_length=80)
    text = forms.CharField(label="Text", max_length=4096, widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 10,'placeholder': 'Write something about this place'}))
    review_image = forms.ImageField(label="photo", required=False)

buy_choices =(
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (5, "5"),
    (7, "7"),
)
class BuyTickets(forms.Form):
    phone = forms.CharField(label='Phone number', min_length=7, max_length=15)
    adults = forms.IntegerField(label='Amount of adults')
    kids = forms.IntegerField(label='Amount of kids')
    days = forms.ChoiceField(choices=buy_choices)
