from django.shortcuts import render, get_object_or_404

from apps.user.models import User
from django.core.paginator import Paginator


def user_list_by_department(request, department_id):
    users = User.objects.filter(department_id=department_id)
    paginator = Paginator(users, 10)  # Show 10 users per page

    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, 'user_list_by_department.html', {'users': users})


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})