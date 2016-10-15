from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Student
from .forms import StudentForm


# Create your views here.
def student_list(request):
    students = Student.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'student/student_list.html', {'students':students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(
        request,
        'student/student_detail.html',
        {'student':student}
    )


def student_new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.author = request.user
            student.published_date = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()

    return render(request, 'student/student_edit.html', {'form': form})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.author = request.user
            student.published_date = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_edit.html', {'form': form})
