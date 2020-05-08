from django.views.generic import TemplateView

class PagedAccueil(TemplateView):
    template_name = 'page_d_accueil.html'

class TestPageView(TemplateView):
    template_name=  'TestPage.html'


class ThanksPageView(TemplateView):
    template_name = 'ThanksPage.html'
















