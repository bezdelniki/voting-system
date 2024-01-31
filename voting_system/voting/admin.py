from django.contrib import admin
from .models import Users, Voting, VotingProcess, SendResults, Candidate

class UsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    search_fields = ('full_name', 'email')

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1

class VotingAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'finish_date', 'quorum', 'is_secret')  
    filter_horizontal = ('allowed_users',)
    inlines = [CandidateInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

admin.site.register(Users, UsersAdmin)
admin.site.register(Voting, VotingAdmin)
admin.site.register(VotingProcess)
admin.site.register(SendResults)