from django.contrib import admin
from .models import Doctor, Appointment, Patient  # Import Appointment model

# Register the Doctor and Patient models (if necessary)
admin.site.register(Doctor)
admin.site.register(Patient)

# Admin configuration for the Appointment model
class AppointmentAdmin(admin.ModelAdmin):
    # Update 'date' to 'requested_appointment_date'
    list_display = ('patient_name', 'doctor', 'requested_appointment_date', 'appointment_created_at', 'status', 'motive', 'contact_method')
    
    # Add filters to the right sidebar for better management
    list_filter = ('doctor', 'status', 'contact_method')  # Filter appointments by doctor, status, and contact method
    
    # Allow searching by patient name, patient email, and doctor name
    search_fields = ('patient_name', 'patient_email', 'doctor__name', 'contact_method')
    
    # Default ordering by requested appointment date
    ordering = ('appointment_created_at',)  # Order appointments by requested date
    
    # Add contact_method as a field to display in the form
    fieldsets = (
        (None, {
            'fields': ('patient_name', 'patient_email', 'doctor', 'requested_appointment_date', 'motive', 'contact_method')
        }),
    )

# Register the Appointment model with custom admin view
admin.site.register(Appointment, AppointmentAdmin)