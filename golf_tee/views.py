from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "oscar/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        products = ['empy', 'for', 'now']
        context.update({
            'products': products,
        })
        return context