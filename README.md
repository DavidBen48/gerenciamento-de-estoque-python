# **Desafio - Aceleradora Ágil**
### Tema: Gerenciamento de Produtos para a Loja AgilStore

Enunciado: A AgilStore é uma pequena loja de eletrônicos que recentemente expandiu seu catálogo de produtos para incluir uma variedade maior de itens, desde smartphones e laptops até acessórios como cabos, carregadores e fones de ouvido. Com o aumento do número de produtos e a diversidade das categorias, a equipe de gerenciamento percebeu a necessidade de otimizar o controle do inventário para garantir que os produtos estejam sempre disponíveis para os clientes e que os níveis de estoque sejam mantidos de forma eficiente.
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
ID
Nome do Produto
Categoria
Quantidade em Estoque
Preço
Permitir opções de filtragem por categoria ou ordenação por nome, quantidade ou preço (opcional).
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

Aqui está uma explicação detalhada para o README, conforme solicitado:

---

## Como rodar o projeto em sua máquina?

### 1. Clonando o projeto no CMD e rodando o mesmo no próprio CMD:

Para rodar o projeto diretamente no seu CMD (Prompt de Comando), siga os passos abaixo:

1. **Abra o CMD (Prompt de Comando):**
   - No Windows, pressione `Windows + R`, digite `cmd` e pressione Enter.

2. **Clone o repositório do projeto:**
   Execute o seguinte comando no CMD para clonar o repositório para a sua máquina (certifique-se de que o Git está instalado):
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```
   Substitua `https://github.com/usuario/repositorio.git` pela URL correta do repositório que você deseja clonar.

3. **Navegue até a pasta do projeto:**
   Após o repositório ser clonado, entre na pasta do projeto com o comando:
   ```bash
   cd nome-do-repositorio
   ```

4. **Instale a biblioteca `tabulate`:**
   Caso não tenha a biblioteca `tabulate` instalada, você pode instalá-la com o comando:
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
   git clone https://github.com/usuario/repositorio.git
   ```

3. **Navegue até a pasta do projeto:**
   Entre na pasta do projeto com o comando:
   ```bash
   cd nome-do-repositorio
   ```

4. **Abra o Visual Studio Code:**
   Com o projeto já clonado, basta executar o comando para abrir o projeto no VSC:
   ```bash
   code .
   ```

5. **Instale a biblioteca `tabulate`:**
   Caso não tenha a biblioteca `tabulate` instalada, abra o terminal integrado no VSC (pressionando `Ctrl + ``) e execute:
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
   No Colab, você pode instalar a biblioteca `tabulate` diretamente no ambiente com o comando abaixo. Execute a célula de código para instalar:
   ```python
   !pip install tabulate
   ```

4. **Execute o código:**
   Depois de carregar o projeto e instalar as dependências, basta executar as células de código clicando no botão de play ao lado de cada célula.

Com isso, o projeto estará rodando no Google Colab e você poderá interagir com ele diretamente no ambiente da web!

---

Agora, com essas opções, você pode rodar o projeto de diferentes maneiras, seja no CMD, no Visual Studio Code, ou no Google Colab. Se tiver algum problema, não hesite em consultar os tutoriais ou procurar mais ajuda!

---
