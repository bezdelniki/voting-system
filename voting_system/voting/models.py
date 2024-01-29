from django.db import models


class Users(models.Model):
    full_name = models.CharField(max_length=256, blank=False, null=False)


class Voting(models.Model):
    variants = models.TextField(blank=False, null=False)


class VotingProcess(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    enter_code = models.TextField(max_length=10, blank=False, null=False)
    chosen = models.TextField(blank=False)

class SendResults(models.Model):
    voting_process = models.ForeignKey(VotingProcess, on_delete=models.CASCADE)
    email = models.TextField(blank=False, null=False)