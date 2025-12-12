from django import forms
from .models import Vendor, VendorAssignment


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'category', 'contact_person', 'email', 'phone', 'address',
                  'service_description', 'base_price', 'rating', 'is_active', 'notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'service_description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.widget.__class__.__name__ != 'CheckboxInput':
                field.widget.attrs.update({'class': 'form-control'})


class VendorAssignmentForm(forms.ModelForm):
    class Meta:
        model = VendorAssignment
        fields = ['vendor', 'service_date', 'service_time', 'agreed_price', 'notes']
        widgets = {
            'service_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'service_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendor'].queryset = Vendor.objects.filter(is_active=True)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


