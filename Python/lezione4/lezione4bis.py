def is_palindrome(x: int) -> bool:
    """
    Dato un intero x, restituisce True se x è
    palindromo, e False altrimenti

    Esempio 1:
    x = 121 -> True
    Speigaione: 121 si lege come 121 sia da destra che da sinistra

    Esempio 1:
    x = -121 -> False
    Speigaione: Da sinistra a destra, leggiamo -121.
                Da destra a sinistra abbiamo 121-.
                Perciò, questo numero non è palindromo
    
    Esempio 3:
    x = 10 -> False
    Spiegazione: 01 da destra a sinistra.
    Perciò, non è palindromo
    """
    s:str = str(x)
    s1:str = ""
    for i in range(len(s), 0, -1):
        s1 = s1 + s[i]
    return s == s1
print("")

""""
s:str = str(x)
i:int = 0
s_length = len(s)
while i < (s_length // 2): # for i in range(len(s))
    j = s_length - (i+1)
    if s[i] != s[j]:
        return False
    i += 1
return True
"""
