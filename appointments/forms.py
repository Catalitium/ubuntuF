from django import forms
from .models import Appointment, Doctor

class AppointmentForm(forms.ModelForm):
    patient_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))  # Keep the email field
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
   
    contact_method = forms.ChoiceField(
        choices=[('whatsapp', 'WhatsApp'), ('email', 'Email')],
        initial='email',
        widget=forms.RadioSelect,
    )
    
    requested_appointment_date = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter appointment date and time'}),
    )
    
    motive = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter the reason for your appointment', 'class': 'mobile-friendly-textarea'}), 
        required=False
    )

    class Meta:
        model = Appointment
        fields = ['patient_name', 'phone', 'requested_appointment_date', 'doctor', 'email', 'motive','contact_method']

    def save(self, commit=True):
        # Override save to map the email field to patient_email
        instance = super().save(commit=False)
        instance.patient_email = self.cleaned_data.get('email')  # Map form email to model patient_email
        if commit:
            instance.save()
        return instance