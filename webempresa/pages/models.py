from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name='Título', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='Order', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última Modificación')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order']

    def __str__(self):
        return self.title
    
