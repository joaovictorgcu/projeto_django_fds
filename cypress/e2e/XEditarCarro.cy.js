describe('Fluxo completo de registro, login, criação e edição de anúncio.', () => {
    const timestamp = Date.now();
    const username = `usuario_teste_${timestamp}`;
    const senha = '123';

    it('Cenário Positivo 1: Registra novo usuário, faz login, cria carro e edita anúncio', () => {
      // 1. Registro
      cy.visit('http://127.0.0.1:8000/registro/');
      cy.get('input[name="username"]').type(username);
      cy.get('input[name="password1"]').type(senha);
      cy.get('input[name="password2"]').type(senha);
      cy.contains('button', 'Registrar').click();

      // 2. Login após registro
      cy.url().should('include', '/login/?from=register');
      cy.get('input[name="username"]').type(username);
      cy.get('input[name="password"]').type(senha);
      cy.contains('button', 'Entrar').click();

      // 3. Criação de carro
      cy.url().should('include', '/interacoes/carros');
      cy.contains('Novo Carro').click();

      cy.url().should('include', '/interacoes/novo-carro');
      cy.get('input[name="model"]').type(`Fusca`);
      cy.get('select[name="brand"]').select('BYD');
      cy.get('input[name="factory_year"]').type('2022');
      cy.get('input[name="model_year"]').type('2023');
      cy.get('input[name="km"]').type('15000');
      cy.get('input[name="value"]').type('25000');

      // 4. Seleção de imagem para upload
      cy.get('input[type="file"]').selectFile('cypress/fixtures/brasilia_50eX28r.webp');  // Caminho correto

      // 5. Submissão do formulário
      cy.contains('button', 'Registrar').click();

      // 6. Edição do anúncio recém-criado
      cy.visit('http://127.0.0.1:8000/meus-anuncios/');  // Garantir que está na página correta
      cy.get('.btn-warning').first().click();  // Seleciona o primeiro botão de editar

      // Alterar o valor para 1010
      cy.get('#value').clear().type('1010');
      cy.get('.btn-save').click();

      // Verifica se o valor alterado aparece na tela
      cy.contains(' R$ 1010,0');
    }); 
    it('Cenário Negativo(3): Tentativa de editar ou excluir anúncio sem estar logado', () => {
        // 1. Acessa a página de detalhes do carro sem estar logado
        cy.visit('http://127.0.0.1:8000/interacoes/carros/');
        cy.contains('.car-card', 'Fusca').click();
  
        // 2. Tenta acessar o botão de edição
        cy.get('.edit-car-btn').should('not.exist'); // O botão de edição não deve aparecer
  
        // 3. Tenta acessar o botão de exclusão
        cy.get('.delete-car-btn').should('not.exist'); // O botão de exclusão não deve aparecer
  
        // 4. Verifica se o botão de login está presente
        cy.get('p > a').should('exist'); // Verifica se o link de login está disponível
      });

    it('Cenário Positivo 2: Excluir anúncio com sucesso', () => {
      cy.visit('http://127.0.0.1:8000/login/');
      cy.get('input[name="username"]').type(username);
      cy.get('input[name="password"]').type(senha);
      cy.contains('button', 'Entrar').click();

      // Acessar a página "Meus Anúncios"
      cy.visit('http://127.0.0.1:8000/meus-anuncios/');

      // Clicar no botão de deletar
      cy.get('.btn-danger').click();
      cy.wait(2000);

      // Confirmar a exclusão
      cy.on('window:confirm', () => true);

      // Verificar se o anúncio foi excluído
      cy.url().should('include', '/meus-anuncios/');
      cy.get('.car-card').should('not.exist');
    });
});
