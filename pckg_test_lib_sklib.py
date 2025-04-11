from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

pckg_test_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'V', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ammeter', 'VS', 'AMMETER', 'V', 'v', 'vs'}), 'ref_prefix':'V', 'fplist':None, 'footprint':None, 'keywords':'voltage source', 'description':'Voltage source', 'datasheet':None, 'pins':[
            Pin(num='1',name='p',func=pin_types.PASSIVE),
            Pin(num='2',name='n',func=pin_types.PASSIVE)] }),
        Part(**{ 'name':'PULSEV', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'PULSEV', 'pulsevoltage', 'PULSEVOLTAGE', 'pulsev'}), 'ref_prefix':'V', 'fplist':None, 'footprint':None, 'keywords':'pulsed voltage source', 'description':'Pulsed voltage source', 'datasheet':None, 'pins':[
            Pin(num='1',name='p',func=pin_types.PASSIVE),
            Pin(num='2',name='n',func=pin_types.PASSIVE)] }),
        Part(**{ 'name':'sky130_fd_pr__pfet_01v8', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'sky130_fd_pr__pfet_01v8'}), 'ref_prefix':'X', 'fplist':[], 'footprint':None, 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='d',name='d',func=pin_types.UNSPEC),
            Pin(num='g',name='g',func=pin_types.UNSPEC),
            Pin(num='s',name='s',func=pin_types.UNSPEC),
            Pin(num='b',name='b',func=pin_types.UNSPEC)] }),
        Part(**{ 'name':'sky130_fd_pr__nfet_01v8', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'sky130_fd_pr__nfet_01v8'}), 'ref_prefix':'X', 'fplist':[], 'footprint':None, 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='d',name='d',func=pin_types.UNSPEC),
            Pin(num='g',name='g',func=pin_types.UNSPEC),
            Pin(num='s',name='s',func=pin_types.UNSPEC),
            Pin(num='b',name='b',func=pin_types.UNSPEC)] })])