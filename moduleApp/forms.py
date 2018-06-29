from django import forms

from .models import AddModule, EditModule

class AddModuleForm(forms.ModelForm):
    class Meta:
        # ordering=('order_no')
        model = AddModule
        fields = ('module_name', 'order_no')

class EditModuleForm(forms.ModelForm):
    class Meta:
        model = EditModule
        fields = ( 'module_name', 'submodule_name', 'path' )
