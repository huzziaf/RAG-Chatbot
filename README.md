# RAG Chat Application with Qdrant and GPT-2

This project implements a web-based chat application using Retrieval Augmented Generation (RAG) techniques. It leverages Qdrant as the vector database for thesis data and GPT-2 as the large language model (LLM) for generating responses. 

## Overview

The chat application allows users to interact with the system by providing input queries related to MS Thesis titles and abstracts. The application retrieves relevant information from the vector database and generates contextually enriched responses using the GPT-2 model.

## Components

- **Qdrant**: An in-memory vector database used to store and retrieve thesis data based on user queries.
- **GPT-2**: A pre-trained large language model used for generating responses based on user input and retrieved thesis data.
- **Flask**: Web framework used to develop the web-based chat interface.
- **Sentence Transformers**: Library used for encoding input queries and thesis abstracts into vector representations.

## Usage

1. **Setup**: Ensure that all necessary Python libraries are installed (`qdrant_client`, `sentence_transformers`, `transformers`, `flask`, `pandas`). Also, download the pre-trained GPT-2 model.
2. **Data Integration**: Load the provided MS Thesis dataset and upload the relevant data to the Qdrant vector database.
3. **Model Initialization**: Initialize the Sentence Transformers encoder and the Qdrant client.
4. **User Interaction**: Run the Flask application and interact with the chat interface by entering queries related to MS Thesis topics.
5. **Response Generation**: The application retrieves relevant thesis information from the vector database and generates contextually enriched responses using the GPT-2 model.

## Files

- **app.py**: Main Python script containing the Flask application and logic for querying the vector database and generating responses.
- **index.html**: HTML template for the chat interface.
- **dataset.xlsx**: Sample dataset containing MS Thesis titles and abstracts.
- **README.md**: This documentation file.

