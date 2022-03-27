
import numpy as np
import matplotlib.pyplot as plt

"""
THIS IS FOR THE ORIGINAL STATE
"""

# Constants
in_to_m = 0.0254
nose_to_s1 = 6.755200984  # [m]
small_pitch_in = 31  # [in]
small_pitch = small_pitch_in * in_to_m
medium_pitch = 1.002145455  # [m]
big_pitch = 1.145309091  # [m]
aft_cargo_cg = 29.51789474  # [m]
fwd_cargo_cg = 12.05168483  # [m]
first_seat_cg = 6.755200984  # [m]
last_seat_cg = first_seat_cg + small_pitch * 22 + medium_pitch + big_pitch
middle_fuel_cg = 18.94325581  # [m]
wings_fuel_cg = 20.32453488  # [m]
lemac = 19.20840  # [m]
mac = 3.48  # [m]
oew_cg = 20.12092  # [m]
g0 = 9.80665  # [m/s^2]
pax_mass = 90  # [kg]
oew_mass = 23187  # [kg]
aft_cargo_mass = 2172.855109  # [kg]
fwd_cargo_mass = 793.1448907  # [kg]
total_fuel_mass = 6487  # [kg]
middle_fuel_mass = total_fuel_mass * 0.2
wings_fuel_mass = total_fuel_mass * 0.8

# Initialise lists
cargo_cg1 = np.array([oew_cg])
cargo_moment1 = np.array([oew_cg * oew_mass])
cargo_mass1 = np.array([oew_mass])

cargo_cg2 = np.array([oew_cg])
cargo_moment2 = np.array([oew_cg * oew_mass])
cargo_mass2 = np.array([oew_mass])

# Add cargo influence
cargo_mass1 = np.append(cargo_mass1, cargo_mass1[-1] + fwd_cargo_mass)
cargo_moment1 = np.append(cargo_moment1, cargo_moment1[-1] + fwd_cargo_mass * fwd_cargo_cg)
cargo_cg1 = np.append(cargo_cg1, cargo_moment1[-1] / cargo_mass1[-1])

cargo_mass1 = np.append(cargo_mass1, cargo_mass1[-1] + aft_cargo_mass)
cargo_moment1 = np.append(cargo_moment1, cargo_moment1[-1] + aft_cargo_mass * aft_cargo_cg)
cargo_cg1 = np.append(cargo_cg1, cargo_moment1[-1] / cargo_mass1[-1])

cargo_mass2 = np.append(cargo_mass2, cargo_mass2[-1] + aft_cargo_mass)
cargo_moment2 = np.append(cargo_moment2, cargo_moment2[-1] + aft_cargo_mass * aft_cargo_cg)
cargo_cg2 = np.append(cargo_cg2, cargo_moment2[-1] / cargo_mass2[-1])

cargo_mass2 = np.append(cargo_mass2, cargo_mass2[-1] + fwd_cargo_mass)
cargo_moment2 = np.append(cargo_moment2, cargo_moment2[-1] + fwd_cargo_mass * fwd_cargo_cg)
cargo_cg2 = np.append(cargo_cg2, cargo_moment1[-1] / cargo_mass1[-1])

cargo_cg_mac1 = (cargo_cg1 - lemac) / mac * 100
cargo_cg_mac2 = (cargo_cg2 - lemac) / mac * 100

# Add window seat influence
# Initialisation
window_cg1 = np.array([cargo_cg1[-1]])
window_moment1 = np.array([cargo_moment1[-1]])
window_mass1 = np.array([cargo_mass1[-1]])

window_cg2 = np.array([cargo_cg2[-1]])
window_moment2 = np.array([cargo_moment2[-1]])
window_mass2 = np.array([cargo_mass2[-1]])

# Actually adding it
for i in range(15):
    seat_cg = first_seat_cg + i * small_pitch
    window_mass1 = np.append(window_mass1, window_mass1[-1] + pax_mass*2)
    window_moment1 = np.append(window_moment1, window_moment1[-1] + pax_mass*2 * seat_cg)
    window_cg1 = np.append(window_cg1, window_moment1[-1] / window_mass1[-1])

seat_cg = first_seat_cg + 14 * small_pitch + big_pitch
window_mass1 = np.append(window_mass1, window_mass1[-1] + pax_mass*2)
window_moment1 = np.append(window_moment1, window_moment1[-1] + pax_mass*2 * seat_cg)
window_cg1 = np.append(window_cg1, window_moment1[-1] / window_mass1[-1])

for i in range(9):
    seat_cg = first_seat_cg + 14 * small_pitch + big_pitch + medium_pitch + i * small_pitch
    window_mass1 = np.append(window_mass1, window_mass1[-1] + pax_mass*2)
    window_moment1 = np.append(window_moment1, window_moment1[-1] + pax_mass*2 * seat_cg)
    window_cg1 = np.append(window_cg1, window_moment1[-1] / window_mass1[-1])


for i in range(9):
    seat_cg = last_seat_cg - i * small_pitch
    window_mass2 = np.append(window_mass2, window_mass2[-1] + pax_mass*2)
    window_moment2 = np.append(window_moment2, window_moment2[-1] + pax_mass*2 * seat_cg)
    window_cg2 = np.append(window_cg2, window_moment2[-1] / window_mass2[-1])

seat_cg = last_seat_cg - 8 * small_pitch - medium_pitch
window_mass2 = np.append(window_mass2, window_mass2[-1] + pax_mass*2)
window_moment2 = np.append(window_moment2, window_moment2[-1] + pax_mass*2 * seat_cg)
window_cg2 = np.append(window_cg2, window_moment2[-1] / window_mass2[-1])

for i in range(15):
    seat_cg = last_seat_cg - 8 * small_pitch - big_pitch - medium_pitch - i * small_pitch
    window_mass2 = np.append(window_mass2, window_mass2[-1] + pax_mass*2)
    window_moment2 = np.append(window_moment2, window_moment2[-1] + pax_mass*2 * seat_cg)
    window_cg2 = np.append(window_cg2, window_moment2[-1] / window_mass2[-1])

window_cg_mac1 = (window_cg1 - lemac) / mac * 100
window_cg_mac2 = (window_cg2 - lemac) / mac * 100


# Add aisle seat influence
# Initialisation
aisle_cg1 = np.array([window_cg1[-1]])
aisle_moment1 = np.array([window_moment1[-1]])
aisle_mass1 = np.array([window_mass1[-1]])

aisle_cg2 = np.array([window_cg2[-1]])
aisle_moment2 = np.array([window_moment2[-1]])
aisle_mass2 = np.array([window_mass2[-1]])

# Actually adding it
for i in range(15):
    seat_cg = first_seat_cg + i * small_pitch
    aisle_mass1 = np.append(aisle_mass1, aisle_mass1[-1] + pax_mass*2)
    aisle_moment1 = np.append(aisle_moment1, aisle_moment1[-1] + pax_mass*2 * seat_cg)
    aisle_cg1 = np.append(aisle_cg1, aisle_moment1[-1] / aisle_mass1[-1])

seat_cg = first_seat_cg + 14 * small_pitch + big_pitch
aisle_mass1 = np.append(aisle_mass1, aisle_mass1[-1] + pax_mass*2)
aisle_moment1 = np.append(aisle_moment1, aisle_moment1[-1] + pax_mass*2 * seat_cg)
aisle_cg1 = np.append(aisle_cg1, aisle_moment1[-1] / aisle_mass1[-1])

for i in range(9):
    seat_cg = first_seat_cg + 14 * small_pitch + big_pitch + medium_pitch + i * small_pitch
    aisle_mass1 = np.append(aisle_mass1, aisle_mass1[-1] + pax_mass*2)
    aisle_moment1 = np.append(aisle_moment1, aisle_moment1[-1] + pax_mass*2 * seat_cg)
    aisle_cg1 = np.append(aisle_cg1, aisle_moment1[-1] / aisle_mass1[-1])


for i in range(9):
    seat_cg = last_seat_cg - i * small_pitch
    aisle_mass2 = np.append(aisle_mass2, aisle_mass2[-1] + pax_mass*2)
    aisle_moment2 = np.append(aisle_moment2, aisle_moment2[-1] + pax_mass*2 * seat_cg)
    aisle_cg2 = np.append(aisle_cg2, aisle_moment2[-1] / aisle_mass2[-1])

seat_cg = last_seat_cg - 8 * small_pitch - medium_pitch
aisle_mass2 = np.append(aisle_mass2, aisle_mass2[-1] + pax_mass*2)
aisle_moment2 = np.append(aisle_moment2, aisle_moment2[-1] + pax_mass*2 * seat_cg)
aisle_cg2 = np.append(aisle_cg2, aisle_moment2[-1] / aisle_mass2[-1])

for i in range(15):
    seat_cg = last_seat_cg - 8 * small_pitch - big_pitch - medium_pitch - i * small_pitch
    aisle_mass2 = np.append(aisle_mass2, aisle_mass2[-1] + pax_mass*2)
    aisle_moment2 = np.append(aisle_moment2, aisle_moment2[-1] + pax_mass*2 * seat_cg)
    aisle_cg2 = np.append(aisle_cg2, aisle_moment2[-1] / aisle_mass2[-1])

aisle_cg_mac1 = (aisle_cg1 - lemac) / mac * 100
aisle_cg_mac2 = (aisle_cg2 - lemac) / mac * 100


# Add fuel influence
# Initialisation
fuel_cg = np.array([aisle_cg1[-1]])
fuel_moment = np.array([aisle_moment1[-1]])
fuel_mass = np.array([aisle_mass1[-1]])

# Actually adding it
fuel_mass = np.append(fuel_mass, fuel_mass[-1] + wings_fuel_mass)
fuel_moment = np.append(fuel_moment, fuel_moment[-1] + wings_fuel_mass * wings_fuel_cg)
fuel_cg = np.append(fuel_cg, fuel_moment[-1] / fuel_mass[-1])

fuel_mass = np.append(fuel_mass, fuel_mass[-1] + middle_fuel_mass)
fuel_moment = np.append(fuel_moment, fuel_moment[-1] + middle_fuel_mass * middle_fuel_cg)
fuel_cg = np.append(fuel_cg, fuel_moment[-1] / fuel_mass[-1])

fuel_cg_mac = (fuel_cg - lemac) / mac * 100

most_aft_cg = max(np.max(cargo_cg_mac1), np.max(cargo_cg_mac2), np.max(window_cg_mac1), np.max(window_cg_mac2), np.max(aisle_cg_mac1), np.max(aisle_cg_mac2), np.max(fuel_cg_mac))
most_fwd_cg = min(np.min(cargo_cg_mac1), np.min(cargo_cg_mac2), np.min(window_cg_mac1), np.min(window_cg_mac2), np.min(aisle_cg_mac1), np.min(aisle_cg_mac2), np.min(fuel_cg_mac))
most_aft_cg_2pc = most_aft_cg + 2.0
most_fwd_cg_2pc = most_fwd_cg - 2.0

# Plot the loading diagram
fig1 = plt.figure()
fig1.suptitle('Loading Diagram CRJ 1000 standard configuration')
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(cargo_cg_mac1, cargo_mass1, 'x-', label="Cargo 1")
ax1.plot(cargo_cg_mac2, cargo_mass2, 'x-', label="Cargo 2")
ax1.plot(window_cg_mac1, window_mass1, '.-', label="Window seats 1")
ax1.plot(window_cg_mac2, window_mass2, '.-', label="Window seats 2")
ax1.plot(aisle_cg_mac1, aisle_mass1, '.-', label="Aisle seats 1")
ax1.plot(aisle_cg_mac2, aisle_mass2, '.-', label="Aisle seats 2")
ax1.plot([fuel_cg_mac[0], fuel_cg_mac[-1]], [fuel_mass[0], fuel_mass[-1]], 'x-', label="Fuel")
ax1.axvline(most_aft_cg, color='grey', label=r"Extreme $x_{cg}$ values")
ax1.axvline(most_fwd_cg, color='grey')
ax1.axvline(most_aft_cg_2pc, color='black', label="2% margin")
ax1.axvline(most_fwd_cg_2pc, color='black')
ax1.set_xlabel(r'$x_{cg}$ [%MAC]')
ax1.set_ylabel(r'Mass [kg]')
ax1.legend()
ax1.grid()
ax1.set_xlim(-5.0, 55.0)
ax1.set_ylim(22500.0, 42500.0)



"""
THIS IS FOR THE MODIFIED STATE
"""

# Constants
in_to_m = 0.0254
nose_to_s1 = 6.755200984  # [m]
small_pitch_in = 31  # [in]
small_pitch = small_pitch_in * in_to_m
medium_pitch = 1.002145455  # [m]
big_pitch = 1.145309091  # [m]
aft_cargo_cg = 29.51789474  # [m]
fwd_cargo_cg = 12.05168483  # [m]
first_seat_cg = 6.755200984  # [m]
last_seat_cg = first_seat_cg + small_pitch * 20 + medium_pitch + big_pitch
middle_fuel_cg = 18.94325581  # [m]
wings_fuel_cg = 20.32453488  # [m]
lemac = 19.20840  # [m]
mac = 3.48  # [m]
oew_cg = 19.7526423  # [m]
g0 = 9.80665  # [m/s^2]
pax_mass = 90  # [kg]
oew_mass = 25027.65  # [kg]
aft_cargo_mass = 2236.7221  # [kg]
fwd_cargo_mass = 729.2779  # [kg]
total_fuel_mass = 5366.35  # [kg]
middle_fuel_mass = total_fuel_mass * 0.2
wings_fuel_mass = total_fuel_mass * 0.8

# Initialise lists
cargo_cg1 = np.array([oew_cg])
cargo_moment1 = np.array([oew_cg * oew_mass])
cargo_mass1 = np.array([oew_mass])

cargo_cg2 = np.array([oew_cg])
cargo_moment2 = np.array([oew_cg * oew_mass])
cargo_mass2 = np.array([oew_mass])

# Add cargo influence
cargo_mass1 = np.append(cargo_mass1, cargo_mass1[-1] + fwd_cargo_mass)
cargo_moment1 = np.append(cargo_moment1, cargo_moment1[-1] + fwd_cargo_mass * fwd_cargo_cg)
cargo_cg1 = np.append(cargo_cg1, cargo_moment1[-1] / cargo_mass1[-1])

cargo_mass1 = np.append(cargo_mass1, cargo_mass1[-1] + aft_cargo_mass)
cargo_moment1 = np.append(cargo_moment1, cargo_moment1[-1] + aft_cargo_mass * aft_cargo_cg)
cargo_cg1 = np.append(cargo_cg1, cargo_moment1[-1] / cargo_mass1[-1])

cargo_mass2 = np.append(cargo_mass2, cargo_mass2[-1] + aft_cargo_mass)
cargo_moment2 = np.append(cargo_moment2, cargo_moment2[-1] + aft_cargo_mass * aft_cargo_cg)
cargo_cg2 = np.append(cargo_cg2, cargo_moment2[-1] / cargo_mass2[-1])

cargo_mass2 = np.append(cargo_mass2, cargo_mass2[-1] + fwd_cargo_mass)
cargo_moment2 = np.append(cargo_moment2, cargo_moment2[-1] + fwd_cargo_mass * fwd_cargo_cg)
cargo_cg2 = np.append(cargo_cg2, cargo_moment1[-1] / cargo_mass1[-1])

cargo_cg_mac1 = (cargo_cg1 - lemac) / mac * 100
cargo_cg_mac2 = (cargo_cg2 - lemac) / mac * 100

# Add window seat influence
# Initialisation
window_cg1 = np.array([cargo_cg1[-1]])
window_moment1 = np.array([cargo_moment1[-1]])
window_mass1 = np.array([cargo_mass1[-1]])

window_cg2 = np.array([cargo_cg2[-1]])
window_moment2 = np.array([cargo_moment2[-1]])
window_mass2 = np.array([cargo_mass2[-1]])

# Actually adding it
for i in range(15):
    seat_cg = first_seat_cg + i * small_pitch
    window_mass1 = np.append(window_mass1, window_mass1[-1] + pax_mass*2)
    window_moment1 = np.append(window_moment1, window_moment1[-1] + pax_mass*2 * seat_cg)
    window_cg1 = np.append(window_cg1, window_moment1[-1] / window_mass1[-1])

seat_cg = first_seat_cg + 14 * small_pitch + big_pitch
window_mass1 = np.append(window_mass1, window_mass1[-1] + pax_mass*2)
window_moment1 = np.append(window_moment1, window_moment1[-1] + pax_mass*2 * seat_cg)
window_cg1 = np.append(window_cg1, window_moment1[-1] / window_mass1[-1])

for i in range(7):
    seat_cg = first_seat_cg + 14 * small_pitch + big_pitch + medium_pitch + i * small_pitch
    window_mass1 = np.append(window_mass1, window_mass1[-1] + pax_mass*2)
    window_moment1 = np.append(window_moment1, window_moment1[-1] + pax_mass*2 * seat_cg)
    window_cg1 = np.append(window_cg1, window_moment1[-1] / window_mass1[-1])


for i in range(7):
    seat_cg = last_seat_cg - i * small_pitch
    window_mass2 = np.append(window_mass2, window_mass2[-1] + pax_mass*2)
    window_moment2 = np.append(window_moment2, window_moment2[-1] + pax_mass*2 * seat_cg)
    window_cg2 = np.append(window_cg2, window_moment2[-1] / window_mass2[-1])

seat_cg = last_seat_cg - 6 * small_pitch - medium_pitch
window_mass2 = np.append(window_mass2, window_mass2[-1] + pax_mass*2)
window_moment2 = np.append(window_moment2, window_moment2[-1] + pax_mass*2 * seat_cg)
window_cg2 = np.append(window_cg2, window_moment2[-1] / window_mass2[-1])

for i in range(15):
    seat_cg = last_seat_cg - 6 * small_pitch - big_pitch - medium_pitch - i * small_pitch
    window_mass2 = np.append(window_mass2, window_mass2[-1] + pax_mass*2)
    window_moment2 = np.append(window_moment2, window_moment2[-1] + pax_mass*2 * seat_cg)
    window_cg2 = np.append(window_cg2, window_moment2[-1] / window_mass2[-1])

window_cg_mac1 = (window_cg1 - lemac) / mac * 100
window_cg_mac2 = (window_cg2 - lemac) / mac * 100


# Add aisle seat influence
# Initialisation
aisle_cg1 = np.array([window_cg1[-1]])
aisle_moment1 = np.array([window_moment1[-1]])
aisle_mass1 = np.array([window_mass1[-1]])

aisle_cg2 = np.array([window_cg2[-1]])
aisle_moment2 = np.array([window_moment2[-1]])
aisle_mass2 = np.array([window_mass2[-1]])

# Actually adding it
for i in range(15):
    seat_cg = first_seat_cg + i * small_pitch
    aisle_mass1 = np.append(aisle_mass1, aisle_mass1[-1] + pax_mass*2)
    aisle_moment1 = np.append(aisle_moment1, aisle_moment1[-1] + pax_mass*2 * seat_cg)
    aisle_cg1 = np.append(aisle_cg1, aisle_moment1[-1] / aisle_mass1[-1])

seat_cg = first_seat_cg + 14 * small_pitch + big_pitch
aisle_mass1 = np.append(aisle_mass1, aisle_mass1[-1] + pax_mass*2)
aisle_moment1 = np.append(aisle_moment1, aisle_moment1[-1] + pax_mass*2 * seat_cg)
aisle_cg1 = np.append(aisle_cg1, aisle_moment1[-1] / aisle_mass1[-1])

for i in range(7):
    seat_cg = first_seat_cg + 14 * small_pitch + big_pitch + medium_pitch + i * small_pitch
    aisle_mass1 = np.append(aisle_mass1, aisle_mass1[-1] + pax_mass*2)
    aisle_moment1 = np.append(aisle_moment1, aisle_moment1[-1] + pax_mass*2 * seat_cg)
    aisle_cg1 = np.append(aisle_cg1, aisle_moment1[-1] / aisle_mass1[-1])


for i in range(7):
    seat_cg = last_seat_cg - i * small_pitch
    aisle_mass2 = np.append(aisle_mass2, aisle_mass2[-1] + pax_mass*2)
    aisle_moment2 = np.append(aisle_moment2, aisle_moment2[-1] + pax_mass*2 * seat_cg)
    aisle_cg2 = np.append(aisle_cg2, aisle_moment2[-1] / aisle_mass2[-1])

seat_cg = last_seat_cg - 6 * small_pitch - medium_pitch
aisle_mass2 = np.append(aisle_mass2, aisle_mass2[-1] + pax_mass*2)
aisle_moment2 = np.append(aisle_moment2, aisle_moment2[-1] + pax_mass*2 * seat_cg)
aisle_cg2 = np.append(aisle_cg2, aisle_moment2[-1] / aisle_mass2[-1])

for i in range(15):
    seat_cg = last_seat_cg - 6 * small_pitch - big_pitch - medium_pitch - i * small_pitch
    aisle_mass2 = np.append(aisle_mass2, aisle_mass2[-1] + pax_mass*2)
    aisle_moment2 = np.append(aisle_moment2, aisle_moment2[-1] + pax_mass*2 * seat_cg)
    aisle_cg2 = np.append(aisle_cg2, aisle_moment2[-1] / aisle_mass2[-1])

aisle_cg_mac1 = (aisle_cg1 - lemac) / mac * 100
aisle_cg_mac2 = (aisle_cg2 - lemac) / mac * 100


# Add fuel influence
# Initialisation
fuel_cg = np.array([aisle_cg1[-1]])
fuel_moment = np.array([aisle_moment1[-1]])
fuel_mass = np.array([aisle_mass1[-1]])

# Actually adding it
fuel_mass = np.append(fuel_mass, fuel_mass[-1] + wings_fuel_mass)
fuel_moment = np.append(fuel_moment, fuel_moment[-1] + wings_fuel_mass * wings_fuel_cg)
fuel_cg = np.append(fuel_cg, fuel_moment[-1] / fuel_mass[-1])

fuel_mass = np.append(fuel_mass, fuel_mass[-1] + middle_fuel_mass)
fuel_moment = np.append(fuel_moment, fuel_moment[-1] + middle_fuel_mass * middle_fuel_cg)
fuel_cg = np.append(fuel_cg, fuel_moment[-1] / fuel_mass[-1])

fuel_cg_mac = (fuel_cg - lemac) / mac * 100

most_aft_cg = max(np.max(cargo_cg_mac1), np.max(cargo_cg_mac2), np.max(window_cg_mac1), np.max(window_cg_mac2), np.max(aisle_cg_mac1), np.max(aisle_cg_mac2), np.max(fuel_cg_mac))
most_fwd_cg = min(np.min(cargo_cg_mac1), np.min(cargo_cg_mac2), np.min(window_cg_mac1), np.min(window_cg_mac2), np.min(aisle_cg_mac1), np.min(aisle_cg_mac2), np.min(fuel_cg_mac))
most_aft_cg_2pc = most_aft_cg + 2.0
most_fwd_cg_2pc = most_fwd_cg - 2.0

# Plot the loading diagram
fig1 = plt.figure()
fig1.suptitle('Loading Diagram CRJ 1000 new configuration')
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(cargo_cg_mac1, cargo_mass1, 'x-', label="Cargo 1 new")
ax1.plot(cargo_cg_mac2, cargo_mass2, 'x-', label="Cargo 2 new")
ax1.plot(window_cg_mac1, window_mass1, '.-', label="Window seats 1 new")
ax1.plot(window_cg_mac2, window_mass2, '.-', label="Window seats 2 new")
ax1.plot(aisle_cg_mac1, aisle_mass1, '.-', label="Aisle seats 1 new")
ax1.plot(aisle_cg_mac2, aisle_mass2, '.-', label="Aisle seats 2 new")
ax1.plot([fuel_cg_mac[0], fuel_cg_mac[-1]], [fuel_mass[0], fuel_mass[-1]], 'x-', label="Fuel new")
ax1.axvline(most_aft_cg, color='grey', label=r"Extreme $x_{cg}$ values new")
ax1.axvline(most_fwd_cg, color='grey')
ax1.axvline(most_aft_cg_2pc, color='black', label="2% margin new")
ax1.axvline(most_fwd_cg_2pc, color='black')
ax1.set_xlabel(r'$x_{cg}$ [%MAC]')
ax1.set_ylabel(r'Mass [kg]')
ax1.legend()
ax1.set_xlim(-5.0, 55.0)
ax1.set_ylim(22500.0, 42500.0)
ax1.grid()


plt.plot()
plt.show()

print(f"Aft cg 2%: {most_aft_cg_2pc} %, fwd cg 2%: {most_fwd_cg_2pc} %")
most_aft_cg_2pc_m = most_aft_cg_2pc / 100 * mac + lemac
most_fwd_cg_2pc_m = most_fwd_cg_2pc / 100 * mac + lemac
print(f"Aft cg 2%: {most_aft_cg_2pc_m} m, fwd cg 2%: {most_fwd_cg_2pc_m} m")
print(f"x_cg % MAC after cargo: {cargo_cg_mac1[-1]}")
print(f"Number of rows new: {window_cg_mac1.shape[0] - 1}")
print(f"New total mass: {fuel_mass[-1]} kg")
