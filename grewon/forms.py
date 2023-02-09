from django import forms

class FreeUsersForm(forms.Form):
    date_time = forms.DateTimeField(
                            widget= forms.TextInput
                           (attrs={'placeholder':'YYYY-MM-DD HH:MM:SS'})
                        )