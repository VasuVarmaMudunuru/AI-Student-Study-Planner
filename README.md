\# AI Student Study Planner



An AI-powered multi-agent web application designed to help students plan their studies, analyze notes, and generate quizzes using a locally running Large Language Model (LLM).



The application is built using Flask and Ollama and provides a simple web interface for students to organize and improve their learning process.



\---



\## Project Overview



Students often struggle with organizing study schedules, understanding large amounts of study material, and preparing for examinations.



The \*\*AI Student Study Planner\*\* addresses these challenges through multiple AI-powered agents:



\- \*\*Study Planner Agent\*\* – Creates a personalized study plan based on subjects, available study hours, and number of days.

\- \*\*Notes Analyzer Agent\*\* – Analyzes study notes and generates useful summaries and important topics.

\- \*\*Quiz Agent\*\* – Generates multiple-choice questions from the provided study material.



The agents work together to provide a simple AI-assisted study experience.



\---



\## Features



\### 1. AI Study Planner



Creates a study schedule based on:



\- Subjects

\- Available study hours

\- Number of study days



The AI generates a structured plan to help students organize their preparation.



\### 2. Notes Analyzer



Students can enter their study notes and use the AI to:



\- Summarize the content

\- Identify important topics

\- Highlight key information

\- Provide study recommendations



\### 3. AI Quiz Generator



The Quiz Agent generates multiple-choice questions from the student's notes.



This can be used for:



\- Self-assessment

\- Exam preparation

\- Revision

\- Practice testing



\### 4. Multi-Agent Architecture



The application uses separate AI agents for different tasks:



```text

&#x20;                   AI Student Study Planner

&#x20;                             |

&#x20;             +---------------+---------------+

&#x20;             |               |               |

&#x20;             v               v               v

&#x20;      Study Planner    Notes Analyzer    Quiz Generator

&#x20;          Agent             Agent             Agent

&#x20;             |               |               |

&#x20;             +---------------+---------------+

&#x20;                             |

&#x20;                             v

&#x20;                        Ollama LLM

&#x20;                      llama3.2:3b

