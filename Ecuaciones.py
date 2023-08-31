# FUNCIÓN AREA BARRAS DE REFUERZO
# Nb: Número de la barra
# Asb: Área de la barra _ cm²

def f_Asb(Nb):
    Nb = Nb
#    print ('Nb =',Nb)
    match Nb:
        case 2:
            Asb = 0.32
        case 3:
            Asb = 0.71
        case 4:
            Asb = 1.29
        case 5:
            Asb = 1.99
        case 6:
            Asb = 2.84
        case 7:
           Asb = 3.87
        case 8:
            Asb = 5.10
        case _ :
            print ('Nb no valido')
    return (Asb)

# FUNCIÓN DIÁMETRO EN PULG'S BARRAS DE REFUERZO
# Nb: Número de la barra
# Db: Diametro de la barra en pulgadas

def f_dbp(Nb):
    Nb = Nb
#    print ('Nb =',Nb)
    match Nb:
        case 2:
            dbp = '1/4'
        case 3:
            dbp = '3/8'
        case 4:
            dbp = '1/2'
        case 5:
            dbp = '5/8'
        case 6:
            dbp = '3/4'
        case 7:
           dbp = '7/8'
        case 8:
            dbp = '1'
        case _ :
            print ('Nb no valido')
    return (dbp)

# FUNCIÓN PARA EL CALCULO DE CUANTÍAS PARA UN MOMENTO DADO
# fc: resistencia del concreto _ N/mm^2
# Fy: Fluencia del acero _ N/mm^2
# Mu: Momento de diseño _ kN.cm
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_pcal(fc, fy, Mu, b, d):
    k = (Mu/(b*d**2))
    m = (fy/(0.85*fc))
    pcal = 1/m*(1-(1-(2*m*k)/(0.90*fy/10))**0.5)
    return (pcal)

# FUNCIÓN PARA EL CALCULO DE ACERO CALCULADO
# pcal: Cuantía calculado de refuerzo
# b: Base del elemento _ cm
# d: Altura efectiva del elemento _ cm

def f_Ascal(pcal, b, d):
    Ascal = pcal*b*d
    return (Ascal)

# FUNCIÓN PARA EL CALCULO DE ACERO MÍNIMO
# pmin: Cuantía de refuerzo mínimo
# b: Base del elemento _ cm
# h: Altura del elemento _ cm

def f_Asmin(pmin, b, h):
    Asmin = pmin*b*h
    return (Asmin)

# FUNCIÓN PARA EL CALCULO DE ACERO REQUERIDO
# Ascal: Acero calculado _ cm²
# Asmin: Acero mínimo _ cm²

def f_Asreq(Ascal, Asmin):
    Asreq = max(Ascal, Asmin)
    return (Asreq)

# FUNCIÓN PARA LA SEPARACIÓN DEL REFUERZO
# Ascal: Acero requerido _ cm²
# Asb: Area de la barra a usar _ cm²
# b: ancho de la sección

def f_sep(Asreq, Asb, b):
    import math
    Cant = math.ceil(Asreq/Asb)
    s = b/(Asreq/Asb)
    if (s > 30):
        s = 30
    else:
        s = s
    return (s)

# FUNCIÓN PARA LA DISTRIBUCIÓN DEL REFUERZO
# Ascal: Acero requerido _ cm²
# Asb: Area de la barra a usar _ cm²
# b: Ancho de la sección
# Nb: Número de la barra a usar

def f_dist(Asreq, Asb, b, dbp ):
    import math
    Cant = math.ceil(Asreq/Asb)
    s = b/(Asreq/Asb)
    if (s > 30):
        s = 30
    else:
        s = s
    dist = str(Cant) + ' _ ø ' +  str(dbp) + "\" C/ " + "{:.1f}".format(s) + ' cm' 
    return (dist)

# FUNCIÓN PARA EL CALCULO DE ACERO COLOCADO
# Ascal: Acero requerido _ cm²
# Asb: Area de la barra a usar _ cm²

def f_Ascol(Asreq, Asb):
    import math
    Cant = math.ceil(Asreq/Asb)
    Ascol = Asb*Cant
    return (Ascol)

# FUNCIÓN PARA EL CÁLCULO DE MOMENTO NOMINAL
# fc: resistencia del concreto _ N/mm^2
# Fy: Fluencia del acero _ N/mm^2
# Asc: Acero colocado _ cm²
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_Mn (fc, fy, Asc, b, d):
    Mn = 0.9*Asc*fy/10*(d-(Asc*fy/10)/(1.7*fc/10*b))
    return (Mn)

def f_ChMn (Mu, Mn):
    if (Mu < Mn):
        r = 'Ok'
    else:
        r = 'No cumple'
    return (r)    

# FUNCIÓN PARA EL CÁLCULO DEL CORTANTE EN EL CONCRETO
# fiv: Factor de reducción de cortante
# fc: Resistencia del concreto _ N/mm^2
# b: Base del elemento _ cm
# d: Altura efetiva _ cm

def f_Vc (fiv, fc, b, d):
  b=b*10
  d=d*10
  Vc = (0.17*fiv*(fc)**0.5*b*d)/1000
  return (Vc)

def f_ChVc (Vu, Vc):
    if (Vu < Vc):
        r = 'Ok'
    else:
        r = 'No cumple'
    return (r) 
