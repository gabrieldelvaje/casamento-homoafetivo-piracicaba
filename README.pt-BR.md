# Casamento civil entre pessoas do mesmo sexo em Piracicaba

Uma história de dados sobre a evolução dos registros de casamento civil entre cônjuges do mesmo sexo em Piracicaba desde 2013.

[English version](README.md)

![Capa do carrossel](assets/carousel/01-cover.jpeg)

## Pergunta de pesquisa

**Desde a padronização nacional do casamento civil entre pessoas do mesmo sexo, como evoluíram os registros em Piracicaba e como a trajetória local se compara ao Estado de São Paulo e ao Brasil?**

O projeto combina uma série local divulgada como dados da CRC Nacional / Arpen-Brasil com fontes oficiais do CNJ, Fundação Seade e IBGE. O repositório documenta os números do carrossel, a metodologia, as limitações e uma divergência real entre fontes locais.

## Por que 2013 importa

A Resolução nº 175/2013 do CNJ vedou aos cartórios a recusa da habilitação, celebração ou conversão de união estável em casamento civil quando o casal é formado por duas pessoas do mesmo sexo. A norma entrou em vigor em maio de 2013. Decisões anteriores do STF e do STJ já haviam estabelecido bases jurídicas importantes; por isso, o projeto não apresenta 2013 como o ano em que o casamento homoafetivo foi "criado".

## Principais resultados

- Piracicaba registrou **37** casamentos entre pessoas do mesmo sexo em 2019, **20** em 2020 e **19** em 2021. Em 2022, o número voltou a **34** e, em 2024, chegou a **62**, valor reportado como recorde local pela fonte de 2025.
- A variação de 2019 para 2020 foi de aproximadamente **-45,9%**. A quebra coincide com a pandemia, mas a análise é descritiva e não atribui a queda a uma única causa.
- No acumulado local disponível até abril de 2023, **153 de 239** registros foram entre duas mulheres, cerca de **64,0%**.
- No Estado de São Paulo, o Seade contabilizou **37.625** casamentos civis entre pessoas do mesmo sexo acumulados entre 2013 e 2024. A participação no total de casamentos passou de **0,7%** para **1,8%**; em 2024, **65%** dessas uniões foram entre duas mulheres.
- No Brasil, o IBGE registrou **12.187** casamentos entre pessoas do mesmo sexo em 2024, **8,8%** acima dos 11.198 de 2023; **64,6%** foram entre duas mulheres.

## Nota de validação dos dados

Há uma divergência entre duas fontes locais. A sequência detalhada publicada em 2023, atribuída à CRC/Arpen, informa **2013=17 e 2014=22**. Já uma reportagem de 2025 usa **2014=17** como base para afirmar crescimento superior a 250% em dez anos. O carrossel é preservado exatamente como foi fornecido, inclusive a arte com 17→62 / +264,7%, mas o repositório **não trata 2014=17 como valor definitivamente validado**.

Na série estruturada, 2014 aparece como **22**, e a divergência está documentada em [`docs/data-validation.md`](docs/data-validation.md).

A fonte de 2023 também informa **12 registros até abril de 2023**. Esse número é parcial e não representa o ano completo. Por isso, `data/piracicaba_series.csv` deixa 2023 sem total anual e não usa 12 como valor comparável aos demais anos.

## O que os dados medem — e o que não medem

Os números representam atos de registro civil entre cônjuges registrados como do mesmo sexo. Eles não permitem estimar orientação sexual, identidade de gênero, tamanho da população LGBTQIA+, número total de casais homoafetivos ou grau de aceitação social. O projeto também não apresenta ranking de Piracicaba entre cidades do interior paulista, pois não utiliza uma base municipal completa e reproduzível para isso.

## Carrossel

As sete imagens abaixo são as artes originais fornecidas, armazenadas sem alterações visuais.

### 1. Pergunta de pesquisa
![Slide 1](assets/carousel/01-cover.jpeg)

### 2. Marco jurídico de 2013
![Slide 2](assets/carousel/02-legal-context-2013.jpeg)

### 3. Piracicaba atinge o maior valor local reportado
![Slide 3](assets/carousel/03-piracicaba-growth.jpeg)

### 4. Mulheres são maioria nas amostras comparadas
![Slide 4](assets/carousel/04-women-majority.jpeg)

### 5. A quebra no período da pandemia
![Slide 5](assets/carousel/05-pandemic-series.jpeg)

### 6. Contexto de São Paulo e Brasil
![Slide 6](assets/carousel/06-sp-brazil-context.jpeg)

### 7. Resumo
![Slide 7](assets/carousel/07-summary.jpeg)

## Estrutura do repositório

```text
assets/carousel/          sete imagens originais do carrossel
data/piracicaba_series.csv
data/comparison_metrics.csv
docs/methodology.md
docs/sources.md
docs/data-validation.md
src/validate_metrics.py
```

## Reprodutibilidade

O script de validação utiliza apenas a biblioteca padrão do Python:

```bash
python src/validate_metrics.py
```

Ele recalcula os principais percentuais, confere os valores anuais usados na análise, verifica que 2023 não foi preenchido como ano completo e imprime a divergência de 2014 como alerta explícito.

## Fontes

- CNJ — Resolução nº 175/2013
- Fundação Seade — *Panorama dos casamentos civis de pessoas do mesmo sexo* (junho de 2025)
- IBGE — *Estatísticas do Registro Civil 2024*
- Dados locais da CRC Nacional / Arpen-Brasil reproduzidos por reportagens do Sampi em 2023 e 2025

Referências e links completos: [`docs/sources.md`](docs/sources.md).

## Documentação metodológica

- [`docs/methodology.md`](docs/methodology.md)
- [`docs/data-validation.md`](docs/data-validation.md)
- [`data/piracicaba_series.csv`](data/piracicaba_series.csv)
- [`data/comparison_metrics.csv`](data/comparison_metrics.csv)

## Autor

Gabriel Delvaje — análise de dados e data storytelling.
