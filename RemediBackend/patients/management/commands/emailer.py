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

        #we only want to send emails to users who are due for taking a prescription
        #to do this, we compare the time of each prescription to the current time (now)
        due = Prescription.objects.filter (
            day = current_day,
            hour = current_hour,
            min = current_min
        )

        #now we send an email to each patient for each due prescription
        for prescription in due:
            patient = prescription.patient
            user_email = patient.user.email
            
            send_mail(
                subject='Medication Reminder',
                message=f"Hi {patient.first}, it's {prescription.hour:02}:{prescription.min:02}, time to take {prescription.med}!",
                from_email='camdenwalker0622@gmail.com',
                recipient_list=[user_email],
                fail_silently=False,
            )

        self.stdout.write(self.style.SUCCESS(f'Sent {due.count()} medication reminders at {current_hour:02}:{current_min:02} on {current_day}'))

        