import re
from datetime import datetime

class TextParser:
    def __init__(self):
        self.pattern_list_of_items = re.compile(
            r'(?P<description>.+?)\s*\(Código:\s*(?P<code>\d+)\s*\)\s*'
            r'Qtde\.:([\s]*)(?P<quantity>[\d,]+)\s*UN:\s*(?P<unit>\w+)\s*Vl\. Unit\.\:\s*(?P<unit_value>[\d,]+)\s*Vl\. Total\s*(?P<total_value>[\d,]+)',
            re.DOTALL
        )

        self.pattern_nfe_data = re.compile(
            r'(?P<emission_type>EMISSÃO .+?)\s+'
            r'Número:\s*(?P<number>\d+)\s+Série:\s*(?P<series>\d+)\s+Emissão:\s*(?P<emission_datetime>[\d/]+\s+[\d:]+).*?'
            r'Protocolo de Autorização:\s*(?P<protocol_number>\d+)\s*(?P<protocol_datetime>[\d/]+\s+[\d:]+).*?'
            r'Ambiente de\s*(?P<environment>.+?)\s*-\s*Versão XML:\s*(?P<xml_version>[\d.]+)\s*-\s*Versão XSLT:\s*(?P<xslt_version>[\d.]+)',
            re.DOTALL
        )
        
    def parse_list_of_items(self, text):
        itens = []

        for match in self.pattern_list_of_items.finditer(text):
            item = {
                'description': match.group('description').strip(),
                'code': match.group('code').strip(),
                'quantity': float(match.group('quantity').replace(',', '.')),
                'unit': match.group('unit').strip(),
                'unit_value': float(match.group('unit_value').replace(',', '.')),
                'total_value': float(match.group('total_value').replace(',', '.'))
            }
            itens.append(item)

        return itens
    
    def parse_nfe_data(self, text):
        match = self.pattern_nfe_data.search(text)

        if match:
            data = match.groupdict()
            # Convert date strings to datetime objects
            data['emission_datetime'] = datetime.strptime(data['emission_datetime'], '%d/%m/%Y %H:%M:%S')
            data['protocol_datetime'] = datetime.strptime(data['protocol_datetime'], '%d/%m/%Y %H:%M:%S')

            return data
        
        return None
    