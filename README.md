# Raffle Selection

Raffle Selection is a Python-based application designed to randomly select a specified number of records from a dataset for prize raffling purposes. It ensures that once a record is selected, it is removed from future iterations, preventing duplicate winners.

## Features

- Random selection of records from a dataset.
- Ensures unique selections by removing chosen records from subsequent draws.
- User-friendly graphical interface built with Tkinter.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Anaconda](https://www.anaconda.com/products/distribution) (for managing the virtual environment)
- [Git](https://git-scm.com/) (for cloning the repository)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bofethe/raffle-selection.git
   cd raffle-selection
   ```
2. **Create the Python Environment** *(you'll need tkinter and pandas)*:
   ```bash
   conda env create -f requirements.yml
   conda activate raffle-selection
   ```
4. **Launch the Application**:
```bash
python gui.py
```
4. **Use the Application**:
   + Add the path to the xlsx (relative or absolute)
   + Specify the unique field, such as full name.  Duplicates will be dropped
   + Pick the selection size
   + repeat as many times as needed, or re-load the data to start over with the full list
