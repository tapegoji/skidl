import string
import json
import inspect

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *  # Only if you actually need the units.
if 1:
    header = '''# -*- coding: utf-8 -*-

# The MIT License (MIT) - Copyright (c) Dave Vandenbout.

"""
An interface from SKiDL to PySpice.
"""

# Create a SKiDL library of SPICE elements. All PySpice-related info goes into
# a pyspice dictionary that is added as an attribute to the SKiDL Part object.


from skidl import SKIDL, TEMPLATE, Part, Pin, SchLib
from skidl.pin import pin_types
from skidl.tools.spice import (
    add_part_to_circuit,
    add_xspice_to_circuit,
    not_implemented,
)
'''
###############################################################################
# Force the circuit to expose all its element methods from A .. Z.
###############################################################################
circuit = Circuit('Example')

# Some letters (like 'X' for subcircuits) may not work or may need special handling.
# This loop tries them all, ignoring any that fail.
for letter in string.ascii_uppercase:
    try:
        getattr(circuit, letter)('dummy_ref')
    except:
        pass

###############################################################################
# Helper function to detect that a member has the PySpice ELEMENT_CLASS attached.
###############################################################################
def has_element_class(member):
    # Check the member itself.
    if hasattr(member, 'ELEMENT_CLASS'):
        return True
    # Check if it's a bound method whose underlying function has 'ELEMENT_CLASS'.
    if hasattr(member, '__func__') and hasattr(member.__func__, 'ELEMENT_CLASS'):
        return True
    return False

###############################################################################
# Build up the JSON by introspecting the circuit methods that hold ELEMENT_CLASS.
###############################################################################

###############################################################################
# Write the python out.
###############################################################################
_POS_DIPOLE_ALIASES = ["+", "plus", "anode", "A"]
_NEG_DIPOLE_ALIASES = ["-", "minus", "m", "negative", "neg", "cathode", "C", "K"]
_POS_IN_PORT_ALIASES = ["+i", "i+", "ip", "input_plus", "plus_input"]
_NEG_IN_PORT_ALIASES = ["-i", "i-", "in","input_minus", "minus_input"]
_POS_OUT_PORT_ALIASES = ["+o", "o+", "op", "output_plus", "plus_output"]
_NEG_OUT_PORT_ALIASES = ["-o", "o-", "on", "output_minus", "minus_output"]

# add pin_aliases to the header
header += f"# Pin aliases\n"
header += f"_POS_DIPOLE_ALIASES = {repr(_POS_DIPOLE_ALIASES)}\n"
header += f"_NEG_DIPOLE_ALIASES = {repr(_NEG_DIPOLE_ALIASES)}\n"
header += f"_POS_IN_PORT_ALIASES = {repr(_POS_IN_PORT_ALIASES)}\n"
header += f"_NEG_IN_PORT_ALIASES = {repr(_NEG_IN_PORT_ALIASES)}\n"
header += f"_POS_OUT_PORT_ALIASES = {repr(_POS_OUT_PORT_ALIASES)}\n"
header += f"_NEG_OUT_PORT_ALIASES = {repr(_NEG_OUT_PORT_ALIASES)}\n\n"
import pprint
with open("/home/asepahvand/repos/skidl/src/skidl/tools/skidl/libs/skidlpyspice_sklib.py", "w") as f:
    # f.write(f"pyspice_lib = {repr(pyspice)}\n")
    # `pformat` returns a nicely formatted representation of an object    
    f.write(header)
    f.write("pyspice_lib = SchLib(tool=SKIDL).add_parts(\n"
    "     *[\n")
    pyspice = {}
    for name, member in inspect.getmembers(circuit, predicate=callable):
        if has_element_class(member):
            elem_class = member.ELEMENT_CLASS
            pyspice = {}

            # Inspect attributes of the underlying ELEMENT_CLASS (e.g., "PINS", "PIN_NAMES", etc.).
            aliases = []            
            keywords = [name]

            for line in str(member.__doc__).split('\n'): 
                first_line = line
                break
            if 'None' not in first_line:
                description = f"'{first_line}'"
                try:
                    keywords.append(description.split('This class implements a ')[1])
                except:
                    pass
            else:
                description = None

            for nn, mm in inspect.getmembers(elem_class):

                # Skip anything “private” or obviously not relevant.
                if nn.startswith('_'):
                    continue
                if inspect.isfunction(mm) or inspect.ismethod(mm) or isinstance(mm, property):
                    continue

                if 'alias' in nn.lower():
                    aliases.append(mm)
                    keywords.append(mm) if mm not in keywords else None
                    continue
                if nn == 'PINS':
                    pin_map = {}
                    for p in mm:
                        pin_map[p.position] = p.name
                    pyspice['pin_map'] = pin_map
                    continue

                # If it’s PIN_NAMES, rename it to pin_names_map.
                if nn == "PIN_NAMES":
                    # Master dictionary: each canonical key -> all synonyms (including itself).
                    pin_name_synonyms = {
                        # Dipole aliases:
                        "plus": "p",
                        "minus": "n",

                        #diode aliases:
                        "anode": "a",
                        "cathode": "c",

                        # Input port aliases:
                        "input_plus": "ip",
                        "input_minus": "in",

                        # Output port aliases:
                        "output_plus": "op",
                        "output_minus": "on",

                        # Transistor / device pins:
                        "collector": "c",
                        "base": "b",
                        "emitter": "e",
                        "gate": "g",
                        "source": "s",
                        "substrate": "s",
                        "drain": "d",
                        "bulk": "b",  # Note overlap with 'base' => 'b'.

                        # Any other special pins from the file:
                        "input": "i",
                        "output": "o",
                        # etc. for any other specialized pin names you want grouped.
                    }

                    def find_pin_synonyms(pin_name):
                        """
                        Return a tuple of all known synonyms for a given pin_name,
                        or just (pin_name,) if no match is found.
                        """
                        p_lower = pin_name.lower()
                        # Check each synonym group. If p_lower is found among a group, return that entire tuple.
                        for key, value in pin_name_synonyms.items():
                            if p_lower in key:
                                return value
                        # Fallback: unrecognized pin -> return a 1-tuple with original name.
                        return (pin_name,)

                    pin_names_map = {}
                    for p in mm:
                        pp= find_pin_synonyms(p)
                        # pin_names_map[pp] = p
                        if '*' in pp:
                            continue
                        pyspice[pp] = p

                elif nn == 'resistance':
                    pyspice['value'] = 'resistance'
                    pyspice['resistance'] = 'resistance'
                elif nn == 'capacitance':
                    pyspice['value'] = 'capacitance'
                    pyspice['capacitance'] = 'capacitance'
                elif nn == 'inductance':
                    pyspice['value'] = 'inductance'
                    pyspice['inductance'] = 'inductance'
                elif nn == 'dc_value':
                    pyspice['value'] = 'dc_value'
                    pyspice['dc_value'] = 'dc_value'
                elif nn == 'voltage_gain':
                    pyspice['value'] = 'voltage_gain'
                    pyspice['voltage_gain'] = 'voltage_gain'
                elif nn == 'current_gain':
                    pyspice['value'] = 'current_gain'
                    pyspice['current_gain'] = 'current_gain'
                elif nn == 'i_expression':
                    pyspice['i'] = 'i_expression'
                    pyspice['i_expression'] = 'i_expression'
                elif nn == 'v_expression':
                    pyspice['v'] = 'v_expression'
                    pyspice['v_expression'] = 'v_expression'
                elif nn == 'temperature':
                    pyspice['temp'] = 'temperature'
                    pyspice['temperature'] = 'temperature'
                elif nn == 'device_temperature':
                    pyspice['dtemp'] = 'device_temperature'
                    pyspice['device_temperature'] = 'device_temperature'
                elif nn == 'ic':
                    pyspice['ic'] = 'initial_condition'
                    pyspice['initial_condition'] = 'initial_condition'
                elif nn == 'multiplier':
                    pyspice['m'] = 'multiplier'
                    pyspice['multiplier'] = 'multiplier'
                elif nn == 'PREFIX':
                    ref_prefix =  mm
                elif nn == 'length':
                    pyspice['l'] = 'length'
                    pyspice['length'] = 'length'
                elif nn == 'width':
                    pyspice['w'] = 'width'
                    pyspice['width'] = 'width'
                elif nn == 'subcircuit_name':
                    pyspice['model'] = 'subcircuit_name'
                    pyspice['subcircuit_name'] = 'subcircuit_name'
                else:
                    # For any other attribute, just copy it over.
                    pyspice[nn] = nn     


            pin_map = pyspice['pin_map']
            if '*' in pin_map.values():
                pin_map = {}
                pyspice['pin_map'] = pin_map
            else:
                tmp_map = {}
                for k, v in pin_map.items():
                    tmp_map[k + 1] = v
                pin_map = tmp_map
                tmp_map = {}
                for k, v in pin_map.items():
                    for key, value in pyspice.items():
                        if v == value:
                            tmp_map[k] = key
                pin_map = tmp_map
        
                pyspice['pin_map'] = pin_map


            lines = []
            for k, v in pyspice.items():
                if isinstance(v, dict):
                    lines.append(f'                              "{k}": {v},')
                else:
                    lines.append(f'                              "{k}": "{v}",')

            kw = (
                '{\n'
                + "\n".join(lines)
                + '\n                        }'
            )


            pins = []
            # Start building the output string
            pins = "[\n"
            # Iterate over the items in pin_map
            for num, ppname in pin_map.items():
                    if ppname == '*':
                        continue
                    # Determine aliases based on the pin name
                    if pyspice[ppname] in _POS_DIPOLE_ALIASES:
                        alias = "_POS_DIPOLE_ALIASES"
                    elif pyspice[ppname] in _NEG_DIPOLE_ALIASES:
                        alias = "_NEG_DIPOLE_ALIASES"
                    elif pyspice[ppname] in _POS_IN_PORT_ALIASES:
                        alias = "_POS_IN_PORT_ALIASES"
                    elif pyspice[ppname] in _NEG_IN_PORT_ALIASES:
                        alias = "_NEG_IN_PORT_ALIASES"
                    elif '*' in ppname:
                        alias = []
                        continue
                    else:
                        alias = []
                        alias.append(f'{pyspice[ppname]}')
                    
                    # Append the formatted Pin block to the output string
                    pins += f"                  Pin(\n"
                    pins += f"                      num=\"{num}\",\n"
                    pins += f"                      name=\"{ppname}\",\n"
                    pins += f"                      func=pin_types.PASSIVE,\n"
                    pins += f"                      do_erc=True,\n"
                    pins += f"                      aliases={alias},\n"
                    pins += "                   ),\n"

            # Close the list definition
            pins += "              ]"
            
            f.write(f'            Part(\n')
            f.write(f'                name="{name}",\n')
            f.write(f'                aliases={aliases},\n')
            f.write(f'                dest=TEMPLATE,\n')
            f.write(f'                tool=SKIDL,\n')
            f.write(f'                keywords={keywords},\n')
            f.write(f'                description={description},\n')
            f.write(f'                ref_prefix="{ref_prefix}",\n')
            f.write(f'                pyspice={{\n')
            f.write(f'                         "name": "{name}",\n')
            f.write(f'                         "kw": {kw},\n')
            if name == 'A':
                f.write(f'                         "add": add_xspice_to_circuit,\n')                
            else:
                f.write(f'                         "add": add_part_to_circuit,\n')
            f.write(f'                }},\n')
            f.write(f'                num_units=1,\n')
            f.write(f'                do_erc=True,\n')
            f.write(f'                pins={pins},\n')
            f.write(f'            ),\n')



    # f.write('           Part(\n')
    # f.write(pprint.pformat(pyspice))
    f.write(""
    "      ]\n"
    ")\n")

print("pyspice.json has been generated.")
