from django.contrib import admin
from .models import EventPicture, Teacher, Notice, StudentRegistration, ResultYear, Result12th, Result10th, Event

admin.site.site_header = "Staff-Admin MCHS School"


class CustSR(admin.ModelAdmin):
    list_display = ('name', 'date', 'contact_number', 'city')


class CustEP(admin.ModelAdmin):
    list_display = ('event', 'featured')
    radio_fields = {'event': admin.VERTICAL}


class CustE(admin.ModelAdmin):
    pass


admin.site.register(Teacher)
admin.site.register(Notice)
admin.site.register(ResultYear)
admin.site.register(Result12th)
admin.site.register(Result10th)
admin.site.register(StudentRegistration, CustSR)
admin.site.register(Event)
admin.site.register(EventPicture, CustEP)
