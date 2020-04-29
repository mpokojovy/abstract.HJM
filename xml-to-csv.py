% Copyright   : Valerii Maltsev & Michael Pokojovy (2020)
% Version     : 1.0
% Last edited : 04/19/2020
% License     : Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
%               https://creativecommons.org/licenses/by-sa/4.0/

import pandas as pd 
import xml.etree.ElementTree as et 

ns = {'d': 'http://schemas.microsoft.com/ado/2007/08/dataservices',
      'm': 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata',
      'b': 'http://www.w3.org/2005/Atom'}

xroot = et.parse("yield.xml").getroot()

df_cols = ["NEW_DATE",
           "BC_1MONTH", 
           "BC_2MONTH", 
           "BC_3MONTH", 
           "BC_6MONTH", 
           "BC_1YEAR", 
           "BC_2YEAR", 
           "BC_3YEAR", 
           "BC_5YEAR", 
           "BC_7YEAR", 
           "BC_10YEAR", 
           "BC_20YEAR", 
           "BC_30YEAR", 
           "BC_30YEARDISPLAY"]
rows = []


for node in xroot.findall("b:entry", ns):
    print(node)
    node = node.find("b:content", ns)
    print(node)
    node = node.find("m:properties", ns)
    print(node)
    NEW_DATE = node.find("d:NEW_DATE", ns).text if node is not None else None
    BC_1MONTH = node.find("d:BC_1MONTH", ns).text if node is not None else None
    BC_2MONTH = node.find("d:BC_2MONTH", ns).text if node is not None else None
    BC_3MONTH = node.find("d:BC_3MONTH", ns).text if node is not None else None
    BC_6MONTH = node.find("d:BC_6MONTH", ns).text if node is not None else None
    BC_1YEAR = node.find("d:BC_1YEAR", ns).text if node is not None else None
    BC_2YEAR = node.find("d:BC_2YEAR", ns).text if node is not None else None
    BC_3YEAR = node.find("d:BC_3YEAR", ns).text if node is not None else None
    BC_5YEAR = node.find("d:BC_5YEAR", ns).text if node is not None else None
    BC_7YEAR = node.find("d:BC_7YEAR", ns).text if node is not None else None
    BC_10YEAR = node.find("d:BC_10YEAR", ns).text if node is not None else None
    BC_20YEAR = node.find("d:BC_20YEAR", ns).text if node is not None else None
    BC_30YEAR = node.find("d:BC_30YEAR", ns).text if node is not None else None
    BC_30YEARDISPLAY = node.find("d:BC_30YEARDISPLAY", ns).text if node is not None else None
    rows.append({"NEW_DATE": NEW_DATE, 
                 "BC_1MONTH": BC_1MONTH, 
                 "BC_2MONTH": BC_2MONTH, 
                 "BC_3MONTH": BC_3MONTH,
                 "BC_6MONTH": BC_6MONTH, 
                 "BC_1YEAR": BC_1YEAR, 
                 "BC_2YEAR": BC_2YEAR,
                 "BC_3YEAR": BC_3YEAR, 
                 "BC_5YEAR": BC_5YEAR, 
                 "BC_7YEAR": BC_7YEAR,
                 "BC_10YEAR": BC_10YEAR, 
                 "BC_20YEAR": BC_20YEAR, 
                 "BC_30YEAR": BC_30YEAR,
                 "BC_30YEARDISPLAY": BC_30YEARDISPLAY
                 })

out_df = pd.DataFrame(rows, columns=df_cols)
out_df.to_csv(path_or_buf="D:\Python scripts\yield.csv", index = False)