from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = "myblog.html.j2"

    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(BlogView, self).dispatch(*args, **kwargs)
