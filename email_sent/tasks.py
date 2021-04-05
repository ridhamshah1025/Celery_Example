from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def sent_mail():
    sleep(10)
    send_mail("hello", 'hi How are You?' , 'ridhamdata@gmail.com', ['ridhamshah1025@gmail.com'])
    return None

