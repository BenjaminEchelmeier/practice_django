from django import forms
from .models import Users


class AddUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        """first = forms.CharField(max_length=20)
        last = forms.CharField(max_length=20)
        email = forms.EmailField(max_length=50)
        vemail = forms.EmailField(label="Confirm Email: ", max_length=50)"""

        """def clean(self):
            all_clean_data = super(AddUser, self).clean()
            email = all_clean_data['email']
            vemail = all_clean_data['verify_email']

            if email != vemail:
                raise forms.ValidationError("Please ensure emails match")
"""