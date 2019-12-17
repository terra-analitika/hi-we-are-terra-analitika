import math 

def ai(vp, rho):
    """Construct log AI (Acoustic Impedance) from log Vp and Rho"""
    return [vp[i]*rho[i] for i in range(len(vp))]

def si(vs, rho):
    """Construct log SI(Shear Impedance) from log Vs and Rho"""
    return [vs[i]*rho[i] for i in range(len(vs))] 

def mu(vs, rho):
    """Construct log mu from log Vs and Rho"""
    return [(vs[i]**2)*rho(i) for i in range(len(vs))]

def eei(vp, vs, rho):
    """Construct log EEI(Extended Elastic Impedance) from log Vs and Vp"""
    log_ai = ai(vp, rho)
    log_si = si(vs, rho)
    chi = list(range(-90, 91))
    log_eei = [[0 for j in range(len(chi))] for i in range(len(vp))]

    for i in range(len(vp)):
        for j in range(len(chi)):
            log_eei[i][j] = (log_ai[i]**(math.cos(math.radians(chi[j])))) * (log_si[i]**math.sin(chi[j]))
    
    return log_eei








