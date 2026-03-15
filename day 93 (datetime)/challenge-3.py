# 3️⃣ Days Between Two Dates Given: d1 = "2026-01-01" d2 = "2026-12-31" Find how many days are between them.

from datetime import datetime 

date_1 =datetime.strptime("2026-01-01", "%Y-%m-%d")

date_2 =datetime.strptime("2026-12-3", "%Y-%m-%d")

diff=(date_2 - date_1).days

print(diff)
