from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class EjReportsConfig(AppConfig):
    name = 'ej_reports'
    verbose_name = _('Reports')
    rules = None
    roles = None
    fixes = None

    def ready(self):
        from . import rules, roles, fixes
        self.rules = rules
        self.roles = roles
        self.fixes = fixes
