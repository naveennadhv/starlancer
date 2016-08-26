from django.contrib import admin
from .models import Student,School

class StudentAdmin(admin.ModelAdmin):
    list_display = ('getname', 'marks', 'percentage', 'getSchool','uuid')
    exclude = ('uuid',)
    # Name
    def getname(self, obj):
        return obj.name.capitalize()
    getname.short_description = 'Name'

    # School
    def getSchool(self, obj):
        return obj.school.name.capitalize()
    getSchool.short_description = 'School'

    # Percentage
    def percentage(self, obj):
        percent = round((obj.marks/150) * 100,2)
        return str("{0:.2f}".format(percent)) + '%'

admin.site.register(Student, StudentAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','location')

admin.site.register(School, SchoolAdmin)

# Register your models here.
