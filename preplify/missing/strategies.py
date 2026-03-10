# preplify/missing/strategies.py

def fill_mean(series):
    return series.fillna(series.mean())

def fill_median(series):
    return series.fillna(series.median())

def fill_mode(series):
    mode = series.mode()
    return series.fillna(mode[0] if not mode.empty else series)

def fill_constant(series, value=0):
    return series.fillna(value)
