import configparser
import os

config = configparser.ConfigParser()
base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, 'config.ini')
config.read(config_path)

azure_openai_key = config.get('general', 'AZURE_OPENAI_KEY')

azure_openai_endpoint = config.get('gpt', 'AZURE_OPENAI_ENDPOINT')
azure_openai_api_version = config.get('gpt', 'AZURE_OPENAI_API_VERSION')
azure_openai_gpt_deployment = config.get('gpt', 'AZURE_OPENAI_GPT_DEPLOYMENT')

azure_openai_embedding_deployment = config.get('embedding', 'AZURE_OPENAI_EMBEDDING_DEPLOYMENT')