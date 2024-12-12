from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Appointment
from .forms import AppointmentForm
import logging
from django.shortcuts import render, get_object_or_404
from .models import Appointment

logger = logging.getLogger(__name__)

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Create the appointment object without saving to DB yet
            appointment = form.save(commit=False)
            
            # Directly assign the requested appointment date as a string
            appointment.requested_appointment_date = form.cleaned_data['requested_appointment_date']
            
            # Save the appointment to the database
            appointment.save()

            # Store the appointment ID in the session
            request.session['appointment_id'] = appointment.id

            # Send the confirmation email to the user (patient)
            subject = 'Appointment Confirmation'
            message = f'Your appointment has been booked with Dr. {appointment.doctor.name} on {appointment.requested_appointment_date}.'
            from_email = 'catalitium@gmail.com'  # Replace with your actual email
            """ recipient_list = [form.cleaned_data['email']] """
            """ recipient_list = ['catalitium@gmail.com']
            send_mail(subject, message, from_email, recipient_list) """

            # Optionally, send a confirmation email to the doctor's secretary as well
            doctor_secretary_email = 'catalitium@gmail.com'  # Replace with the secretary's email
            """ send_mail(subject, message, from_email, [doctor_secretary_email]) """

            return redirect('success')  # Redirect to the success page after booking the appointment
        else:
            print(form.errors)  # Log form errors to help with debugging

    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form})

def success(request):
    appointment_id = request.session.get('appointment_id')
    if not appointment_id:
        # Handle the case where there is no appointment ID in the session
        return render(request, 'appointments/error.html', {'error_message': "No appointment found."})

    # Fetch the appointment from the database
    appointment = get_object_or_404(Appointment, id=appointment_id)

    context = {
        'appointment': appointment
    }
    return render(request, 'appointments/success.html', context)
