from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from providers.models import Patient, Prescription
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Sends reminders to patients'
    #this is what the command actually does
    def handle(self, *args, **kwargs):
        #sets now to current time
        now = timezone.now()
        now = timezone.localtime(now)
        
        #save hour, min, and day info to compare to prescription
        current_hour = now.hour
        current_min = now.minute
        current_day = now.strftime('%A')

        #round minute to the nearest 15 minute mark (in case command runs a lil late)
        current_min = (current_min // 15) * 15

        #currently, Prescription.hour is in 12 hour time.
        #first, we just want prescriptions that match the other two fields (day and min)
        prescriptions_today = Prescription.objects.filter(
        day__iexact=current_day,
        min=current_min
        )

        #create a list of all due medications (defaults as empty)
        due = []

        #now we want to take all those prescriptions and convert to 24 hour time before comparing
        for prescription in prescriptions_today:
            hour = prescription.hour

            if prescription.meridiem == 'PM' and hour != 12:
                hour = hour + 12

            if prescription.meridiem == 'AM' and hour == 12:
                hour = 0

            #append if prescription is due
            if hour == current_hour:
                due.append(prescription)


        #now we send an email to each patient for each due prescription
        for prescription in due:
            patient = prescription.patient
            user_email = patient.user.email
            
            send_mail(
                subject='Medication Reminder',
                message=f"Hi {patient.first}, it's {prescription.hour:02}:{prescription.min:02}, time to take {prescription.med}!",
                from_email='remedireminders@gmail.com',
                recipient_list=[user_email],
                fail_silently=False,
            )

        self.stdout.write(self.style.SUCCESS(f'Sent {len(due)} medication reminders at {current_hour:02}:{current_min:02} on {current_day}'))

        