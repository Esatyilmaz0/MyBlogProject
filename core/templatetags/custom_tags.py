from django import template
from django.utils import timesince
import datetime

register = template.Library()

@register.simple_tag
def get_timesince():
    date = datetime.datetime.now()
    return timesince.timesince(date)

@register.simple_tag(takes_context=True)
def pagination_url(context, search_query, page):
    """
        Creates A Pagination URL.

        If the url has a query, it is added next to the page query and the url is returned
        If the url does not have a page query is added and the URL is returned.

        Examples:

        URL: .../?query1=example --> Returned: .../?query1=example&page=1
        URL: .../ --> Returned: .../?page=1

    """
    request = context["request"]
    if request.GET.get(search_query) != None:
        full_path = request.get_full_path().split("&")[0]
        query = full_path + "&page=" + str(page)
        return query

    return "?page=" + str(page)
