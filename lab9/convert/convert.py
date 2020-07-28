def float_default(string, float_value):
    try:
        float_value = float(string)
    except:
        return(float_value)
    return float_value



