# nfe-data-extraction

Ferramenta completa para extração, parsing, visualização e análise de dados de Notas Fiscais Eletrônicas (NFe). O projeto inclui um módulo Python para leitura e normalização dos dados e um aplicativo Streamlit que permite realizar upload de arquivos, executar o processamento e visualizar os resultados de forma interativa.

## Funcionalidades

Leitura e decodificação do QR Code da NFe.

Parsing estruturado do texto bruto.

Extração dos principais campos fiscais (itens, valores, impostos, emitente etc.).

Módulo de utils com funções auxiliares de limpeza e padronização.

Aplicativo Streamlit para:

Upload de imagens ou texto da NFe.

Execução da extração via interface gráfica.

Exibição estruturada dos dados.

Download dos dados extraídos.

## Executando o Aplicativo Streamlit

Instale as dependências:
```
pip install -r requirements.txt
```

Execute o app:
```
streamlit run app/app.py
```

Acesse no navegador:
```
http://localhost:8501
```
## Requisitos

- Python 3.10+
- pillow
- pyzbar
- pandas
- streamlit

## Status do Projeto

Em desenvolvimento contínuo. Novas funcionalidades serão adicionadas, incluindo:
- Extração expandida de itens e impostos
- Exportação avançada para CSV/Excel
- Dashboard com métricas financeiras
