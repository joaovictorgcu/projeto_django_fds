# Guia de Contribuição para o Projeto Match Auto

Seja bem-vindo(a) à comunidade de desenvolvimento do Match Auto! Agradecemos seu interesse em contribuir para este projeto, uma plataforma de compra e venda de carros desenvolvida com o framework Django. O Match Auto nasceu como um projeto acadêmico para a disciplina de Fundamentos de Desenvolvimento de Software na CESAR School (turma 2025.1) e tem como objetivo simplificar a conexão entre compradores e vendedores de veículos.

Este guia foi elaborado para orientar você sobre como pode colaborar conosco, seja adicionando novas funcionalidades, corrigindo bugs ou propondo melhorias. Antes de iniciar, recomendamos a leitura atenta deste documento para compreender nosso fluxo de trabalho e as melhores práticas adotadas pela equipe.

## Como Você Pode Contribuir?

Existem diversas maneiras de agregar valor ao Match Auto. Você pode implementar uma funcionalidade que ainda não existe, investigar e solucionar alguma das issues abertas no repositório (verifique a aba "Issues" para mais detalhes) ou refinar aspectos existentes da aplicação. Toda contribuição é valiosa e nos ajuda a aprimorar a experiência dos usuários.

## Preparando Seu Ambiente de Contribuição

Para garantir um processo de contribuição organizado e sem conflitos com o código principal, seguimos um fluxo baseado em forks e branches.

Primeiramente, realize um "Fork" do repositório `joaovictorgcu/projeto_django_fds`. Isso criará uma cópia completa do projeto em sua própria conta do GitHub, permitindo que você trabalhe livremente sem afetar o repositório original. O botão "Fork" geralmente se encontra no canto superior direito da página do repositório.

Após criar o fork, clone o seu repositório copiado para a sua máquina local. Utilize o comando `git clone` substituindo `SuaConta` pelo seu nome de usuário no GitHub:

```bash
git clone https://github.com/SuaConta/projeto_django_fds.git
```

Com o repositório clonado, navegue até o diretório do projeto e crie uma nova branch específica para a sua contribuição. É fundamental trabalhar em uma branch separada para manter o histórico organizado e facilitar a integração das suas mudanças. Use um nome descritivo para a branch, como `feature/nova-tela-login` ou `fix/correcao-bug-cadastro`:

```bash
git checkout -b nome-da-sua-branch
```

## Configurando o Ambiente de Desenvolvimento Local

Com o repositório e a branch prontos, o próximo passo é configurar o ambiente de desenvolvimento em sua máquina.

Acesse o diretório raiz do projeto que você clonou:

```bash
cd projeto_django_fds
```

Recomendamos fortemente o uso de ambientes virtuais para isolar as dependências do projeto. Crie um ambiente virtual utilizando o módulo `venv` do Python:

```bash
python -m venv venv
```

Ative o ambiente virtual recém-criado. Os comandos variam ligeiramente dependendo do seu sistema operacional:

*   **Windows:** `venv\Scripts\activate`
*   **Linux/Mac:** `source venv/bin/activate`

Com o ambiente virtual ativo, instale todas as dependências necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

O Django utiliza migrações para gerenciar o esquema do banco de dados. Aplique as migrações para configurar o banco de dados local (por padrão, o projeto utiliza SQLite para desenvolvimento):

```bash
python manage.py migrate
```

Finalmente, inicie o servidor de desenvolvimento do Django para visualizar a aplicação em seu navegador:

```bash
python manage.py runserver
```

Agora você está pronto para começar a codificar suas contribuições!

## Garantindo a Qualidade: Executando Testes

Para assegurar que suas alterações não introduzam regressões ou quebrem funcionalidades existentes, incentivamos a execução dos testes automatizados. O projeto utiliza Cypress para testes end-to-end. Caso sua contribuição envolva novas funcionalidades, considere adicionar novos testes para cobri-las.

Para executar os testes com Cypress, siga estes passos:

1.  Certifique-se de ter o [Node.js](https://nodejs.org/) instalado em sua máquina (recomendamos a versão LTS).
2.  Instale as dependências do Node.js listadas no `package.json` (se houver um e for necessário para os testes):
    ```bash
    npm ci
    ```
3.  Execute os testes Cypress:
    ```bash
    npx cypress run
    ```

A execução dos testes ajuda a manter a estabilidade e a qualidade do código do Match Auto.

## Submetendo Suas Alterações: O Pull Request

Após concluir suas modificações e testá-las adequadamente, é hora de submetê-las para revisão através de um Pull Request (PR).

Faça o commit das suas alterações na sua branch local com mensagens claras e descritivas. Envie a sua branch para o seu repositório forkado no GitHub:

```bash
git add .
git commit -m "Descrição concisa das suas alterações"
git push origin nome-da-sua-branch
```

Acesse a página do seu fork no GitHub. Você verá uma notificação sugerindo a criação de um Pull Request para a branch que você acabou de enviar. Clique nela ou navegue até a aba "Pull requests" e clique em "New pull request".

Certifique-se de que a base branch seja a `main` do repositório original (`joaovictorgcu/projeto_django_fds`) e a head branch seja a sua branch de contribuição no seu fork.

Escreva um título claro e uma descrição detalhada para o seu Pull Request, explicando o propósito das suas alterações, as decisões tomadas e, se aplicável, referenciando a issue que está sendo resolvida. Quanto mais contexto você fornecer, mais fácil será para a equipe revisar seu código.

Finalmente, clique em "Create pull request".

## Processo de Revisão e Agradecimentos

A equipe do Match Auto revisará seu Pull Request assim que possível. Poderemos fazer perguntas, sugerir modificações ou solicitar ajustes para garantir que a contribuição esteja alinhada com os padrões e objetivos do projeto. A comunicação será feita através dos comentários no próprio Pull Request.

Queremos expressar nossa profunda gratidão por sua disposição em contribuir com o Match Auto. Cada linha de código, correção de bug ou nova ideia impulsiona o projeto e nos ajuda a construir uma ferramenta cada vez melhor para a comunidade.

Estamos entusiasmados para ver suas contribuições e trabalhar juntos na evolução desta plataforma.

## Contato

Caso tenha dúvidas durante o processo de contribuição ou precise de ajuda, não hesite em entrar em contato com a equipe. Você pode abrir uma issue no repositório ou contatar diretamente os membros:

*   Pablo José Pellegrino Cintra ([@PabloJPCintra](https://github.com/PabloJPCintra)) - pjpc@cesar.school
*   Raul Vitor Ferraz Silva ([@raulferraz85](https://github.com/raulferraz85)) - rvfs@cesar.school
*   João Victor Guimarães Cavalcanti Uchôa ([@joaovictorgcu](https://github.com/joaovictorgcu)) - jvgcu@cesar.school
*   Luís Eduardo Bérard de Paiva Moura Rodrigues ([@luisedu975](https://github.com/luisedu975)) - lebpmr@cesar.school

Obrigado por fazer parte do desenvolvimento do Match Auto!