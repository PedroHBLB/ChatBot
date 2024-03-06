{"intents":
  [
    =================================================================================================================================================================================
    1 - Tag de Saudação para inicio de conversa com  o Chat
    =================================================================================================================================================================================
    { "tag": "Saudacoes",
      "patterns":["Olá", "Ola", "Oi", "Bom dia", "Boa tarde", "Boa noite", "Tudo bem"],
      "responses": ["Olá! Como posso ajudar?"]
    },
    =================================================================================================================================================================================
    2 - Tag de Despedida para encerrar conversa
    =================================================================================================================================================================================
    { "tag": "Despedida",
      "patterns":["Obrigado", "Tchau", "Até mais", "Finalizar", "Fim"],
      "responses": ["Obrigado por utilizar o PIPEBot!"]
    },
    =================================================================================================================================================================================
    3 - Tag de Objetivos para especificar os objetivos do programa PIPE
    =================================================================================================================================================================================
    { "tag": "Objetivos",
      "patterns":["Objetivos", "Metas", "Foco", "Propósito", "Finalidade", "Objetivos"],
      "responses": ["Os objetivos do PIPE são: \n1. Apoiar a pesquisa em ciência e tecnologia como instrumento para promover a inovação tecnológica, promover o desenvolvimento empresarial e aumentar a competitividade das pequenas empresas. \n2. Incrementar a contribuição da pesquisa para o desenvolvimento econômico e social. \n3. Induzir o aumento do investimento privado em pesquisa tecnológica. \n4. Possibilitar que as empresas se associem a pesquisadores do ambiente acadêmico em projetos de pesquisa visando à inovação tecnológica. \n5. Contribuir para a formação e o desenvolvimento de núcleos de desenvolvimento tecnológico nas empresas e para o emprego de pesquisadores no mercado."]
    },
    =================================================================================================================================================================================
    4 - Tag de Significado para explicar o significado da sigla "PIPE"
    =================================================================================================================================================================================
    { "tag": "Significado",
      "patterns":["Significa", "Significado", "Abreviação", "Abreviacao", "Palavra", "PIPE"],
      "responses": ["'PIPE' significa 'Pesquisa Inovativa em Pequenas Empresas'"]
    },
    =================================================================================================================================================================================
    5 - Tag de Sobre para fornecer informações sobre o PIPE-FAPESP:
    =================================================================================================================================================================================
    { "tag": "Sobre",
      "patterns":["O que", "O que e", "O que é", "Sobre"],
      "responses": ["O PIPE-FAPESP apoia a execução de pesquisa científica e/ou tecnológica em micro, pequenas e médias empresas no Estado de São Paulo."]
    },
    =================================================================================================================================================================================
    6 - Tag de Começo para orientar sobre o início do processo de submissão ao Programa PIPE:
    =================================================================================================================================================================================
    {
      "tag": "Comeco",
      "patterns": ["Começo","Início","Iniciar","Começar","Iniciação","Início de atividades","Iniciar processo","Iniciar trabalho","Dar início","Começando", "Submeter", "Submissão"],
      "responses": [
        "A submissão de propostas ao Programa FAPESP Pesquisa Inovativa em Pequenas Empresas (PIPE) deve ser feita exclusivamente por meio do Sistema de Apoio à Gestão (SAGe), no endereço: www.fapesp.br/sage. \n 1 - Fase 1 PIPE: Análise de Viabilidade Técnico-Científica da proposta de pesquisa para inovação \n 2 - Fase 2: Desenvolvimento da Proposta de Pesquisa para inovação \n 3 - PIPE Invest: Aceleração da chegada ao mercado de Projetos apoiados nas Fase 1 e/ou 2, quando houver terceira parte interessada, em situações de investimento privado simultâneo \n 4 - Fase 3: desenvolvimento comercial e industrial dos produtos, processos, sistemas e/ou serviços inovadores obtidos a partir de pesquisas anteriores realizadas pela pequena empresa sem o apoio da FAPESP ou a partir de pesquisa apoiada no âmbito do PIPE."
      ]
    },
    =================================================================================================================================================================================
    7 - Tag de Datas para informar sobre o período de submissão de propostas no Programa PIPE:
    =================================================================================================================================================================================
    {
      "tag": "Datas",
      "patterns": ["Datas", "Data de Solicitação", "Tempo", "Prazo", "Data de Entrega", "Data de Início", "Data Limite", "Intervalo de Tempo", "Período"],
      "responses": [
        "As propostas de pesquisa para inovação para o PIPE Fase 1, Fase 2 e PIPE Invest são recebidas em fluxo contínuo."
      ]
    },
    =================================================================================================================================================================================
    8 - Tag de Primeira Fase para descrever a fase inicial do Programa PIPE:
    =================================================================================================================================================================================
    {
      "tag": "Primeira_Fase",
      "patterns": ["1", "Primeira", "primeira fase", "fase 1", "primeira etapa", "etapa 1", "primeira fase do processo", "fase inicial", "primeira parte", "início do processo"],
      "responses": ["Na Fase 1, com duração prevista de até 9 (nove) meses, o objetivo é conduzir pesquisas sobre a viabilidade técnico-científica da inovação proposta. Durante esta etapa, o financiamento máximo disponível é de R$ 300.000,00 (trezentos mil reais) por projeto, cobrindo todos os itens concedidos pela FAPESP, incluindo Bolsas de Treinamento Técnico e Bolsas de Pesquisa em Pequenas Empresas, exceto Benefícios Complementares e Parcela para Custos de Infraestrutura Direta do Projeto."]
    },
    =================================================================================================================================================================================
    9 - Tag de Segunda Fase para explicar a segunda etapa do Programa PIPE:
    =================================================================================================================================================================================
    {
      "tag": "Segunda_Fase",
      "patterns": ["2", "Segunda", "segunda fase", "fase 2", "segunda etapa", "etapa 2", "segunda fase do processo", "fase intermediária", "segunda parte", "próxima fase", "fase seguinte", "continuação do processo"],
      "responses": ["Na Fase 2, com duração prevista de até 24 (vinte e quatro) meses, o foco é no desenvolvimento da proposta de pesquisa para a inovação propriamente dita, podendo englobar atividades preliminares para a inserção dos resultados da pesquisa no mercado (atividades de apoio à comercialização). Durante esta fase, o financiamento máximo disponível é de até R$ 1.500.000,00 (um milhão e quinhentos mil reais) por projeto, cobrindo todos os itens concedidos pela FAPESP, incluindo Bolsas de Treinamento Técnico e Bolsas de Pesquisa em Pequenas Empresas, com exceção de Benefícios Complementares e Parcela para Custos de Infraestrutura Direta do Projeto."]
    },
    =================================================================================================================================================================================
    10 - Tag de Pipe Invest para explicar o programa PIPE Invest:
    =================================================================================================================================================================================
    {
      "tag": "Pipe_Invest",
      "patterns": ["PIPE Invest", "PIPE investment", "investimento PIPE", "rodada de investimento PIPE","rodada de financiamento PIPE"],
      "responses": ["O PIPE Invest visa fornecer financiamento adicional para projetos PIPE Fases 1 e 2 que tenham alcançado ou excedido seus objetivos nas fases correspondentes, com o propósito de impulsionar o processo de comercialização das inovações desenvolvidas durante o projeto. \n São elegíveis os projetos Fase 1 e 2 que demonstrem capacidade de atrair investimento privado, de uma terceira parte"]
    },
    =================================================================================================================================================================================
    11 - Tag de Terceira Fase para descrever a última etapa do Programa PIPE:
    =================================================================================================================================================================================
    {
      "tag": "Terceira_Fase",
      "patterns": ["3", "Terceira", "Fase 3", "Fase Três", "Última Fase", "Etapa 3", "Etapa Três", "Parte 3", "Parte Três", "Ciclo 3", "Seção 3", "Sequência 3", "Estágio 3", "Terceira Etapa", "Terceira Parte", "Terceiro Ciclo", "Terceiro Estágio"],
      "responses": ["Na Fase 3, é esperado que a pequena empresa assuma internamente a responsabilidade pelo desenvolvimento comercial e industrial dos produtos, processos, sistemas e/ou serviços inovadores obtidos a partir de pesquisas anteriores realizadas pela empresa sem o apoio da FAPESP, ou a partir de pesquisas apoiadas no âmbito do PIPE."]
    },
    =================================================================================================================================================================================
    12 - Tag de Requisitos para detalhar os documentos necessários para solicitação do Programa PIPE:
    =================================================================================================================================================================================
    {
      "tag": "Requisitos",
      "patterns": ["Requisito", "Necessidade", "Envio", "Documentos", "Proposta Inicial", "Critério", "Pré-requisito", "Elegibilidade", "Termos", "Condições", "Diretrizes", "Procedimentos", "Obrigações", "Itens Necessários"],
      "responses": ["Os seguintes documentos devem ser anexados à proposta inicial para solicitação do PIPE Fase 1, Fase 2 \n 1 - Elaboração da Proposta: Anexar o Projeto de Pesquisa para inovação, seguindo o modelo fornecido pela FAPESP \n 2 - Documentação dos Pesquisadores e Equipe: * Incluir a Súmula Curricular do Pesquisador Responsável, dos Pesquisadores Principais e Associados \n * Detalhar a Qualificação de empresas e instituições de pesquisa a serem subcontratadas \n * Anexar os currículos dos consultores a serem subcontratados, designados como membros da equipe na função de 'Consultor' \n * Apresentar os Planos de atividades individuais para cada Bolsa de Treinamento Técnico solicitada. \n 3 - Descrição das Responsabilidades e Atividades: * Descrever sucintamente as responsabilidades de cada membro da equipe, especificando os desafios científicos e tecnológicos a serem superados para alcançar os objetivos. \n * Detalhar as atividades desenvolvidas pela equipe, incluindo pesquisadores associados, bolsistas, estudantes sem bolsa e colaboradores, em um parágrafo para cada um."]
    }
  ]
}