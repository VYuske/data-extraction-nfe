from data_extraction_nfe.text_parser import TextParser

text = """
EMISSÃO NORMAL Número: 7539 Série: 102 Emissão: 18/10/2025 19:02:31 - Via Consumidor Protocolo de Autorização: 150250385090161 18/10/2025 19:04:22 Ambiente de Produção - Versão XML: 4.00 - Versão XSLT: 2.05
    """
parser = TextParser()
result = parser.parse_nfe_data(text)

print(result)
