from django.shortcuts import render
from .models import Match
import json
from django.http import JsonResponse

def matches_per_year(request):
    matches = Match.objects.values('season').order_by('season').annotate(matches=Count('id'))
    data = []
    for match in matches:
        data.append({
            'name': match['season'],
            'matches': match['matches']
        })
    return JsonResponse(data, safe=False)

def matches_won(request):
    matches = Match.objects.values('winner').annotate(matches=Count('id'))
    data = []
    for match in matches:
        data.append({
            'name': match['winner'],
            'matches': match['matches']
        })
    return JsonResponse(data, safe=False)

def extra_runs_conceded(request, year):
    matches = Match.objects.filter(season=year).values('bowling_team').annotate(runs=Sum('extra_runs'))
    data = []
    for match in matches:
        data.append({
            'name': match['bowling_team'],
            'runs': match['runs']
        })
    return JsonResponse(data, safe=False)

def top_economical_bowlers(request, year):
    deliveries = Delivery.objects.filter(match__season=year).values('bowler').annotate(runs=Sum('total_runs')).annotate(balls=Count('id'))
    data = []
    for delivery in deliveries:
        data.append({
            'name': delivery['bowler'],
            'economy': delivery['runs']/delivery['balls']*6
        })
    data.sort(key=lambda x: x['economy'])
    return JsonResponse(data[:10], safe=False)

def matches_played_vs_won(request, year):
    matches = Match.objects.filter(season=year).values('team1', 'team2', 'winner')
    data = []
    for match in matches:
        data.append({
            'name': match['team1'],
            'played': 1,
            'won': 1 if match['team1'] == match['winner'] else 0
        })
        data.append({
            'name': match['team2'],
            'played': 1,
            'won': 1 if match['team2'] == match['winner'] else 0
        })
    chart_data = {}
    for item in data:
        if item['name'] in chart_data:
            chart_data[item['name']]['played'] += item['played']
            chart_data[item['name']]['won'] += item['won']
        else:
            chart_data[item['name']] = {
                'name': item['name'],
                'played': item['played'],
                'won': item['won']
            }
    return JsonResponse(list(chart_data.values()), safe=False)
