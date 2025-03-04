from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

RF_Switch = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'ADG901BCPZ', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ADG901BCPZ'}), 'ref_prefix':'U', 'fplist':['Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm'], 'footprint':'Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm', 'keywords':'RF SPST switch CMOS LVTTL', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG901_902.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nADG901BCPZ\n\nRF SPST switch CMOS LVTTL', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='CTRL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ADG901BRMZ', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ADG901BRMZ'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'RF SPST switch CMOS LVTTL', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG901_902.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nADG901BRMZ\n\nRF SPST switch CMOS LVTTL', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='CTRL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ADG902BRMZ', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ADG902BRMZ'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'RF SPST switch CMOS LVTTL', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG901_902.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nADG902BRMZ\n\nRF SPST switch CMOS LVTTL', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='CTRL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ADG918BCPZ', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ADG918BCPZ'}), 'ref_prefix':'U', 'fplist':['Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm'], 'footprint':'Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm', 'keywords':'RF Mux SPDT switch CMOS LVTTL', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG918_919.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nADG918BCPZ\n\nRF Mux SPDT switch CMOS LVTTL', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='CTRL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ADG918BRM', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ADG918BRM'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'RF Mux SPDT switch CMOS LVTTL', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG918_919.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nADG918BRM\n\nRF Mux SPDT switch CMOS LVTTL', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='CTRL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF1',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ADG919BCPZ', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ADG919BCPZ'}), 'ref_prefix':'U', 'fplist':['Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm'], 'footprint':'Package_CSP:LFCSP-8-1EP_3x3mm_P0.5mm_EP1.45x1.74mm', 'keywords':'RF Mux SPDT switch CMOS LVTTL', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG918_919.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nADG919BCPZ\n\nRF Mux SPDT switch CMOS LVTTL', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='CTRL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'ADG919BRMZ', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'ADG919BRMZ'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8_3x3mm_P0.65mm'], 'footprint':'Package_SO:MSOP-8_3x3mm_P0.65mm', 'keywords':'RF Mux SPDT switch CMOS LVTTL', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/ADG918_919.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nADG919BRMZ\n\nRF Mux SPDT switch CMOS LVTTL', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='2',name='CTRL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='4',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF1',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'AS179-92LF', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'AS179-92LF'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'rf spdt switch', 'description':'', 'datasheet':'http://www.skyworksinc.com/uploads/documents/AS179_92LF_200176H.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nAS179-92LF\n\nrf spdt switch', 'pins':[
            Pin(num='1',name='J3',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='J2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V1',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='J1',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V2',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'BGS12WN6E6327', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'BGS12WN6E6327'}), 'ref_prefix':'U', 'fplist':['Package_LGA:Infineon_PG-TSNP-6-10_0.7x1.1mm_0.7x1.1mm_P0.4mm'], 'footprint':'Package_LGA:Infineon_PG-TSNP-6-10_0.7x1.1mm_0.7x1.1mm_P0.4mm', 'keywords':'RF Mux SPDT switch CMOS', 'description':'', 'datasheet':'https://www.infineon.com/dgdl/Infineon-BGS12WN6-DataSheet-v02_05-EN.pdf?fileId=5546d4626b2d8e69016b89d2b3334727', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nBGS12WN6E6327\n\nRF Mux SPDT switch CMOS', 'pins':[
            Pin(num='1',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RFIN',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='CTRL',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'HMC7992', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'HMC7992'}), 'ref_prefix':'U', 'fplist':['Package_CSP:LFCSP-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm'], 'footprint':'Package_CSP:LFCSP-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm', 'keywords':'rf switch sp4t absorptive', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/HMC7992.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nHMC7992\n\nrf switch sp4t absorptive', 'pins':[
            Pin(num='1',name='RF4',func=pin_types.PASSIVE,unit=1),
            Pin(num='10',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='11',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='12',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='13',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='14',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='15',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='16',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='17',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='RF3',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='7',name='B',func=pin_types.INPUT,unit=1),
            Pin(num='8',name='A',func=pin_types.INPUT,unit=1),
            Pin(num='9',name='RF2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'HMC849A', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'HMC849A'}), 'ref_prefix':'U', 'fplist':['Package_CSP:LFCSP-16-1EP_4x4mm_P0.65mm_EP2.4x2.4mm'], 'footprint':'Package_CSP:LFCSP-16-1EP_4x4mm_P0.65mm_EP2.4x2.4mm', 'keywords':'RF SPDT switch', 'description':'', 'datasheet':'https://www.analog.com/media/en/technical-documentation/data-sheets/hmc849a.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nHMC849A\n\nRF SPDT switch', 'pins':[
            Pin(num='1',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='10',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='11',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='12',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='13',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='14',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='15',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='16',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='17',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='VCTL',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='EN',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='RF1',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'KSW-2-46', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'KSW-2-46'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'RF SPDT switch', 'description':'', 'datasheet':'https://www.minicircuits.com/pdfs/KSW-2-46+.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nKSW-2-46\n\nRF SPDT switch', 'pins':[
            Pin(num='1',name='CONTROL2',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='RF_IN',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='CONTROL1',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RF_OUT1',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF_OUT2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'KSWA-2-46', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'KSWA-2-46'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'RF SPDT switch', 'description':'', 'datasheet':'https://www.minicircuits.com/pdfs/KSWA-2-46+.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nKSWA-2-46\n\nRF SPDT switch', 'pins':[
            Pin(num='1',name='CONTROL2',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='RF_IN',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='CONTROL1',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RF_OUT1',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF_OUT2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'KSWHA-1-20', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'KSWHA-1-20'}), 'ref_prefix':'U', 'fplist':[''], 'footprint':'', 'keywords':'RF SPST switch', 'description':'', 'datasheet':'https://www.minicircuits.com/pdfs/KSWHA-1-20+.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nKSWHA-1-20\n\nRF SPST switch', 'pins':[
            Pin(num='1',name='RF_IN',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='CONTROL1',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='CONTROL2',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RF_OUT',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0136', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0136'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0136.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0136\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0178', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0178'}), 'ref_prefix':'U', 'fplist':['Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm_ThermalVias'], 'footprint':'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm_ThermalVias', 'keywords':'RF switch SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0178.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0178\n\nRF switch SPDT', 'pins':[
            Pin(num='1',name='CTL1',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='CTL2',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0179', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0179'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-23-6'], 'footprint':'Package_TO_SOT_SMD:SOT-23-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0179.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0179\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MSW-2-20', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MSW-2-20'}), 'ref_prefix':'U', 'fplist':['Package_SO:SOP-8_3.76x4.96mm_P1.27mm'], 'footprint':'Package_SO:SOP-8_3.76x4.96mm_P1.27mm', 'keywords':'RF SPDT switch', 'description':'', 'datasheet':'https://www.minicircuits.com/pdfs/MSW-2-20+.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMSW-2-20\n\nRF SPDT switch', 'pins':[
            Pin(num='1',name='RF_IN',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF_OUT2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='CONTROL2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='CONTROL1',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='RF_OUT1',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MSW2-50', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MSW2-50'}), 'ref_prefix':'U', 'fplist':['Package_DFN_QFN:QFN-12-1EP_3x3mm_P0.51mm_EP1.45x1.45mm'], 'footprint':'Package_DFN_QFN:QFN-12-1EP_3x3mm_P0.51mm_EP1.45x1.45mm', 'keywords':'RF SPDT switch', 'description':'', 'datasheet':'https://www.minicircuits.com/pdfs/MSW2-50+.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMSW2-50\n\nRF SPDT switch', 'pins':[
            Pin(num='1',name='CONTROL1',func=pin_types.INPUT,unit=1),
            Pin(num='10',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='11',name='RF_OUT1',func=pin_types.PASSIVE,unit=1),
            Pin(num='12',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='13',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='NC',func=pin_types.NOCONNECT,unit=1),
            Pin(num='3',name='CONTROL2',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RF_OUT2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF_IN',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MSWA-2-20', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MSWA-2-20'}), 'ref_prefix':'U', 'fplist':['Package_SO:SOP-8_3.76x4.96mm_P1.27mm'], 'footprint':'Package_SO:SOP-8_3.76x4.96mm_P1.27mm', 'keywords':'RF SPDT switch', 'description':'', 'datasheet':'https://www.minicircuits.com/pdfs/MSWA-2-20+.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMSWA-2-20\n\nRF SPDT switch', 'pins':[
            Pin(num='1',name='CONTROL2',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='RF_IN',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='CONTROL1',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RF_OUT2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF_OUT1',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MSWA2-50', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MSWA2-50'}), 'ref_prefix':'U', 'fplist':['Package_DFN_QFN:QFN-12-1EP_3x3mm_P0.51mm_EP1.45x1.45mm'], 'footprint':'Package_DFN_QFN:QFN-12-1EP_3x3mm_P0.51mm_EP1.45x1.45mm', 'keywords':'RF SPDT switch', 'description':'', 'datasheet':'https://www.minicircuits.com/pdfs/MSWA2-50+.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMSWA2-50\n\nRF SPDT switch', 'pins':[
            Pin(num='1',name='CONTROL1',func=pin_types.INPUT,unit=1),
            Pin(num='10',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='11',name='RF_OUT1',func=pin_types.PASSIVE,unit=1),
            Pin(num='12',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='13',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='NC',func=pin_types.NOCONNECT,unit=1),
            Pin(num='3',name='CONTROL2',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='5',name='RF_OUT2',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF_IN',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'SKY13380-350LF', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'SKY13380-350LF'}), 'ref_prefix':'U', 'fplist':['Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm'], 'footprint':'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm', 'keywords':'rf switch sp4t', 'description':'', 'datasheet':'https://www.skyworksinc.com/-/media/SkyWorks/Documents/Products/601-700/201486C.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nSKY13380-350LF\n\nrf switch sp4t', 'pins':[
            Pin(num='1',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='10',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='11',name='ANT',func=pin_types.PASSIVE,unit=1),
            Pin(num='12',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='13',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='14',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='15',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='16',name='NC',func=pin_types.NOCONNECT,unit=1),
            Pin(num='2',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='CTRL2',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='CTRL1',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='RF4',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='RF3',func=pin_types.PASSIVE,unit=1),
            Pin(num='9',name='GND',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'SKY13575-639LF', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'SKY13575-639LF'}), 'ref_prefix':'U', 'fplist':['RF:Skyworks_SKY13575_639LF'], 'footprint':'RF:Skyworks_SKY13575_639LF', 'keywords':'rf switch sp4t absorptive', 'description':'', 'datasheet':'https://www.skyworksinc.com/-/media/SkyWorks/Documents/Products/2201-2300/SKY13575_639LF_203270D.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nSKY13575-639LF\n\nrf switch sp4t absorptive', 'pins':[
            Pin(num='1',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='10',name='VDD',func=pin_types.PWRIN,unit=1),
            Pin(num='11',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='12',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='13',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='14',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='15',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='5',name='RF4',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='GND',func=pin_types.PASSIVE,unit=1),
            Pin(num='7',name='RF3',func=pin_types.PASSIVE,unit=1),
            Pin(num='8',name='VC1',func=pin_types.INPUT,unit=1),
            Pin(num='9',name='VC2',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASW-007221', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASW-007221'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'http://cdn.macom.com/datasheets/masw-007221.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASW-007221\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0115', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0115'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'http://cdn.macom.com/datasheets/maswss0115.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0115\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0143', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0143'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0143.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0143\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0151', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0151'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0151.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0151\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0166', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0166'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0166.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0166\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0176', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0176'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0176.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0176\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'MASWSS0192', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MASWSS0192'}), 'ref_prefix':'U', 'fplist':['Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'Package_TO_SOT_SMD:SOT-363_SC-70-6'], 'footprint':'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'keywords':'RF SWITCH SPDT', 'description':'', 'datasheet':'https://cdn.macom.com/datasheets/MASWSS0192.pdf', 'search_text':'/usr/share/kicad/symbols/RF_Switch.kicad_sym\nMASWSS0192\n\nRF SWITCH SPDT', 'pins':[
            Pin(num='1',name='RF1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='GND',func=pin_types.PWRIN,unit=1),
            Pin(num='3',name='RF2',func=pin_types.PASSIVE,unit=1),
            Pin(num='4',name='V2',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='RFC',func=pin_types.PASSIVE,unit=1),
            Pin(num='6',name='V1',func=pin_types.INPUT,unit=1)], 'unit_defs':[] })])