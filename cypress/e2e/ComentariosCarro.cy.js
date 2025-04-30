describe('Funcionalidade de Comentários em Carros', () => {
    const username = `user_${Date.now()}`
    const senha = '123'
  
    before(() => {
      // Registrar novo usuário
      cy.visit('http://127.0.0.1:8000/registro/')
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password1"]').type(senha)
      cy.get('input[name="password2"]').type(senha)
      cy.contains('button', 'Registrar').click()
  
      // Login após registro
      cy.url().should('include', '/login/?from=register')
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password"]').type(senha)
      cy.contains('button', 'Entrar').click()
    })
  
    beforeEach(() => {
      // Login antes de cada cenário (menos o último que testa sem login)
      if (!Cypress.currentTest.title.includes('sem login')) {
        cy.visit('http://127.0.0.1:8000/login/')
        cy.get('input[name="username"]').type(username)
        cy.get('input[name="password"]').type(senha)
        cy.contains('button', 'Entrar').click()
      }
    })
  
    // ✅ Cenário 1: Enviar comentário com sucesso
    it('Cenário 1: Enviar comentário com sucesso', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
      cy.wait(2000)
      
      // Escrever o comentário
      cy.get('textarea').type('Teste Automatizado - Entrega 1 - SR2')
      
      // Enviar o comentário
      cy.get('#comentario-form > button').click()
      
      // Verificar se o comentário foi publicado
      cy.contains('Teste Automatizado - Entrega 1 - SR2').should('exist')
    })
  
    // ✅ Cenário 2: Visualizar comentários de outros usuários
    it('Cenário 2: Visualizar comentários de outros usuários', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
      cy.wait(2000)
  
      // Verificar se o comentário do Cenário 1 está visível
      cy.contains('Teste Automatizado - Entrega 1 - SR2').should('exist')
    })
  
    // ❌ Cenário 4: Tentar comentar sem estar logado
    it('Cenário 4: Tentar comentar sem estar logado', () => {
      cy.visit('http://127.0.0.1:8000/logout/') // Logout para testar sem login
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
      cy.wait(2000)
  
      // Verificar se existe o link de login para solicitar que o usuário faça login
      cy.get('p > a').should('exist') // Verifica o botão de login
    })
  })
  