from datetime import timedelta
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from theWowAdv.models import Advertisement, NewsLetterSubscribedUsers
from django.conf import settings

def send_notification(subscriber, adv_obj):
    template ='mailing/weekly_notification.html'
    subject = f'Еженедельная рассылка новых публикаций'
    html = render_to_string(
        template_name = template,
        context = {
            'subscriber': subscriber,
            'advertisements_for_a_week': adv_obj,
            },
        )
    
    msg = EmailMultiAlternatives(
        subject = subject,
        body = '',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = [subscriber.email,],
        )
    msg.attach_alternative(html, "text/html")
    msg.send()
   
def weelky_advertisements_job():
    advForWeek = Advertisement.objects.filter(pub_date__lte=timezone.now()-timedelta(weeks=1))
    if not advForWeek:
        return   
    for subscriber in NewsLetterSubscribedUsers.objects.all(): 
        send_notification(subscriber, advForWeek)