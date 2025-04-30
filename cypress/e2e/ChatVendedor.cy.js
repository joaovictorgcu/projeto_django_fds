describe('Testes de chat para comprador e vendedor', () => {
  
    const username = 'usuario_' + new Date().toISOString().replace(/[-:.]/g, ''); // Nome de usuário baseado na hora
    const senha = 'senha123'; // A mesma senha será reutilizada para login
  
    // Cenário 1: Envio de mensagem com sucesso
    it('Cenário Positivo (1): Envio de mensagem com sucesso', () => {
      // 1. Registro do usuário
      cy.visit('http://127.0.0.1:8000/registro/')
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password1"]').type(senha)
      cy.get('input[name="password2"]').type(senha)
      cy.contains('button', 'Registrar').click()
  
      // 2. Login após registro
      cy.url().should('include', '/login/?from=register')
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password"]').type(senha)
      cy.contains('button', 'Entrar').click()
  
      // 3. Acessa a página de carros
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
  
      // 4. Iniciar conversa com o vendedor
      cy.get('.mensagem-btn').click();  // Clica no botão de iniciar conversa
      cy.wait(2000);  // Aguarda o carregamento do chat
  
      // 5. Digitar mensagem no textarea
      cy.get('textarea').type('Teste automatizado Entrega 1 - Sprint 2');
  
      // 6. Clicar em "Enviar"
      cy.get('.chat-detail-container > form > button').click();
  
      // 7. Verifica se a mensagem foi enviada e aparece na conversa
      cy.contains('Teste automatizado Entrega 1 - Sprint 2').should('exist');
    });
  
    // Cenário 2: Histórico de conversas salvo
    it('Cenário Positivo(2): Histórico de conversas salvo', () => {
      // 1. Login do usuário
      cy.visit('http://127.0.0.1:8000/login/')
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password"]').type(senha)
      cy.contains('button', 'Entrar').click()
  
      // 2. Acessa a página de carros
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
  
      // 3. Iniciar conversa com o vendedor
      cy.get('.mensagem-btn').click();  // Clica no botão de iniciar conversa
      cy.wait(2000);  // Aguarda o carregamento do chat
  
      // 4. Digitar mensagem no textarea e enviar
      cy.get('textarea').type('Mensagem de teste para o vendedor');
      cy.get('.chat-detail-container > form > button').click();
  
      // 5. Fecha e reabre o chat
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click();
      cy.get('.mensagem-btn').click();
  
      // 6. Verifica se a mensagem anterior ainda está visível no histórico
      cy.contains('Mensagem de teste para o vendedor').should('exist');
    });
  
    // Cenário 4: Envio de mensagem sem estar logado
    // Cenário 4: Envio de mensagem sem estar logado
    it('Cenário Negativo(3): Envio de mensagem sem estar logado', () => {
    // 1. Acessa a página de carros sem estar logado
        cy.visit('http://127.0.0.1:8000/interacoes/carros/')
        cy.contains('.car-card', 'BYD Brasilia').click()
  
    // 3. Verifica se o botão de login está presente na página
        cy.get('p > a').should('exist');
    });
  
  });
  