import re

class TextParser:
    def __init__(self):
        self.pattern = re.compile(
            r'(?P<description>.+?)\s*\(Código:\s*(?P<code>\d+)\s*\)\s*'
            r'Qtde\.:([\s]*)(?P<quantity>[\d,]+)\s*UN:\s*(?P<unit>\w+)\s*Vl\. Unit\.\:\s*(?P<unit_value>[\d,]+)\s*Vl\. Total\s*(?P<total_value>[\d,]+)',
            re.DOTALL
        )

    def parse_text(self, text):
        itens = []

        for match in self.pattern.finditer(text):
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