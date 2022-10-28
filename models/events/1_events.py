    from django.db import models

    class DateMixin(models.Model):
        """eine abstrakte Klasse, die selbst keine DB-Tabelle erstellt"""
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            abstract = True

    class Category(DateMixin):
        """Eine Kategorie für einen Event."""
        name = models.CharField(max_length=100)
        sub_title = models.CharField(max_length=200, null=True, blank=True)
        description = models.TextField(null=True, blank=True)

        def __str__(self):
            return self.name
