from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
import pandas as pd
from transformers import pipeline
from flask import Flask, render_template, request

encoder = SentenceTransformer('all-MiniLM-L6-v2') 
qdrant = QdrantClient(":memory:") # Create in-memory Qdrant instance

# Create collection to store books
qdrant.recreate_collection(
    collection_name="thesis-info",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(), 
        distance=models.Distance.COSINE
    )
)

file_path = 'dataset.xlsx'
data_list = []

with pd.ExcelFile(file_path) as xls:
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name, skiprows=1)
            for index, row in df.iterrows():
                documents = {
                    'title': ''.join([word for word in row[1].split('\n')[1:] if word]),
                    'abstract': row[3]
                }
                data_list.append(documents)


qdrant.upload_records(
    collection_name="thesis-info",
    records=[
        models.Record(
            id=idx,
            vector=encoder.encode(doc["abstract"]).tolist(),
            payload=doc
        ) for idx, doc in enumerate(data_list)
    ]
)


generator = pipeline("text-generation", model="gpt2")

def query_vector_database(user_input):
    hits = qdrant.search(
    collection_name="thesis-info",
    query_vector=encoder.encode(user_input).tolist(),
    limit=1
)
    for hit in hits:
      return hit.payload

def generate_response(user_input, relevant_theses):
    prompt = f"User input: {user_input}\n Relevant theses: {relevant_theses}\n"
    generated_text = generator(prompt, max_length=500, num_return_sequences=1)[0]['generated_text']
    return generated_text.strip()

# user_input = "what do you know about Prosodic alignment for Automatic dubbing"

# relevant_theses = query_vector_database(user_input)
# response = generate_response(user_input, relevant_theses)
# print("Generated Response:", response)

app = Flask(__name__)

# Home route to render the HTML template
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user input and generate response
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    relevant_theses = query_vector_database(user_input) 
    response = generate_response(user_input, relevant_theses)
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)

