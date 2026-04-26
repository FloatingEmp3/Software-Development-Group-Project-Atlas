from django.shortcuts import render
from teams.models import Team
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from openpyxl import Workbook


def report_dashboard(request):
    teams = Team.objects.all()

    total_teams = teams.count()

    # FIXED: use team_leader instead of manager
    teams_without_manager = teams.filter(team_leader__isnull=True) | teams.filter(team_leader="")

    return render(request, 'reports/report.html', {
        'total_teams': total_teams,
        'teams': teams,
        'teams_without_manager': teams_without_manager
    })



def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    teams = Team.objects.all()
    total = teams.count()

    content = []
    content.append(Paragraph(f"Total Teams: {total}", styles['Title']))

    for team in teams:
        leader = team.team_leader if team.team_leader else "No Manager"
        content.append(Paragraph(f"{team.team_name} - {leader}", styles['Normal']))

    doc.build(content)
    return response



def generate_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Teams Report"

    ws.append(["Team Name", "Team Leader", "Department"])

    teams = Team.objects.all()

    for team in teams:
        leader = team.team_leader if team.team_leader else "No Manager"
        ws.append([team.team_name, leader, team.department])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=report.xlsx'

    wb.save(response)
    return response