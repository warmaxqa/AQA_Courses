import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


xml_data = '''<?xml version="1.0"?>
<groups>
  <group>
    <number>0</number>
    <name>Equity</name>
    <isEquity/>
    <populatesUnderlyings/>
    <hasLmeData/>
    <calculatesIndexVolumes/>
    <timingExbytes>
      <micro>0xFFFF</micro>
      <bbo>0xBTLS</bbo>
      <incoming>0xQUIN</incoming>
    </timingExbytes>
  </group>
  <group>
    <number>1</number>
    <name>Ofen</name>
    <isOfen/>
  </group>
  <group>
    <number>2</number>
    <name>Gost</name>
    <isGost/>
    <hasNews/>
    <netAddsXcnt/>
    <timingExbytes>
      <micro>0xBONYM</micro>
      <bbo>0xABBA</bbo>
      <incoming>0xACDC</incoming>
    </timingExbytes>
  </group>
  <group>
    <number>4</number>
    <name>US</name>
    <isUS/>
    <populatesUnderlyings/>
    <calculatesIndexVolumes/>
    <timingExbytes>
      <micro>0x8888</micro>
      <bbo>0xCCCC</bbo>
      <incoming>0x2000</incoming>
    </timingExbytes>
  </group>
  <group>
    <number>5</number>
    <name>MSG</name>
    <isMessage/>
    <timingExbytes>
      <micro>0x4444</micro>
      <incoming>0x6666</incoming>
    </timingExbytes>
  </group>
</groups>
'''


root = ET.fromstring(xml_data)


def find_incoming_by_group_number(group_number):
    for group in root.findall('group'):
        number = group.find('number').text
        if number == str(group_number):
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    return incoming.text
    return None


group_number_to_search = 2
incoming_value = find_incoming_by_group_number(group_number_to_search)

if incoming_value:
    logger.info(f"Group number {group_number_to_search} has incoming value: {incoming_value}")
else:
    logger.info(f"No incoming value found for group number {group_number_to_search}")