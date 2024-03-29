from django.contrib import admin
from django.db import models
from django.forms import TextInput
from .models import Users, Voting, VotingProcess, Candidate


class UsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    search_fields = ('full_name', 'email')


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '25'})},
    }


class VotingAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'finish_date', 'quorum', 'is_secret')
    filter_horizontal = ('allowed_users',)
    inlines = [CandidateInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)


admin.site.register(Users, UsersAdmin)
admin.site.register(Voting, VotingAdmin)

# Параметры ниже удалить при фактическом показе проекта с целью скрытия возможности их редактирования
admin.site.register(VotingProcess)
