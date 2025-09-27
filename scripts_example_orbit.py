from astropy import units as u
from astropy.time import Time
from astropy.coordinates import CartesianRepresentation, CartesianDifferential
from poliastro.bodies import Sun
from poliastro.twobody import Orbit

# Epoka (tu: t2)
epoch = Time("2024-01-17 00:00:00", scale="tdb")

# Wektor stanu z przykładu (jednostki AU i AU/d)
r2 = [-0.2687, 2.2781, 0.7945]  # AU
v2 = [-0.0100, -0.0049, 0.0020]  # AU/day

rep = CartesianRepresentation(r2[0] * u.AU, r2[1] * u.AU, r2[2] * u.AU)
diff = CartesianDifferential(v2[0] * (u.AU / u.day),
                             v2[1] * (u.AU / u.day),
                             v2[2] * (u.AU / u.day))

orb = Orbit.from_vectors(Sun, rep, diff, epoch=epoch)

# Wypisz elementy klasyczne
p = orb.p.to(u.AU)
a = orb.a.to(u.AU)
ecc = orb.ecc
inc = orb.inc.to(u.deg)
raan = orb.raan.to(u.deg)
argp = orb.argp.to(u.deg)
M = orb.M.to(u.deg)

print(f"p  = {p:.6f}")
print(f"a  = {a:.6f}")
print(f"e  = {ecc:.6f}")
print(f"i  = {inc:.6f}")
print(f"Ω  = {raan:.6f}")
print(f"ω  = {argp:.6f}")
print(f"M  = {M:.6f} at epoch {epoch.isot}")