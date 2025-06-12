# framework-core
core framework


#project structre
framework-core/
├── core/                                 # Core abstractions, types, utilities
│   ├── interfaces/
│   │   ├── data/
│   │   │   ├── document.py               # IDocument
│   │   │   └── embedding.py              # IEmbedding
│   │   ├── services/
│   │   │   ├── logger.py                 # ILogger
│   │   │   └── cache.py                  # ICache
│   │   └── stores/
│   │       ├── vector_store.py           # IVectorStore
│   │       └── graph_store.py            # IGraphStore
│
│   ├── connectors/                       # Concrete implementations (pluggable)
│   │   ├── vector_stores/
│   │   │   ├── qdrant.py
│   │   │   ├── chroma.py
│   │   │   └── factory.py
│   │   ├── databases/
│   │   │   └── mongo.py
│   │   ├── apis/
│   │   │   ├── openai.py
│   │   │   └── huggingface.py
│   │   └── llms/
│   │       ├── openai_llm.py             # OpenAI GPT wrappers
│   │       └── local_llm.py              # For ollama, vllm, etc.
│
│   ├── config/
│   │   ├── loader.py
│   │   └── schemas/
│   │       ├── vector_store.yaml
│   │       └── logging.yaml
│
│   ├── exceptions/
│   │   ├── base.py
│   │   ├── vector.py
│   │   └── config.py
│
│   ├── types/
│   │   ├── document.py
│   │   └── embedding.py
│
│   ├── utilities/
│   │   ├── hashing/
│   │   │   ├── simhash.py
│   │   │   └── minhash.py
│   │   ├── serialization/
│   │   │   ├── arrow.py
│   │   │   └── protobuf.py
│   │   └── concurrency/
│   │       ├── async_utils.py
│   │       └── redis_queue.py
│
│   ├── telemetry/
│   │   ├── opentelemetry.py
│   │   └── log_formatter.py
│
│   └── registry.py
│
├── agents/                               # Agent classes and loop logic
│   ├── base.py                           # BaseAgent: think(), act(), observe()
│   ├── planner.py                        # Chain-of-thought, task planning
│   ├── executor.py                       # Runs the agent loop (reAct, ToolFormer-style)
│   ├── memory/
│   │   ├── long_term.py                  # VectorStore-backed memory
│   │   └── short_term.py                 # Cache-based session memory
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── search.py                     # External search tool
│   │   ├── calculator.py
│   │   ├── data_loader.py
│   │   └── tool_base.py                  # ITool: run(input) → output
│   └── types.py                          # Observation, Action, Thought classes
│
├── workflows/                            # Pipeline/workflow runners
│   ├── builder.py                        # Build agent pipelines from config
│   └── executor.py                       # Orchestrate step-by-step execution
│
├── server/                               # Optional server layer (API/gRPC)
│   ├── main.py                           # Entry point (FastAPI, etc.)
│   └── router.py                         # Routes requests to agents/pipelines
│
├── orchestrator/                         # Boot & lifecycle orchestration
│   ├── lifecycle.py
│   └── task_runner.py
│
├── middleware/                           # Cross-cutting logic (fail-safes, retries)
│   ├── retry.py
│   └── circuit_breaker.py
│
├── scheduler/                            # Background cron jobs (APScheduler, etc.)
│   └── cron.py
│
├── plugins/                              # External features (observability, experimentation)
│   ├── tracing_plugin.py
│   └── feature_flags.py
│
├── tests/                                # Test coverage
│   ├── conftest.py
│   ├── test_registry.py
│   ├── test_vector_store.py
│   └── test_agent_loop.py
│
├── docs/                                 # Design docs and usage guides
│   ├── architecture.md
│   ├── agent_lifecycle.md
│   ├── tool_integration.md
│   └── config_examples/
│       ├── vectorstore_qdrant.yaml
│       └── agent_example.yaml
│
├── version.py                            # Version metadata (__version__)
├── README.md
└── pyproject.toml / poetry.lock

