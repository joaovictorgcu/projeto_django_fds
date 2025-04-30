// ✅ Cenário 1: Imagens carregadas corretamente
it('Cenário Positivo (1): Imagens carregadas corretamente', () => {
    // Acessar a listagem de carros
    cy.visit('http://127.0.0.1:8000/interacoes/carros/')
  
    // Verificar se cada card de carro tem uma imagem visível
    cy.get('.car-card img').each(($img) => {
      cy.wrap($img).should('be.visible')
      cy.wrap($img).should('have.attr', 'src').and('not.be.empty')
    })
  
    // Clicar em um carro específico para abrir a página de detalhes
    cy.contains('.car-card', 'BYD Brasilia').click()
  
  })
  
  
  // ✅ Cenário 2: Ampliar imagens para visualização detalhada
  it('Cenário Positivo (2): Imagens para visualização detalhada', () => {
    // Acessar a página de detalhes do carro
    cy.visit('http://127.0.0.1:8000/interacoes/carros/')
    cy.contains('.car-card', 'BYD Brasilia').click()
  
    // Clicar na imagem para ampliar (assumindo que ela abre em modal/fullscreen)
  
    // Verificar se o modal ou visualização ampliada foi exibido
  })
  
  
  // ❌ Cenário 4: Erro ao carregar imagens
  it('Cenário Negativo (3): Erro ao carregar imagem', () => {
    // Simula acesso a página com imagem quebrada
    // (Você pode ter uma imagem propositalmente com src errado para testes)
  
    cy.visit('http://127.0.0.1:8000/interacoes/carros/')
  
    // Verificar se aparece uma mensagem de erro ou placeholder para imagem quebrada
    cy.get('img').each(($img) => {
      const img = $img[0];
      if (!img.complete || img.naturalWidth === 0) {
        // Simula caso de falha e verifica se há um placeholder ou texto informando falha
        cy.wrap($img).parent().should('contain.text', 'imagem não disponível').or('contain.text', 'erro ao carregar')
      }
    })
  
    // Ou alternativa mais direta (caso tenha um elemento substituto para falhas):
    // cy.get('.image-error, .image-placeholder').should('exist')
  })
  