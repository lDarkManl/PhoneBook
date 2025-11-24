from django.http import HttpResponse
import csv
from contacts.models import EmployeeDivision

def export_department_csv(request, subdivision_id):
    qs = EmployeeDivision.objects.filter(subdivision_id=subdivision_id).select_related('employee','post')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="department_{subdivision_id}.csv"'
    writer = csv.writer(response)
    writer.writerow(['ФИО','Должность','Вн. телефон','Гор. телефон','Email'])
    for ed in qs:
        writer.writerow([f"{ed.employee.surname} {ed.employee.name}", ed.post.name, ed.internal_phone or '', ed.city_phone or '', ed.email or ''])
    return response

# Import helper referencing uploaded DOCX path
def import_from_docx(request):
    # This view is a stub. For full import use management command pointing to the uploaded file.
    return HttpResponse('Use management command to import from /mnt/data/Kursovaya_BD2.docx')
