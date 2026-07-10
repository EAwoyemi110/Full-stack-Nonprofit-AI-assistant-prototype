# NonProfSupport

An AI-powered Streamlit application designed for community nonprofits to automatically triage, categorize, and draft initial empathetic responses for incoming community assistance requests.

**Live Application:** [https://nonprofsupport.streamlit.app/](https://nonprofsupport.streamlit.app/)

## Project Inspiration & Mission

This project was inspired by the Claude Corps project and its mission to leverage artificial intelligence for public good and civic support. It was built to demonstrate my full-stack development skills and show how modern generative AI can be practically integrated into real-world workflows. By automating administrative triaging, this tool allows nonprofit coordinators to respond to community crises faster, proving my passion for building mission-driven technology that scales human impact.

---

## Features

* **Automated Triage:** Instantly categorizes incoming emails and requests into defined buckets: Crisis, Funding, Volunteer, or General.
* **Entity Extraction:** Automatically parses out primary contacts, secondary contacts, urgent core needs, and highlights potential input errors like missing email domains.
* **Executive Summarization:** Generates a concise, two-sentence summary of the request for rapid internal review.
* **Empathetic Draft Generator:** Creates a professional, highly contextual initial response email ready to be tailored and sent.
* **Robust Processing Pipeline:** Implements a parsing structure that handles Claude's content blocks safely, ensuring hidden thinking structures are filtered out before displaying the final output.

---

## Technical Architecture & AI Integration

The application uses a full-stack Python architecture. Streamlit serves as the interactive web frontend, communicating directly with the Anthropic API on the backend. 

* **Model Used:** Claude 3.5 Sonnet (`claude-3-5-sonnet-latest`)
* **Prompt Engineering:** The core logic relies on a structured system instruction block that forces the model to act as an expert administrative assistant and output data in a predictable, standardized markdown hierarchy.
* **Response Parsing:** The application programmatically loops through the model's message content blocks to safely extract text content while filtering out native AI thinking processes.

---

## Installation & Local Setup

To run this prototype locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/NonProfSupport.git](https://github.com/YOUR_USERNAME/NonProfSupport.git)
cd NonProfSupport/Light-AI-Prototyper-Claude
