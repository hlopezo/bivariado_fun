import pandas as pd
import numpy as np

def calcular_estadisticas(tabla, grupo, objetivo):
    grouped = tabla.groupby(grupo)
    total_count = grouped.size()
    good_count = grouped[objetivo].apply(lambda x: np.sum(x == 0))
    bad_count = grouped[objetivo].apply(lambda x: np.sum(x == 1))
    total_pct = total_count / np.sum(total_count)
    good_pct = good_count / np.sum(good_count)
    bad_pct = bad_count / np.sum(bad_count)
    bad_rate = bad_count / total_count
    good_pct_pct = good_pct / np.sum(good_pct)
    bad_pct_pct = bad_pct / np.sum(bad_pct)
    woe = np.where(bad_pct_pct == 0, 0, np.log(good_pct_pct / bad_pct_pct))#woe = np.log(good_pct_pct / bad_pct_pct)
    iv = (good_pct_pct - bad_pct_pct) * woe
    total_iv=np.sum(iv)
    result = pd.DataFrame({
        'Cantidad de deudores': total_count,
        'Distribucion de deudores': total_pct*100,
        'Numero de deudores Buenos': good_count,
        'Numero de deudores Malos': bad_count,
        'Tasa de malos': bad_rate*100,
        'Distribucion de buenos': good_pct*100,
        'Distribucion de malos': bad_pct*100,
        'WOE': woe,
        'IV': iv*100,
        'Sum_IV' :total_iv*100
    })
    return result
