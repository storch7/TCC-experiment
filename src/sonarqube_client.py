import requests
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

class SonarQubeClient:
    def __init__(self, host: str, username: str, password: str):
        self.host = host
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = (username, password)
    
    def get_system_health(self):
        """Verifica se SonarQube está respondendo"""
        url = f"{self.host}/api/system/health"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def get_projects(self):
        """Lista projetos no SonarQube"""
        url = f"{self.host}/api/projects/search"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


if __name__ == "__main__":
    # Lê do .env
    sonarqube_host = os.getenv("SONARQUBE_HOST")
    sonarqube_user = os.getenv("SONARQUBE_USER")
    sonarqube_password = os.getenv("SONARQUBE_PASSWORD")
    
    print(f"Conectando a: {sonarqube_host}")
    print(f"Usuário: {sonarqube_user}")
    
    client = SonarQubeClient(
        host=sonarqube_host,
        username=sonarqube_user,
        password=sonarqube_password
    )
    
    print("\nSonarQube Health:")
    print(client.get_system_health())
    
    print("\nProjetos:")
    print(client.get_projects())