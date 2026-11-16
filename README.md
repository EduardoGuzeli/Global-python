<p align="center">
  <img src="assets/bimo-logo.png" alt="BIMO — suporte emocional, sempre por perto" width="850">
</p><h3 align="center">
  Suporte emocional, sempre por perto.
</h3><p align="center">
  Um companheiro inteligente desenvolvido para oferecer
  acolhimento, companhia e suporte emocional.
</p>---

## 1. Sobre o projeto

O **BIMO** é uma aplicação de terminal desenvolvida em Python para incentivar práticas simples de autocuidado e ajudar o usuário a observar suas próprias emoções ao longo do tempo.

Por meio de uma interface textual, o usuário pode registrar como está se sentindo, escrever pensamentos em um diário, conversar com o assistente, acompanhar seu histórico e visualizar conquistas relacionadas à continuidade desses registros.

A proposta é oferecer uma experiência acessível, acolhedora e simples de utilizar. O BIMO não tem a finalidade de avaliar a saúde mental do usuário, realizar diagnósticos ou substituir acompanhamento psicológico, médico ou qualquer atendimento profissional.

## 2. Problema e oportunidade

Nem sempre é fácil reservar um momento para reconhecer as próprias emoções, organizar pensamentos ou perceber mudanças no humor ao longo da rotina. A falta de um registro contínuo também pode dificultar que a própria pessoa observe padrões em suas experiências.

O BIMO propõe uma ferramenta digital de uso individual que reúne, em um só lugar:

- um registro rápido de humor;

- um espaço privado de escrita pessoal;

- mensagens de acolhimento;

- um histórico para consulta;

- indicadores simples de continuidade e participação.

### Relação com CitizenTech

A proposta utiliza tecnologia para apoiar uma necessidade cotidiana ligada ao bem-estar. Seu foco é facilitar o acesso a uma ferramenta de autorregistro e reflexão, com interação simples e sem exigir serviços externos ou conexão com a internet durante o uso normal do programa.

O projeto foi desenvolvido como protótipo acadêmico. Sua aplicação não está vinculada a um bairro ou município específico e não apresenta resultados de pesquisa de campo como se fossem dados comprovados.

## 3. Objetivo e público

**Objetivo geral:** disponibilizar uma ferramenta simples para que as pessoas possam registrar emoções, organizar pensamentos e acompanhar seus próprios registros de autocuidado.

**Público:** pessoas que desejam criar o hábito de fazer pequenas pausas de reflexão e manter um histórico pessoal de humor e anotações.

**Benefício esperado:** tornar o registro de emoções mais organizado e acessível, incentivando a reflexão pessoal sem prometer resultados clínicos ou terapêuticos.

## 4. Funcionalidades

| Recurso | Descrição |

|---|---|

| Cadastro e acesso | Criação e seleção de perfil pelo nome. |

| Check-in de humor | Registro de uma nota de 1 a 5, escolha de emoção e anotação opcional. |

| Conversa com o BIMO | Interação por mensagens com respostas predefinidas, selecionadas conforme palavras-chave e informações do perfil. |

| Diário pessoal | Criação, consulta e exclusão de registros escritos. |

| Personalidade | Seleção entre os estilos acolhedor, divertido e calmo. |

| Recompensas | Pontos, níveis, sequência de dias e conquistas para incentivar a continuidade dos registros. |

| Estatísticas | Consulta à média das notas e à emoção mais frequente. |

| Orientações de apoio | Exibição de mensagens e contatos de apoio quando determinadas expressões são identificadas. |

| Persistência | Salvamento local dos perfis e registros em arquivo JSON. |

## 5. Como funciona

1. O usuário inicia o programa pelo terminal.

2. Cria um perfil ou seleciona um perfil existente.

3. Escolhe uma opção no menu principal.

4. Registra o humor, conversa com o BIMO, utiliza o diário ou consulta suas estatísticas.

5. O programa atualiza e salva os dados localmente.

6. Em execuções futuras, os dados salvos podem ser carregados novamente.

**Fluxo resumido:**

```text

Iniciar BIMO

    |

    v

Criar ou selecionar perfil

    |

    v

Menu principal

    |

    +--> Check-in de humor

    |

    +--> Conversar com o BIMO

    |

    +--> Diário pessoal

    |

    +--> Estatísticas e conquistas

    |

    v

Salvar dados em JSON

    |

    v

Continuar usando ou sair

```

## 6. Tecnologias utilizadas

- **Python 3.10 ou superior:** linguagem principal do projeto.

- **json:** leitura e gravação dos dados.

- **os:** operações com arquivos e recursos do terminal.

- **random:** seleção de mensagens.

- **shutil:** criação de cópia de segurança em situações de erro no arquivo de dados.

- **unicodedata:** normalização de textos para auxiliar a identificação de palavras.

- **datetime:** manipulação de datas e acompanhamento da sequência de dias.

Todas as bibliotecas utilizadas são da biblioteca padrão do Python. **Não é necessário instalar dependências externas.**

## 7. Instalação e execução

### Pré-requisitos

- Python **3.10 ou superior** instalado.

- Terminal do Windows, Linux ou macOS.

- Arquivo `bimo.py`.

### Windows

Abra o terminal na pasta em que está o arquivo e execute:

```bash

python --version

python bimo.py

```

Caso o comando `python` não funcione, tente:

```bash

py --version

py bimo.py

```

### Linux ou macOS

```bash

python3 --version

python3 bimo.py

```

Na primeira execução, o programa cria o arquivo `dados.json` para armazenar as informações. Esse arquivo é gerado automaticamente na pasta de execução e não precisa ser criado manualmente.

## 8. Armazenamento e privacidade

O BIMO utiliza um arquivo JSON local para manter os dados entre execuções. Entre as informações armazenadas estão perfis, check-ins, emoções, anotações, entradas do diário, pontos, níveis, sequência de dias e conquistas.

O armazenamento local permite utilizar o protótipo sem depender de uma conta em servidor ou de sincronização em nuvem. Entretanto, isso também significa que os dados permanecem no computador em que o programa é executado.

**Limitações importantes de privacidade:**

- O arquivo JSON armazena informações em texto legível.

- O projeto não implementa criptografia.

- O acesso ao perfil é feito pelo nome, sem autenticação por senha.

- Não há sincronização entre dispositivos.

- Recomenda-se não inserir informações pessoais sensíveis ou dados reais de terceiros durante demonstrações.

Se o arquivo de dados apresentar conteúdo inválido, o programa possui tratamento para lidar com o erro e tentar preservar uma cópia de segurança. Isso não garante a recuperação de informações corrompidas.

## 9. Conceitos de Python demonstrados

A implementação reúne os principais conteúdos trabalhados na disciplina:

| Conteúdo solicitado | Aplicação no BIMO |

|---|---|

| Entrada e saída | `input()` e `print()` para interação pelo terminal. |

| Validação de dados | Funções de validação para números, textos, confirmações e nomes. |

| Tratamento de exceções | `try/except` para tratar entradas inválidas e erros de leitura e gravação. |

| Condicionais | `if`, `elif` e `else` para decisões e regras do programa. |

| Seleção de opções | `match/case` nos menus e escolhas do usuário. |

| Repetição | `while` para manter menus e fluxos ativos; `for` para percorrer coleções. |

| Funções | Organização das tarefas em funções, com parâmetros e retornos. |

| Listas | Armazenamento de históricos, entradas e conquistas. |

| Tuplas | Organização de conjuntos de valores que não precisam ser alterados. |

| Dicionários | Representação de perfis e registros. |

| JSON | Persistência dos dados entre execuções. |

| Boas práticas | Nomes descritivos, separação de responsabilidades e documentação por docstrings. |

## 10. Segurança, limites e uso responsável

O BIMO possui uma verificação baseada em uma lista de palavras e expressões previamente definidas. Quando identifica uma expressão cadastrada, o programa pode interromper o fluxo normal e exibir orientações de apoio.

Esse mecanismo é limitado: pode não reconhecer uma situação expressa com outras palavras e pode interpretar uma frase fora de contexto. Portanto, não deve ser entendido como avaliação clínica, diagnóstico, prevenção garantida ou monitoramento de risco.

As mensagens da conversa também são predefinidas e selecionadas por palavras-chave. O BIMO **não é uma IA conversacional**, não compreende livremente todas as mensagens e não substitui o contato com pessoas de confiança ou profissionais qualificados.

Quando necessário, o programa apresenta os seguintes contatos:

- **CVV — 188:** apoio emocional.

- **SAMU — 192:** atendimento móvel de urgência em situações de emergência médica.

Em uma situação de risco imediato, procure ajuda presencial e acione o serviço de emergência adequado.

## 11. Validação antes da apresentação

Para demonstrar o funcionamento do projeto, recomenda-se executar e conferir os seguintes cenários:

- [ ] Iniciar o programa e acessar o menu principal.

- [ ] Criar um perfil e acessar novamente o mesmo perfil.

- [ ] Informar uma entrada inválida em uma opção numérica e verificar a validação.

- [ ] Realizar um check-in com nota, emoção e anotação.

- [ ] Criar e consultar uma entrada no diário.

- [ ] Consultar estatísticas e recompensas após registrar informações.

- [ ] Encerrar e iniciar o programa novamente para verificar a persistência dos dados.

- [ ] Conferir a apresentação das orientações de apoio para uma expressão prevista pelo programa.

Esta lista é um roteiro de conferência. Registre como concluídos apenas os cenários efetivamente executados pelo grupo.

## 12. Uso de inteligência artificial

A documentação do apoio de inteligência artificial está no arquivo [`prompts.md`](prompts.md). Ele reúne os prompts utilizados como apoio ao planejamento, à organização e ao desenvolvimento, além de uma reflexão sobre o uso da ferramenta.

A IA foi utilizada como apoio, e não como substituta da compreensão do grupo sobre o código. A implementação final foi consolidada em um único arquivo (`bimo.py`), mesmo que algumas etapas de planejamento tenham considerado uma organização modular.

## 13. Integrantes

| Integrante | RM |

|---|---:|

| Eduardo Guzeli Nogueira | 571143 |

| Diego Caio de Ulhôa | 572190 |

| Lucas dos Santos Oliveira | 571718 |

| Octávio Mello Covre de Souza | 571811 |

| Gabriel Torres Zambo | 569883 |

## 14. Relação com o ODS

O projeto se relaciona ao **ODS 3 — Saúde e Bem-Estar**, por abordar autocuidado, reflexão pessoal e bem-estar. Essa relação representa a intenção educativa e de apoio do protótipo, não uma afirmação de eficácia clínica ou de oferta de tratamento.

## 15. Estrutura da entrega

```text

BIMO_Entrega_Python/

├── bimo.py          # Código-fonte da aplicação

├── README.md        # Apresentação, requisitos e instruções

├── prompts.md       # Registro do uso de IA

└── logo_bimo.png    # Identidade visual do projeto

```

O arquivo `dados.json` é criado automaticamente durante a execução e, por isso, não faz parte dos arquivos iniciais da entrega.

---

<div align="center">

**BIMO — suporte emocional, sempre por perto.**  

*Um momento para cuidar de você.*

</div>