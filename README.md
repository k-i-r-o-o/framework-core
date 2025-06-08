# framework-core
core framework


#project structre
framework-core/
│
├── core/
│   ├── config/
│   │   └── loader.py
│   ├── interfaces/
│   │   ├── base_ingestor.py
│   │   ├── base_executor.py
│   ├── vector_store/
│   │   ├── base_store.py
│   │   ├── chroma_store.py
│   ├── models/
│   │   ├── document.py
│   │   ├── embedding.py
│   ├── utils/
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── helpers.py
│
├── pyproject.toml
├── README.md
└── tests/
