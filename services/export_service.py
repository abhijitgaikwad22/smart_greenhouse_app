"""
Export service module.
Handles PDF and CSV export functionality.
"""

from flask import make_response
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import io
import csv
from datetime import datetime

def export_to_pdf(data):
    """Generate PDF report from detection data"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        alignment=TA_CENTER,
        spaceAfter=30
    )
    title = Paragraph("Greenhouse Environment Report", title_style)
    story.append(title)
    
    # Timestamp
    timestamp = Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal'])
    story.append(timestamp)
    story.append(Spacer(1, 20))
    
    # Input Data
    story.append(Paragraph("Input Parameters", styles['Heading2']))
    input_data = [
        ["Parameter", "Value"],
        ["Crop Type", data['crop']],
        ["Temperature", f"{data['temperature']}°C"],
        ["Humidity", f"{data['humidity']}%"],
        ["Soil Moisture", f"{data['soil_moisture']}%"],
        ["Light Intensity", f"{data['light']}%"]
    ]
    
    input_table = Table(input_data)
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(input_table)
    story.append(Spacer(1, 20))
    
    # Analysis Results
    story.append(Paragraph("Analysis Results", styles['Heading2']))
    
    # Status and Score
    status_data = [
        ["Overall Status", data['result']['status']],
        ["Suitability Score", f"{data['result']['score']}%"],
        ["Health Indicator", data['result']['health_indicator']]
    ]
    
    status_table = Table(status_data)
    status_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(status_table)
    story.append(Spacer(1, 20))
    
    # Alerts
    story.append(Paragraph("Alerts", styles['Heading3']))
    for alert in data['result']['alerts']:
        story.append(Paragraph(f"• {alert}", styles['Normal']))
    story.append(Spacer(1, 10))
    
    # Recommendations
    story.append(Paragraph("Recommendations", styles['Heading3']))
    for rec in data['result']['recommendations']:
        story.append(Paragraph(f"• {rec}", styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    
    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=greenhouse_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
    
    return response

def export_history_csv():
    """Export detection history as CSV"""
    csv_path = 'data/history.csv'
    
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            csv_data = f.read()
        
        response = make_response(csv_data)
        response.headers['Content-Type'] = 'text/csv; charset=utf-8'
        response.headers['Content-Disposition'] = f'attachment; filename=greenhouse_history_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        
        return response
    except FileNotFoundError:
        return "History not found", 404
    except Exception as e:
        return str(e), 500
