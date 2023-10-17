from django.core.paginator import Paginator
from django.shortcuts import render

from django.shortcuts import render
from .models import Department
from apps.user.models import User


def department_tree(request):
    departments = Department.objects.all()
    paginator = Paginator(departments, 10)

    page = request.GET.get('page')
    departments = paginator.get_page(page)

    return render(request, 'department_tree.html', {'departments': departments})
