import pypsa
import matplotlib.pyplot as plt

network = pypsa.Network()

nbus=5 #number of buses

for i in range(nbus):
    network.add("Bus", "Bus number {}".format(i), v_nom=132)

for i in range(nbus-1):
    network.add("Line", "Line number {}".format(i), bus0="Bus number {}".format(i), bus1="Bus number {}".format(i+1),
                 r=0.02, x=0.3)

network.add("Generator", "Slack Generator", bus="Bus number 0", p_set=0, control="Slack")

network.add("Generator", "Gen number 1", bus="Bus number 3", p_set=60, control="PV")

network.add("Load", "Load number 1", bus="Bus number 4", p_set=91, q_set=41)

network.plot()

plt.show()

network.pf()

print(network.lines_t.p0) #active power flows on each line

print(network.lines_t.q0) #reactive power flows on each line