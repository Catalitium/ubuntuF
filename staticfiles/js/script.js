
document.addEventListener('DOMContentLoaded', function () {
    // Get the doctor dropdown and the submission method prompt
    const doctorDropdown = document.getElementById('doctor');
    const submissionMethodPrompt = document.getElementById('submission-method-prompt');

    // Listen for changes on the doctor dropdown
    doctorDropdown.addEventListener('change', function () {
        // Check if a valid doctor is selected
        if (doctorDropdown.value) {
            // Show the submission method prompt
            submissionMethodPrompt.style.display = 'block';
        } else {
            // Hide the submission method prompt if no doctor is selected
            submissionMethodPrompt.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
  const doctorDropdown = document.getElementById('doctor');
  const submissionMethodPrompt = document.getElementById('submission-method-prompt');
  const appointmentFormFields = document.getElementById('appointment-form-fields');
  
  // Buttons for WhatsApp and Email
  const whatsappButton = document.getElementById('whatsapp-button');
  const emailButton = document.getElementById('email-button');

  // Listen for changes on the doctor dropdown
  doctorDropdown.addEventListener('change', function () {
      if (doctorDropdown.value) {
          submissionMethodPrompt.style.display = 'block';
      } else {
          submissionMethodPrompt.style.display = 'none';
          appointmentFormFields.style.display = 'none';
      }
  });

  // Show the form when a method is chosen
  whatsappButton.addEventListener('click', function () {
      appointmentFormFields.style.display = 'block';
      console.log('WhatsApp method selected'); // Optional: Debugging/logging
  });

  emailButton.addEventListener('click', function () {
      appointmentFormFields.style.display = 'block';
      console.log('Email method selected'); // Optional: Debugging/logging
  });
});    

// Function to handle selection of contact method (WhatsApp or Email)
function selectMethod(method) {
// Store the selected method in the hidden input field
document.getElementById('contact_method').value = method;

// Display the appointment form fields after selection
document.getElementById('appointment-form-fields').style.display = 'block';

// Optionally hide the submission method prompt after selection
document.getElementById('submission-method-prompt').style.display = 'none';
}

function selectMethod(method) {
// Store the selected method in the hidden input field
document.getElementById('contact_method').value = method;

// Display the appointment form fields after selection
document.getElementById('appointment-form-fields').style.display = 'block';

// Optionally hide the submission method prompt after selection
document.getElementById('submission-method-prompt').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function () {
    const doctorDropdown = document.getElementById('doctor');
    const doctorDetails = document.getElementById('doctor-details');
    const doctorName = document.getElementById('doctor-name');
    const doctorSpecialty = document.getElementById('doctor-specialty');
    const toggleDetails = document.getElementById('toggle-details');
    const doctorInfo = document.getElementById('doctor-info');

    // Handle doctor selection
    doctorDropdown.addEventListener('change', function () {
        const selectedDoctor = doctorDropdown.value;

        // Show doctor details based on selection
        if (selectedDoctor) {
            doctorDetails.style.display = 'block';
            // Replace doctor info dynamically based on selection
            doctorName.textContent = `Nombre: Dr. ${selectedDoctor}`;
            doctorSpecialty.textContent = `Especialidad: Medicina General`;

            // Reset or set specific doctor details based on the selected doctor
        } else {
            doctorDetails.style.display = 'none';
        }
    });

    // Toggle doctor details visibility
    toggleDetails.addEventListener('click', function () {
        if (doctorInfo.style.display === 'none') {
            doctorInfo.style.display = 'block';
            toggleDetails.innerHTML = '&#x25B2;'; // Up arrow
        } else {
            doctorInfo.style.display = 'none';
            toggleDetails.innerHTML = '&#x25BC;'; // Down arrow
        }
    });
});
