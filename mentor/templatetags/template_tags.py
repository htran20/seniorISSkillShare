from django import template
from mentor.models import MentorProfile

register = template.Library()
#
#
# @register.filter
# def cart_item_count(user):
#     if user.is_authenticated:
#         qs = Order.objects.filter(user=user, ordered=False)
#         if qs.exists():
#             return qs[0].items.count()
#     return 0

@register.filter
def recommend_list(user):
    if user.is_authenticated:
        # qs = Order.objects.filter(user=user, ordered=False)
        qs = MentorProfile.objects.all()
        if qs.exists():
            # return qs[0].items.count()
            return qs
    return 0
