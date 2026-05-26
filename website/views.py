from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import EmissionRecord
import csv
import io


# DASHBOARD
def dashboard(request):

    # SEARCH
    query = request.GET.get('q')
    status_filter = request.GET.get('status')

    records = EmissionRecord.objects.all()

    if query:
        records = records.filter(company_name__icontains=query)

    if status_filter:
        records = records.filter(status=status_filter)

    # ADD RECORD
    if request.method == 'POST' and 'company_name' in request.POST:

        company_name = request.POST.get('company_name')
        amount = request.POST.get('amount')
        facility_name = request.POST.get('facility_name')
        status = request.POST.get('status')
        source_type = request.POST.get('source_type')

        # SUSPICIOUS CHECK
        is_suspicious = False

        if float(amount) > 500:
            is_suspicious = True

        EmissionRecord.objects.create(
            company_name=company_name,
            amount=amount,
            facility_name=facility_name,
            status=status,
            source_type=source_type,
            is_suspicious=is_suspicious
        )

        return redirect('/')

    # TOTAL EMISSION
    total_emission = 0

    for record in records:
        total_emission += record.amount

    return render(
        request,
        'index.html',
        {
            'records': records,
            'total_emission': total_emission
        }
    )


# DELETE RECORD
def delete_record(request, id):

    record = get_object_or_404(EmissionRecord, id=id)

    record.delete()

    return redirect('/')


# EDIT RECORD
def edit_record(request, id):

    record = get_object_or_404(EmissionRecord, id=id)

    if request.method == 'POST':

        record.company_name = request.POST.get('company_name')
        record.amount = request.POST.get('amount')
        record.facility_name = request.POST.get('facility_name')
        record.status = request.POST.get('status')
        record.source_type = request.POST.get('source_type')

        # UPDATE SUSPICIOUS
        if float(record.amount) > 500:
            record.is_suspicious = True
        else:
            record.is_suspicious = False

        record.save()

        return redirect('/')

    return render(
        request,
        'edit.html',
        {
            'record': record
        }
    )


# CSV UPLOAD
def upload_csv(request):

    if request.method == 'POST':

        csv_file = request.FILES['file']

        data = csv_file.read().decode('utf-8')

        io_string = io.StringIO(data)

        next(io_string)

        for row in csv.reader(io_string):

            is_suspicious = False

            if float(row[1]) > 500:
                is_suspicious = True

            EmissionRecord.objects.create(
                company_name=row[0],
                amount=row[1],
                facility_name=row[2],
                status=row[3],
                source_type=row[4],
                is_suspicious=is_suspicious
            )

    return redirect('/')


# API
def api_records(request):

    records = EmissionRecord.objects.all()

    data = []

    for record in records:

        data.append({
            'company_name': record.company_name,
            'amount': record.amount,
            'facility_name': record.facility_name,
            'status': record.status,
            'source_type': record.source_type,
            'is_suspicious': record.is_suspicious,
        })

    return JsonResponse(data, safe=False)