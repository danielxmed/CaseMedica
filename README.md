# **CaseMedica**

## **Índice**

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instruções de Instalação](#instruções-de-instalação)
- [Como Usar a Aplicação](#como-usar-a-aplicação)
  - [Registro e Login](#registro-e-login)
  - [Editar Perfil](#editar-perfil)
  - [Seguir Usuários](#seguir-usuários)
  - [Publicar Casos Clínicos](#publicar-casos-clínicos)
  - [Interagir com Casos Clínicos](#interagir-com-casos-clínicos)
  - [Mural Personalizado](#mural-personalizado)
- [Contribuindo com o Projeto](#contribuindo-com-o-projeto)
- [Licença](#licença)
- [Contato](#contato)
- [Agradecimentos](#agradecimentos)

---

## **Descrição do Projeto**

O **CaseMedica** é uma plataforma web destinada a profissionais e estudantes da área de saúde, com o objetivo de promover a colaboração e o compartilhamento de conhecimento por meio de casos clínicos. A plataforma permite que os usuários publiquem casos, sigam outros profissionais, interajam por meio de curtidas e comentários, e mantenham-se atualizados com as novidades na área médica.

## **Funcionalidades Principais**

- **Registro e Autenticação de Usuários**: Criação de contas e login seguro.
- **Perfis Personalizados**: Cada usuário possui um perfil com informações profissionais e pode ser seguido por outros usuários.
- **Sistema de Seguidores**: Possibilidade de seguir e ser seguido por outros profissionais.
- **Publicação de Casos Clínicos**: Criação, edição e exclusão de casos clínicos, com suporte para upload de imagens com legendas.
- **Interações Sociais**:
  - **Curtidas**: Demonstrar apreciação por casos clínicos.
  - **Comentários**: Participar de discussões e trocar insights sobre os casos.
- **Mural Personalizado**: Feed com os casos clínicos publicados pelos usuários seguidos.
- **Busca de Usuários**: Ferramenta para encontrar e conectar-se com outros profissionais.

## **Tecnologias Utilizadas**

- **Backend**: Django 3.x (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Banco de Dados**: SQLite (ambiente de desenvolvimento)
- **Outras Bibliotecas**:
  - **Pillow**: Manipulação de imagens.
  - **Django Crispy Forms**: Estilização de formulários com Bootstrap.
  - **Bootstrap Icons**: Ícones para melhorar a interface do usuário.

## **Pré-requisitos**

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes do Python)
- **Virtualenv** (recomendado para criação de ambiente virtual)

## **Instruções de Instalação**

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/danielxmed/CaseMedica
   cd casemedica
   ```

2. **Criar um Ambiente Virtual**

   ```bash
   python -m venv venv
   ```

   Ativar o ambiente virtual:

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Linux/MacOS**:

     ```bash
     source venv/bin/activate
     ```

3. **Instalar as Dependências**

   ```bash
   pip install -r requirements.txt
   ```

   **Nota**: Certifique-se de que o arquivo `requirements.txt` contém todas as dependências necessárias.

4. **Configurar as Variáveis de Ambiente**

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes configurações:

   ```env
   DEBUG=True
   SECRET_KEY='sua-chave-secreta'
   ```

   **Nota**: Substitua `'sua-chave-secreta'` por uma chave secreta segura.

5. **Aplicar Migrações do Banco de Dados**

   ```bash
   python manage.py migrate
   ```

6. **Criar um Superusuário (Opcional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Executar o Servidor de Desenvolvimento**

   ```bash
   python manage.py runserver
   ```

   Acesse a aplicação em `http://127.0.0.1:8000/`.

## **Como Usar a Aplicação**

### **Registro e Login**

- **Registrar-se**: Acesse `http://127.0.0.1:8000/usuarios/signup/` para criar uma nova conta.
- **Login**: Acesse `http://127.0.0.1:8000/usuarios/login/` para entrar na sua conta.

### **Editar Perfil**

- Após o login, clique no seu nome de usuário no canto superior direito e selecione **"Meu Perfil"**.
- Clique em **"Editar Perfil"** para adicionar ou atualizar suas informações profissionais, como formação, afiliações e especialidades.

### **Seguir Usuários**

- Utilize a ferramenta de busca em `http://127.0.0.1:8000/usuarios/buscar/` para encontrar outros profissionais.
- Nos resultados da busca, clique no nome do usuário para acessar seu perfil e, em seguida, clique em **"Seguir"**.

### **Publicar Casos Clínicos**

- No menu principal, clique em **"Novo Caso Clínico"** ou acesse `http://127.0.0.1:8000/casos/caso/novo/`.
- Preencha os campos obrigatórios, adicione uma imagem com legenda (opcional) e clique em **"Salvar"**.

### **Interagir com Casos Clínicos**

- **Curtir**: No mural ou na página de detalhes do caso, clique em **"Curtir"** para demonstrar interesse.
- **Comentar**: Na página de detalhes do caso, desça até a seção de comentários, escreva sua mensagem e clique em **"Enviar Comentário"**.

### **Mural Personalizado**

- Acesse o mural em `http://127.0.0.1:8000/casos/mural/` para ver os casos clínicos publicados pelos usuários que você segue.

## **Contribuindo com o Projeto**

Contribuições são bem-vindas! Para contribuir:

1. **Faça um Fork do Repositório**

   Clique em **"Fork"** no canto superior direito da página do GitHub.

2. **Clone o Seu Fork**

   ```bash
   git clone https://github.com/seu-usuario/casemedica.git
   cd casemedica
   ```

3. **Crie uma Branch para Sua Funcionalidade ou Correção**

   ```bash
   git checkout -b minha-nova-funcionalidade
   ```

4. **Faça as Alterações Desejadas e Commit**

   ```bash
   git add .
   git commit -m "Adiciona nova funcionalidade X"
   ```

5. **Envie as Alterações para o Seu Fork**

   ```bash
   git push origin minha-nova-funcionalidade
   ```

6. **Abra um Pull Request**

   No repositório original, clique em **"Pull Requests"** e em seguida em **"New Pull Request"**.

## **Licença**

Este projeto está licenciado sob a licença MIT.

## **Contato**

- **Desenvolvedor**: Daniel Nobrega Medeiros
- **E-mail**: danielnobregamedeiros@gmail.com
- **LinkedIn**: [Daniel Nobrega] https://www.linkedin.com/in/daniel-nobrega-187272124/

## **Agradecimentos**

Agradecemos a todos os colaboradores e membros da comunidade que contribuíram para o desenvolvimento do **CaseMedica**.

