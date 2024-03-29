# Load the package for drawing graphs.
import matplotlib.pyplot as plt

# Load the SKiDL + PySpice packages and initialize them for doing circuit simulations.
from skidl.pyspice import *

# Omit the following line if you're not using a Jupyter notebook.
#%matplotlib inline

print(lib_search_paths)

reset()  # You know what this does by now, right?

# Create a power supply for all the following circuitry.
pwr = V(dc_value=5 @ u_V)
pwr["n"] += gnd
vcc = pwr["p"]

# Create a logic inverter using a transistor and a few resistors.
@subcircuit
def inverter(inp, outp):
    """When inp is driven high, outp is pulled low by transistor. When inp is driven low, outp is pulled high by resistor."""
    q = BJT(model="2n2222a")  # NPN transistor.
    rc = R(value=1 @ u_kOhm)  # Resistor attached between transistor collector and VCC.
    rc[1, 2] += vcc, q["c"]
    rb = R(value=10 @ u_kOhm)  # Resistor attached between transistor base and input.
    rb[1, 2] += inp, q["b"]
    q["e"] += gnd  # Transistor emitter attached to ground.
    outp += q[
        "c"
    ]  # Inverted output comes from junction of the transistor collector and collector resistor.


# Create a pulsed voltage source to drive the input of the inverters. I set the rise and fall times to make
# it easier to distinguish the input and output waveforms in the plot.
vs = PULSEV(
    initial_value=0,
    pulsed_value=5 @ u_V,
    pulse_width=0.8 @ u_ms,
    period=2 @ u_ms,
    rise_time=0.2 @ u_ms,
    fall_time=0.2 @ u_ms,
)  # 1ms ON, 1ms OFF pulses.
vs["n"] += gnd

# Create three inverters and cascade the output of one to the input of the next.
outp = Net() * 3  # Create three nets to attach to the outputs of each inverter.
inverter(vs["p"], outp[0])  # First inverter is driven by the pulsed voltage source.
inverter(outp[0], outp[1])  # Second inverter is driven by the output of the first.
inverter(outp[1], outp[2])  # Third inverter is driven by the output of the second.

# Simulate the cascaded inverters.
circ = generate_netlist()  # Pass-in the library where the transistor model is stored.
sim = circ.simulator()
waveforms = sim.transient(step_time=0.01 @ u_ms, end_time=5 @ u_ms)

# Get the waveforms for the input and output.
time = waveforms.time
inp = waveforms[node(vs["p"])]
outp = waveforms[
    node(outp[2])
]  # Get the output waveform for the final inverter in the cascade.

# Plot the input and output waveforms. The output will be the inverse of the input since it passed
# through three inverters.
figure = plt.figure(1)
plt.title("Output Voltage vs. Input Voltage")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.plot(time * 1000, inp)
plt.plot(time * 1000, outp)
plt.legend(("Input Voltage", "Output Voltage"), loc=(1.1, 0.5))
plt.show()
