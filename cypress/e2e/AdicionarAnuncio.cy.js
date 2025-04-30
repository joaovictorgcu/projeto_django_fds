describe('Fluxo completo de registro, login, criação e edição de anúncio.', () => {
  const timestamp = Date.now();
  const username = `kk`;
  const senha = '123';

  it('Cenário Positivo 1: Registra novo usuário, faz login e cria carro com dados válidos', () => {
    // 1. Registro
    cy.visit('http://127.0.0.1:8000/registro/');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password1"]').type(senha);
    cy.get('input[name="password2"]').type(senha);
    cy.contains('button', 'Registrar').click();

    // 2. Login após registro
    cy.url().should('include', '/login/?from=register');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(senha);
    cy.contains('button', 'Entrar').click();

    // 3. Criação de carro
    cy.url().should('include', '/interacoes/carros');
    cy.contains('Novo Carro').click();

    cy.url().should('include', '/interacoes/novo-carro');
    cy.get('input[name="model"]').type(`Brasilia`);
    cy.get('select[name="brand"]').select('BYD');
    cy.get('input[name="factory_year"]').type('2022');
    cy.get('input[name="model_year"]').type('2023');
    cy.get('input[name="km"]').type('15000');
    cy.get('input[name="value"]').type('25000');

    // 4. Seleção de imagem para upload
    cy.get('input[type="file"]').selectFile('cypress/fixtures/brasilia_50eX28r.webp');  // Caminho correto

    // 5. Submissão do formulário
    cy.contains('button', 'Registrar').click();
  });

  it('Cenário Negativo: Erro ao tentar cadastrar carro com campos obrigatórios faltando', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(senha);
    cy.contains('button', 'Entrar').click();

    cy.contains('Novo Carro').click();
    cy.url().should('include', '/interacoes/novo-carro');

    cy.contains('button', 'Registrar').click();
    cy.url().should('include', '/interacoes/novo-carro');

    cy.get('input[name="model"]')
      .then(($input) => {
        $input[0].reportValidity();
      });
  });

  it('Cenário Positivo 2: Edita o anúncio recém-cadastrado e altera o valor', () => {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(senha);
    cy.contains('button', 'Entrar').click();

    // Clicar na página "Meus Anúncios"
    cy.get(':nth-child(5) > a').click();

    // Clicar no botão de editar
    cy.get('.btn-warning').first().click();
    cy.wait(2000);

    // Alterar o valor para 1010
    cy.get('#value').clear().type('1010');

    // Clicar no botão de salvar
    cy.get('.btn-save').click();

    // Verifica se redirecionou corretamente
    cy.url().should('include', '/meus-anuncios/');

    // Verifica se o valor alterado aparece na tela
    cy.contains(' R$ 1010,0');
  });
});
