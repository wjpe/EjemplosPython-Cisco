ingreso=float(input("Ingrese el ingreso anual:"))
impuesto = 0

#
# Coloca tu código aquí.
#

excencion_fiscal_menor= 556.2
excencion_fiscal_mayor= 14839.2

if ingreso < 85528:
    impuesto = (ingreso * 0.182) - excencion_fiscal_menor

if ingreso > 85528:
    #print("impuesto antes de: ", impuesto)
    #impuesto=(ingreso*0.182)
    impuesto = 14839 + (ingreso - 85528) * 0.32
    #excedente = (salario - 85528) * 0.32
    
if impuesto < 0.0:
    print("El impuesto es : 0.0pesos")
else:
    impuesto=round(impuesto, 0)
    print("El impuesto es: ", impuesto, "pesos")
