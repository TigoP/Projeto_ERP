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
        return (round(1412.00 * 0.075 + (2666.68 - 1412.00)*0.09 + (4000.03 - 2666.68)*0.12 + (sal_base - 4000.03) , 2))    
            
def calcular_fgts(sal_base):
    return sal_base * 0.08

def calcular_irrf():
    pass #precisa fazer os calculos ainda

def calcular_transporte(sal_base):
    vlr_passagem = 4.70
    dias_trabalhados = 22
    total_cheio = vlr_passagem * dias_trabalhados

    if ((sal_base * 0.06) > total_cheio ):
        return total_cheio
    else:
        return sal_base * 0.06

def calcular_pensao(sal_base, ):

    '''
    Base de Cálculo (R$) 	 Alíquota (%)	 Parcela a Deduzir do IR (R$)
    Até 2.259,20*	0	0
    De 2.259,21 até 2.826,65*	7,5 	       169,44
    De 2.826,66 até 3.751,05	15	           381,44
    De 3.751,06 até 4.664,68	22,5	       662,77
    Acima de 4.664,68	        27,5	       896,00

    Fonte: Agência Senado

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
