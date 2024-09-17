from  django import forms 

from .models import Employee 

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee 
        fields = '__all__'

    # apply bootstrap form class to all fields
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.label

        # resize default textarea
        self.fields['short_desc'].widget.attrs.update({'rows':5, 'columns':5})

    # validate phone number
    def validate_phone(self, phone):
        phone = self.phon
        print(' i am calling', phone)
        if Employee.objects.filter(phone=phone).exists():
            raise forms.ValidationError('A user with this phone number is already exist.')
        return phone


class UpdateEmployeeForm(EmployeeForm): # ops last time i inherit this form :) 

    class Meta:
        model = Employee 
        exclude = ('salary','designation')

    # # apply bootstrap form class to all fields
    # def __init__(self, *args, **kwargs):
    #     super(UpdateEmployeeForm,self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
    #         visible.field.widget.attrs['placeholder'] = visible.label

    #     # resize default textarea
    #     self.fields['short_desc'].widget.attrs.update({'rows':5, 'columns':5})

    # # validate phone number
    # def validate_phone(self, phone):
    #     phone = self.phon
    #     print(' i am calling', phone)
    #     if Employee.objects.filter(phone=phone).exists():
    #         raise forms.ValidationError('A user with this phone number is already exist.')
    #     return phone
    