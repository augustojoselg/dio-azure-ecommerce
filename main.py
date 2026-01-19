import streamlit as st
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import pymssql
import os
import uuid

# ======================================
# Load environment variables
# ======================================
load_dotenv()

BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
BLOB_ACCOUNT_NAME = os.getenv("BLOB_ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

# ======================================
# Validations
# ======================================
if not BLOB_CONNECTION_STRING:
    st.error("BLOB_CONNECTION_STRING não definida no .env")
    st.stop()

if not BLOB_CONTAINER_NAME:
    st.error("BLOB_CONTAINER_NAME não definida no .env")
    st.stop()

if not BLOB_ACCOUNT_NAME:
    st.error("BLOB_ACCOUNT_NAME não definida no .env")
    st.stop()

if not SQL_SERVER or not SQL_DATABASE or not SQL_USER or not SQL_PASSWORD:
    st.error("Variáveis de conexão com o SQL Server não definidas no .env")
    st.stop()

# ======================================
# Blob upload function
# ======================================
def upload_blob(file):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            BLOB_CONNECTION_STRING
        )

        container_client = blob_service_client.get_container_client(
            BLOB_CONTAINER_NAME
        )

        file_extension = file.name.split(".")[-1]
        blob_name = f"{uuid.uuid4()}.{file_extension}"

        blob_client = container_client.get_blob_client(blob_name)

        blob_client.upload_blob(
            file,
            overwrite=True,
            content_type=file.type
        )

        image_url = (
            f"https://{BLOB_ACCOUNT_NAME}.blob.core.windows.net/"
            f"{BLOB_CONTAINER_NAME}/{blob_name}"
        )

        return image_url

    except Exception as e:
        st.error(f"Erro ao fazer upload da imagem: {e}")
        return None

# ======================================
# Insert product function
# ======================================
def insert_product(nome, preco, descricao, imagem_url):
    try:
        conn = pymssql.connect(
            server=SQL_SERVER,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )

        cursor = conn.cursor()

        query = """
        INSERT INTO Produtos (
            nome,
            descricao,
            preco,
            imagem_url
        )
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (nome, descricao, preco, imagem_url)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return True

    except Exception as e:
        st.error(f"Erro ao inserir produto no banco: {e}")
        return False

# ======================================
# Streamlit UI
# ======================================
st.title("Cadastro de Produtos")

product_name = st.text_input("Nome do Produto")
product_price = st.number_input(
    "Preço do Produto",
    min_value=0.0,
    format="%.2f"
)
product_description = st.text_area("Descrição do Produto")
product_image = st.file_uploader(
    "Imagem do Produto",
    type=["jpg", "jpeg", "png"]
)

# ======================================
# Save product
# ======================================
if st.button("Salvar Produto"):
    if not product_name or not product_image:
        st.warning("Preencha todos os campos obrigatórios")
    else:
        image_url = upload_blob(product_image)

        if image_url:
            success = insert_product(
                product_name,
                product_price,
                product_description,
                image_url
            )

            if success:
                st.success("Produto salvo com sucesso!")
                st.write("Imagem salva em:")
                st.write(image_url)
            else:
                st.error("Erro ao salvar o produto no banco")

# ======================================
# List products (placeholder)
# ======================================
st.header("Produtos Cadastrados")

if st.button("Listar Produtos"):
    st.info("Funcionalidade de listagem será implementada no próximo passo")
