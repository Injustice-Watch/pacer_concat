import csv
import glob
import os
import pandas as pd

#convert files to csv

txt_files = os.path.join('txt', '*.txt')
output = 'output/individuals'

for txt_file in glob.glob(txt_files):
    with open(txt_file, 'rb') as input_file:
        in_txt = csv.reader(input_file, delimiter='|')
        filename = os.path.splitext(os.path.basename(txt_file))[0] + '.csv'
        
        with open(os.path.join(output, filename), 'wb') as output_file:
            out_csv = csv.writer(output_file)
            out_csv.writerows(in_txt)

path = r'output/individuals'    
                 
all_files = glob.glob(os.path.join(path, "*.csv"))     

df_from_each_file = (pd.read_csv(f) for f in all_files)

df = pd.concat(df_from_each_file, ignore_index=False, keys=all_files)

df.to_csv('output/output.csv')