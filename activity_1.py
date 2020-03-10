# Listas com valores para unidades e dezenas

unities = ["zero", "um", "dois", "três", "quatro",
            "cinco", "seis", "sete", "oito", "nove"]

teens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

tens = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"]

def transform(num):
    number = str(num)
    number.zfill(3)
    
    fstDig = int(number[0]) # Primeiro (First) digito da centena
    secDig = int(number[1]) # Segundo (Second) digito da centena
    thdDig = int(number[2]) # Terceiro (Third) digito da centena

    if fstDig == 0:
        if secDig == 0: 
            result = unities[thdDig]
            return result
        elif secDig == 1:
            if thdDig >= 0 and thdDig <= 9:
                result = teens[thdDig]
                return result
        elif secDig == 2:
            if thdDig == 0:
                result = 'vinte'
                return result
            elif thdDig > 0 and thdDig <= 9:
                result = 'vinte e ' + unities[thdDig]
                return result
        elif secDig >= 3 and secDig <= 9:
            if thdDig == 0:
                result = tens[secDig-1]
                return result
            if thdDig >= 1 and thdDig <= 9:
                result = tens[secDig-1] + ' e ' + unities[thdDig]
                return result
    if fstDig == 1:
        if secDig == 0:
            if thdDig == 0:
                result = 'cem'
                return result
            elif thdDig > 0 and thdDig <= 9:
                result = 'cento e ' + unities[thdDig]
                return result
        elif  secDig == 1:
            if thdDig >= 0 and thdDig <= 9:
                result = 'cento e ' + teens[thdDig]
                return result
        elif secDig == 2:
            if thdDig == 0:
                result = 'cento e vinte'
                return result
            elif thdDig > 0 and thdDig <= 9:
                result = 'cento e vinte e ' + unities[thdDig]
                return result
        elif secDig >= 3 and secDig <= 9:
            if thdDig == 0:
                result = 'cento e ' + tens[secDig-1]
                return result
            elif thdDig > 0 and thdDig <= 9:
                result = 'cento e ' + tens[secDig-1] + ' e ' + unities[thdDig]
                return result

    elif fstDig >= 2 and fstDig <= 9:
        if fstDig == 2 and secDig == 0 and thdDig == 0:
            prefix= 'duzentos'
        elif fstDig == 2:
            prefix= 'duzentos e '

        if fstDig == 3 and secDig == 0 and thdDig == 0:
            prefix= 'trezentos'
        elif fstDig == 3:
            prefix= 'trezentos e '
        if fstDig == 4 and secDig == 0 and thdDig == 0:
            prefix= 'quatrocentos'
        elif fstDig == 4:
            prefix= 'quatrocentos e '
        if fstDig == 5 and secDig == 0 and thdDig == 0:
            prefix= 'quinhentos'
        elif fstDig == 5:
            prefix= 'quinhentos e '
        if fstDig == 6 and secDig == 0 and thdDig == 0:
            prefix= 'seiscentos'
        elif fstDig == 6:
            prefix= 'seiscentos e '

        if fstDig == 7 and secDig == 0 and thdDig == 0:
            prefix= 'setecentos'
        
        elif fstDig == 7:
            prefix= 'setecentos e '
        if fstDig == 8 and secDig == 0 and thdDig == 0:
            prefix= 'oitocentos'
        elif fstDig == 8:
            prefix= 'oitocentos e '
        if fstDig == 9 and secDig == 0 and thdDig == 0:
            prefix= 'novecentos'
        elif fstDig == 9:
            prefix= 'novecentos e '

        if secDig == 0:
            if thdDig == 0:
                result = prefix
                return result
            elif thdDig > 0 and thdDig <= 9:
                result = prefix + unities[thdDig]
                return result
        elif secDig == 1:
            if thdDig >= 0 and thdDig <= 9:
                result = prefix + teens[thdDig]
                return result
        elif secDig == 2:
            if thdDig == 0:
                result = prefix + 'vinte'
                return result
            elif thdDig > 0 and thdDig <= 9:
                result = prefix + 'vinte e ' + unities[thdDig]
                return result
        elif secDig >= 3 and secDig <= 9:
            if thdDig == 0:
                result = prefix + tens[secDig-1]
                return result
            elif thdDig > 0 and thdDig <= 9:
                result = prefix + tens[secDig-1] + ' e ' + unities[thdDig]
                return result

num = input("Por favor, digite o valor (Obs: para casas décimais usar a vírgula):")
if num.count(",") <= 1:
    try:
        num = num.split(",") # Separa inteiro do décimal
        beforeComma = '' 
        afterComma = ''
        number = str(num[0])
        number = number.zfill(9) + number
        if len(num) > 1:
            cent = str(num[1])
            cent = cent.zfill(9) + cent
        
        for i in [0,3,6]:
            var = number[i] + number[i+1] + number[i+2]
            if int(var) != 0:
                res = transform(var)
                if i == 0:
                    beforeComma = res + " milhões "
                elif i == 3:
                    beforeComma = beforeComma + res + " mil "
                elif i == 6:
                    beforeComma = beforeComma + res
        if int(num[0]) > 1:
            beforeComma += " reais"
        else:
            beforeComma += " real"
        if len(num) > 1: # Verifica se existe décimal
            for c in [0,3,6]:
                var2 = cent[c] + cent[c+1] + cent[c+2]
                if int(var2) != 0:
                    res2 = transform(var2)
                    afterComma =" e " + afterComma + res2 + " centavo(s)"
        ext = beforeComma + afterComma
        print(ext.capitalize())
    except:
        print("Operação não permitida. Verifique se o valor digitado é um número, em caso de casa décimal, é necessário usar vírgula.")
else:
    print("Operação não permitida. Não é possível existir mais de uma vírgula no número.")
