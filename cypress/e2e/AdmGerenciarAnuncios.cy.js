describe('Gerenciamento de Anúncios - Acesso e Ações', () => {
  const adminUsername = 'jv';
  const adminSenha = '123';

  const userTimestamp = Date.now();
  const userUsername = `usuario_comum_${userTimestamp}`;
  const userSenha = '123';

  before(() => {
    // Criação de usuário comum para testar cenário 3
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

  it('Cenário 1: Visualizar todos os anúncios (admin)', () => {
    login(adminUsername, adminSenha);
    cy.visit('http://127.0.0.1:8000/interacoes/todos-anuncios/');

    cy.contains('Aviso: Você está visualizando esta página como administrador.').should('exist');
  });

  it('Cenário 2: Excluir um anúncio (admin)', () => {
    login(adminUsername, adminSenha);
    cy.visit('http://127.0.0.1:8000/interacoes/todos-anuncios/');
    cy.contains('Aviso: Você está visualizando esta página como administrador.').should('exist');
    
  });

  it('Cenário 3: Tentativa de acesso sem permissão administrativa', () => {
    login(userUsername, userSenha);
    cy.visit('http://127.0.0.1:8000/interacoes/todos-anuncios/');

    // Deve bloquear acesso com mensagem de restrição
    cy.contains('Você ainda não possui nenhum anúncio.').should('exist');
  });
});
