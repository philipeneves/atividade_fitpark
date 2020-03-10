unities = ["zero", "um", "dois", "três", "quatro",
            "cinco", "seis", "sete", "oito", "nove"]

teens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

tens = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"]

def tercia(num):
    number = str(num)
    number.zfill(3)
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    if a == 0:
        if b == 0:
            result = unities[c]
            return result
        elif b == 1:
            if c >= 0 and c <= 9:
                result = teens[c]
                return result
        elif b == 2:
            if c == 0:
                result = 'vinte'
                return result
            elif c > 0 and c <= 9:
                result = 'vinte e ' + unities[c]
                return result
        elif b >=3 and b <= 9:
            if c == 0:
                result = tens[b-1]
                return result
            if c >= 1 and c <= 9:
                result = tens[b-1] + ' e ' + unities[c]
                return result
    if a == 1:
        if b == 0:
            if c == 0:
                result = 'cem'
                return result
            elif c > 0 and c <= 9:
                result = 'cento e ' + unities[c]
                return result
        elif  b == 1:
            if c >= 0 and c <= 9:
                result = 'cento e ' + teens[c]
                return result
        elif b == 2:
            if c == 0:
                result = 'cento e vinte'
                return result
            elif c > 0 and c <= 9:
                result = 'cento e vinte e ' + unities[c]
                return result
        elif b >= 3 and b <= 9:
            if c == 0:
                result = 'cento e ' + tens[b-1]
                return result
            elif c > 0 and c <= 9:
                result = 'cento e ' + tens[b-1] + ' e ' + unities[c]
                return result

    elif a >= 2 and a <= 9:
        if a == 2 and b ==0 and c == 0:
            prefix= 'duzentos'
        elif a ==2:
            prefix= 'duzentos e '

        if a == 3 and b ==0 and c == 0:
            prefix= 'trezentos'
        elif a == 3:
            prefix= 'trezentos e '
        if a == 4 and b ==0 and c == 0:
            prefix= 'quatrocentos'
        elif a == 4:
            prefix= 'quatrocentos e '
        if a == 5 and b ==0 and c == 0:
            prefix= 'quinhentos'
        elif a == 5:
            prefix= 'quinhentos e '
        if a == 6 and b ==0 and c == 0:
            prefix= 'seiscentos'
        elif a == 6:
            prefix= 'seiscentos e '

        if a == 7 and b ==0 and c == 0:
            prefix= 'setecentos'
        
        elif a == 7:
            prefix= 'setecentos e '
        if a == 8 and b ==0 and c == 0:
            prefix= 'oitocentos'
        elif a == 8:
            prefix= 'oitocentos e '
        if a == 9 and b ==0 and c == 0:
            prefix= 'novecentos'
        elif a == 9:
            prefix= 'novecentos e '

        if b == 0:
            if c == 0:
                result = prefix
                return result
            elif c > 0 and c <= 9:
                result = prefix + unities[c]
                return result
        elif b == 1:
            if c >= 0 and c <= 9:
                result = prefix + teens[c]
                return result
        elif b == 2:
            if c == 0:
                result = prefix + 'vinte'
                return result
            elif c > 0 and c <= 9:
                result = prefix + 'vinte e ' + unities[c]
                return result
        elif b >= 3 and b <= 9:
            if c == 0:
                result = prefix + tens[b-1]
                return result
            elif c > 0 and c <= 9:
                result = prefix + tens[b-1] + ' e ' + unities[c]
                return result
def main():
    num = input("Por favor, digite o valor (Obs: para casas décimais usar a vírgula):")
    if num.count(",") <= 1:
        try:
            num = num.split(",")
            beforeComma = ''
            afterComma = ''
            number = str(num[0])
            if len(num) > 1:
                cent = str(num[1])
                cent = cent.zfill(9) + cent
            number = number.zfill(9) + number
            
            posicion = 1
            for i in [0,3,6]:
                var = number[i] + number[i+1] + number[i+2]
                if int(var) != 0:
                    res = tercia(var)
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
            if len(num) > 1:
                for c in [0,3,6]:
                    var2 = cent[c] + cent[c+1] + cent[c+2]
                    if int(var2) != 0:
                        res2 = tercia(var2)
                        afterComma =" e " + afterComma + res2 + " centavo(s)"
            ext = beforeComma + afterComma
            print(ext.capitalize())
        except:
            print("Operação não permitida. Verifique se o valor digitado é um número, em caso de casa décimal, é necessário usar vírgula.")
    else:
        print("Operação não permitida. Não é possível existir mais de uma vírgula no número.")

main()