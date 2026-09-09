<h1 align="center">Hi, I'm Hariharan Loganathan</h1>
<h3 align="center">AI Engineer · Founding SWE @ CEART · Founding Engineer @ GeneGenius · MSCS @ NYU '26 · Ex-Zenoti</h3>

---

### About Me

- **Founding Software Engineer @ CEART**: AI-powered due diligence for renewable energy developments (CEARTscore); I work across the Next.js/Supabase scoring dashboard and the Python event-sourced analysis worker on Railway
- **Founding Engineer @ GeneGenius**: early-stage AI platform for clinical genomic variant interpretation (NVIDIA Inception member)
- M.S. in Computer Science @ **NYU** (2024–2026) · TA for Information Visualization & Information Security
- 3 years @ **Zenoti** as a Software Engineer: C#/.NET microservices, Kafka event pipelines, and high-throughput backend systems serving 1,000+ globally distributed nodes
- Contributing to open source

---

### Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/hariharan-loganathan-1615b7169)
[![Portfolio](https://img.shields.io/badge/Portfolio-000?style=for-the-badge&logo=firefox&logoColor=white)](https://hariharan-l-portfolio.netlify.app/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hariharan.poru@gmail.com)

---

### Highlight Projects

#### [Time-Series Foundation Models vs HAR](https://github.com/hariharan-brucewayne220/rv-tsfm-bench): Realized-Volatility Benchmark
> Do zero-shot foundation models beat a twenty-year-old econometric baseline? Mostly no, and the write-up says so
- Chronos-Bolt and Granite TTM against HAR/GARCH across 30 assets plus true 5-minute crypto RV
- Parity at h=1 on daily proxies, a genuine win on crypto, decisive losses at h=5 and h=22; the daily edge disappears under Mincer-Zarnowitz recalibration, so it was scaling rather than skill
- Lookahead and Diebold-Mariano are unit-tested rather than asserted
- Python · PyTorch · statsmodels · arch

#### [GitHub Ecosystem Analytics](https://github.com/Shreyas191/Github-Analytics): Lambda-Architecture Data Platform
> Predicting which new repositories reach 1,000 stars within 90 days, from batch and stream at once
- Batch: GitHub Archive → HDFS/Parquet via PySpark → Spark MLlib RandomForest, evaluated on PR-AUC
- Streaming: Events API → Kafka → Structured Streaming on 5-minute windows → InfluxDB → Grafana
- Data Infrastructure Lead on a 4-person team: the batch layer, both Airflow DAGs, the 15-service topology, and the project's only test suite (261 cases)
- Python · Spark · Kafka · Airflow · HDFS · InfluxDB · Grafana

#### [Sentinel](https://github.com/hariharan-brucewayne220/sentinel-blockchain-agent): Autonomous Agent with On-Chain Guardrails
> The LLM only proposes a trade; a smart contract decides whether it happens
- `PolicyGuard` enforces token allowlists, Chainlink-priced caps with staleness reverts, cooldowns and a drawdown window — a violating proposal reverts regardless of what the model concluded
- ERC-4337 v0.7 packed UserOperations built and signed by hand in Python, submitted through a Pimlico bundler
- Every decision's reasoning pinned to IPFS with the CID in calldata, surfaced by a "WHY?" button over a subgraph
- 41 Foundry tests (incl. fuzz) + 35 pytest, with a cross-language test pinning the paymaster packing against the EntryPoint's own unpacker
- Testnet demonstrator: swaps run against a mock DEX, and the ZK attestation path is scaffolding
- Solidity · Foundry · Python · LangGraph · Next.js · The Graph

#### [RevLens](https://github.com/hariharan-brucewayne220/rev-lens): Multi-Tenant Sales Call Intelligence
> B2B SaaS turning raw sales calls into pipeline health scores, objections and buying signals
- Three-stage Inngest event chain: Whisper transcription → GPT-4o structured extraction → health-score delta
- Org scoping in the data layer rather than per route, verified with real cross-tenant requests; AES-256-GCM per-org key storage; 20-model Prisma schema
- Next.js · TypeScript · Inngest · Whisper · GPT-4o · Prisma · PostgreSQL

#### [City Witness](https://github.com/hariharan-brucewayne220/city_pulse): Real-Time Voice+Vision AI Agent
> Point your camera at anything in NYC; the agent sees it, narrates live, and pulls city data for that exact location
- Gemini Live bidirectional audio+vision streaming, with a parallel ADK multi-agent path running SQL over DuckDB through MCP
- Grounded in NYC Open Data (311, restaurant inspections, crime) for the caller's location
- Python · FastAPI · Gemini Live · Google ADK · MCP · DuckDB · Cloud Run
- Built at NYC Build With AI Hackathon, NYU Tandon

#### [AI Financial Advisor](https://github.com/hariharan-brucewayne220/ai-financial-advisor): Hybrid-Retrieval RAG with LangGraph
> Document-grounded financial Q&A with citation-backed answers and redaction before indexing
- Hybrid retrieval: HyDE-expanded queries over pgvector and per-client BM25, fused with reciprocal rank fusion
- A LangGraph agent that re-retrieves and regenerates when its own faithfulness score falls below threshold
- PII detected and redacted before chunking, so client identifiers never reach the vector store
- FastAPI · React · pgvector · LangGraph · Presidio

#### [MacroDash](https://d389ljtx6u31j8.cloudfront.net/): Agentic Investment Research Platform (Live)
> Macro, markets and crypto in one dashboard, with LLM analysts running on a schedule
- Portfolio BUY/SELL/HOLD and news-synthesis agents on a 6-hourly scheduler, emailing opted-in users
- FRED, BLS, Yahoo Finance and crypto feeds; technical indicators, custom formula charts, price alerts and watchlists
- Owned the backend and most features on a 5-person team (119 of 234 commits)
- Django REST · React · PostgreSQL · MongoDB · APScheduler · AWS (Lightsail, S3, CloudFront)

#### [Sentinel](https://github.com/hariharan-brucewayne220/sentinal-anomoly-detection): End-to-End MLOps Pipeline
> An anomaly detector taken through the whole lifecycle, not just trained
- Isolation Forest on NAB sensor data — ROC-AUC 0.8233, F1 48.26% against the four labelled failure windows, reproducible offline from the persisted model
- MLflow tracking, FastAPI serving, Evidently drift and data-quality reports, Streamlit dashboard
- CI runs lint → tests → image build → container smoke test → Docker Hub on every push to main
- scikit-learn · MLflow · Evidently · Docker · GitHub Actions · Railway

#### [LLM Red Team Platform](https://github.com/hariharan-brucewayne220/task-llm): Adversarial Assessment Harness
> Runs adversarial suites against a target model and scores what comes back
- Five attack categories — jailbreak, bias, hallucination, privacy leakage, manipulation — over OpenAI, Anthropic and Google behind one client abstraction
- Background run queue with working pause/resume/stop and live Socket.IO progress; PDF and CSV export
- Scoring runs as either a named keyword heuristic or a real LLM judge, chosen explicitly rather than one masquerading as the other
- Next.js · TypeScript · Flask · Socket.IO · SQLAlchemy

#### [API Monitor](https://github.com/hariharan-brucewayne220/distributed-api-monitor): Go Health Checker with Local LLM Insights
> Concurrent endpoint checks, Postgres history, and a language model running on my own hardware
- Goroutine fan-out with per-target status, latency and health, behind a JSON API and a live dashboard
- Insights from a locally hosted GGUF model over an OpenAI-compatible shim, degrading to deterministic rule-based output when it is unreachable
- History behind a `Store` interface: Postgres when configured, in-memory otherwise, with an idempotent schema migration and 28 tests
- Go · PostgreSQL · Docker · llama.cpp

#### [AI Gesture Gaming Controller](https://github.com/hariharan-brucewayne220/ai-gesture-gaming-controller): CV + Voice Game Input
> Replacing keyboard and mouse with a webcam and a microphone
- MediaPipe Hands with rule-based landmark heuristics and majority-vote smoothing, plus an optional trained MLP classifier
- Face Mesh eye-aspect-ratio wink detection for aim-hold; DirectInput scan-code injection so AAA titles register the keys
- Offline-first voice via Vosk with cloud fallbacks, and an LLM used once to map a game's control scheme onto available gestures
- Python · MediaPipe · OpenCV · scikit-learn · Vosk · Groq

---

### Open Source

- **[orval](https://github.com/orval-labs/orval)** (OpenAPI → TypeScript client generator): fixed mock generation leaking runtime enum imports into generated clients, which broke `consistent-type-imports` for consumers ([#4009](https://github.com/orval-labs/orval/pull/4009) ![merged](https://img.shields.io/badge/merged-2ea44f?style=flat-square), follow-up [#4010](https://github.com/orval-labs/orval/pull/4010) ![merged](https://img.shields.io/badge/merged-2ea44f?style=flat-square))
- **[Mastra](https://github.com/mastra-ai/mastra)** (TypeScript AI agent framework): memory recall no longer requests vector search when no vector store is configured ([#20941](https://github.com/mastra-ai/mastra/pull/20941) ![merged](https://img.shields.io/badge/merged-2ea44f?style=flat-square))
- **[DSPy](https://github.com/stanfordnlp/dspy)** (Stanford NLP): fixes for multimodal file/video block handling ([#9903](https://github.com/stanfordnlp/dspy/pull/9903) ![open](https://img.shields.io/badge/open-d4a017?style=flat-square)) and chat-history formatting in system prompts ([#9905](https://github.com/stanfordnlp/dspy/pull/9905) ![open](https://img.shields.io/badge/open-d4a017?style=flat-square))
- **[typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)**: `no-unnecessary-type-assertion` no longer reports number-to-enum assertions, which are mutually assignable but not the same type ([#12835](https://github.com/typescript-eslint/typescript-eslint/pull/12835) ![open](https://img.shields.io/badge/open-d4a017?style=flat-square))
- **[Langfuse](https://github.com/langfuse/langfuse)** (LLM observability): batched a per-user notification-preference lookup that ran one query per mentioned user inside a loop ([#15895](https://github.com/langfuse/langfuse/pull/15895) ![open](https://img.shields.io/badge/open-d4a017?style=flat-square))

---

### Tech Stack

**Languages**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![C#](https://img.shields.io/badge/C%23-239120?style=flat&logo=csharp&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat&logo=solidity&logoColor=white)

**AI / LLM**
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai)
![Anthropic](https://img.shields.io/badge/Anthropic-191919?style=flat&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat&logo=googlegemini&logoColor=white)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logoColor=black)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)

**Backend & Data**
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-4169E1?style=flat)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apachekafka)
![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat&logo=apacheairflow&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)

**Frontend**
![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=nextdotjs&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat&logo=tailwindcss&logoColor=white)

**Cloud & DevOps**
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonwebservices&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

---

### GitHub Stats

<p>
  <img src="generated/stats.svg" alt="Hariharan's GitHub Stats" />
  <img src="generated/top-langs.svg" alt="Most Used Languages" />
</p>

<sub>Stats generated weekly from the GitHub API by <a href=".github/workflows/update-stats.yml">a GitHub Action</a>.</sub>

---
