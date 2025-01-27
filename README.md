# Entrega capacitação - Controle de Despesas Pessoais

## Mudanças Principais feitas no Backend

- Mudança de appraiser para user no modelo de usuário
- Remoção do modelo de diretor
- Mudança dos dados do usuário
- Troca de SendGrid para Gmail para envio de e-mails
- Arquivo env agora possui os seguintes campos: 
    - `MONGO_USER` - Usuário do MongoDB
    - `MONGO_PWD` - Senha do MongoDB
    - `FERNET_SECRET_KEY` - Chave de criptografia
    - `USER_JWT_SECRET` - Chave de criptografia do JWT
    - `GMAIL_PASSWORD` - Senha do Gmail

## Funcionalidades Implementadas no Backend

### Autenticação
- Já estava implementada na aplicação, porém foi necessário fazer algumas alterações, como por exemplo no modelo do usuário
- Implementação de uma rota de logout

#### Visualização principal - Apenas dados, quem faz o gráfico nesse caso é o front
- Gráfico de Despesas por Categoria
- Gráfico de Despesas x Receita Total
- Gráfico de Saldo Mensal
- Gráfico de Orçamento x Despesa por Categoria

### Despesas e Receitas - Denominado "Finance"
- Cadastro de receitas e despesas
- Listagem de receitas e despesas
- Edição de receitas e despesas
- Exclusão de receitas e despesas

### Orçamentos
- Criação de orçamentos
- Listagem de orçamentos
- Exclusão de orçamentos

### Histórico de transações
- Listagem de transações (despesas)
- Filtro de transações por data
- Filtro de transações por categoria
- Filtro de transações por descrição