import os
# Path to handle differnrt styles of defining directories & files distinations in CLI, cmd/bash
from pathlib import Path


# src -> folder contains slource code
# components -> folder has several files for the pipeline of different ML project stages, like..data ingesttion, EDA, Feature Engineering, model building, evaluation,...

list_of_files = [

    ".github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    
]

