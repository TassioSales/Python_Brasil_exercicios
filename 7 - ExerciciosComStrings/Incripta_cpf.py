# criar uma função que receba um cpf e retorne o mesmo com os números incriptados

def incripta_cpf(cpf):
    cpf_incriptado = ""
    for i in cpf:
        if i == "0":
            cpf_incriptado += "a"
        elif i == "1":
            cpf_incriptado += "b"
        elif i == "2":
            cpf_incriptado += "c"
        elif i == "3":
            cpf_incriptado += "d"
        elif i == "4":
            cpf_incriptado += "e"
        elif i == "5":
            cpf_incriptado += "f"
        elif i == "6":
            cpf_incriptado += "g"
        elif i == "7":
            cpf_incriptado += "h"
        elif i == "8":
            cpf_incriptado += "i"
        elif i == "9":
            cpf_incriptado += "j"
        else:
            cpf_incriptado += i
    return cpf_incriptado