"""
Padrões de prompt para análise de manutenibilidade
"""

class PromptPatterns:
    
    @staticmethod
    def zero_shot(code_snippet: str) -> str:
        """Zero-shot: pergunta direta sem exemplos"""
        prompt = f"""Analise o seguinte código e avalie sua manutenibilidade em uma escala de 1-10.

Código:
{code_snippet}

Responda com:
1. Score (1-10)
2. Razão principal
3. Sugestões (máximo 2 linhas)
"""
        return prompt

    @staticmethod
    def few_shot(code_snippet: str) -> str:
        """Few-shot: com exemplos antes"""
        prompt = f"""Exemplos de análise:

EXEMPLO 1:
def add(a, b):
    return a + b

Score: 9/10
Razão: Função clara, sem complexidade
Sugestão: Adicionar docstring

EXEMPLO 2:
def process(d):
    r = []
    for i in range(len(d)):
        if d[i] > 0:
            r.append(d[i] * 2)
    return r

Score: 5/10
Razão: Nomes obscuros, lógica confusa
Sugestão: Usar list comprehension, melhorar nomes

Agora analise este:
{code_snippet}

Responda com:
1. Score (1-10)
2. Razão principal
3. Sugestões (máximo 2 linhas)
"""
        return prompt

    @staticmethod
    def chain_of_thought(code_snippet: str) -> str:
        """Chain-of-thought: raciocínio passo-a-passo"""
        prompt = f"""Analise passo-a-passo:

Código:
{code_snippet}

Responda:
1. Qual é a complexidade? (quantas branches?)
2. Variáveis têm nomes claros?
3. Há duplicação de código?
4. É fácil adicionar funcionalidade?
5. Um novo dev entenderia rápido?

DEPOIS disso, dê:
- Score (1-10)
- Razão principal
- Sugestões (máximo 2 linhas)
"""
        return prompt


if __name__ == "__main__":
    code = "def calc(x, y):\\n    return (x + y) * 2"
    
    print("ZERO-SHOT:")
    print(PromptPatterns.zero_shot(code))
    print("\\n" + "="*50 + "\\n")
    
    print("FEW-SHOT:")
    print(PromptPatterns.few_shot(code))
    print("\\n" + "="*50 + "\\n")
    
    print("CHAIN-OF-THOUGHT:")
    print(PromptPatterns.chain_of_thought(code))