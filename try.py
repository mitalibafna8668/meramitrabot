import pandas as pd 
import glob
import os

folder_path = r""
file_path = r"C:\Users\DELL\Desktop\intents" 
files = r"C:\Users\DELL\Desktop\intents\Noise*.json"
json_files = os.path.join(folder_path, file_path, files)
out_csv = r"C:\Users\DELL\Desktop\intents\Noise.csv"
file_list = [] 
df_list = [] 

for file in glob.glob(json_files):
    allFiles = file_list.append(file)
    print(file_list)
for item in file_list:
    pd_files = pd.read_json(item, lines = True)
    df_list.append(item)
    print(df_list)
for i in df_list:
    pdf = pd.DataFrame(i)
pdf.to_csv(out_csv)