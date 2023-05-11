# Advanced_python

Code for Advanced Python training, along with solutions and dummy data

## Create environment and install dependencies

I have only tested the creation of virtual environments with `pip` and `conda`

Create a new environment with `venv` with the command `python3 -m venv /path/to/new/virtual/environment` and activate with `source /path/to/your/environment/bin/activate
` on Linux or MacOS or `\path\to\your\environment\Scripts\activate`
To create a virtual environment with `conda` and install dependencies at the same time you can simply use the `conda env create -f environment.yml` command. Alternatively you can create you own environment and use `pip`

Once you've activated your environment you can install the dependencies with `pip` using `pip install -r requirements.txt`

## Structure

notebooks contains the exercises. Please note that one of the exercises isn't actually a notebook, but a vanilla `.py` file. This is due to multiprocessing not allowing for execution in notebooks or IDE interactive consoles, and obviously as a result this can be edited anywhere, but must be run via the terminal using `python multi.py`

models contains subfolders for the individual sections, along with the solutions as well as code that was used to generate dummy data

Finally data contains the data used in the exercises along with some solution data for the exercises that have a fixed solution.
