# Nutry Foody - LLM-Powered Nutrition and Fitness Assistant

## Overview

**Nutry Foody** is an intelligent chatbot application designed to provide personalized nutritional advice and fitness recommendations. Powered by a Large Language Model (LLM) API, this application is tailored to consider the user's dietary restrictions, fitness goals, and preferred foods while delivering concise and relevant answers. The project integrates various technologies and features to ensure a seamless and interactive user experience.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)

## Features

- **Personalized Responses**: Takes into account user-specific dietary restrictions and fitness goals.
- **Interactive Chat Interface**: A responsive chat interface and seamless conversation flow.
- **Real-Time Streaming**: Supports real-time streaming of responses from the LLM API.

## Project Structure
```
your_project/
│
├── config/
│   └── config.py
│
├── src/
│   ├── inference/
│   │   └── chat_handler.py
│   ├── utils/
│   │   ├── food_utils.py
│   │   ├── groq_utils.py
│   │   └── llm_utils.py
│   └── __init__.py
│
├── static/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── app.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used

- **Python**
- **Flask**: For serving the backend and REST API.
- **Llama 3.1**: Utilized for advanced natural language processing tasks, enabling the generation of contextually relevant responses.
- **HTML/CSS/JavaScript**: For the front-end interface.
- **LLM API (via Groq)**: Large Language Model integration for natural language understanding and response generation.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wicaksatya/llm.git
   cd llm
   ```
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   Define your environment variables in a `.env` file or set them directly in your environment. Refer to `config/config.py` for required variables.
4. **Run the application:**
   ```bash
   python app.py
   ```

## Usage

- Navigate to the running application in your browser.
- Use the chat interface to ask nutrition and fitness-related questions.
- The assistant will respond considering your dietary restrictions and fitness goals.

## API Integration 
This project uses the LLM API from Groq with the following key settings:

- **Base URL:** https://api.groq.com/openai/v1
- **Model:** meta-llama/llama-3-8b-instruct
- **API Key:** Access [Groq console](https://console.groq.com/keys), _**Note:**_ _you have to register first_
- **Streaming:** Enabled

Refer to `llm_utils.py` for details on how API requests are structured and handled.


