from django.db import models

class ContatarSuporte(models.Model):
    nomeSuporte     = models.TextField(blank=False, verbose_name='Nome completo', max_length=99)
    emailSuporte    = models.EmailField(blank=False,verbose_name='Seu melhor e-mail')
    assuntoSuporte  = models.TextField(blank=False, verbose_name='Assunto', max_length=99)
    mensagemSuporte = models.TextField(blank=False,verbose_name='Descreva seu problema', max_length=600)

    def __str__(self):
        return f'Suporte: {self.nomeSuporte}'
