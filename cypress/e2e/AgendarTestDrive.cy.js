describe('Fluxo completo de agendamento de test drive', () => {
  const timestamp = Date.now();
  const username = `usuario_teste_${timestamp}`;
  const senha = '123';

  before(() => {
    // Criação do usuário
    cy.visit('http://127.0.0.1:8000/registro/');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password1"]').type(senha);
    cy.get('input[name="password2"]').type(senha);
    cy.contains('button', 'Registrar').click();
    cy.url().should('include', '/login/?from=register');
  });

  beforeEach(() => {
    // Login manual antes de cada cenário que precisa de autenticação
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(senha);
    cy.contains('button', 'Entrar').click();
  });

  it('Cenários 1 e 2: Exibe botão de agendamento e realiza o agendamento de test drive', () => {
    cy.visit('http://127.0.0.1:8000/interacoes/carros/');
    cy.contains('.car-card', 'SSsaa').click();

    // Verifica se o botão de agendar está visível
    cy.get('.agendar-container > form > .avaliar-btn').should('exist');

    // Realiza o agendamento clicando no campo com atributo data-top e preenchendo a data
    cy.get('#data_visita').click().type('2025-05-29');
    cy.get('.agendar-container').click();

    // Verifica redirecionamento ou outra confirmação
    cy.url().should('not.include', '/interacoes/carros/');
  });

  it('Cenário 3: Impedir agendamento sem login', () => {
    cy.visit('http://127.0.0.1:8000/logout/');
    cy.visit('http://127.0.0.1:8000/interacoes/carros/');
    cy.contains('.car-card', 'SSsaa').click();

    cy.contains('Entre para favoritar, avaliar ou agendar visita.').should('exist');
  });
});
