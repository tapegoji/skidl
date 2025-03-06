import os

# Import the skidl library.
from skidl import *
from skidl import KICAD8
set_default_tool(KICAD8)

# Create input & output voltages and ground reference.
vin, vout, gnd = Net('VI'), Net('VO'), Net('GND')

# Create two resistors.
r1, r2 = 2 * Part("Device", 'R', TEMPLATE, footprint="Resistor_SMD:R_0603_1608Metric")
r1.value = '1K'   # Set upper resistor value.
r2.value = '500'  # Set lower resistor value.

# Connect the nets and resistors.
vin += r1[1]      # Connect the input to the upper resistor.
gnd += r2[2]      # Connect the lower resistor to ground.
vout += r1[2], r2[1] # Output comes from the connection of the two resistors.

# Output the netlist to a file.
generate_netlist()

# generate_schematic()
# generate_pcb()

####################################################################################################

from PySpice import Circuit, Simulator
from PySpice.Unit import *

### Create a circuit based on the skidl netlist
circuit = Circuit('Voltage Divider')
for prt in default_circuit.parts:
    if prt.ref.startswith('R'):
        circuit.R(prt.ref[1:], prt.p1.net.name, prt.p2.net.name, prt.value)

# add a voltage source
circuit.V('VI', vin.name, gnd.name, 5@u_V)
print(circuit)
simulator = Simulator.factory()
simulation = simulator.simulation(circuit, temperature=25, nominal_temperature=25)
analysis = simulation.operating_point()

for node in analysis.nodes.values():
    print('Node {}: {:5.2f} V'.format(str(node), float(node))) # Fixme: format value + unit