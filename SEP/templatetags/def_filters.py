from django import template

register = template.Library()

@register.filter
def in_department(users, department):
	return users.filter(groups__name=department)

@register.filter
def assigned_tasks(tasks, user):
	return tasks.filter(assigned=user)
