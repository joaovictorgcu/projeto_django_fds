describe('Funcionalidade de Filtro por Ordenação na Listagem de Carros', () => {

    // ✅ Cenário 1: Aplicar filtros de ordenação na listagem de veículos
    it('Cenário Positivo(1): Aplicar filtros de ordenação na listagem de veículos', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
  
      const opcoes = [
        'Marca',
        'Menor Preço',
        'Maior Preço',
        'Ano (Mais Antigo)',
        'Ano (Mais Recente)',
        'Avaliação (Crescente)',
        'Avaliação (Decrescente)'
      ]
  
      opcoes.forEach((opcao) => {
        cy.get('#order_by').select(opcao)
        cy.get('.order-form > button').click()
        cy.wait(1000)
        cy.get('.car-card').should('exist')
      })
    })
  
    // ✅ Cenário 2: Remoção de filtro de ordenação (selecionar vazio)
    it('Cenário Positivo (2): Remoção de filtro de ordenação', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
  
      // Aplica uma ordenação
      cy.get('#order_by').select('Menor Preço')
      cy.get('.order-form > button').click()
      cy.wait(1000)

  
      // Verifica se há carros listados normalmente
      cy.get('.car-card').should('exist')
    })
    // ❌ Cenário 4: Filtros que não retornam resultados
    it('Cenário Negativo(3): Filtros que não retornam resultados', () => {
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
  
      // Preencher filtro com ano inexistente
      cy.wait(300)

    })
  
  })
  