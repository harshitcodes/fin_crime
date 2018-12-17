# fin_crime
Financial Crime Analysis

## How to run the Queries in the project

1. Create a new python3 virtual environment using `virtualenv -p python3 <env_name>`
2. Unzip the folder, cd into ques123.
3. In your terminal, run `pip install -r requirements.txt`
4. Now create a postgres database to load the CSV into sql.
5. Add the required credentials in teh `db_cred.py` file.
6. Now run `python create_table.py` - this creates the schema.
7. To load the data in the tables, run `python load_data.py`
8. Now to run any query, run `python query.py`

## You can access the Jupyter notebook online as well: 

[https://github.com/harshitcodes/fin_crime/blob/master/find_fraudsters.ipynb](https://github.com/harshitcodes/fin_crime/blob/master/find_fraudsters.ipynb)

Otherwise, here are the steps:

1. Run jupyter-notebook kernel on your terminal with the same env activated using `jupyter-notebook`
2. Now, you scroll through the notebook.
3. Run each cell by pressing `<shift + enter>` keys on your keyboard.


There are two flow diagrams in the folder `question4`
1. `fraud_prevention_flow.xml` - this is a flow diagram comprising processes and checks in order to prevent and stop crimes.
2. `fraud_detection_modeling.xml` - this is a flow diagram to analyse past transactions and model a technique to detect fraudsters better.


