def validar_rango(valor: float, minimo: float, maximo: float) -> bool:
    """Valida si un valor numerico esta dentro de [minimo, maximo]."""
    resultado = False
    if minimo > maximo:
        resultado = validar_rango(valor, maximo, minimo)
    else:
        if minimo <= valor <= maximo:
            resultado = True
    return resultado


def es_par(numero: int) -> bool:
    """Determina recursivamente si un entero es par."""
    resultado = False
    if numero == 0:
        resultado = True
    elif numero > 0:
        resultado = not es_par(numero - 1)
    else:
        resultado = es_par(-numero)
    return resultado


def _tiene_divisor_desde(numero: int, divisor: int) -> bool:
    """Verifica recursivamente si existe algun divisor desde `divisor`."""
    tiene_divisor = False
    if divisor * divisor > numero:
        tiene_divisor = False
    elif numero % divisor == 0:
        tiene_divisor = True
    else:
        tiene_divisor = _tiene_divisor_desde(numero, divisor + 2)
    return tiene_divisor


def es_primo(numero: int) -> bool:
    """Determina recursivamente si un entero es primo."""
    resultado = False
    if numero < 2:
        resultado = False
    elif numero == 2:
        resultado = True
    elif numero % 2 == 0:
        resultado = False
    else:
        resultado = not _tiene_divisor_desde(numero, 3)
    return resultado


def es_multiplo(numero: int, base: int) -> bool:
    """Determina recursivamente si `numero` es multiplo de `base`."""
    resultado = False
    if base == 0:
        resultado = False
    elif numero == 0:
        resultado = True
    elif numero < 0:
        resultado = es_multiplo(-numero, abs_entero(base))
    elif base < 0:
        resultado = es_multiplo(numero, -base)
    elif numero < base:
        resultado = False
    else:
        resultado = es_multiplo(numero - base, base)
    return resultado


def abs_entero(valor: int) -> int:
    """Retorna el valor absoluto de un entero con single return."""
    absoluto = valor
    if valor < 0:
        absoluto = -valor
    return absoluto