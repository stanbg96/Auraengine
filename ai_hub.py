import requests

class AIHub:
    def __init__(self):
        self.base_url = "https://openrouter.ai/api/v1"
        self.models = []

    def fetch_free_models(self):
        """Динамично извлича актуалния списък от OpenRouter и ги подрежда с приоритет на безплатните"""
        try:
            response = requests.get(f"{self.base_url}/models", timeout=12)
            if response.status_code == 200:
                data = response.json().get("data", [])
                # Сортиране: безплатните модели излизат най-отгоре в списъка
                self.models = sorted(
                    data, 
                    key=lambda x: not x.get("per_request_limits", {}).get("free", False)
                )
                return self.models
            return []
        except Exception as e:
            print(f"AI Hub Connection Error: {e}")
            return []

    def get_optimal_model(self, task_type="general"):
        if not self.models:
            self.fetch_free_models()
        if self.models:
            return self.models[0].get("id")
        return "deepseek/deepseek-chat"
