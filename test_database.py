import sqlite3
import pandas as pd

conn = sqlite3.connect("mutual_fund_analysis.db")

query = """
SELECT fund_house, COUNT(*) AS total_schemes
FROM fund_master
GROUP BY fund_house
ORDER BY total_schemes DESC;
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()