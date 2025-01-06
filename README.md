# **Desafio da Aceleradora Ágil 2025/1**
## Tema: Gerenciamento de Produtos para a Loja AgilStore
## Tecnologias Usadas: Python e Json
## Feito por: David Ben
> ### Copyright 2025 | garanto que todo o texto e código gerado foram feitos totalmente por mim sem uso de ChatGPT ou outras tecnologias artificiais.

---

> ## Enunciado
A AgilStore é uma pequena loja de eletrônicos que recentemente expandiu seu catálogo de produtos para incluir uma variedade maior de itens, desde smartphones e laptops até acessórios como cabos, carregadores e fones de ouvido. Com o aumento do número de produtos e a diversidade das categorias, a equipe de gerenciamento percebeu a necessidade de otimizar o controle do inventário para garantir que os produtos estejam sempre disponíveis para os clientes e que os níveis de estoque sejam mantidos de forma eficiente.
Atualmente, o controle de inventário está sendo feito manualmente em planilhas, o que tem se mostrado ineficiente e propenso a erros, especialmente quando se trata de atualizações rápidas ou buscas específicas. Para resolver esse problema, a loja decidiu desenvolver uma aplicação que permita a gestão automatizada do inventário de produtos, facilitando operações como adicionar novos produtos, listar produtos existentes, atualizar informações e remover itens obsoletos.

Requisitos Funcionais:
1. Adicionar Produto: Permitir que o usuário adicione um novo produto ao inventário.
Solicitar ao usuário a inserção dos seguintes dados:
Nome do Produto
Categoria
Quantidade em Estoque
Preço
Gerar um id único para cada produto automaticamente.

2. Listar Produtos: Exibir todos os produtos cadastrados no inventário. Mostrar uma tabela com as seguintes colunas:
```
- ID
- Nome do Produto
- Categoria
- Quantidade em Estoque
- Preço
- Permitir opções de filtragem por categoria ou ordenação por nome, quantidade ou preço (opcional).
```

3. Atualizar Produto: Atualizar as informações de um produto existente identificado pelo seu id.
Verificar se o id informado existe no inventário.
Solicitar ao usuário quais campos deseja atualizar (Nome, Categoria, Quantidade, Preço).
Validar os novos dados antes de salvar as alterações.

4. Excluir Produto: Remover um produto do inventário pelo seu id.
Verificar se o id informado existe no inventário.
Confirmar a ação com o usuário antes de excluir (opcional).
Remover o produto do inventário após a confirmação.

5. Buscar Produto: Buscar e exibir detalhes de um produto específico pelo id ou pelo nome.
Permitir a busca por id ou por parte do nome do produto.
Exibir todas as informações detalhadas do produto encontrado.
Exibir mensagem apropriada se nenhum produto for encontrado.


- Requisitos Extras (Opcional):
Persistência de Dados:
Implementar salvamento automático dos dados em um arquivo JSON para que os produtos não sejam perdidos ao encerrar a aplicação.

> ## Resolução Do Projeto:

O código implementa um sistema de gerenciamento de inventário simples, que permite adicionar, listar, atualizar, excluir e buscar produtos. Vou explicar as funções e o papel de cada item importado, com ênfase na parte do JSON, que é o diferencial do código.

#### 1. **Importações**
- **`import json`**:
  - O módulo `json` é utilizado para manipular dados no formato JSON (JavaScript Object Notation). No código, ele é usado para carregar e salvar o inventário de produtos em um arquivo JSON. Isso permite que os dados sejam persistidos entre execuções do programa, ou seja, os dados não são perdidos quando o programa é fechado.
  
- **`import random`**:
  - O módulo `random` é utilizado para gerar dados aleatórios. No código, ele é usado para gerar IDs de produtos aleatórios.

- **`import string`**:
  - O módulo `string` fornece uma série de funções e constantes, como o conjunto de letras do alfabeto. É usado em conjunto com o `random` para gerar IDs com letras aleatórias.

- **`from tabulate import tabulate`**:
  - O `tabulate` é uma biblioteca que permite formatar tabelas de forma bonita e legível no terminal. Ele é usado para exibir os produtos de maneira organizada quando listamos ou buscamos produtos.

---

#### 2. **Funções da Classe `AgilStore`**

- **`__init__(self, arquivo="inventario.json")`**:
  - O método `__init__` é o inicializador da classe, sendo chamado quando um objeto `AgilStore` é criado. Ele define o nome do arquivo onde os dados serão armazenados (por padrão, `inventario.json`) e chama o método `carregar_dados` para carregar os dados do arquivo.
  
- **`carregar_dados(self)`**:
  - Esse método tenta abrir o arquivo `inventario.json` e carrega os dados nele contidos para o atributo `inventario`. Se o arquivo não for encontrado, ele inicializa `inventario` como uma lista vazia.
  - **Aqui é onde o JSON é utilizado**: O arquivo JSON contém os dados dos produtos e é carregado utilizando a função `json.load()`, que converte o conteúdo do arquivo JSON em uma estrutura de dados Python (geralmente um dicionário ou lista).

- **`salvar_dados(self)`**:
  - Esse método salva os dados do inventário no arquivo `inventario.json`. Ele usa a função `json.dump()` para converter a lista de produtos (`inventario`) em formato JSON e gravá-la no arquivo. O parâmetro `indent=4` é usado para formatar o JSON de maneira legível, com uma indentação de 4 espaços.

- **`gerar_id(self)`**:
  - Esse método gera um ID único para cada produto. Ele usa as funções do módulo `random` para gerar duas letras maiúsculas seguidas de quatro dígitos numéricos. Este ID é único, mas não garante que não haverá colisões, já que é gerado de forma aleatória.

- **`adicionar_produto(self)`**:
  - Esse método permite adicionar um novo produto ao inventário. Ele solicita ao usuário o nome, categoria, quantidade e preço do produto. Depois, ele gera um ID único para o produto e o adiciona à lista `inventario`. Em seguida, ele chama o método `salvar_dados()` para salvar o inventário atualizado no arquivo.
  
- **`listar_produtos(self)`**:
  - Esse método lista todos os produtos no inventário. Caso o inventário esteja vazio, ele exibe uma mensagem informando que não há produtos cadastrados. Caso contrário, ele usa a biblioteca `tabulate` para formatar e exibir os dados dos produtos em uma tabela no terminal.

- **`atualizar_produto(self)`**:
  - Esse método permite atualizar as informações de um produto existente. O usuário deve fornecer o ID do produto e escolher qual campo (nome, categoria, quantidade ou preço) deseja atualizar. Depois de realizar a atualização, o método chama `salvar_dados()` para persistir as mudanças no arquivo JSON.

- **`excluir_produto(self)`**:
  - Esse método permite excluir um produto do inventário. O usuário fornece o ID do produto e, caso o produto seja encontrado, ele será removido da lista `inventario`. Em seguida, as alterações são salvas no arquivo JSON.

- **`buscar_produto(self)`**:
  - Esse método permite buscar produtos no inventário pelo ID ou nome (parte do nome). Ele solicita um termo de pesquisa e filtra os produtos que contêm esse termo. Os resultados são exibidos de forma formatada usando o `tabulate`.

---

### **3. Implementação do JSON: Persistência de Dados**

- **`carregar_dados(self)`**:
  - A função `json.load(file)` é responsável por carregar o conteúdo do arquivo `inventario.json` e convertê-lo para um formato que o Python possa manipular, geralmente um dicionário ou lista. Isso permite que os dados sejam lidos e trabalhados como objetos Python durante a execução do programa.

- **`salvar_dados(self)`**:
  - A função `json.dump(self.inventario, file, indent=4)` é responsável por salvar o inventário de produtos no arquivo `inventario.json`. O parâmetro `indent=4` é utilizado para garantir que o JSON seja gravado de maneira legível e estruturada, facilitando a leitura dos dados quando necessário.

---

> ## Como rodar o projeto em sua máquina?

### 1. Clonando o projeto no CMD e rodando o mesmo no próprio CMD:

Para rodar o projeto diretamente no seu CMD (Prompt de Comando), siga os passos abaixo:

1. **Abra o CMD (Prompt de Comando):**
   - No Windows, pressione `Windows + R`, digite `cmd` e pressione Enter.

2. **Clone o repositório do projeto:**
   Execute o seguinte comando no CMD para clonar o repositório para a sua máquina (certifique-se de que o Git está instalado):
   ```bash
   git clone https://github.com/DavidBen48/gerenciamento-de-estoque-python.git
   ```

3. **Navegue até a pasta do projeto:**
   Após o repositório ser clonado, entre na pasta do projeto com o comando:
   ```bash
   cd gerenciamento-de-estoque-python
   ```

4. **Instale a biblioteca `tabulate` (OPCIONAL):**
   Você pode instalar essa biblioteca manualmente se quiser que o código tenha 100% de êxito, mas mesmo se não instalar ele irá rodar sem nenhum problema. Se você for apenas uma pessoa precavida, insira esse comando:
   ```bash
   pip install tabulate
   ```

5. **Execute o código:**
   Para rodar o código, execute o arquivo `main.py` com o seguinte comando:
   ```bash
   python main.py
   ```

Agora, o projeto será executado no seu CMD e você poderá interagir com ele diretamente.

---

### 2. Clonando o projeto no CMD e rodando no VSC:

Se preferir usar o Visual Studio Code (VSC), siga os passos abaixo:

1. **Abra o CMD (Prompt de Comando):**
   - No Windows, pressione `Windows + R`, digite `cmd` e pressione Enter.

2. **Clone o repositório do projeto:**
   Execute o seguinte comando no CMD para clonar o repositório para a sua máquina:
   ```bash
   git clone https://github.com/DavidBen48/gerenciamento-de-estoque-python.git
   ```

3. **Navegue até a pasta do projeto:**
   Entre na pasta do projeto com o comando:
   ```bash
   cd gerenciamento-de-estoque-python
   ```

4. **Abra o Visual Studio Code:**
   Com o projeto já clonado, basta executar o comando para abrir o projeto no VSC:
   ```bash
   code .
   ```

5. **Instale a biblioteca `tabulate` (OPCIONAL):**
   Não é obrigatório a instalação, apenas para ter uma segurança maior. Se quiser se precaver, abra o terminal integrado no VSC (pressionando `Ctrl + ``) e execute:
   ```bash
   pip install tabulate
   ```

6. **Execute o código:**
   No VSC, abra o arquivo `main.py` e clique no botão de play no canto superior direito ou pressione `Ctrl + F5` para rodar o código.

Agora você estará executando o projeto diretamente no Visual Studio Code!

---

### 3. Extra: Rodando o projeto no Google Colab

Se você tiver dificuldades para rodar o projeto na sua máquina, você pode executar o código diretamente no **Google Colab**. Siga os passos abaixo:

1. **Abra o link do Google Colab:**
   Clique no link a seguir ou cole-o no seu navegador:
   [Google Colab - Projeto AgilStore](https://colab.research.google.com/drive/1D-cQSbGhKweGlhUGiPmkPYdFw1v0yOt7?usp=sharing)

2. **Importe o projeto no Colab:**
   No Google Colab, clique em `Arquivo` > `Abrir notebook`. Na aba `GitHub`, cole o link do repositório GitHub do projeto (ou carregue os arquivos diretamente, se necessário).

3. **Instale a biblioteca `tabulate`:**
   No Colab, você pode instalar a biblioteca `tabulate` diretamente no ambiente com o comando abaixo. Ele já estará em amostra e no gatilho para poder instalar. Execute a célula que aparecer indicando. (pura precaução).

4. **Execute o código:**
   Depois de carregar o projeto e instalar as dependências, basta executar as células de código clicando no botão de play ao lado de cada célula.

Com isso, o projeto estará rodando no Google Colab e você poderá interagir com ele diretamente no ambiente da web, sem a necessidade de baixar ou clonar o projeto em sua máquina!

---
