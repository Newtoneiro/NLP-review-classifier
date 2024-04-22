# NLP-reviews-classifier

This project aims to train a model which will classify hotel reviews as number of stars

## Project setup

- Step 1: Install Git LFS

  - If you haven't already installed Git LFS, you can download and install it from the official website or use a package manager like Homebrew (for macOS) or Chocolatey (for Windows). Refer to the Git LFS documentation for detailed installation instructions.

- Step 2: Clone the Repository

  - To clone a repository with LFS files, use the git clone command followed by the repository URL:

    `git clone https://github.com/Newtoneiro/NLP-review-classifier`

- Step 3: Fetch LFS Files

  - Once the repository is cloned, navigate into the repository directory and run the following command to fetch the LFS files:

    `git lfs pull`

  - This command downloads the LFS-tracked files associated with the repository.

- Step 4: Pull Updates

  - If you've previously cloned the repository and new LFS files have been added or modified, you can pull the updates using the standard git pull command:

    `git pull`

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py < - This script was used to convert 50M record dataset into arround 1M records.
    |   |   └── data_preprocess.ipynb <- This script preprocesses and balances the 1M records dataset (data.zip)
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
