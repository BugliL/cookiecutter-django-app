from __future__ import annotations

from django.apps import AppConfig


class {{ cookiecutter.app_name | replace('_', ' ') | title | replace(' ', '') }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.app_name }}"
