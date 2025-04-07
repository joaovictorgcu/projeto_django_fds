# MATCH AUTO
- *O que é a Match Auto?*

A Match Auto é um site de compra e venda de carros pela internet. Você pode procurar veículos à venda, comparar preços, ver fotos e detalhes, tudo em um só lugar. Também é possível anunciar seu carro para revenda de forma fácil e rápida. Nosso objetivo é facilitar o processo de compra e venda de carros, conectando vendedores e compradores com segurança e praticidade.

# Links:
- *Jira:* https://gymstatsfds.atlassian.net/jira/software/projects/MA/summary

- *Figma:* https://www.figma.com/design/rtAiMw6YY3s3NuRIypEiRF/Match-Auto?node-id=0-1&t=cZqzLADlYnRPBjW0-1  

- *DOCS Historias:* https://docs.google.com/document/d/1_1PDX6QptQCONxTx7huafMM-O5dQoRCzrxRWjcWn7Ic/edit?usp=sharing

# Entrega 1️⃣:
![alt text](<media/entregas/Backlog 1.jpg>)

- *ScreenCast:* https://www.youtube.com/watch?v=Ry6wK9M6WPc&feature=youtu.be

- *DOCS Historias:* https://docs.google.com/document/d/1_1PDX6QptQCONxTx7huafMM-O5dQoRCzrxRWjcWn7Ic/edit?usp=sharing

- *Figma:* https://www.figma.com/design/rtAiMw6YY3s3NuRIypEiRF/Match-Auto?node-id=0-1&t=cZqzLADlYnRPBjW0-1

# Entrega 2️⃣:
- *Sprint 1(Concluida):* 
![alt text](<media/entregas/Sprint 1.jpg>)
![alt text](<media/entregas/Quadro 1 concluido.jpg>)

- *Jira:* https://gymstatsfds.atlassian.net/jira/software/projects/MA/summary

- *Programação em Par:*
Nosso grupo passou por um momento complicado com a saída de alguns integrantes, e isso nos obrigou a começar tudo do zero. Com o tempo apertado, fizemos uma chamada para trabalhar juntos no código, pesquisamos bastante e fomos corrigindo os erros ao longo do processo. Na última reunião, nos encontramos presencialmente para ajustar os últimos detalhes, resolver os problemas que ainda tinham e conseguir fazer o deploy na Azure.

- *Bug tracker:*
1. Campo de ano do carro aceita valores inválidos (ex: 1200)

Descrição:
O campo destinado ao ano de fabricação do carro está aceitando qualquer valor numérico, inclusive anos irreais como 1200 ou 3025. Isso compromete a integridade dos dados e pode gerar inconsistências na listagem de veículos.

2. Login falha sem mensagem clara quando senha está incorreta

Descrição:
Quando o usuário tenta fazer login com um nome de usuário válido, mas insere a senha incorreta, o sistema não apresenta uma mensagem de erro clara. Isso pode causar frustração, já que o usuário não sabe o que deu errado.

3. Permite cadastro com usuário que já existe

Descrição:
O sistema permite tentar cadastrar um novo usuário com um nome de usuário (username) que já está em uso, sem exibir uma mensagem clara de erro. Isso pode causar confusão para o usuário, que não entende o motivo do cadastro falhar.

4. Usuário não consegue adicionar carro, favoritar ou comentar sem estar logado

Descrição:
Atualmente, o sistema exige que o usuário esteja logado para poder adicionar carros, favoritar anúncios ou comentar em publicações. No entanto, essa limitação não está prevista nos requisitos e impede a interação de usuários não autenticados com funcionalidades importantes da plataforma.

Funcionalidades afetadas:
	4.1 Adicionar um novo carro
	4.2 Favoritar veículos
	4.3 Comentar em anúncios

# Contribuidores

- *Pablo José Pellegrino Cintra - pjpc@cesar.school*

- *Raul Vitor Ferraz Silva - rvfs@cesar.shool*

- *Joao Victor Guimarães Cavalcanti Uchôa - jvgcu@cesar.school*

- *Luís Eduardo Bérard de Paiva Moura Rodrigues - lebpmr@cesar.school*
