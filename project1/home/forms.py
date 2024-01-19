from django import forms

class addEmpForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    age = forms.IntegerField()


class findUserForm(forms.Form):
    email = forms.EmailField()

# <label for="email">Enter Email:</label>
        # <input type="email" name="email">


# form for the Member model.

# 1)change template
# 2)update view to pass this form in context