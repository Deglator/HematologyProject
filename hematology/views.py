from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Record
from django.utils import timezone
from .forms import RecordForm



def record_list(request):
    records = Record.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hematology/record_list.html', {'records' : records})

def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'hematology/record_detail.html', {'record': record})

@login_required
def record_new(request):
    form = RecordForm()
    return render(request, 'hematology/record_edit.html', {'form': form})

@login_required
def record_new(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.doctor = request.user
            record.published_date = timezone.now()
            record.save()
            return redirect('record_detail', pk=record.pk)
    else:
        form = RecordForm()
    return render(request, 'hematology/record_edit.html', {'form': form})

@login_required
def record_edit(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.doctor = request.user
            record.published_date = timezone.now()
            record.save()
            return redirect('record_detail', pk=record.pk)
    else:
        form = RecordForm(instance=record)
    return render(request, 'hematology/record_edit.html', {'form': form})


# Create your views here.
