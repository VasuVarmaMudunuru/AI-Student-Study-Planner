# AI Student Study Planner

## Project Overview

AI Student Study Planner is a multi-agent AI web application designed to help college students organize their studies, analyze study notes, and practice through AI-generated quizzes.

The application uses three specialized AI agents:

1. Study Planner Agent
2. Notes Analyzer Agent
3. Quiz Agent

The agents use Ollama and the Llama 3.2 model for AI-powered processing.

## Features

### 1. Study Planner Agent

The Study Planner Agent creates a study schedule based on:

- Subjects
- Available study hours
- Number of study days

### 2. Notes Analyzer Agent

The Notes Analyzer Agent analyzes student notes and provides:

- Summary
- Important topics
- Study recommendations

### 3. Quiz Agent

The Quiz Agent generates multiple-choice questions from the student's study notes.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Ollama
- Llama 3.2
- REST API

## System Architecture

Student
↓
Flask Web Application
↓
AI Agents
├── Study Planner Agent
├── Notes Analyzer Agent
└── Quiz Agent
↓
Ollama
↓
Llama 3.2
↓
AI Study Results

## How to Run

### Step 1

Install Python.

### Step 2

Install Ollama and download the Llama 3.2 model.

### Step 3

Create and activate the virtual environment.

### Step 4

Install dependencies:

pip install -r requirements.txt

### Step 5

Start the Flask application:

python app.py

### Step 6

Open the application in a browser:

http://127.0.0.1:5000

## Project Objective

The objective of this project is to demonstrate how multiple specialized AI agents can be integrated into a web application to provide personalized educational assistance.

## Conclusion

The AI Student Study Planner provides an intelligent learning assistant that helps students plan their studies, understand their notes, and test their knowledge using AI.