import math

def countInvocations(v, m):
    # Compute log(v!)
    log_varian = 0.0
    for i in range(1, v + 1):
        log_varian += math.log(i)

    log_m = math.log(m)

    k = 0
    log_mateo = 0.0

    while log_mateo <= log_varian:
        k += 1
        log_mateo += log_m

    return k