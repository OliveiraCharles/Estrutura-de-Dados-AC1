# Estrutura de Dados - AC1

## Descrição

Neste projeto, criaremos um programa em Python que lê informações pessoais de um arquivo e executa instruções específicas. O objetivo é praticar o uso de classes, leitura de arquivos e implementação de algoritmos de busca e ordenação.

### Tarefas

1. **Leitura do Arquivo**
   - Crie um programa que leia um arquivo chamado `entrada.txt`.
   - Cada linha do arquivo contém informações sobre uma pessoa no seguinte formato: `NOME; IDADE; PROFISSÃO; RENDA`.

2. **Instruções**
   - Além dos registros de pessoas, o arquivo também contém comandos que devem ser executadas como instruções.
   - As comandos possíveis são: `BUBBLESORT`, `MERGESORT`, `BUSCABINARIA`, `BUSCALINEAR` e `IDX`.

3. **Algoritmos de Ordenação**
   - Se a palavra-chave for `BUBBLESORT` ou `MERGESORT`, ordene o vetor de pessoas de acordo com o critério especificado (por exemplo, nome).
   - Mostre o vetor ordenado na tela.

4. **Buscas**
   - Se a palavra-chave for `BUSCABINARIA` ou `BUSCALINEAR`, procure por uma pessoa específica (por exemplo, Marta) no vetor.
   - Exiba um booleano indicando se a pessoa foi encontrada e o índice onde ela está no vetor (-1 se não encontrada).

5. **IDX**
   - Se a palavra-chave for `IDX`, mostre o registro completo da pessoa no índice especificado.

### Critérios de Avaliação

- **Estrutura, Comentários e Legibilidade do Código** (5.0 pontos)
  - Organização do código, uso de comentários e clareza.
- **Execução Correta nos Casos de Teste** (5.0 pontos)
  - O programa deve funcionar corretamente para diferentes instruções e arquivos de entrada.

### Observações

- No início do arquivo, inclua os nomes e RAs dos integrantes do grupo.

## Instalação

1. Clone o repositório e acesse a pagina do projeto

```sh
git clone https://path.to/project/repository.git

cd path_to/project
```

## Execução

1. Na pasta raiz do projeto execute:

```sh
python src/main.py
```

## Contribuição

### Git Flow

Neste projeto, utilizamos o fluxo de trabalho Git Flow. Se você não está familiarizado com ele, pode ler mais sobre isso aqui. Aqui está uma visão geral rápida:

1. **Master**: Este ramo está sempre pronto para implantação e contém o histórico oficial de lançamentos. Todos os commits neste ramo são versionados.

2. **Develop**: Este é o ramo principal de desenvolvimento, onde as últimas funcionalidades são integradas.

3. **Ramos de feature**: São criados a partir do ramo develop e é onde o trabalho de novas funcionalidades acontece.

```sh
git flow feature start <feature-name>
```

4. **Ramos de release**: São criados a partir do develop para testes finais em preparação para um lançamento.

```sh
git flow release start <feature-name>
```

5. **Ramos de hotfix**: São criados a partir do master se um problema é encontrado em produção e precisa ser corrigido.

```sh
git flow hotfix start <feature-name>
```

Por favor, siga o fluxo de trabalho Git Flow ao contribuir para este projeto.

### Mensagens de commit

Ao contribuir para este projeto, siga as melhores práticas para mensagens de commit:

1. **Use termos iniciais específicos na linha de assunto**. Isso ajuda a entender rapidamente o propósito do commit. Aqui estão alguns exemplos:
   - `[Add]` quando você adiciona novas funcionalidades ou arquivos.
   - `[Update]` ou `[Change]` quando você faz alterações em funcionalidades existentes.
   - `[Fix]` quando você corrige um bug.
   - `[Remove]` quando você remove uma funcionalidade ou arquivo.
   - `[Refactor]` quando você faz alterações no código que não modificam seu comportamento.
   - `[Improve]` quando você aprimora uma funcionalidade sem adicionar uma nova.

2. **Use o modo imperativo** na linha de assunto. Por exemplo, use "[Add] funcionalidade" em vez de "[Adicionada] funcionalidade" ou "[Adiciona] funcionalidade".

3. **Limite a linha de assunto a 50 caracteres**. Isso permite melhor legibilidade e mensagens de commit concisas e claras.

4. **Inicie a linha de assunto com letra maiúscula**. Isso é uma prática padrão.

5. **Não termine a linha de assunto com um ponto**. A linha de assunto deve ser um resumo breve das alterações, não uma frase completa.

6. **Separe o assunto do corpo com uma linha em branco**. Nem todos os commits são complexos o suficiente para exigir um corpo, mas se for necessário explicar o que e por que de uma alteração, é aqui que você deve fazê-lo.

7. **Limite o corpo a 72 caracteres**. Isso garante que a mensagem seja exibida corretamente em várias ferramentas Git.

8. **Use o corpo para explicar o que e por que da alteração**, não o como. O próprio código explica como a alteração é feita, portanto, concentre-se em deixar claro qual é o propósito da alteração e por que ela é necessária.

Lembre-se de que boas mensagens de commit podem ajudar outras pessoas a entender suas alterações e seu propósito. Portanto, reserve um momento para escrever mensagens de commit significativas.

## Testes

```sh
pytest -x -v
```

## Licenças

-

## Autores

- Charles Oliveira
