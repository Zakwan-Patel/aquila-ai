from app.config.settings import settings


class LLMClient:
    def __init__(self, use_mock: bool = False):
        self.use_mock = use_mock

        if not use_mock:
            from openai import OpenAI
            self.client = OpenAI(api_key=settings.openai_api_key)
            self.model = "gpt-3.5-turbo"

    def generate(self, prompt: str) -> str:
        if self.use_mock:
            return (
                "MOCK ANSWER:\n"
                "Based on the provided context, the document discusses the main topic "
                "and relevant details extracted from the source.\n"
                "This answer is generated without calling an external LLM."
            )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful, factual assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content
