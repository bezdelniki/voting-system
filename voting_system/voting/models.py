from django.db import models
from datetime import datetime
import string
import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from math import ceil
from django.db.models.signals import m2m_changed

class Users(models.Model):
    full_name = models.CharField(max_length=256, blank=False, null=False)
    email = models.CharField(max_length=320, blank=False, null=False)

    def __str__(self):
        return self.full_name

class Voting(models.Model):
    start_date = models.DateTimeField(blank=False, null=False, default=datetime.now())
    finish_date = models.DateTimeField(blank=False, null=False, default=datetime.now())
    allowed_users = models.ManyToManyField(Users, related_name='allowed_votings')
    participation_percentage = models.PositiveIntegerField(default=0)
    is_secret = models.BooleanField(default=False)

    @property
    def quorum(self):
        total_users_count = self.allowed_users.count()
        return ceil(total_users_count * (self.participation_percentage / 100))
    
class Candidate(models.Model):
    names = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    birth = models.DateField()
    role = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    voting = models.ForeignKey(Voting, related_name='candidates', on_delete=models.CASCADE)

    def to_json(self):
        return {
            'names': self.names,
            'surnames': self.surnames,
            'birth': self.birth.strftime('%Y-%m-%d'),
            'role': self.role,
            'position': self.position,
        }

class VotingProcess(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    enter_code = models.TextField(max_length=10, blank=False, null=False, unique=True)
    chosen = models.TextField(blank=False)
    is_entered = models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)
    is_secret = models.BooleanField(default=False)

    def __str__(self):
        return f'Бюллетень избирателя {self.user.full_name} в голосовании номер {self.voting.id}'

class SendResults(models.Model):
    voting_process = models.ForeignKey(VotingProcess, on_delete=models.CASCADE)
    email = models.TextField(blank=False, null=False)

@receiver(m2m_changed, sender=Voting.allowed_users.through)
def create_voting_process_for_users(sender, instance, action, **kwargs):
    if action == 'post_add':
        for user_id in kwargs['pk_set']:
            user = Users.objects.get(pk=user_id)
            random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            # ДОБАВИТЬ РЕАЛИЗАЦИЮ ОТПРАВКИ КОДА НА EMAIL
            VotingProcess.objects.create(user=user, voting=instance, enter_code=random_code, is_secret=instance.is_secret)