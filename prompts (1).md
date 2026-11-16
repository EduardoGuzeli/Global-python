# Prompts.md — Desenvolvimento do BIMO

## 1. Ferramenta de Inteligência Artificial utilizada

**Ferramenta:** ChatGPT (OpenAI)

**Finalidade:** Utilizamos o ChatGPT como apoio durante o planejamento e o desenvolvimento do BIMO. A ferramenta nos ajudou a organizar as funcionalidades, entender conceitos de Python, estruturar os arquivos do projeto e identificar possíveis problemas no código.

A IA foi utilizada como ferramenta de apoio, e não como substituta do desenvolvimento e da compreensão do grupo.

> **Observação sobre a versão entregue:** os prompts abaixo registram solicitações feitas durante o planejamento e o desenvolvimento. A estrutura modular foi considerada inicialmente, mas o código-fonte final desta entrega foi consolidado em um único arquivo, `bimo.py`. Assim, os nomes de módulos citados nos prompts representam a organização solicitada naquela etapa, não arquivos adicionais incluídos neste pacote.

---

## 2. Prompts utilizados durante o desenvolvimento

### Prompt 1 — Planejamento e estrutura do projeto

No começo do projeto, estávamos tentando organizar as ideias e entender como poderíamos desenvolver o BIMO utilizando os conteúdos aprendidos em Computational Thinking with Python.

Pedimos ajuda para dividir a aplicação em arquivos menores, de forma que cada integrante pudesse trabalhar em uma parte do sistema.

**Prompt utilizado:**

"Estamos desenvolvendo a Global Solution de Python e tivemos a ideia de criar o BIMO, um robô de terminal voltado à saúde mental e ao bem-estar. Queremos que ele tenha cadastro de usuários, acompanhamento de humor, diário, conversas e um sistema de recompensas.

Como ainda estamos organizando o projeto, você pode nos ajudar a pensar em uma estrutura de arquivos Python? Queremos separar as funcionalidades em módulos para facilitar o desenvolvimento em grupo. É importante que a organização permita utilizar os requisitos da disciplina, como funções, listas, tuplas, dicionários, estruturas de repetição, decisões e arquivos JSON. Por enquanto, não precisamos do código, apenas da estrutura."

### Prompt 2 — Cadastro e login

Depois de definir a estrutura, começamos pelas funcionalidades básicas. Decidimos implementar o cadastro e o login para que cada pessoa pudesse ter seu próprio histórico.

**Prompt utilizado:**

"Vamos começar pelo cadastro e login do BIMO. Pensamos em algo simples: a pessoa informa o nome e, se já existir um cadastro, o sistema carrega o perfil dela. Caso contrário, cria um novo usuário.

Precisamos validar o nome para evitar entradas vazias, aceitar somente letras e espaços e limitar o tamanho entre 2 e 20 caracteres.

Você pode nos ajudar a desenvolver essa parte em um arquivo chamado usuario.py? Gostaríamos de utilizar funções pequenas, com docstrings, e entender o funcionamento de cada uma para conseguir explicar o código na apresentação."

### Prompt 3 — Armazenamento dos dados

Com o cadastro definido, precisávamos garantir que as informações não fossem perdidas quando o programa fosse encerrado.

**Prompt utilizado:**

"Agora precisamos resolver o armazenamento dos usuários. Queremos guardar os perfis e seus históricos em um arquivo chamado dados.json.

Você pode nos ajudar a criar um módulo dados.py com funções para carregar e salvar essas informações? Também precisamos pensar no que acontece quando o arquivo ainda não existe ou quando ele está com algum problema.

Se o JSON estiver corrompido, queremos que o programa avise o usuário, preserve uma cópia do arquivo com problema e consiga iniciar novamente sem simplesmente fechar. Vamos utilizar apenas recursos nativos do Python."

### Prompt 4 — Check-in de humor

Uma das principais funcionalidades do BIMO é permitir que a pessoa registre como está se sentindo. Por isso, começamos a pensar em como fazer esse registro e guardar um histórico.

**Prompt utilizado:**

"Queremos implementar o check-in diário do BIMO. A pessoa deverá escolher uma nota de humor de 1 a 5 e selecionar uma emoção entre algumas opções: feliz, calmo, grato, ansioso, triste, irritado, cansado e sozinho.

Também queremos permitir uma anotação opcional de até 200 caracteres.

Precisamos impedir que a pessoa faça mais de um check-in no mesmo dia e tratar entradas inválidas, como digitar uma letra no lugar da nota.

Pode nos ajudar a desenvolver o arquivo checkin.py? Também seria interessante ter funções para calcular a média das notas e descobrir qual emoção aparece com mais frequência no histórico."

### Prompt 5 — Conversa com o BIMO

Depois do check-in, pensamos em uma maneira de fazer o BIMO interagir com o usuário de acordo com o humor registrado.

**Prompt utilizado:**

"Queremos que o BIMO tenha uma conversa simples com o usuário, mas que não responda sempre da mesma maneira.

A ideia é utilizar a última nota de humor registrada para escolher o tipo de resposta: notas 1 e 2 devem receber mensagens acolhedoras, nota 3 deve receber mensagens leves de incentivo e notas 4 e 5 podem receber mensagens positivas.

Queremos guardar várias respostas em dicionários e escolher uma delas aleatoriamente. A conversa deve continuar até a pessoa digitar 'sair', e o BIMO também deve reconhecer algumas palavras, como 'obrigado' e 'ajuda'.

Você pode nos ajudar a montar o conversa.py utilizando os conceitos que aprendemos em aula?"

### Prompt 6 — Diário pessoal

Além das conversas, queríamos oferecer um espaço para a pessoa escrever sobre seu dia e consultar registros anteriores.

**Prompt utilizado:**

"Estamos pensando em adicionar um diário pessoal ao BIMO. Queremos que ele tenha um submenu com quatro opções: escrever, ler, apagar e voltar.

O texto precisa ter no mínimo 5 e no máximo 500 caracteres. Quando a pessoa consultar o diário, os registros devem aparecer do mais recente para o mais antigo, com numeração para facilitar a identificação.

Na opção de apagar, queremos que o programa peça o número do registro e confirme a exclusão antes de continuar.

Pode nos ajudar a desenvolver essa funcionalidade no arquivo diario.py, mantendo os registros salvos no JSON?"

### Prompt 7 — Personalidade do BIMO

Durante o planejamento, percebemos que seria interessante permitir que cada usuário escolhesse como gostaria de interagir com o BIMO.

**Prompt utilizado:**

"Queremos deixar o BIMO um pouco mais pessoal. Pensamos em três opções de personalidade: acolhedor, divertido e calmo.

A escolha deve alterar o tom das mensagens durante as conversas, além das mensagens de abertura e despedida.

Você pode nos ajudar a adaptar o conversa.py e criar uma opção para configurar essa preferência? Gostaríamos de utilizar match/case para trabalhar com as escolhas do usuário e salvar a configuração no perfil."

### Prompt 8 — Pontos e conquistas

Para incentivar o uso das funcionalidades, tivemos a ideia de criar um sistema simples de recompensas.

**Prompt utilizado:**

"Queremos adicionar um sistema de pontos ao BIMO para incentivar a pessoa a manter uma rotina de autocuidado.

Pensamos em dar 10 pontos por check-in, 15 pontos por registro no diário e 5 pontos por conversa, respeitando o limite de uma recompensa por conversa por dia.

Também queremos implementar uma sequência de dias de utilização (streak), níveis chamados Semente, Broto, Muda, Árvore e Floresta, e algumas conquistas que sejam desbloqueadas automaticamente.

Pode nos ajudar a organizar essas regras no arquivo recompensas.py? Queremos guardar os níveis em tuplas, evitar conquistas duplicadas e mostrar uma barra de progresso feita com caracteres no próprio terminal."

### Prompt 9 — Segurança e responsabilidade

Como o BIMO trabalha com bem-estar e saúde mental, percebemos que não seria adequado tratar todas as mensagens como conversas comuns. Precisávamos pensar em uma forma responsável de lidar com situações delicadas.

**Prompt utilizado:**

"Precisamos melhorar a parte de segurança do BIMO. Como a aplicação aborda saúde mental, queremos que ela reconheça algumas expressões que indiquem uma possível situação de risco no diário, no check-in ou durante uma conversa.

Quando isso acontecer, o programa deve interromper o fluxo normal, responder de maneira acolhedora e sem julgamentos e apresentar orientações para procurar ajuda, incluindo o CVV (188) e o SAMU (192), conforme a situação.

Também pensamos em mostrar uma orientação para buscar apoio profissional caso a pessoa registre notas baixas de humor por três dias consecutivos.

Pode nos ajudar a criar um módulo seguranca.py e explicar em quais partes do programa devemos chamar essas verificações? Queremos evitar que situações de risco recebam pontos ou mensagens de comemoração."

### Prompt 10 — Integração e menu principal

Quando as funcionalidades começaram a ficar prontas, precisávamos integrar os módulos e organizar a navegação do programa.

**Prompt utilizado:**

"Já temos boa parte das funcionalidades separadas em arquivos Python e agora precisamos juntar tudo no main.py.

Queremos criar um menu principal com while e match/case, mostrar o nome e o nível do usuário na parte superior e deixar algumas opções disponíveis apenas depois do login.

Também precisamos de um aviso fixo no rodapé lembrando que o BIMO não substitui acompanhamento profissional.

Você pode nos ajudar a organizar essa integração e criar um utils.py com funções reutilizáveis para limpar a tela, solicitar números, textos e confirmações?

Por último, queremos tratar o Ctrl+C para que o programa encerre de maneira educada, preservando os dados."

### Prompt 11 — Revisão e testes

Depois de integrar os arquivos, percebemos que seria importante revisar o funcionamento geral antes de finalizar o projeto.

**Prompt utilizado:**

"Terminamos uma primeira versão do BIMO e queremos fazer uma revisão antes da entrega.

Você pode analisar nossos arquivos Python procurando erros de lógica, principalmente no cálculo do streak, nas datas, na exclusão de registros e nos índices das listas?

Também queremos verificar se existem entradas que possam fazer o programa travar.

Além da revisão, monte um roteiro de testes manuais para o grupo conferir situações como nome vazio, nota inválida, arquivo JSON inexistente, JSON corrompido, tentativa de fazer dois check-ins no mesmo dia e identificação de palavras relacionadas a situações de risco.

Queremos entender os possíveis problemas e corrigir o que for necessário."

### Prompt 12 — Documentação do projeto

Na etapa final, precisávamos organizar a documentação para que o professor e outras pessoas conseguissem entender o objetivo e o funcionamento da aplicação.

**Prompt utilizado:**

"Estamos chegando à etapa final do BIMO e precisamos preparar o README.md para o GitHub e para a entrega da Global Solution.

Queremos apresentar a ideia do projeto, sua relação com o tema da GS, as funcionalidades disponíveis, os integrantes com seus respectivos RMs e uma tabela relacionando os requisitos da disciplina aos arquivos em que aparecem.

Também precisamos explicar como executar o programa utilizando Python 3.10 ou superior e apresentar as limitações da aplicação.

Pode nos ajudar a organizar essa documentação de maneira clara, objetiva e com uma linguagem natural, sem parecer um texto muito genérico?"

---

## 3. Como utilizamos as sugestões da IA

Durante o desenvolvimento, utilizamos as respostas do ChatGPT como referência para organizar as funcionalidades e compreender algumas soluções de programação.

As sugestões foram analisadas pelo grupo antes de serem incorporadas ao projeto. Também foi necessário adaptar algumas partes para que funcionassem corretamente com a estrutura dos nossos arquivos e com os conhecimentos trabalhados na disciplina.

A intenção foi utilizar os conceitos de Python estudados em aula, mantendo o código compreensível e permitindo que todos os integrantes entendessem as funcionalidades desenvolvidas.

## 4. Verificação e testes

Para verificar as funcionalidades sugeridas, planejamos e realizamos testes envolvendo diferentes situações de uso, incluindo:

- Cadastro com nomes válidos e inválidos.
- Login de usuários já cadastrados.
- Criação e leitura dos dados no JSON.
- Recuperação diante de arquivos inexistentes ou corrompidos.
- Tentativas de realizar mais de um check-in no mesmo dia.
- Registro, consulta e exclusão de textos no diário.
- Funcionamento das diferentes personalidades do BIMO.
- Cálculo de pontos, níveis, conquistas e sequência de dias.
- Respostas de segurança diante de expressões de risco.
- Navegação entre as opções do menu principal.

Os testes devem ser registrados como concluídos somente quando tiverem sido efetivamente executados pelo grupo. A lista acima funciona como roteiro de verificação das funcionalidades e dos casos de erro; antes da entrega, o grupo deve confirmar quais cenários foram testados e anotar eventuais correções realizadas.

## 5. Análise crítica sobre o uso da IA

O uso do ChatGPT ajudou principalmente na organização inicial do projeto e na compreensão de como dividir uma aplicação maior em arquivos menores.

Durante o desenvolvimento, percebemos que a IA consegue sugerir soluções rapidamente, mas nem sempre elas funcionam exatamente como esperamos. Algumas respostas precisaram ser adaptadas, principalmente na integração entre os módulos, no armazenamento dos dados e nas regras de funcionamento do sistema.

Outro ponto importante foi entender o código antes de utilizá-lo. Apenas copiar uma solução não garantiria que conseguíssemos explicar seu funcionamento ou identificar possíveis erros.

Por isso, consideramos a IA uma ferramenta de apoio ao aprendizado. Ela facilitou algumas etapas do desenvolvimento, mas as decisões, adaptações e verificações precisaram ser feitas pelo grupo.

**Conclusão:** O uso da inteligência artificial contribuiu para acelerar o planejamento e apoiar o desenvolvimento do BIMO, além de nos ajudar a compreender melhor alguns conceitos de programação. Entretanto, também percebemos a importância de testar, questionar e entender cada solução antes de incorporá-la ao projeto.