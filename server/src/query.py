from llama_index.core import Settings
from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.core import load_index_from_storage
from llama_index.core import StorageContext
import os

llm_base_url = os.environ.get('LLM_BASE_URL', 'http://ollama-service:11434')

llm_model_name = os.environ.get('LLM_MODEL_NAME', "qwen2") 
temperature = 0.1
llm_api_base = f"{llm_base_url}/v1"

embedding_model_name = os.environ.get('EMBEDDING_MODEL_NAME', "quentinz/bge-large-zh-v1.5") 
embedding_dimension = 1024
embedding_api_base = llm_base_url 

Settings.chunk_size = 128
Settings.chunk_overlap = 20

data_dir = "./data"
store_dir = "./storage"

index = None


def init():
    global index
    # 设置全局llm
    Settings.llm = OpenAILike(
        model=llm_model_name,
        api_base=llm_api_base,
        api_key="ollama",
        is_chat_model=True,
        temperature=temperature,
        request_timeout=60.0
    )

    # 设置全局embedding
    Settings.embed_model = OllamaEmbedding(
        model_name=embedding_model_name,
        base_url=embedding_api_base,
        # -mirostat N 使用 Mirostat 采样。
        ollama_additional_kwargs={"mirostat": 0},
    )

    # 初始化index
    if not os.path.exists(store_dir):
        documents = SimpleDirectoryReader(
            input_dir=data_dir,  required_exts=[".txt"]).load_data()
        index = VectorStoreIndex.from_documents(documents=documents)

        index.storage_context.persist()
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=store_dir))


def query(prompt):
    query_engine = index.as_query_engine(
        streaming=True,
        similarity_top_k=10
    )

    return query_engine.query(prompt)
