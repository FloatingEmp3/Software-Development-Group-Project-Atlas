#Ayberk Beden w2134939

from django.shortcuts import render
from teams.models import Team
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from openpyxl import Workbook
from openpyxl.styles import Font
from django.db.models import Count

def report_dashboard(request):
    teams = Team.objects.all()

    total_teams = teams.count()

    teams_without_leader = teams.filter(team_leader__isnull=True) | teams.filter(team_leader="")

    teams_per_department = teams.values('department').annotate(count=Count('id')).order_by('-count')

    teams_with_repo = teams.exclude(github_repo="")
    teams_without_repo = teams.filter(github_repo="")

    context = {
        'total_teams': total_teams,
        'teams': teams,
        'teams_without_leader': teams_without_leader,
        'teams_per_department': teams_per_department,
        'teams_with_repo': teams_with_repo.count(),
        'teams_without_repo': teams_without_repo.count(),
    }

    return render(request, 'reports/report.html', context)


def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="teams_report.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    teams = Team.objects.all()
    content = []

    # Title
    content.append(Paragraph("Engineering Teams Full Report", styles['Title']))
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Total Teams: {teams.count()}", styles['Heading2']))
    content.append(Spacer(1, 20))

    for team in teams:
        content.append(Paragraph(f"<b>{team.team_name}</b>", styles['Heading3']))
        content.append(Spacer(1, 6))

        details = f"""
        <b>Department:</b> {team.department}<br/>
        <b>Department Head:</b> {team.department_head or 'N/A'}<br/>
        <b>Team Leader:</b> {team.team_leader or 'N/A'}<br/>
        <b>Project:</b> {team.project_name or 'N/A'}<br/>
        <b>GitHub Repo:</b> {team.github_repo or 'N/A'}<br/>
        <b>Focus Areas:</b> {team.focus_areas or 'N/A'}<br/>
        <b>Skills:</b> {team.skills or 'N/A'}<br/>
        <b>Upstream Dependencies:</b> {team.upstream_dependencies or 'N/A'}<br/>
        <b>Downstream Dependencies:</b> {team.downstream_dependencies or 'N/A'}<br/>
        <b>Slack Channels:</b> {team.slack_channels or 'N/A'}<br/>
        <b>Team Wiki:</b> {team.team_wiki or 'N/A'}<br/>
        """

        content.append(Paragraph(details, styles['Normal']))
        content.append(Spacer(1, 18))

    doc.build(content)
    return response

def generate_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Teams Report"

    headers = [
        "Team Name",
        "Department",
        "Department Head",
        "Team Leader",
        "Project",
        "GitHub Repo",
        "Focus Areas",
        "Skills",
        "Upstream Dependencies",
        "Downstream Dependencies",
        "Slack Channels",
        "Team Wiki"
    ]

    ws.append(headers)

    # Style header row
    for cell in ws[1]:
        cell.font = Font(bold=True)

    teams = Team.objects.all()

    for team in teams:
        ws.append([
            team.team_name,
            team.department,
            team.department_head or "N/A",
            team.team_leader or "N/A",
            team.project_name or "N/A",
            team.github_repo or "N/A",
            team.focus_areas or "N/A",
            team.skills or "N/A",
            team.upstream_dependencies or "N/A",
            team.downstream_dependencies or "N/A",
            team.slack_channels or "N/A",
            team.team_wiki or "N/A"
        ])

    # Auto column width (simple version)
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass

        ws.column_dimensions[column_letter].width = min(max_length + 2, 50)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=teams_report.xlsx'

    wb.save(response)
    return response

