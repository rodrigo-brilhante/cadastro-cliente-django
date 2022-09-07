def cpf_valido(numero_do_cpf):
    return numero_do_cpf == 11

def nome_valido(nome):
    return nome.isalpha()

def rg_valido(self, rg):
    return len(rg) == 9
      
def celular_valido(self, celular):
    return len(celular) == 11