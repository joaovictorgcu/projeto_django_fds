describe('Gerenciamento de Chats - Acesso e Visualização', () => {
  const adminUsername = 'jv';
  const adminSenha = '123';

  const userTimestamp = Date.now();
  const userUsername = `usuario_comum_${userTimestamp}`;
  const userSenha = '123';

  before(() => {
    // Criação de usuário comum
    cy.visit('http://127.0.0.1:8000/registro/');
    cy.get('input[name="username"]').type(userUsername);
    cy.get('input[name="password1"]').type(userSenha);
    cy.get('input[name="password2"]').type(userSenha);
    cy.contains('button', 'Registrar').click();
    cy.url().should('include', '/login/?from=register');
  });

  function login(username, senha) {
    cy.visit('http://127.0.0.1:8000/login/');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(senha);
    cy.contains('button', 'Entrar').click();
    cy.url().should('not.include', '/login');
  }

  it('Cenário 1: Visualizar todos os chats ativos (admin)', () => {
    login(adminUsername, adminSenha);

    cy.visit('http://127.0.0.1:8000/interacoes/todas-mensagens/');

    cy.contains('Aviso: Você está visualizando esta página como administrador.').should('exist');
  });

  it('Cenário 2: Acessar o conteúdo de um chat específico (admin)', () => {
    login(adminUsername, adminSenha);

    cy.visit('http://127.0.0.1:8000/interacoes/todas-mensagens/');

    // Clicar no botão do primeiro chat da lista para abrir o chat
    cy.get(':nth-child(1) > .btn-chat').click();

    // Opcional: validar que o chat foi aberto, se quiser
    // cy.get('.chat-historico').should('exist');
    // cy.get('.mensagem').should('have.length.at.least', 1);
  });

  it('Cenário 3: Tentativa de acesso por usuário comum', () => {
    login(userUsername, userSenha);

    cy.visit('http://127.0.0.1:8000/interacoes/todas-mensagens/');

    cy.contains('Você não tem chats.').should('exist');
  });
});
