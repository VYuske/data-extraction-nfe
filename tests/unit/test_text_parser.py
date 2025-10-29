import pytest
from data_extraction_nfe.text_parser import TextParser

@pytest.fixture
def parser():
    """Fixture to initialize TextParser for all tests."""
    return TextParser()

def test_parse_text_empty(parser):
    result = parser.parse_text("")
    assert result == []  # Assuming it returns an empty list for empty input

def test_parse_text_nfe(parser):
    sample_text = """
        COXA SCOXA COPACOL 800G (Código: 7891527962352 )
        Qtde.:1  UN: UN  Vl. Unit.:   8,98 	Vl. Total
        8,98
        COXA SCOXA COPACOL 800G (Código: 7891527962352 )
        Qtde.:1  UN: UN  Vl. Unit.:   8,98 	Vl. Total
        8,98
        LING SUINA SADIA 700G CO (Código: 7891515594312 )
        Qtde.:1  UN: UN  Vl. Unit.:   7,99 	Vl. Total
        7,99
        COSTELA BOV TIRAS KG BAN (Código: 1582 )
        Qtde.:0,728  UN: KG  Vl. Unit.:   17,89 	Vl. Total
        13,02
        COSTELA BOV TIRAS KG BAN (Código: 1582 )
        Qtde.:0,55  UN: KG  Vl. Unit.:   17,89 	Vl. Total
        9,84
    """

    expected = [
        {
            'description': 'COXA SCOXA COPACOL 800G',
            'code': '7891527962352',
            'quantity': 1,
            'unit': 'UN',
            'unit_value': 8.98,
            'total_value': 8.98
        },
        {
            'description': 'COXA SCOXA COPACOL 800G',
            'code': '7891527962352',
            'quantity': 1,
            'unit': 'UN',
            'unit_value': 8.98,
            'total_value': 8.98
        },
        {
            'description': 'LING SUINA SADIA 700G CO',
            'code': '7891515594312',
            'quantity': 1,
            'unit': 'UN',
            'unit_value': 7.99,
            'total_value': 7.99
        },
        {
            'description': 'COSTELA BOV TIRAS KG BAN',
            'code': '1582',
            'quantity': 0.728,
            'unit': 'KG',
            'unit_value': 17.89,
            'total_value': 13.02
        },
        {
            'description': 'COSTELA BOV TIRAS KG BAN',
            'code': '1582',
            'quantity': 0.55,
            'unit': 'KG',
            'unit_value': 17.89,
            'total_value': 9.84
        }
    ]

    result = parser.parse_text(sample_text)
    assert result == expected
