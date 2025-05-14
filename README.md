# LangChain Models Project

This project is a simple collection of custom **chains** and **output parsers** built using [LangChain](https://github.com/langchain-ai/langchain).  
It helps you structure model outputs and design workflows easily.

---

## 📂 Folder Structure

- **chains/**  
  Different types of model workflows:
  - `conditionalchain.py`: Runs different steps based on conditions.
  - `parallelchain.py`: Runs multiple steps in parallel.
  - `seqchain.py`: Runs steps one after another (sequentially).

- **output-parsers/**  
  Parse and structure model outputs:
  - `jsonoutputparser.py`: Parses JSON outputs.
  - `pydanticoutputparser.py`: Uses Pydantic for validation.
  - `stroutputparser.py`: Parses string outputs.
  - `structuredoutputparser.py`: General structured output handling.

- **struct-outputs/**  
  Typed output examples:
  - `pydantic-output.py`: Example using Pydantic models.
  - `typedict-output.py`: Example using TypedDict.

- **test.py**  
  A sample script to test the modules.

- **requirements.txt**  
  List of Python dependencies.

- **.env**  
  Environment variables (e.g., API keys).

- **.gitignore**  
  Files ignored by Git.

---

## 🚀 Quick Start

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/langchain-models.git
    cd langchain-models
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set your environment variables:**  
Create a `.env` file and add any required variables (like API keys).

5. **Run the test:**

    ```bash
    python test.py
    ```

---

## 📚 Features

- Build simple and flexible chains (sequential, conditional, parallel).
- Parse AI model outputs into structured formats.
- Use Pydantic and TypedDict for validation.

---

## ✅ Requirements

- Python 3.9 or higher
- LangChain
- Pydantic
- (Other packages in `requirements.txt`)

---

## 📜 License

This project is licensed under the MIT License.

---

## ✨ Example Use Case

You can easily design a model workflow like:
- **If** a condition is true, **run specific chains**.
- **Run multiple models in parallel**.
- **Parse and validate** model outputs automatically.

---
