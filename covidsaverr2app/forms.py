from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from covidsaverr2app.models import covidappUser, Person, Grad, Restoran,appuser


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    # phone_no = forms.CharField(max_length=20)
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    #
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        # fields = ['first_name', 'last_name', 'year_of_birth', 'tel_no', 'grad', 'password1', 'password2']
        # exclude=("kategorija",)
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class kadesakateform(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['grad', 'restoran']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['restoran'].queryset = Restoran.objects.none()

            if 'grad' in self.data:
                try:
                    grad_id = int(self.data.get('grad'))
                    self.fields['restoran'].queryset = Restoran.objects.filter(grad_id=grad_id).order_by('grad')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['restoran'].queryset = self.instance.grad.restoran_set.order_by('grad')


class statusform(forms.ModelForm):
    class Meta:
        model = appuser
        fields = ['vakciniran', 'prelezankovid','first_name','last_name' ]

        def __init__(self, *args, **kwargs):
            super(statusform, self).__init__(*args, **kwargs)
            for field in self.visible_fields():
                print(field)
                field.field.widget.attrs["class"] = "form-control"


class kadesteform(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['grad', 'restoran']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['restoran'].queryset = Restoran.objects.none()

            if 'grad' in self.data:
                try:
                    grad_id = int(self.data.get('grad'))
                    self.fields['restoran'].queryset = Restoran.objects.filter(grad_id=grad_id).order_by('grad')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['restoran'].queryset = self.instance.grad.restoran_set.order_by('grad')


class welcomeform(forms.ModelForm):
    class Meta:
        model = covidappUser
        fields = ['cover_image']

    def __init__(self, *args, **kwargs):
        super(welcomeform, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"
