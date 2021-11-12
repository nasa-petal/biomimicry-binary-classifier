import pandas as pd
import os 

# !pip install wandb -qqq
# import wandb
# wandb.login()

# for run in range(1):
  # Start a new run to track this script
  # wandb.init(
  #     # Set entity to specify your username or team name
  #     # ex: entity="aralevski",
  #     # Set the project where this run will be logged
  #     project="SciBERT", 
  #     # Track hyperparameters and run metadata
  #     config={
  #     "learning_rate": 0.02,
  #     "architecture": "CNN",
  #     "dataset": "golden_abbr.csv",})

def convert_golden_to_csv():
    df = pd.read_json('petal-labeler-data-pipeline\FinalFile\golden.json')
    df.to_csv(index=False)
    df2 = df.copy(deep=True)
    df2.drop(columns=['paper', 'mag', 'venue_mag', 'author', 'reference', 'venue', 'level1', 'level2', 'level3', 'url','fullDocLink', 'isOpenAccess'], inplace=True)
    df2.to_csv('scibert_golden.csv', index=False)
    print(df2.columns)

convert_golden_to_csv()

os.system('binary_labeler_scibert_new.py')

# wandb.log({"acc":acc, "loss":loss})

  # Mark the run as finished
# wandb.finish()