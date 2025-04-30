describe('Testes de busca e filtragem de carros', () => {

    it('Cenário 1: Busca com resultados corretos de modelo', () => {
        cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      
        // Preenche o campo de busca com o modelo
        cy.get('input[name="search"]').type('Teste')
      
        // Clica no botão de busca
        cy.get('.search-container > button').click()
      
        // Verifica se os resultados contêm "Modelo X"
        cy.get('.car-card').each(($card) => {
          cy.wrap($card).should('contain.text', 'Teste')
        })
      })
      
  
    // Cenário 2: Ordenação por menor preço
    it('Cenário 2: Busca com resultados corretos de marca', () => {
        cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      
        // Preenche o campo de busca com a marca
        cy.get('input[name="search"]').type('BYD')
      
        // Clica no botão de busca
        cy.get('.search-container > button').click()
      
        // Verifica se os resultados contêm "Marca Y"
        cy.get('.car-card').each(($card) => {
          cy.wrap($card).should('contain.text', 'BYD')
        })
      })
      
  
    // Cenário 3: Busca com filtros incompatíveis
    it('Cenário 3: Busca com filtros incompatíveis', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
  
      // Preenche o campo de busca com um termo impossível de encontrar
      cy.get('input[name="search"]').type('Modelo Inexistente')
  
      // Clica no botão de busca
      cy.get('.search-container > button').click()
  
      // Verifica se nenhum carro foi encontrado
      cy.get('.car-card').should('have.length', 0)
      cy.contains('Nenhum carro encontrado').should('be.visible')
    })
  
  })
  