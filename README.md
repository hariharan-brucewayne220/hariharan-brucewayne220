<h1 align="center">Hi 👋, I'm Hariharan Loganathan</h1>
<h3 align="center">AI Engineer · Founding Engineer @ GeneGenius · MSCS @ NYU '26 · Ex-Zenoti</h3>

---

### 🧠 About Me

- 🧬 **Founding Engineer @ GeneGenius**: early-stage AI platform for clinical genomic variant interpretation (NVIDIA Inception member)
- 🤖 I build **agentic LLM systems**: RAG pipelines, LangGraph agents, real-time voice+vision AI, and LLM evaluation platforms
- 🎓 M.S. in Computer Science @ **NYU** (2024–2026) · TA for Information Visualization & Information Security
- 🏗️ 3 years @ **Zenoti** as a Software Engineer: C#/.NET microservices, Kafka event pipelines, and high-throughput backend systems serving 1,000+ globally distributed nodes
- 🌱 Contributing to open source: **[DSPy](https://github.com/stanfordnlp/dspy)** (Stanford NLP)
- ⚡ Fun fact: My side projects have <100ms latency. My sleep schedule doesn't.

---

### 🌐 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/hariharan-loganathan-1615b7169)
[![Portfolio](https://img.shields.io/badge/Portfolio-000?style=for-the-badge&logo=firefox&logoColor=white)](https://hariharan-l-portfolio.netlify.app/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hariharan.poru@gmail.com)

---

### 🚀 Highlight Projects

#### 🗽 [City Witness](https://github.com/hariharan-brucewayne220/city_pulse): Real-Time Voice+Vision AI Agent
> Point your camera at anything in NYC; the agent sees it, narrates live, and pulls city data for that exact location
- Gemini Live API (bidirectional audio+vision streaming) + NYC Open Data (311, inspections, crime stats)
- Voice follow-up Q&A grounded in live civic data
- 🛠️ Python · FastAPI · Gemini Live · Google ADK · MCP · DuckDB · Cloud Run
- 🏆 Built at NYC Build With AI Hackathon, NYU Tandon

#### 📞 [RevLens](https://github.com/hariharan-brucewayne220/rev-lens): Multi-Tenant Sales Call Intelligence SaaS
> B2B SaaS that turns raw sales calls into pipeline health scores, objections, and buying signals
- 3-stage Inngest event pipeline: Whisper transcription → GPT-4o structured analysis → health score deltas
- Org-scoped data isolation, role-gated APIs, AES-256-GCM encryption, 20+ model Prisma/PostgreSQL schema
- 🛠️ Next.js · TypeScript · Inngest · Whisper · GPT-4o · Prisma · PostgreSQL

#### 📡 [Distributed API Monitor](https://github.com/hariharan-brucewayne220/distributed-api-monitor): Go ML-Serving Health Monitor
> Low-latency monitoring system simulating model-serving health across 1,000+ endpoints
- Goroutine-per-endpoint fan-out, buffered channel backpressure, graceful shutdown
- Prometheus metrics, gRPC streaming, 3-tier AI degradation (OpenAI → local GGUF → rule-based)
- 🛠️ Go · Prometheus · gRPC · Docker · PostgreSQL

#### 💰 [AI Financial Advisor](https://github.com/hariharan-brucewayne220/ai-financial-advisor): RAG Platform with LangGraph Agents
> Document-grounded financial Q&A with sub-second retrieval and citation-backed answers
- Hybrid retrieval: dense embeddings + BM25 + HyDE with RRF reranking
- LangGraph agents for multi-step reasoning and automated report generation
- 🛠️ FastAPI · React · pgvector · Redis · LangGraph · AWS

#### 📈 [MacroDash](https://d389ljtx6u31j8.cloudfront.net/): Agentic AI Investment Research Platform (Live)
> Daily BUY/SELL/HOLD recommendations from news sentiment + 14,000+ FRED macro indicators
- Agentic LLM workflow with ARIMA forecasting via scheduled background jobs
- 🛠️ Django REST · React · PostgreSQL · Redis · AWS (CloudFront, S3, EC2)

#### 🎮 [AI Gesture Gaming Controller](https://github.com/hariharan-brucewayne220/ai-gesture-gaming-controller): CV + ML Game Input
> Full keyboard/mouse replacement: hand gestures, wink detection, head tracking, and voice commands
- 5-thread lock-free architecture fusing MediaPipe landmarks, LSTM sequence model, and 3 STT engines at 60 FPS
- 🛠️ Python · MediaPipe · PyTorch · OpenCV · Vosk · Whisper

#### 🔍 [Sentinel](https://github.com/hariharan-brucewayne220/sentinal-anomoly-detection): Production MLOps Pipeline
> End-to-end anomaly detection with drift monitoring and automated deploys
- Isolation Forest on NAB sensor data (ROC-AUC 0.82), MLflow tracking + model registry
- Evidently drift alerts → Slack, full CI/CD via GitHub Actions
- 🛠️ MLflow · Evidently · Docker · GitHub Actions · Railway

---

### 🌱 Open Source

- **[DSPy](https://github.com/stanfordnlp/dspy)** (Stanford NLP): fixes for multimodal file/video block handling ([#9903](https://github.com/stanfordnlp/dspy/pull/9903)) and chat-history formatting in system prompts ([#9905](https://github.com/stanfordnlp/dspy/pull/9905))

---

### 🧰 Tech Stack

**Languages**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![C#](https://img.shields.io/badge/C%23-239120?style=flat&logo=csharp&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)

**AI / LLM**
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai)
![Anthropic](https://img.shields.io/badge/Anthropic-191919?style=flat&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat&logo=googlegemini&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗%20Hugging%20Face-FFD21E?style=flat&logoColor=black)

**Backend & Data**
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-4169E1?style=flat)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apachekafka)
![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)

**Frontend**
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=nextdotjs&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat&logo=tailwindcss&logoColor=white)

**Cloud & DevOps**
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

---

### 📊 GitHub Stats

<p>
  <img src="generated/stats.svg" alt="Hariharan's GitHub Stats" />
  <img src="generated/top-langs.svg" alt="Most Used Languages" />
</p>

<sub>Stats generated weekly from the GitHub API by <a href=".github/workflows/update-stats.yml">a GitHub Action</a>.</sub>

---

> *"I build systems that think. Then I teach them to listen."*
