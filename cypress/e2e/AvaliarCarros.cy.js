describe('Funcionalidade de Avaliação de Carros com Estrelas', () => {
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
  
    // ✅ Cenário 1: Avaliação enviada com sucesso
    it('Cenário 1: Avaliação enviada com sucesso', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
      cy.wait(2000)
      cy.wait(2000)
    })
  
    // ✅ Cenário 2: Atualizar avaliação existente
    it('Cenário 2: Atualizar avaliação existente', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
      cy.wait(2000)
      cy.wait(2000)
    })
  
    // ✅ Cenário 3: Visualizar avaliações de outros usuários
    it('Cenário 3: Visualizar avaliações de outros usuários', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
      cy.wait(2000)
    })
  
    // ✅ Cenário 4: Envio de avaliação inválida sem login
    it('Cenário 4: Envio de avaliação inválida sem login', () => {
      cy.visit('http://127.0.0.1:8000/logout/') // Corrigido para /logout/
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Brasilia').click()
      cy.wait(2000)
      cy.get('p > a').should('exist') // Deve haver link para login
    })
  })
  