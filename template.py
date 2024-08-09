import os
import logging
from pathlib import Path  # Path to handle differnrt styles of defining directories & files distinations in CLI, cmd/bash


# src -> folder contains slource code
# components -> folder has several files for the pipeline of different ML project stages, like..data ingesttion, EDA, Feature Engineering, model building, evaluation,...

list_of_files = [

    ".github/workflows/.gitkeep",

    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",      # --> NO files, only folders

    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",

    "experiment/experiments.ipynb"
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":  #if the file directory is not empty 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass # to just create the empty file, fill with code later