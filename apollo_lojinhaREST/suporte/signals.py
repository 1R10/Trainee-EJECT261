from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import ContatarSuporte

def SuporteSignals(sender, instance, created, **kwargs):
    if created:
        corpo_email = f'''
        Nome: {instance.nomeSuporte}
        Email: {instance.emailSuporte}
        Mensagem:
        {instance.mensagemSuporte}
        '''
        # falta coisa. pesquisar mais
        

post_save.connect(SuporteSignals, sender=ContatarSuporte)