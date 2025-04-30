describe('Testes de favoritar carros', () => {
  
    const username = 'usuario_' + new Date().toISOString().replace(/[-:.]/g, ''); // Nome de usuário baseado na hora
    const senha = 'senha123'; // A mesma senha será reutilizada para login
  
    // Cenário 1: Adicionar carro aos favoritos com sucesso
    it('Cenário Positivo (1): Adicionar carro aos favoritos com sucesso', () => {
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
  
      // 4. Clica no botão de favoritar
      cy.get('.favorito-btn').click()
  
    })
  
    // Cenário 2: Visualizar lista de favoritos
    it('Cenário Positivo (2): Visualizar lista de favoritos', () => {
      // 1. Login do usuário
      cy.visit('http://127.0.0.1:8000/login/')
      cy.get('input[name="username"]').type(username)
      cy.get('input[name="password"]').type(senha)
      cy.contains('button', 'Entrar').click()
  
      // 2. Acessa a página de favoritos
      cy.visit('http://127.0.0.1:8000/interacoes/favoritos/')
  
      // 3. Verifica se o carro favoritado aparece na lista
      cy.contains('BYD Brasilia').should('exist')
    })
  
    // Cenário 4: Tentativa de favoritar sem estar logado
    it('Cenário Negativo (3): Tentativa de favoritar sem estar logado', () => {
        // 1. Acessa a página de carros
        cy.visit('http://127.0.0.1:8000/interacoes/carros/')
        cy.contains('.car-card', 'BYD Brasilia').click()
    
        // 2. Verifica se existe o botão de login
        cy.get('p > a').should('exist')
    })
  })
  