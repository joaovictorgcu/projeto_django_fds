describe('Testes de edição e exclusão de anúncios', () => {

    // Cenário 1: Edição de anúncio com sucesso
    // Cenário 1: Edição de anúncio com sucesso
    it('Cenário Positivo (1): Edição de anúncio com sucesso', () => {
    // Fazer login
        cy.visit('http://127.0.0.1:8000/login/')
        cy.get('input[name="username"]').type('jv')
        cy.get('input[name="password"]').type('123')
        cy.contains('button', 'Entrar').click()
  
    // Acessar a página "Meus Anúncios"
        cy.visit('http://127.0.0.1:8000/meus-anuncios/')
  
    // Clicar no botão de editar
        cy.get('.btn-warning').click()
        cy.wait(200)
  
    // Reescrever o valor no campo #value com 1010
        cy.get('#value').clear().type('1010')
  
    // Clicar no botão de salvar
        cy.get('.btn-save').click()
  
    // Esperar 5 segundos
        cy.wait(200)
  
    // Verificar se o valor foi atualizado
        cy.get('.car-card').should('contain.text', '1010')
  })
  
  // Cenário 2: Excluir anúncio com sucesso
  it('Cenário Positivo (2): Excluir anúncio com sucesso', () => {
    // Fazer login
    cy.visit('http://127.0.0.1:8000/login/')
    cy.get('input[name="username"]').type('jv')
    cy.get('input[name="password"]').type('123')
    cy.contains('button', 'Entrar').click()
  
    // Acessar a página "Meus Anúncios"
    cy.visit('http://127.0.0.1:8000/meus-anuncios/')
  
    // Clicar no botão de deletar
    cy.get('.btn-danger').click()
    cy.wait(2000)
    // Confirmar a exclusão
    cy.on('window:confirm', () => true)
  
    // Esperar 5 segundos
  })
  
  
    // Cenário 3: Tentativa de editar ou excluir anúncio sem estar logado
    it('Cenário Negativo(3): Tentativa de editar ou excluir anúncio sem estar logado', () => {
      // 1. Acessa a página de detalhes do carro sem estar logado
      cy.visit('http://127.0.0.1:8000/interacoes/carros/')
      cy.contains('.car-card', 'BYD Cinquentinha').click()
  
      // 2. Tenta acessar o botão de edição
      cy.get('.edit-car-btn').should('not.exist') // O botão de edição não deve aparecer
  
      // 3. Tenta acessar o botão de exclusão
      cy.get('.delete-car-btn').should('not.exist') // O botão de exclusão não deve aparecer
  
      // 4. Verifica se o botão de login está presente
      cy.get('p > a').should('exist'); // Verifica se o link de login está disponível, pois o usuário não está logado
    })
  
  })
  