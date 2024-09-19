from dp_rh.models import Cargo, Funcionario

sal_base = Cargo.sal_base

#-----------------------vencimentos----------------------------------#
def calcular_comissao(sal_base):
    return sal_base * 0.15

def calcular_hora_extra50(sal_base, qtd_hora_extra50):
    return ((sal_base / 220) * 1.5) * qtd_hora_extra50

def calcular_hora_extra100(sal_base, qtd_hora_extra100):
    return ((sal_base / 220) * 2) * qtd_hora_extra100

def calcular_ad_noturno(sal_base, qtd_ad_noturno):
    vlr_hora = (sal_base / 220)
    vlr_ad_noturno = ((vlr_hora * 2) * qtd_ad_noturno)
    return vlr_ad_noturno + (vlr_ad_noturno * 0.2)

def calcular_sal_familia(sal_base):
    return sal_base * 0.2

def calcular_total_vencimentos(comissao, hora_extra50, hora_extra100, ad_noturno, sal_familia, adiantamentoV, gratificacao, emprestimoV) :
    return comissao + hora_extra50 + hora_extra100 + ad_noturno + sal_familia + adiantamentoV + gratificacao + emprestimoV

#-----------------------descontos----------------------------------#

def calcular_inss(sal_base):
    if sal_base <= 1412.00:
        return sal_base * 0.075
    elif sal_base > 1412.00 and sal_base <= 2666.68:
        return (round(1412.00 * 0.075 + (sal_base - 1412.00)*0.09, 2))
    elif sal_base > 2666.68 and sal_base <= 4000.03:
        return (round(1412.00 * 0.075 + (2666.68 - 1412.00)*0.09 + (sal_base - 2666.68)*0.12, 2))
    else:
        return (round(1412.00 * 0.075 + (2666.68 - 1412.00)*0.09 + (4000.03 - 2666.68)*0.12 + (sal_base - 4000.03)*0.14 , 2))    
            
def calcular_fgts(sal_base):
    return (round(sal_base * 0.08), 2)

def calcular_pensao():
    return Funcionario.dependentes * 189.59

def calcular_irrf():

    faixa1 = sal_base <= 2259.20
    faixa2 = sal_base > 2259.20 and sal_base <= 22826.65
    faixa3 = sal_base > 22826.65 and sal_base <= 3751.05
    faixa4 = sal_base > 3751.055 and sal_base <= 4664.68

    if faixa1:
        return 0
    elif faixa2:
        return (sal_base - 169.44 - calcular_inss() - calcular_pensao()) * 0.075
    elif faixa3:
        return (sal_base - 381.44 - calcular_inss() - calcular_pensao()) * 0.15 
    elif faixa4:
        return (sal_base - 662.77 - calcular_inss() - calcular_pensao()) * 0.225 
    else:
        return (sal_base - 896.00 - calcular_inss() - calcular_pensao()) * 0.275 

def calcular_transporte(sal_base):
    vlr_passagem = 4.70
    dias_trabalhados = 22
    total_cheio = vlr_passagem * dias_trabalhados

    if ((sal_base * 0.06) > total_cheio ):
        return total_cheio
    else:
        return sal_base * 0.06

    '''
        irrf = models.DecimalField (max_digits=10, decimal_places=2)
        alimentacao = models.DecimalField (max_digits=10, decimal_places=2)
        atrasos = models.DecimalField (max_digits=10, decimal_places=2)
        qtd_faltas = models.IntegerField(max_length=3)
        faltas = models.DecimalField (max_digits=10, decimal_places=2)
        adiantamentoD = models.DecimalField (max_digits=10, decimal_places=2)
        pensao = models.DecimalField (max_digits=10, decimal_places=2)
        plano_saude = models.DecimalField (max_digits=10, decimal_places=2)
        plano_odonto = models.DecimalField (max_digits=10, decimal_places=2)
        emprestimoD = models.DecimalField (max_digits=10, decimal_places=2)
        total_descontos = models.DecimalField(max_digits=20, decimal_places=2)
        total_vencimentos = models.DecimalField(max_digits=20, decimal_places=2)

    '''
