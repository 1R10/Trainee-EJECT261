import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# isso aqui se joga no settings e vai pro serializer

class validatorSenha():
    def validate(self, senha, user=None):
        self.maiuscula(senha)
        self.minuscula(senha)
        self.numero(senha)
        self.simbolo(senha)

    def maiuscula(self, senha, user=None):
        if not re.search(r'[A-Z]', senha):
             raise ValidationError(_('A senha deve ter no mínimo uma letra maiúscula.'))
        
    def minuscula(self, senha, user=None):
        if not re.search(r'[a-z]', senha):
             raise ValidationError(_('A senha deve ter no mínimo uma letra minúscula.'))
    
    def numero(self, senha, user=None):
        if not re.search(r'[0-9]', senha):
            raise ValidationError(_('A senha deve ter no mínimo um número.'))

    def simbolo(self, senha, user=None):
        tem_simbolo = False

        for caractere in senha:
            codigo = ord(caractere)
            if (33 <= codigo <= 47) or (58 <= codigo <= 64) or (91 <= codigo <= 96) or (123 <= codigo <= 126):
                tem_simbolo = True
                break

        if not tem_simbolo:
            raise ValidationError(_('A senha deve conter pelo menos um caracter especial'))
        
        

    def get_help_text(self):
        return _('''
                 A senha deve conter no mínimo um de cada parâmetro:
                 - Uma letra maiúscula
                 - Uma letra minúscula
                 - Um caracter especial como .@-_#$ e etc
                 - Um número 0-9   ''')