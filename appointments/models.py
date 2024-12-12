from django.db import models

# Patient Table
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Doctor Table (Lookup Table)
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# Appointment Table
class Appointment(models.Model):
    # Basic patient details
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    phone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    # Appointment date as a string
    requested_appointment_date = models.CharField(max_length=19) 
    appointment_created_at = models.DateTimeField(auto_now_add=True)

    # Additional details
    motive = models.TextField(blank=True, null=True)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    # Contact method choice (Email or WhatsApp)
    
    CONTACT_METHOD_CHOICES = [
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
    ]
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES, default='email')

    def __str__(self):
        return f"Appointment for {self.patient_name} with {self.doctor.name} on {self.requested_appointment_date} ({self.status}) via {self.contact_method}"