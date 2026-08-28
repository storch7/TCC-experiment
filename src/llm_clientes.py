import os
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    """Interface base para clientes LLM"""
    
    def send_prompt(self, prompt: str) -> str:
        raise NotImplementedError


class OpenAIClient(LLMClient):
    """Cliente para ChatGPT via OpenAI API"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY não definida em .env")
        try:
            import openai
            self.client = openai.OpenAI(api_key=self.api_key)
        except ImportError:
            raise ImportError("openai não instalado. pip install openai")
    
    def send_prompt(self, prompt: str, model: str = "gpt-3.5-turbo") -> str:
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao chamar OpenAI: {str(e)}"


class AnthropicClient(LLMClient):
    """Cliente para Claude via Anthropic API"""
    
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY não definida em .env")
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError("anthropic não instalado. pip install anthropic")
    
    def send_prompt(self, prompt: str, model: str = "claude-3-haiku-20240307") -> str:
        try:
            message = self.client.messages.create(
                model=model,
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            return f"Erro ao chamar Anthropic: {str(e)}"


class DeepSeekClient(LLMClient):
    """Cliente para DeepSeek via API"""
    
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise ValueError("DEEPSEEK_API_KEY não definida em .env")
        try:
            import openai
            self.client = openai.OpenAI(
                api_key=self.api_key,
                base_url="https://api.deepseek.com"
            )
        except ImportError:
            raise ImportError("openai não instalado. pip install openai")
    
    def send_prompt(self, prompt: str, model: str = "deepseek-chat") -> str:
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao chamar DeepSeek: {str(e)}"


if __name__ == "__main__":
    print("Testando clientes LLM...")
    
    test_prompt = "Qual é a capital da França? Responda em 1 linha."
    
    try:
        print("\n=== Claude (Anthropic) ===")
        claude = AnthropicClient()
        response = claude.send_prompt(test_prompt)
        print(response)
    except Exception as e:
        print(f"Erro: {e}")
    
    try:
        print("\n=== ChatGPT (OpenAI) ===")
        openai_client = OpenAIClient()
        response = openai_client.send_prompt(test_prompt)
        print(response)
    except Exception as e:
        print(f"Erro: {e}")
    
    try:
        print("\n=== DeepSeek ===")
        deepseek = DeepSeekClient()
        response = deepseek.send_prompt(test_prompt)
        print(response)
    except Exception as e:
        print(f"Erro: {e}")