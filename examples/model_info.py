from llmproxy import LLMProxy

if __name__ == '__main__':

    client = LLMProxy(backend="llmproxy")
    response = client.model_info()

    print(response['result'])