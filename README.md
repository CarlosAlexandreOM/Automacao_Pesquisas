# Automação de Pesquisas de Vagas

Scripts em Python desenvolvidos para automatizar a abertura de pesquisas de vagas no LinkedIn e na Gupy, utilizando filtros e termos relacionados a oportunidades na área de Dados e Business Intelligence.

O projeto surgiu de uma necessidade pessoal de agilizar a busca por vagas, reduzindo o trabalho manual de abrir repetidamente as mesmas pesquisas no navegador.

## Funcionalidades

- Abre o Google Chrome automaticamente.
- Acessa pesquisas predefinidas no LinkedIn e na Gupy.
- Abre cada pesquisa em uma aba separada do navegador.
- Utiliza URLs com filtros e termos específicos para direcionar as buscas a oportunidades de interesse.

### Pesquisas configuradas

**LinkedIn**
- Analista de BI Júnior.
- Analista de Dados Júnior.
- Estágio em BI, Business Intelligence e Analytics.
- Estágio em Análise de Dados e Dados.

**Gupy**
- Dados.
- Estágio.
- Estagiário.

As pesquisas foram configuradas para priorizar oportunidades remotas, conforme os filtros presentes nas respectivas URLs.

## Tecnologias utilizadas

- **Python 3.12:** linguagem utilizada no desenvolvimento dos scripts de automação.
- **PyAutoGUI:** biblioteca utilizada para controlar o teclado e interagir com a interface gráfica do sistema operacional.
- **Pyperclip:** biblioteca utilizada para manipular a área de transferência e inserir as URLs no navegador.
- **Time:** módulo da biblioteca padrão do Python utilizado para controlar os intervalos de espera durante a execução.
- **Conda:** ferramenta utilizada para criar e gerenciar o ambiente de desenvolvimento e suas dependências.

## Requisitos

- Python 3.12.
- Conda instalado.
- Google Chrome instalado.
- Sistema operacional Windows.
- Conexão com a internet.
- Conta no LinkedIn ou na Gupy, quando necessária para acessar determinados conteúdos.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/CarlosAlexandreOM/Automacao_Pesquisas.git
```

Acesse a pasta do projeto:

```bash
cd Automacao_Pesquisas
```

Crie o ambiente Conda a partir do arquivo `environment.yml`:

```bash
conda env create -f environment.yml
```

Ative o ambiente:

```bash
conda activate automacao_pesquisa
```

## Como executar

Execute o script correspondente à plataforma desejada:

```bash
python pesquisa_linkedin.py
```

Ou:

```bash
python pesquisa_gupy.py
```

Após iniciar o script, aguarde o tempo inicial configurado para que a automação comece a executar as ações no computador.

## Personalização

As URLs das pesquisas ficam armazenadas em listas no início de cada script. Para adicionar, remover ou modificar pesquisas, basta editar essas listas.

Os tempos de espera também podem ser ajustados conforme o desempenho do computador e a velocidade de carregamento das páginas.

## Limitações

- A automação foi desenvolvida para uso pessoal em ambiente Windows.
- Os tempos de espera foram definidos com base no ambiente utilizado durante o desenvolvimento.
- O funcionamento depende da interface gráfica, da inicialização do navegador e do carregamento das páginas.
- Alterações na interface dos sites ou nas URLs de pesquisa podem exigir ajustes nos scripts.
- A automação abre as pesquisas, mas não realiza candidaturas nem verifica automaticamente a relevância ou a disponibilidade das vagas.

## Objetivo do projeto e aprendizados

Além de resolver uma necessidade pessoal, o projeto permitiu praticar automação com Python, manipulação da área de transferência, interação com aplicações por meio da interface gráfica e gerenciamento de ambientes com Conda.