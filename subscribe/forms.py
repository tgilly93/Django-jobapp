from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        # exclude=('first_name',)
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email')
        }
        # help_texts={'first_name':_("Enter characters only")}
        error_messages={
            'first_name':{
                'required':_('You cannot move forward without first name')
            },
        }


# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid Last Name")
#     return value

# class SubscribeForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100, label="Enter first name", help_text="Enter characters only")
#     last_name = forms.CharField(max_length=100, disabled=False, validators=[validate_comma])
#     email = forms.EmailField(max_length=100,)
    
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return data
    
