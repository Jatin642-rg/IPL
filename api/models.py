from django.db import models

class Match(models.Model):
    id = models.BigAutoField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=100)
    date = models.DateField()
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    toss_winner = models.CharField(max_length=100)
    toss_decision = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=100)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    umpire1 = models.CharField(max_length=100)
    umpire2 = models.CharField(max_length=100)
    umpire3 = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)