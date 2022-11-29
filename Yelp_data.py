import json
import pandas as pd
data_file = open("yelp_academic_dataset_checkin.json")
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)
data_file.close()
print("Shape is: " + str(checkin_df.shape))
print(checkin_df.head())