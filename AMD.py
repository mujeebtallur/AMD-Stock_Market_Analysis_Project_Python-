import numpy as np
"""
AMD.py
Short description:
    Script that reads historical AMD stock data from 'amd.csv', converts the 'Date'
    column to datetime, then repeatedly selects month-long date ranges to:
      - print the selected subset,
      - compute and print the monthly mean of either 'Open' or 'Close' prices,
      - plot the daily series for that month and show the plot.
Dependencies:
    - pandas
    - numpy (imported but not necessary for current operations)
    - matplotlib.pyplot
Expected input (amd.csv):
    - A CSV file with at least the following columns:
        - 'Date'  : string or datetime-compatible values (e.g. 'YYYY-MM-DD')
        - 'Open'  : numeric opening price
        - 'Close' : numeric closing price
    - Dates are assumed to be in a format that pandas.to_datetime can parse.
Behavior / side effects:
    - Converts df['Date'] to pandas datetime repeatedly (calling pd.to_datetime many times).
    - For each hard-coded month window the script:
        1. Slices the dataframe using a boolean mask on the 'Date' column.
           The slices use comparisons like "df['Date'] >= 'YYYY-MM-01' and df['Date'] < 'YYYY-MM-DD'".
           Note: this approach mixes inclusive lower-bounds with exclusive upper-bounds.
        2. Prints the sliced DataFrame to stdout.
        3. Computes the mean of the requested price column (Open or Close) and prints it.
        4. Plots the daily series for that month (one plot per iteration) and calls plt.show(),
           which blocks until the figure window is closed.
Known issues / caveats:
    - Repetition: The file contains a very large amount of repeated code (same imports and
      conversion repeated, identical plotting logic). This is fragile and hard to maintain.
    - Date slicing inconsistencies:
        - Many slices use an exclusive upper bound like "< 'YYYY-MM-DD'". If the upper-bound
          string is not the first day of the following month, rows for the actual month's
          last day may be accidentally excluded or included incorrectly.
        - Some months use fixed day counts (e.g. '< "YYYY-02-29"') which is error-prone
          across non-leap years. Prefer using next-month start or month-end-aware logic.
    - Performance: Printing and plotting for every month is slow and may exhaust resources for long spans.
    - Repeated pd.to_datetime calls are unnecessary after the first conversion.
    - numpy is imported repeatedly but not used in the shown logic.
    - The script mixes analysis and plotting: no functions, no return values, and no configurability.
Recommended improvements (refactor suggestions):
    - Convert 'Date' to datetime once, set it as the DataFrame index (df.set_index('Date')).
    - Use pandas time-series tools:
        - df.resample('M').mean() to compute monthly means for 'Open' and 'Close'.
        - df.groupby(df['Date'].dt.to_period('M')).agg(...) to compute monthly aggregates.
    - Replace repetitive blocks with a loop or vectorized operation.
    - Use datetime-aware upper bounds (e.g., use pd.Timestamp(next_month_start) for exclusive upper bounds),
      or use inclusive slicing with between_time / between_dates.
    - Avoid calling plt.show() inside a tight loop; instead, collect subplots and show once, or save figures.
    - Remove duplicate imports and redundant conversions.
    - Add CLI arguments or a small function API so the script can be reused and tested.
    - Add logging instead of printing raw DataFrames for large outputs.
Output:
    - Terminal prints of each monthly DataFrame and its mean price (Open/Close).
    - Individual matplotlib figures for each month displayed interactively.
Examples (behavioral, not code to copy):
    - After running, the user will see many printed DataFrame slices for each month,
      followed by lines like: "August 1992 Mean Opening Price: <value>".
    - A plot window will appear for every month showing the daily Open or Close values.
Testing / validation:
    - Ensure 'Date' parsing succeeds and no NaT values are introduced.
    - Validate that monthly slices include expected calendar days (compare counts to business-day calendar).
    - Check for empty slices (months with no data) before computing mean to avoid NaN confusion.
Author / notes:
    - This docstring documents observed behavior from the provided script selection.
    - Consider modularizing and adding unit tests after refactoring.
"""
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv('amd.csv')

df['Date'] = pd.to_datetime(df['Date'])

Aug2025=df.loc[(df['Date'] >= '2025-08-01') & (df['Date'] < '2025-08-31')]
print(Aug2025)
Aug2025_mean=Aug2025['Close'].mean()
print("August 2025 Mean Closing Price:", Aug2025_mean)
Aug2025.plot(x='Date', y='Close', title='AMD Closing Prices in August 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb1992=df.loc[(df['Date'] >= '1992-02-01') & (df['Date'] < '1992-02-29')]
print(Feb1992)
Feb1992_mean=Feb1992['Open'].mean()
print("February 1992 Mean Opening Price:", Feb1992_mean)

Feb1992.plot(x='Date', y='Open', title='AMD Opening Prices in February 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar1992=df.loc[(df['Date'] >= '1992-03-01') & (df['Date'] < '1992-03-31')]
print(Mar1992)
Mar1992_mean=Mar1992['Open'].mean()
print("March 1992 Mean Opening Price:", Mar1992_mean)

Mar1992.plot(x='Date', y='Open', title='AMD Opening Prices in March 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr1992=df.loc[(df['Date'] >= '1992-04-01') & (df['Date'] < '1992-04-30')]
print(Apr1992)          

Apr1992_mean=Apr1992['Open'].mean()
print("April 1992 Mean Opening Price:", Apr1992_mean)
Apr1992.plot(x='Date', y='Open', title='AMD Opening Prices in April 1992')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
May1992=df.loc[(df['Date'] >= '1992-05-01') & (df['Date'] < '1992-05-31')]
print(May1992)

May1992_mean=May1992['Open'].mean()
print("May 1992 Mean Opening Price:", May1992_mean)
May1992.plot(x='Date', y='Open', title='AMD Opening Prices in May 1992')

plt.xlabel('Date')  
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun1992=df.loc[(df['Date'] >= '1992-06-01') & (df['Date'] < '1992-06-30')]
print(Jun1992)

Jun1992_mean=Jun1992['Open'].mean()
print("June 1992 Mean Opening Price:", Jun1992_mean)

Jun1992.plot(x='Date', y='Open', title='AMD Opening Prices in June 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])

Jul1992=df.loc[(df['Date'] >= '1992-07-01') & (df['Date'] < '1992-07-31')]
print(Jul1992)

Jul1992_mean=Jul1992['Open'].mean()
print("July 1992 Mean Opening Price:", Jul1992_mean)    

Jul1992.plot(x='Date', y='Open', title='AMD Opening Prices in July 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug1992=df.loc[(df['Date'] >= '1992-08-01') & (df['Date'] < '1992-08-31')]
print(Aug1992)

Aug1992_mean=Aug1992['Open'].mean()
print("August 1992 Mean Opening Price:", Aug1992_mean)  

Aug1992.plot(x='Date', y='Open', title='AMD Opening Prices in August 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep1992=df.loc[(df['Date'] >= '1992-09-01') & (df['Date'] < '1992-09-30')]
print(Sep1992)

Sep1992_mean=Sep1992['Open'].mean()
print("September 1992 Mean Opening Price:", Sep1992_mean)

Sep1992.plot(x='Date', y='Open', title='AMD Opening Prices in September 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')    
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct1992=df.loc[(df['Date'] >= '1992-10-01') & (df['Date'] < '1992-10-31')]
print(Oct1992)

Oct1992_mean=Oct1992['Open'].mean()
print("October 1992 Mean Opening Price:", Oct1992_mean)

Oct1992.plot(x='Date', y='Open', title='AMD Opening Prices in October 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov1992=df.loc[(df['Date'] >= '1992-11-01') & (df['Date'] < '1992-11-30')]
print(Nov1992)

Nov1992_mean=Nov1992['Open'].mean()
print("November 1992 Mean Opening Price:", Nov1992_mean)

Nov1992.plot(x='Date', y='Open', title='AMD Opening Prices in November 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec1992=df.loc[(df['Date'] >= '1992-12-01') & (df['Date'] < '1992-12-31')]
print(Dec1992)
Dec1992_mean=Dec1992['Open'].mean()
print("December 1992 Mean Opening Price:", Dec1992_mean)

Dec1992.plot(x='Date', y='Open', title='AMD Opening Prices in December 1992')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan1993=df.loc[(df['Date'] >= '1993-01-01') & (df['Date'] < '1993-01-31')]
print(Jan1993)

Jan1993_mean=Jan1993['Open'].mean()
print("January 1993 Mean Opening Price:", Jan1993_mean) 

Jan1993.plot(x='Date', y='Open', title='AMD Opening Prices in January 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb1993=df.loc[(df['Date'] >= '1993-02-01') & (df['Date'] < '1993-02-28')]
print(Feb1993)

Feb1993_mean=Feb1993['Open'].mean()
print("February 1993 Mean Opening Price:", Feb1993_mean)

Feb1993.plot(x='Date', y='Open', title='AMD Opening Prices in February 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar1993=df.loc[(df['Date'] >= '1993-03-01') & (df['Date'] < '1993-03-31')]
print(Mar1993)

Mar1993_mean=Mar1993['Open'].mean()
print("March 1993 Mean Opening Price:", Mar1993_mean)

Mar1993.plot(x='Date', y='Open', title='AMD Opening Prices in March 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr1993=df.loc[(df['Date'] >= '1993-04-01') & (df['Date'] < '1993-04-30')]
print(Apr1993)

Apr1993_mean=Apr1993['Open'].mean()
print("April 1993 Mean Opening Price:", Apr1993_mean)
Apr1993.plot(x='Date', y='Open', title='AMD Opening Prices in April 1993')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May1993=df.loc[(df['Date'] >= '1993-05-01') & (df['Date'] < '1993-05-31')]
print(May1993)

May1993_mean=May1993['Open'].mean()
print("May 1993 Mean Opening Price:", May1993_mean)

May1993.plot(x='Date', y='Open', title='AMD Opening Prices in May 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun1993=df.loc[(df['Date'] >= '1993-06-01') & (df['Date'] < '1993-06-30')]
print(Jun1993)

Jun1993_mean=Jun1993['Open'].mean()
print("June 1993 Mean Opening Price:", Jun1993_mean)

Jun1993.plot(x='Date', y='Open', title='AMD Opening Prices in June 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul1993=df.loc[(df['Date'] >= '1993-07-01') & (df['Date'] < '1993-07-31')]
print(Jul1993)

Jul1993_mean=Jul1993['Open'].mean()
print("July 1993 Mean Opening Price:", Jul1993_mean)

Jul1993.plot(x='Date', y='Open', title='AMD Opening Prices in July 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Aug1993=df.loc[(df['Date'] >= '1993-08-01') & (df['Date'] < '1993-08-31')]
print(Aug1993)

Aug1993_mean=Aug1993['Open'].mean()
print("August 1993 Mean Opening Price:", Aug1993_mean)  

Aug1993.plot(x='Date', y='Open', title='AMD Opening Prices in August 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep1993=df.loc[(df['Date'] >= '1993-09-01') & (df['Date'] < '1993-09-30')]
print(Sep1993)

Sep1993_mean=Sep1993['Open'].mean()
print("September 1993 Mean Opening Price:", Sep1993_mean)

Sep1993.plot(x='Date', y='Open', title='AMD Opening Prices in September 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Oct1993=df.loc[(df['Date'] >= '1993-10-01') & (df['Date'] < '1993-10-31')]
print(Oct1993)

Oct1993_mean=Oct1993['Open'].mean()
print("October 1993 Mean Opening Price:", Oct1993_mean)
Oct1993.plot(x='Date', y='Open', title='AMD Opening Prices in October 1993')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov1993=df.loc[(df['Date'] >= '1993-11-01') & (df['Date'] < '1993-11-30')]
print(Nov1993)

Nov1993_mean=Nov1993['Open'].mean()
print("November 1993 Mean Opening Price:", Nov1993_mean)
Nov1993.plot(x='Date', y='Open', title='AMD Opening Prices in November 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec1993=df.loc[(df['Date'] >= '1993-12-01') & (df['Date'] < '1993-12-31')]
print(Dec1993)

Dec1993_mean=Dec1993['Open'].mean()
print("December 1993 Mean Opening Price:", Dec1993_mean)

Dec1993.plot(x='Date', y='Open', title='AMD Opening Prices in December 1993')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan1994=df.loc[(df['Date'] >= '1994-01-01') & (df['Date'] < '1994-01-31')]
print(Jan1994)

Jan1994_mean=Jan1994['Open'].mean()
print("January 1994 Mean Opening Price:", Jan1994_mean)

Jan1994.plot(x='Date', y='Open', title='AMD Opening Prices in January 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb1994=df.loc[(df['Date'] >= '1994-02-01') & (df['Date'] < '1994-02-28')]
print(Feb1994)

Feb1994_mean=Feb1994['Open'].mean()
print("February 1994 Mean Opening Price:", Feb1994_mean)

Feb1994.plot(x='Date', y='Open', title='AMD Opening Prices in February 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar1994=df.loc[(df['Date'] >= '1994-03-01') & (df['Date'] < '1994-03-31')]
print(Mar1994)

Mar1994_mean=Mar1994['Open'].mean()
print("March 1994 Mean Opening Price:", Mar1994_mean)   

Mar1994.plot(x='Date', y='Open', title='AMD Opening Prices in March 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr1994=df.loc[(df['Date'] >= '1994-04-01') & (df['Date'] < '1994-04-30')]
print(Apr1994)

Apr1994_mean=Apr1994['Open'].mean()
print("April 1994 Mean Opening Price:", Apr1994_mean)   

Apr1994.plot(x='Date', y='Open', title='AMD Opening Prices in April 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May1994=df.loc[(df['Date'] >= '1994-05-01') & (df['Date'] < '1994-05-31')]
print(May1994)

May1994_mean=May1994['Open'].mean()
print("May 1994 Mean Opening Price:", May1994_mean) 

May1994.plot(x='Date', y='Open', title='AMD Opening Prices in May 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun1994=df.loc[(df['Date'] >= '1994-06-01') & (df['Date'] < '1994-06-30')]
print(Jun1994)

Jun1994_mean=Jun1994['Open'].mean()
print("June 1994 Mean Opening Price:", Jun1994_mean)
Jun1994.plot(x='Date', y='Open', title='AMD Opening Prices in June 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jul1994=df.loc[(df['Date'] >= '1994-07-01') & (df['Date'] < '1994-07-31')]
print(Jul1994)

Jul1994_mean=Jul1994['Open'].mean()
print("July 1994 Mean Opening Price:", Jul1994_mean)
Jul1994.plot(x='Date', y='Open', title='AMD Opening Prices in July 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Aug1994=df.loc[(df['Date'] >= '1994-08-01') & (df['Date'] < '1994-08-31')]
print(Aug1994)

Aug1994_mean=Aug1994['Open'].mean()
print("August 1994 Mean Opening Price:", Aug1994_mean)
Aug1994.plot(x='Date', y='Open', title='AMD Opening Prices in August 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep1994=df.loc[(df['Date'] >= '1994-09-01') & (df['Date'] < '1994-09-30')]
print(Sep1994)

Sep1994_mean=Sep1994['Open'].mean()
print("September 1994 Mean Opening Price:", Sep1994_mean)

Sep1994.plot(x='Date', y='Open', title='AMD Opening Prices in September 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct1994=df.loc[(df['Date'] >= '1994-10-01') & (df['Date'] < '1994-10-31')]
print(Oct1994)

Oct1994_mean=Oct1994['Open'].mean()
print("October 1994 Mean Opening Price:", Oct1994_mean)

Oct1994.plot(x='Date', y='Open', title='AMD Opening Prices in October 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov1994=df.loc[(df['Date'] >= '1994-11-01') & (df['Date'] < '1994-11-30')]
print(Nov1994)

Nov1994_mean=Nov1994['Open'].mean()
print("November 1994 Mean Opening Price:", Nov1994_mean)

Nov1994.plot(x='Date', y='Open', title='AMD Opening Prices in November 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec1994=df.loc[(df['Date'] >= '1994-12-01') & (df['Date'] < '1994-12-31')]
print(Dec1994)

Dec1994_mean=Dec1994['Open'].mean()
print("December 1994 Mean Opening Price:", Dec1994_mean)
Dec1994.plot(x='Date', y='Open', title='AMD Opening Prices in December 1994')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jan1995=df.loc[(df['Date'] >= '1995-01-01') & (df['Date'] < '1995-01-31')]
print(Jan1995)

Jan1995_mean=Jan1995['Open'].mean()
print("January 1995 Mean Opening Price:", Jan1995_mean)
Jan1995.plot(x='Date', y='Open', title='AMD Opening Prices in January 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Feb1995=df.loc[(df['Date'] >= '1995-02-01') & (df['Date'] < '1995-02-28')]
print(Feb1995)

Feb1995_mean=Feb1995['Open'].mean()
print("February 1995 Mean Opening Price:", Feb1995_mean)

Feb1995.plot(x='Date', y='Open', title='AMD Opening Prices in February 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar1995=df.loc[(df['Date'] >= '1995-03-01') & (df['Date'] < '1995-03-31')]
print(Mar1995)

Mar1995_mean=Mar1995['Open'].mean()
print("March 1995 Mean Opening Price:", Mar1995_mean)

Mar1995.plot(x='Date', y='Open', title='AMD Opening Prices in March 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr1995=df.loc[(df['Date'] >= '1995-04-01') & (df['Date'] < '1995-04-30')]
print(Apr1995)

Apr1995_mean=Apr1995['Open'].mean()
print("April 1995 Mean Opening Price:", Apr1995_mean)
Apr1995.plot(x='Date', y='Open', title='AMD Opening Prices in April 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May1995=df.loc[(df['Date'] >= '1995-05-01') & (df['Date'] < '1995-05-31')]
print(May1995)

May1995_mean=May1995['Open'].mean()
print("May 1995 Mean Opening Price:", May1995_mean)
May1995.plot(x='Date', y='Open', title='AMD Opening Prices in May 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun1995=df.loc[(df['Date'] >= '1995-06-01') & (df['Date'] < '1995-06-30')]
print(Jun1995)

Jun1995_mean=Jun1995['Open'].mean()
print("June 1995 Mean Opening Price:", Jun1995_mean)
Jun1995.plot(x='Date', y='Open', title='AMD Opening Prices in June 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jul1995=df.loc[(df['Date'] >= '1995-07-01') & (df['Date'] < '1995-07-31')]
print(Jul1995)

Jul1995_mean=Jul1995['Open'].mean()
print("July 1995 Mean Opening Price:", Jul1995_mean)
Jul1995.plot(x='Date', y='Open', title='AMD Opening Prices in July 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug1995=df.loc[(df['Date'] >= '1995-08-01') & (df['Date'] < '1995-08-31')]
print(Aug1995)

Aug1995_mean=Aug1995['Open'].mean()
print("August 1995 Mean Opening Price:", Aug1995_mean)
Aug1995.plot(x='Date', y='Open', title='AMD Opening Prices in August 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep1995=df.loc[(df['Date'] >= '1995-09-01') & (df['Date'] < '1995-09-30')]
print(Sep1995)

Sep1995_mean=Sep1995['Open'].mean()
print("September 1995 Mean Opening Price:", Sep1995_mean)
Sep1995.plot(x='Date', y='Open', title='AMD Opening Prices in September 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct1995=df.loc[(df['Date'] >= '1995-10-01') & (df['Date'] < '1995-10-31')]
print(Oct1995)

Oct1995_mean=Oct1995['Open'].mean()
print("October 1995 Mean Opening Price:", Oct1995_mean)
Oct1995.plot(x='Date', y='Open', title='AMD Opening Prices in October 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov1995=df.loc[(df['Date'] >= '1995-11-01') & (df['Date'] < '1995-11-30')]
print(Nov1995)

Nov1995_mean=Nov1995['Open'].mean()
print("November 1995 Mean Opening Price:", Nov1995_mean)
Nov1995.plot(x='Date', y='Open', title='AMD Opening Prices in November 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Dec1995=df.loc[(df['Date'] >= '1995-12-01') & (df['Date'] < '1995-12-31')]
print(Dec1995)

Dec1995_mean=Dec1995['Open'].mean()
print("December 1995 Mean Opening Price:", Dec1995_mean)
Dec1995.plot(x='Date', y='Open', title='AMD Opening Prices in December 1995')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jan1996=df.loc[(df['Date'] >= '1996-01-01') & (df['Date'] < '1996-01-31')]
print(Jan1996)

Jan1996_mean=Jan1996['Open'].mean()
print("January 1996 Mean Opening Price:", Jan1996_mean)
Jan1996.plot(x='Date', y='Open', title='AMD Opening Prices in January 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Feb1996=df.loc[(df['Date'] >= '1996-02-01') & (df['Date'] < '1996-02-29')]
print(Feb1996)

Feb1996_mean=Feb1996['Open'].mean()
print("February 1996 Mean Opening Price:", Feb1996_mean)
Feb1996.plot(x='Date', y='Open', title='AMD Opening Prices in February 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Mar1996=df.loc[(df['Date'] >= '1996-03-01') & (df['Date'] < '1996-03-31')]
print(Mar1996)

Mar1996_mean=Mar1996['Open'].mean()
print("March 1996 Mean Opening Price:", Mar1996_mean)
Mar1996.plot(x='Date', y='Open', title='AMD Opening Prices in March 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr1996=df.loc[(df['Date'] >= '1996-04-01') & (df['Date'] < '1996-04-30')]
print(Apr1996)

Apr1996_mean=Apr1996['Open'].mean()
print("April 1996 Mean Opening Price:", Apr1996_mean)
Apr1996.plot(x='Date', y='Open', title='AMD Opening Prices in April 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
May1996=df.loc[(df['Date'] >= '1996-05-01') & (df['Date'] < '1996-05-31')]
print(May1996)

May1996_mean=May1996['Open'].mean()
print("May 1996 Mean Opening Price:", May1996_mean)
May1996.plot(x='Date', y='Open', title='AMD Opening Prices in May 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun1996=df.loc[(df['Date'] >= '1996-06-01') & (df['Date'] < '1996-06-30')]
print(Jun1996)

Jun1996_mean=Jun1996['Open'].mean()
print("June 1996 Mean Opening Price:", Jun1996_mean)

Jun1996.plot(x='Date', y='Open', title='AMD Opening Prices in June 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jul1996=df.loc[(df['Date'] >= '1996-07-01') & (df['Date'] < '1996-07-31')]
print(Jul1996)

Jul1996_mean=Jul1996['Open'].mean()
print("July 1996 Mean Opening Price:", Jul1996_mean)
Jul1996.plot(x='Date', y='Open', title='AMD Opening Prices in July 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug1996=df.loc[(df['Date'] >= '1996-08-01') & (df['Date'] < '1996-08-31')]
print(Aug1996)

Aug1996_mean=Aug1996['Open'].mean()
print("August 1996 Mean Opening Price:", Aug1996_mean)

Aug1996.plot(x='Date', y='Open', title='AMD Opening Prices in August 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Sep1996=df.loc[(df['Date'] >= '1996-09-01') & (df['Date'] < '1996-09-30')]
print(Sep1996)

Sep1996_mean=Sep1996['Open'].mean()
print("September 1996 Mean Opening Price:", Sep1996_mean)
Sep1996.plot(x='Date', y='Open', title='AMD Opening Prices in September 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct1996=df.loc[(df['Date'] >= '1996-10-01') & (df['Date'] < '1996-10-31')]
print(Oct1996)

Oct1996_mean=Oct1996['Open'].mean()
print("October 1996 Mean Opening Price:", Oct1996_mean)
Oct1996.plot(x='Date', y='Open', title='AMD Opening Prices in October 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov1996=df.loc[(df['Date'] >= '1996-11-01') & (df['Date'] < '1996-11-30')]
print(Nov1996)

Nov1996_mean=Nov1996['Open'].mean()
print("November 1996 Mean Opening Price:", Nov1996_mean)
Nov1996.plot(x='Date', y='Open', title='AMD Opening Prices in November 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Dec1996=df.loc[(df['Date'] >= '1996-12-01') & (df['Date'] < '1996-12-31')]
print(Dec1996)

Dec1996_mean=Dec1996['Open'].mean()
print("December 1996 Mean Opening Price:", Dec1996_mean)
Dec1996.plot(x='Date', y='Open', title='AMD Opening Prices in December 1996')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jan1997=df.loc[(df['Date'] >= '1997-01-01') & (df['Date'] < '1997-01-31')]
print(Jan1997)

Jan1997_mean=Jan1997['Open'].mean()
print("January 1997 Mean Opening Price:", Jan1997_mean)
Jan1997.plot(x='Date', y='Open', title='AMD Opening Prices in January 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb1997=df.loc[(df['Date'] >= '1997-02-01') & (df['Date'] < '1997-02-28')]
print(Feb1997)

Feb1997_mean=Feb1997['Open'].mean()
print("February 1997 Mean Opening Price:", Feb1997_mean)
Feb1997.plot(x='Date', y='Open', title='AMD Opening Prices in February 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Mar1997=df.loc[(df['Date'] >= '1997-03-01') & (df['Date'] < '1997-03-31')]
print(Mar1997)

Mar1997_mean=Mar1997['Open'].mean()
print("March 1997 Mean Opening Price:", Mar1997_mean)

Mar1997.plot(x='Date', y='Open', title='AMD Opening Prices in March 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Apr1997=df.loc[(df['Date'] >= '1997-04-01') & (df['Date'] < '1997-04-30')]
print(Apr1997)  

Apr1997_mean=Apr1997['Open'].mean()
print("April 1997 Mean Opening Price:", Apr1997_mean)

Apr1997.plot(x='Date', y='Open', title='AMD Opening Prices in April 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
May1997=df.loc[(df['Date'] >= '1997-05-01') & (df['Date'] < '1997-05-31')]
print(May1997)

May1997_mean=May1997['Open'].mean()
print("May 1997 Mean Opening Price:", May1997_mean)
May1997.plot(x='Date', y='Open', title='AMD Opening Prices in May 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun1997=df.loc[(df['Date'] >= '1997-06-01') & (df['Date'] < '1997-06-30')]
print(Jun1997)

Jun1997_mean=Jun1997['Open'].mean()
print("June 1997 Mean Opening Price:", Jun1997_mean)
Jun1997.plot(x='Date', y='Open', title='AMD Opening Prices in June 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jul1997=df.loc[(df['Date'] >= '1997-07-01') & (df['Date'] < '1997-07-31')]
print(Jul1997)

Jul1997_mean=Jul1997['Open'].mean()
print("July 1997 Mean Opening Price:", Jul1997_mean)
Jul1997.plot(x='Date', y='Open', title='AMD Opening Prices in July 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug1997=df.loc[(df['Date'] >= '1997-08-01') & (df['Date'] < '1997-08-31')]
print(Aug1997)

Aug1997_mean=Aug1997['Open'].mean()
print("August 1997 Mean Opening Price:", Aug1997_mean)
Aug1997.plot(x='Date', y='Open', title='AMD Opening Prices in August 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Sep1997=df.loc[(df['Date'] >= '1997-09-01') & (df['Date'] < '1997-09-30')]
print(Sep1997)

Sep1997_mean=Sep1997['Open'].mean()
print("September 1997 Mean Opening Price:", Sep1997_mean)
Sep1997.plot(x='Date', y='Open', title='AMD Opening Prices in September 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Oct1997=df.loc[(df['Date'] >= '1997-10-01') & (df['Date'] < '1997-10-31')]
print(Oct1997)

Oct1997_mean=Oct1997['Open'].mean()
print("October 1997 Mean Opening Price:", Oct1997_mean)
Oct1997.plot(x='Date', y='Open', title='AMD Opening Prices in October 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov1997=df.loc[(df['Date'] >= '1997-11-01') & (df['Date'] < '1997-11-30')]
print(Nov1997)

Nov1997_mean=Nov1997['Open'].mean()
print("November 1997 Mean Opening Price:", Nov1997_mean)
Nov1997.plot(x='Date', y='Open', title='AMD Opening Prices in November 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Dec1997=df.loc[(df['Date'] >= '1997-12-01') & (df['Date'] < '1997-12-31')]
print(Dec1997)

Dec1997_mean=Dec1997['Open'].mean()
print("December 1997 Mean Opening Price:", Dec1997_mean)
Dec1997.plot(x='Date', y='Open', title='AMD Opening Prices in December 1997')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jan1998=df.loc[(df['Date'] >= '1998-01-01') & (df['Date'] < '1998-01-31')]
print(Jan1998)

Jan1998_mean=Jan1998['Open'].mean()
print("January 1998 Mean Opening Price:", Jan1998_mean) 
Jan1998.plot(x='Date', y='Open', title='AMD Opening Prices in January 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb1998=df.loc[(df['Date'] >= '1998-02-01') & (df['Date'] < '1998-02-28')]
print(Feb1998)

Feb1998_mean=Feb1998['Open'].mean()
print("February 1998 Mean Opening Price:", Feb1998_mean)
Feb1998.plot(x='Date', y='Open', title='AMD Opening Prices in February 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar1998=df.loc[(df['Date'] >= '1998-03-01') & (df['Date'] < '1998-03-31')]
print(Mar1998)

Mar1998_mean=Mar1998['Open'].mean()
print("March 1998 Mean Opening Price:", Mar1998_mean)
Mar1998.plot(x='Date', y='Open', title='AMD Opening Prices in March 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Apr1998=df.loc[(df['Date'] >= '1998-04-01') & (df['Date'] < '1998-04-30')]
print(Apr1998)

Apr1998_mean=Apr1998['Open'].mean()
print("April 1998 Mean Opening Price:", Apr1998_mean)
Apr1998.plot(x='Date', y='Open', title='AMD Opening Prices in April 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
May1998=df.loc[(df['Date'] >= '1998-05-01') & (df['Date'] < '1998-05-31')]
print(May1998)

May1998_mean=May1998['Open'].mean()
print("May 1998 Mean Opening Price:", May1998_mean)
May1998.plot(x='Date', y='Open', title='AMD Opening Prices in May 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun1998=df.loc[(df['Date'] >= '1998-06-01') & (df['Date'] < '1998-06-30')]
print(Jun1998)

Jun1998_mean=Jun1998['Open'].mean()
print("June 1998 Mean Opening Price:", Jun1998_mean)
Jun1998.plot(x='Date', y='Open', title='AMD Opening Prices in June 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jul1998=df.loc[(df['Date'] >= '1998-07-01') & (df['Date'] < '1998-07-31')]
print(Jul1998)

Jul1998_mean=Jul1998['Open'].mean()
print("July 1998 Mean Opening Price:", Jul1998_mean)
Jul1998.plot(x='Date', y='Open', title='AMD Opening Prices in July 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Aug1998=df.loc[(df['Date'] >= '1998-08-01') & (df['Date'] < '1998-08-31')]
print(Aug1998)

Aug1998_mean=Aug1998['Open'].mean()
print("August 1998 Mean Opening Price:", Aug1998_mean)
Aug1998.plot(x='Date', y='Open', title='AMD Opening Prices in August 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Sep1998=df.loc[(df['Date'] >= '1998-09-01') & (df['Date'] < '1998-09-30')]
print(Sep1998)

Sep1998_mean=Sep1998['Open'].mean()
print("September 1998 Mean Opening Price:", Sep1998_mean)

Sep1998.plot(x='Date', y='Open', title='AMD Opening Prices in September 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Oct1998=df.loc[(df['Date'] >= '1998-10-01') & (df['Date'] < '1998-10-31')]
print(Oct1998)

Oct1998_mean=Oct1998['Open'].mean()
print("October 1998 Mean Opening Price:", Oct1998_mean)
Oct1998.plot(x='Date', y='Open', title='AMD Opening Prices in October 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov1998=df.loc[(df['Date'] >= '1998-11-01') & (df['Date'] < '1998-11-30')]
print(Nov1998)

Nov1998_mean=Nov1998['Open'].mean()
print("November 1998 Mean Opening Price:", Nov1998_mean)
Nov1998.plot(x='Date', y='Open', title='AMD Opening Prices in November 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Dec1998=df.loc[(df['Date'] >= '1998-12-01') & (df['Date'] < '1998-12-31')]
print(Dec1998)

Dec1998_mean=Dec1998['Open'].mean()
print("December 1998 Mean Opening Price:", Dec1998_mean)
Dec1998.plot(x='Date', y='Open', title='AMD Opening Prices in December 1998')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jan1999=df.loc[(df['Date'] >= '1999-01-01') & (df['Date'] < '1999-01-31')]
print(Jan1999)

Jan1999_mean=Jan1999['Open'].mean()
print("January 1999 Mean Opening Price:", Jan1999_mean)
Jan1999.plot(x='Date', y='Open', title='AMD Opening Prices in January 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb1999=df.loc[(df['Date'] >= '1999-02-01') & (df['Date'] < '1999-02-28')]
print(Feb1999)

Feb1999_mean=Feb1999['Open'].mean()
print("February 1999 Mean Opening Price:", Feb1999_mean)
Feb1999.plot(x='Date', y='Open', title='AMD Opening Prices in February 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Mar1999=df.loc[(df['Date'] >= '1999-03-01') & (df['Date'] < '1999-03-31')]
print(Mar1999)

Mar1999_mean=Mar1999['Open'].mean()
print("March 1999 Mean Opening Price:", Mar1999_mean)
Mar1999.plot(x='Date', y='Open', title='AMD Opening Prices in March 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Apr1999=df.loc[(df['Date'] >= '1999-04-01') & (df['Date'] < '1999-04-30')]  
print(Apr1999)

Apr1999_mean=Apr1999['Open'].mean()
print("April 1999 Mean Opening Price:", Apr1999_mean)
Apr1999.plot(x='Date', y='Open', title='AMD Opening Prices in April 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May1999=df.loc[(df['Date'] >= '1999-05-01') & (df['Date'] < '1999-05-31')]
print(May1999)

May1999_mean=May1999['Open'].mean()
print("May 1999 Mean Opening Price:", May1999_mean)
May1999.plot(x='Date', y='Open', title='AMD Opening Prices in May 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jun1999=df.loc[(df['Date'] >= '1999-06-01') & (df['Date'] < '1999-06-30')]
print(Jun1999)

Jun1999_mean=Jun1999['Open'].mean()
print("June 1999 Mean Opening Price:", Jun1999_mean)
Jun1999.plot(x='Date', y='Open', title='AMD Opening Prices in June 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul1999=df.loc[(df['Date'] >= '1999-07-01') & (df['Date'] < '1999-07-31')]
print(Jul1999)
Jul1999_mean=Jul1999['Open'].mean()
print("July 1999 Mean Opening Price:", Jul1999_mean)

Jul1999.plot(x='Date', y='Open', title='AMD Opening Prices in July 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug1999=df.loc[(df['Date'] >= '1999-08-01') & (df['Date'] < '1999-08-31')]
print(Aug1999)

Aug1999_mean=Aug1999['Open'].mean()
print("August 1999 Mean Opening Price:", Aug1999_mean)
Aug1999.plot(x='Date', y='Open', title='AMD Opening Prices in August 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep1999=df.loc[(df['Date'] >= '1999-09-01') & (df['Date'] < '1999-09-30')]
print(Sep1999)

Sep1999_mean=Sep1999['Open'].mean()
print("September 1999 Mean Opening Price:", Sep1999_mean)
Sep1999.plot(x='Date', y='Open', title='AMD Opening Prices in September 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct1999=df.loc[(df['Date'] >= '1999-10-01') & (df['Date'] < '1999-10-31')]
print(Oct1999)

Oct1999_mean=Oct1999['Open'].mean()
print("October 1999 Mean Opening Price:", Oct1999_mean)
Oct1999.plot(x='Date', y='Open', title='AMD Opening Prices in October 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov1999=df.loc[(df['Date'] >= '1999-11-01') & (df['Date'] < '1999-11-30')]
print(Nov1999)

Nov1999_mean=Nov1999['Open'].mean()
print("November 1999 Mean Opening Price:", Nov1999_mean)
Nov1999.plot(x='Date', y='Open', title='AMD Opening Prices in November 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Dec1999=df.loc[(df['Date'] >= '1999-12-01') & (df['Date'] < '1999-12-31')]
print(Dec1999)

Dec1999_mean=Dec1999['Open'].mean()
print("December 1999 Mean Opening Price:", Dec1999_mean)
Dec1999.plot(x='Date', y='Open', title='AMD Opening Prices in December 1999')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2000=df.loc[(df['Date'] >= '2000-01-01') & (df['Date'] < '2000-01-31')]
print(Jan2000)

Jan2000_mean=Jan2000['Open'].mean()
print("January 2000 Mean Opening Price:", Jan2000_mean)
Jan2000.plot(x='Date', y='Open', title='AMD Opening Prices in January 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2000=df.loc[(df['Date'] >= '2000-02-01') & (df['Date'] < '2000-02-29')]
print(Feb2000)
Feb2000_mean=Feb2000['Open'].mean()
print("February 2000 Mean Opening Price:", Feb2000_mean)
Feb2000.plot(x='Date', y='Open', title='AMD Opening Prices in February 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2000=df.loc[(df['Date'] >= '2000-03-01') & (df['Date'] < '2000-03-31')]
print(Mar2000)

Mar2000_mean=Mar2000['Open'].mean()
print("March 2000 Mean Opening Price:", Mar2000_mean)
Mar2000.plot(x='Date', y='Open', title='AMD Opening Prices in March 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2000=df.loc[(df['Date'] >= '2000-04-01') & (df['Date'] < '2000-04-30')]
print(Apr2000)

Apr2000_mean=Apr2000['Open'].mean()
print("April 2000 Mean Opening Price:", Apr2000_mean)
Apr2000.plot(x='Date', y='Open', title='AMD Opening Prices in April 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])

May2000=df.loc[(df['Date'] >= '2000-05-01') & (df['Date'] < '2000-05-31')]
print(May2000)

May2000_mean=May2000['Open'].mean()
print("May 2000 Mean Opening Price:", May2000_mean)
May2000.plot(x='Date', y='Open', title='AMD Opening Prices in May 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jun2000=df.loc[(df['Date'] >= '2000-06-01') & (df['Date'] < '2000-06-30')]
print(Jun2000)

Jun2000_mean=Jun2000['Open'].mean()
print("June 2000 Mean Opening Price:", Jun2000_mean)
Jun2000.plot(x='Date', y='Open', title='AMD Opening Prices in June 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2000=df.loc[(df['Date'] >= '2000-07-01') & (df['Date'] < '2000-07-31')]
print(Jul2000)

Jul2000_mean=Jul2000['Open'].mean()
print("July 2000 Mean Opening Price:", Jul2000_mean)
Jul2000.plot(x='Date', y='Open', title='AMD Opening Prices in July 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])

Aug2000=df.loc[(df['Date'] >= '2000-08-01') & (df['Date'] < '2000-08-31')]
print(Aug2000)
Aug2000_mean=Aug2000['Open'].mean()
print("August 2000 Mean Opening Price:", Aug2000_mean)
Aug2000.plot(x='Date', y='Open', title='AMD Opening Prices in August 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2000=df.loc[(df['Date'] >= '2000-09-01') & (df['Date'] < '2000-09-30')]
print(Sep2000)

Sep2000_mean=Sep2000['Open'].mean()
print("September 2000 Mean Opening Price:", Sep2000_mean)
Sep2000.plot(x='Date', y='Open', title='AMD Opening Prices in September 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2000=df.loc[(df['Date'] >= '2000-10-01') & (df['Date'] < '2000-10-31')]
print(Oct2000)

Oct2000_mean=Oct2000['Open'].mean()
print("October 2000 Mean Opening Price:", Oct2000_mean)
Oct2000.plot(x='Date', y='Open', title='AMD Opening Prices in October 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov2000=df.loc[(df['Date'] >= '2000-11-01') & (df['Date'] < '2000-11-30')]
print(Nov2000)
Nov2000_mean=Nov2000['Open'].mean()
print("November 2000 Mean Opening Price:", Nov2000_mean)
Nov2000.plot(x='Date', y='Open', title='AMD Opening Prices in November 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Dec2000=df.loc[(df['Date'] >= '2000-12-01') & (df['Date'] < '2000-12-31')]
print(Dec2000)

Dec2000_mean=Dec2000['Open'].mean()
print("December 2000 Mean Opening Price:", Dec2000_mean)
Dec2000.plot(x='Date', y='Open', title='AMD Opening Prices in December 2000')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jan2001=df.loc[(df['Date'] >= '2001-01-01') & (df['Date'] < '2001-01-31')]
print(Jan2001)

Jan2001_mean=Jan2001['Open'].mean()
print("January 2001 Mean Opening Price:", Jan2001_mean)
Jan2001.plot(x='Date', y='Open', title='AMD Opening Prices in January 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Feb2001=df.loc[(df['Date'] >= '2001-02-01') & (df['Date'] < '2001-02-28')]
print(Feb2001)

Feb2001_mean=Feb2001['Open'].mean()
print("February 2001 Mean Opening Price:", Feb2001_mean)
Feb2001.plot(x='Date', y='Open', title='AMD Opening Prices in February 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Mar2001=df.loc[(df['Date'] >= '2001-03-01') & (df['Date'] < '2001-03-31')]
print(Mar2001)

Mar2001_mean=Mar2001['Open'].mean()
print("March 2001 Mean Opening Price:", Mar2001_mean)
Mar2001.plot(x='Date', y='Open', title='AMD Opening Prices in March 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2001=df.loc[(df['Date'] >= '2001-04-01') & (df['Date'] < '2001-04-30')]
print(Apr2001)

Apr2001_mean=Apr2001['Open'].mean()
print("April 2001 Mean Opening Price:", Apr2001_mean)
Apr2001.plot(x='Date', y='Open', title='AMD Opening Prices in April 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])

May2001=df.loc[(df['Date'] >= '2001-05-01') & (df['Date'] < '2001-05-31')]
print(May2001)

May2001_mean=May2001['Open'].mean()
print("May 2001 Mean Opening Price:", May2001_mean)
May2001.plot(x='Date', y='Open', title='AMD Opening Prices in May 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2001=df.loc[(df['Date'] >= '2001-06-01') & (df['Date'] < '2001-06-30')]
print(Jun2001)

Jun2001_mean=Jun2001['Open'].mean()
print("June 2001 Mean Opening Price:", Jun2001_mean)
Jun2001.plot(x='Date', y='Open', title='AMD Opening Prices in June 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2001=df.loc[(df['Date'] >= '2001-07-01') & (df['Date'] < '2001-07-31')]
print(Jul2001)

Jul2001_mean=Jul2001['Open'].mean()
print("July 2001 Mean Opening Price:", Jul2001_mean)
Jul2001.plot(x='Date', y='Open', title='AMD Opening Prices in July 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2001=df.loc[(df['Date'] >= '2001-08-01') & (df['Date'] < '2001-08-31')]
print(Aug2001)

Aug2001_mean=Aug2001['Open'].mean()
print("Aug 2001 Mean Opening Price:", Aug2001_mean)
Aug2001.plot(x='Date', y='Open', title='AMD Opening Prices in August 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2001=df.loc[(df['Date'] >= '2001-09-01') & (df['Date'] < '2001-09-30')]
print(Sep2001)

Sep2001_mean=Sep2001['Open'].mean()
print("Sep 2001 Mean Opening Price:", Sep2001_mean)
Sep2001.plot(x='Date', y='Open', title='AMD Opening Prices in September 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2001=df.loc[(df['Date'] >= '2001-10-01') & (df['Date'] < '2001-10-31')]
print(Oct2001)

Oct2001_mean=Oct2001['Open'].mean()
print("Oct 2001 Mean Opening Price:", Oct2001_mean)
Oct2001.plot(x='Date', y='Open', title='AMD Opening Prices in October 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2001=df.loc[(df['Date'] >= '2001-11-01') & (df['Date'] < '2001-11-30')]
print(Nov2001)

Nov2001_mean=Nov2001['Open'].mean()
print("Nov 2001 Mean Opening Price:", Nov2001_mean)
Nov2001.plot(x='Date', y='Open', title='AMD Opening Prices in November 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2001=df.loc[(df['Date'] >= '2001-12-01') & (df['Date'] < '2001-12-31')]
print(Dec2001)

Dec2001_mean=Dec2001['Open'].mean()
print("Dec 2001 Mean Opening Price:", Dec2001_mean)
Dec2001.plot(x='Date', y='Open', title='AMD Opening Prices in December 2001')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2002=df.loc[(df['Date'] >= '2002-01-01') & (df['Date'] < '2002-01-31')]
print(Jan2002)

Jan2002_mean=Jan2002['Open'].mean()
print("Jan 2002 Mean Opening Price:", Jan2002_mean)
Jan2002.plot(x='Date', y='Open', title='AMD Opening Prices in January 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Feb2002=df.loc[(df['Date'] >= '2002-02-01') & (df['Date'] < '2002-02-28')]
print(Feb2002)

Feb2002_mean=Feb2002['Open'].mean()
print("Feb 2002 Mean Opening Price:", Feb2002_mean)
Feb2002.plot(x='Date', y='Open', title='AMD Opening Prices in February 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Mar2002=df.loc[(df['Date'] >= '2002-03-01') & (df['Date'] < '2002-03-31')]
print(Mar2002)

Mar2002_mean=Mar2002['Open'].mean()
print("Mar 2002 Mean Opening Price:", Mar2002_mean)
Mar2002.plot(x='Date', y='Open', title='AMD Opening Prices in March 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Apr2002=df.loc[(df['Date'] >= '2002-04-01') & (df['Date'] < '2002-04-30')]
print(Apr2002)

Apr2002_mean=Apr2002['Open'].mean()
print("Apr 2002 Mean Opening Price:", Apr2002_mean)
Apr2002.plot(x='Date', y='Open', title='AMD Opening Prices in April 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
May2002=df.loc[(df['Date'] >= '2002-05-01') & (df['Date'] < '2002-05-31')]
print(May2002)

May2002_mean=May2002['Open'].mean()
print("May 2002 Mean Opening Price:", May2002_mean)
May2002.plot(x='Date', y='Open', title='AMD Opening Prices in May 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jun2002=df.loc[(df['Date'] >= '2002-06-01') & (df['Date'] < '2002-06-30')]
print(Jun2002)

Jun2002_mean=Jun2002['Open'].mean()
print("Jun 2002 Mean Opening Price:", Jun2002_mean)
Jun2002.plot(x='Date', y='Open', title='AMD Opening Prices in June 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jul2002=df.loc[(df['Date'] >= '2002-07-01') & (df['Date'] < '2002-07-31')]
print(Jul2002)

Jul2002_mean=Jul2002['Open'].mean()
print("Jul 2002 Mean Opening Price:", Jul2002_mean)
Jul2002.plot(x='Date', y='Open', title='AMD Opening Prices in July 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Aug2002=df.loc[(df['Date'] >= '2002-08-01') & (df['Date'] < '2002-08-31')]
print(Aug2002)

Aug2002_mean=Aug2002['Open'].mean()
print("Aug 2002 Mean Opening Price:", Aug2002_mean)
Aug2002.plot(x='Date', y='Open', title='AMD Opening Prices in Aug 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Sep2002=df.loc[(df['Date'] >= '2002-09-01') & (df['Date'] < '2002-09-30')]
print(Sep2002)

Sep2002_mean=Sep2002['Open'].mean()
print("Sep 2002 Mean Opening Price:", Sep2002_mean)
Sep2002.plot(x='Date', y='Open', title='AMD Opening Prices in Sep 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Oct2002=df.loc[(df['Date'] >= '2002-10-01') & (df['Date'] < '2002-10-31')]
print(May2002)

Oct2002_mean=Oct2002['Open'].mean()
print("Oct 2002 Mean Opening Price:", Oct2002_mean)
Oct2002.plot(x='Date', y='Open', title='AMD Opening Prices in October 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Nov2002=df.loc[(df['Date'] >= '2002-11-01') & (df['Date'] < '2002-11-30')]
print(Nov2002)

Nov2002_mean=Nov2002['Open'].mean()
print("Nov 2002 Mean Opening Price:", Nov2002_mean)
Nov2002.plot(x='Date', y='Open', title='AMD Opening Prices in November 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Dec2002=df.loc[(df['Date'] >= '2002-12-01') & (df['Date'] < '2002-12-31')]
print(Dec2002)

Dec2002_mean=Dec2002['Open'].mean()
print("Dec 2002 Mean Opening Price:", Dec2002_mean)
Dec2002.plot(x='Date', y='Open', title='AMD Opening Prices in December 2002')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jan2003=df.loc[(df['Date'] >= '2003-01-01') & (df['Date'] < '2003-01-31')]
print(Jan2003)

Jan2003_mean=Jan2003['Open'].mean()
print("Jan 2003 Mean Opening Price:", Jan2003_mean)
Jan2003.plot(x='Date', y='Open', title='AMD Opening Prices in January 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Feb2003=df.loc[(df['Date'] >= '2003-02-01') & (df['Date'] < '2003-02-28')]
print(Feb2003)

Feb2003_mean=Feb2003['Open'].mean()
print("Feb 2003 Mean Opening Price:", Feb2003_mean)
Feb2003.plot(x='Date', y='Open', title='AMD Opening Prices in February 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Mar2003=df.loc[(df['Date'] >= '2003-03-01') & (df['Date'] < '2003-03-31')]
print(Mar2003)

Mar2003_mean=Mar2003['Open'].mean()
print("Mar 2003 Mean Opening Price:", Mar2003_mean)
Mar2003.plot(x='Date', y='Open', title='AMD Opening Prices in March 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Apr2003=df.loc[(df['Date'] >= '2003-04-01') & (df['Date'] < '2003-04-30')]
print(Apr2003)

Apr2003_mean=Apr2003['Open'].mean()
print("Apr 2003 Mean Opening Price:", Apr2003_mean)
Apr2003.plot(x='Date', y='Open', title='AMD Opening Prices in April 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
May2003=df.loc[(df['Date'] >= '2003-05-01') & (df['Date'] < '2003-05-31')]
print(May2003)

May2003_mean=May2003['Open'].mean()
print("May 2003 Mean Opening Price:", May2003_mean)
May2003.plot(x='Date', y='Open', title='AMD Opening Prices in May 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jun2003=df.loc[(df['Date'] >= '2003-06-01') & (df['Date'] < '2003-06-30')]
print(Jun2003)

Jun2003_mean=Jun2003['Open'].mean()
print("Jun 2003 Mean Opening Price:", Jun2003_mean)
Jun2003.plot(x='Date', y='Open', title='AMD Opening Prices in June 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jul2003=df.loc[(df['Date'] >= '2003-07-01') & (df['Date'] < '2003-07-31')]
print(Jul2003)

Jul2003_mean=Jul2003['Open'].mean()
print("Jul 2003 Mean Opening Price:", Jul2003_mean)
Jul2003.plot(x='Date', y='Open', title='AMD Opening Prices in July 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Aug2003=df.loc[(df['Date'] >= '2003-08-01') & (df['Date'] < '2003-08-31')]
print(Aug2003)

Aug2003_mean=Aug2003['Open'].mean()
print("Aug 2003 Mean Opening Price:", Aug2003_mean)
Aug2003.plot(x='Date', y='Open', title='AMD Opening Prices in August 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Sep2003=df.loc[(df['Date'] >= '2003-09-01') & (df['Date'] < '2003-09-30')]
print(Sep2003)

Sep2003_mean=Sep2003['Open'].mean()
print("Sep 2003 Mean Opening Price:", Sep2003_mean)
Sep2003.plot(x='Date', y='Open', title='AMD Opening Prices in September 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Oct2003=df.loc[(df['Date'] >= '2003-10-01') & (df['Date'] < '2003-10-31')]
print(Oct2003)

Oct2003_mean=Oct2003['Open'].mean()
print("Oct 2003 Mean Opening Price:", Oct2003_mean)
Oct2003.plot(x='Date', y='Open', title='AMD Opening Prices in October 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Nov2003=df.loc[(df['Date'] >= '2003-11-01') & (df['Date'] < '2003-11-30')]
print(Nov2003)

Nov2003_mean=Nov2003['Open'].mean()
print("Nov 2003 Mean Opening Price:", Nov2003_mean)
Nov2003.plot(x='Date', y='Open', title='AMD Opening Prices in November 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Dec2003=df.loc[(df['Date'] >= '2003-12-01') & (df['Date'] < '2003-12-31')]
print(Dec2003)

Dec2003_mean=Dec2003['Open'].mean()
print("Dec 2003 Mean Opening Price:", Dec2003_mean)
Dec2003.plot(x='Date', y='Open', title='AMD Opening Prices in December 2003')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jan2004=df.loc[(df['Date'] >= '2004-01-01') & (df['Date'] < '2004-01-31')]
print(Jan2004)

Jan2004_mean=Jan2004['Open'].mean()
print("Jan 2004 Mean Opening Price:", Jan2004_mean)
Jan2004.plot(x='Date', y='Open', title='AMD Opening Prices in January 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Feb2004=df.loc[(df['Date'] >= '2004-02-01') & (df['Date'] < '2004-02-28')]
print(Feb2004)

Feb2004_mean=Feb2004['Open'].mean()
print("Feb 2004 Mean Opening Price:", Feb2004_mean)
Feb2004.plot(x='Date', y='Open', title='AMD Opening Prices in February 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Mar2004=df.loc[(df['Date'] >= '2004-03-01') & (df['Date'] < '2004-03-31')]
print(Mar2004)

Mar2004_mean=Mar2004['Open'].mean()
print("Mar 2004 Mean Opening Price:", Mar2004_mean)
Mar2004.plot(x='Date', y='Open', title='AMD Opening Prices in March 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Apr2004=df.loc[(df['Date'] >= '2004-04-01') & (df['Date'] < '2004-04-30')]
print(Apr2004)

Apr2004_mean=Apr2004['Open'].mean()
print("Apr 2004 Mean Opening Price:", Apr2004_mean)
Apr2004.plot(x='Date', y='Open', title='AMD Opening Prices in April 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
May2004=df.loc[(df['Date'] >= '2004-05-01') & (df['Date'] < '2004-05-31')]
print(May2004)

May2004_mean=May2004['Open'].mean()
print("May 2004 Mean Opening Price:", May2004_mean)
May2004.plot(x='Date', y='Open', title='AMD Opening Prices in May 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jun2004=df.loc[(df['Date'] >= '2004-06-01') & (df['Date'] < '2004-06-30')]
print(Jun2004)

Jun2004_mean=Jun2004['Open'].mean()
print("Jun 2004 Mean Opening Price:", Jun2004_mean)
Jun2004.plot(x='Date', y='Open', title='AMD Opening Prices in June 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Aug2004=df.loc[(df['Date'] >= '2004-08-01') & (df['Date'] < '2004-08-31')]
print(Aug2004)

Aug2004_mean=Aug2004['Open'].mean()
print("Aug 2004 Mean Opening Price:", Aug2004_mean)
Aug2004.plot(x='Date', y='Open', title='AMD Opening Prices in August 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Sep2004=df.loc[(df['Date'] >= '2004-09-01') & (df['Date'] < '2004-09-30')]
print(Sep2004)

Sep2004_mean=Sep2004['Open'].mean()
print("Sep 2004 Mean Opening Price:", Sep2004_mean)
Sep2004.plot(x='Date', y='Open', title='AMD Opening Prices in September 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Oct2004=df.loc[(df['Date'] >= '2004-10-01') & (df['Date'] < '2004-10-31')]
print(Oct2004)

Oct2004_mean=Oct2004['Open'].mean()
print("Oct 2004 Mean Opening Price:", Oct2004_mean)
Oct2004.plot(x='Date', y='Open', title='AMD Opening Prices in October 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Nov2004=df.loc[(df['Date'] >= '2004-11-01') & (df['Date'] < '2004-11-30')]
print(Nov2004)

Nov2004_mean=Nov2004['Open'].mean()
print("Nov 2004 Mean Opening Price:", Nov2004_mean)
Nov2004.plot(x='Date', y='Open', title='AMD Opening Prices in November 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Dec2004=df.loc[(df['Date'] >= '2004-12-01') & (df['Date'] < '2004-12-31')]
print(Dec2004)

Dec2004_mean=Dec2004['Open'].mean()
print("Dec 2004 Mean Opening Price:", Dec2004_mean)
Dec2004.plot(x='Date', y='Open', title='AMD Opening Prices in December 2004')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jan2005=df.loc[(df['Date'] >= '2005-01-01') & (df['Date'] < '2005-01-31')]
print(Jan2005)

Jan2005_mean=Jan2005['Open'].mean()
print("Jan 2005 Mean Opening Price:", Jan2005_mean)
Jan2005.plot(x='Date', y='Open', title='AMD Opening Prices in January 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Feb2005=df.loc[(df['Date'] >= '2005-02-01') & (df['Date'] < '2005-02-28')]
print(Feb2005)

Feb2005_mean=Feb2005['Open'].mean()
print("Jan 2005 Mean Opening Price:", Feb2005_mean)
Feb2005.plot(x='Date', y='Open', title='AMD Opening Prices in February 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Mar2005=df.loc[(df['Date'] >= '2005-03-01') & (df['Date'] < '2005-03-31')]
print(Mar2005)

Mar2005_mean=Mar2005['Open'].mean()
print("Mar 2005 Mean Opening Price:", Mar2005_mean)
Mar2005.plot(x='Date', y='Open', title='AMD Opening Prices in March 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Apr2005=df.loc[(df['Date'] >= '2005-04-01') & (df['Date'] < '2005-04-30')]
print(Apr2005)

Apr2005_mean=Apr2005['Open'].mean()
print("Apr 2005 Mean Opening Price:", Apr2005_mean)
Apr2005.plot(x='Date', y='Open', title='AMD Opening Prices in April 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
May2005=df.loc[(df['Date'] >= '2005-05-01') & (df['Date'] < '2005-05-31')]
print(May2005)

May2005_mean=May2005['Open'].mean()
print("Mar 2005 Mean Opening Price:", May2005_mean)
May2005.plot(x='Date', y='Open', title='AMD Opening Prices in May 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])
Jun2005=df.loc[(df['Date'] >= '2005-06-01') & (df['Date'] < '2005-06-30')]
print(Jun2005)

Jun2005_mean=Jun2005['Open'].mean()
print("Jun 2005 Mean Opening Price:", Jun2005_mean)
Jun2005.plot(x='Date', y='Open', title='AMD Opening Prices in June 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jul2005=df.loc[(df['Date'] >= '2005-07-01') & (df['Date'] < '2005-07-31')]
print(Jul2005)

Jul2005_mean=Jul2005['Open'].mean()
print("Jul 2005 Mean Opening Price:", Jul2005_mean)
Jul2005.plot(x='Date', y='Open', title='AMD Opening Prices in July 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Aug2005=df.loc[(df['Date'] >= '2005-08-01') & (df['Date'] < '2005-08-31')]
print(Aug2005)  

Aug2005_mean=Aug2005['Open'].mean()
print("Aug 2005 Mean Opening Price:", Aug2005_mean)
Aug2005.plot(x='Date', y='Open', title='AMD Opening Prices in August 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2005=df.loc[(df['Date'] >= '2005-09-01') & (df['Date'] < '2005-09-30')]
print(Sep2005)  

Sep2005_mean=Sep2005['Open'].mean()
print("Sep 2005 Mean Opening Price:", Sep2005_mean)
Sep2005.plot(x='Date', y='Open', title='AMD Opening Prices in September 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2005=df.loc[(df['Date'] >= '2005-10-01') & (df['Date'] < '2005-10-31')]
print(Oct2005)

Oct2005_mean=Oct2005['Open'].mean()
print("Oct 2005 Mean Opening Price:", Oct2005_mean)
Oct2005.plot(x='Date', y='Open', title='AMD Opening Prices in October 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov2005=df.loc[(df['Date'] >= '2005-11-01') & (df['Date'] < '2005-11-30')]

print(Nov2005)
Nov2005_mean=Nov2005['Open'].mean()
print("Nov 2005 Mean Opening Price:", Nov2005_mean)
Nov2005.plot(x='Date', y='Open', title='AMD Opening Prices in November 2005')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2005=df.loc[(df['Date'] >= '2005-12-01') & (df['Date'] < '2005-12-31')]
print(Dec2005)

Dec2005_mean=Dec2005['Open'].mean()
print("Dec 2005 Mean Opening Price:", Dec2005_mean)
Dec2005.plot(x='Date', y='Open', title='AMD Opening Prices in December 2005')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2006=df.loc[(df['Date'] >= '2006-01-01') & (df['Date'] < '2006-01-31')]
print(Jan2006)
Jan2006_mean=Jan2006['Open'].mean()
print("Jan 2006 Mean Opening Price:", Jan2006_mean)

Jan2006.plot(x='Date', y='Open', title='AMD Opening Prices in January 2006')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2006=df.loc[(df['Date'] >= '2006-02-01') & (df['Date'] < '2006-02-28')]
print(Feb2006)

Feb2006_mean=Feb2006['Open'].mean()
print("Feb 2006 Mean Opening Price:", Feb2006_mean)
Feb2006.plot(x='Date', y='Open', title='AMD Opening Prices in February 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2006=df.loc[(df['Date'] >= '2006-03-01') & (df['Date'] < '2006-03-31')]
print(Mar2006)

Mar2006_mean=Mar2006['Open'].mean()
print("Mar 2006 Mean Opening Price:", Mar2006_mean)
Mar2006.plot(x='Date', y='Open', title='AMD Opening Prices in March 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2006=df.loc[(df['Date'] >= '2006-04-01') & (df['Date'] < '2006-04-30')]
print(Apr2006)
Apr2006_mean=Apr2006['Open'].mean()
print("Apr 2006 Mean Opening Price:", Apr2006_mean)
Apr2006.plot(x='Date', y='Open', title='AMD Opening Prices in April 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2006=df.loc[(df['Date'] >= '2006-05-01') & (df['Date'] < '2006-05-31')]
print(May2006)

May2006_mean=May2006['Open'].mean()
print("May 2006 Mean Opening Price:", May2006_mean)
May2006.plot(x='Date', y='Open', title='AMD Opening Prices in May 2006')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2006=df.loc[(df['Date'] >= '2006-06-01') & (df['Date'] < '2006-06-30')]
print(Jun2006)

Jun2006_mean=Jun2006['Open'].mean()
print("Jun 2006 Mean Opening Price:", Jun2006_mean)
Jun2006.plot(x='Date', y='Open', title='AMD Opening Prices in June 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2006=df.loc[(df['Date'] >= '2006-07-01') & (df['Date'] < '2006-07-31')]
print(Jul2006)

Jul2006_mean=Jul2006['Open'].mean()
print("Jul 2006 Mean Opening Price:", Jul2006_mean)
Jul2006.plot(x='Date', y='Open', title='AMD Opening Prices in July 2006')   
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2006=df.loc[(df['Date'] >= '2006-08-01') & (df['Date'] < '2006-08-31')]
print(Aug2006)

Aug2006_mean=Aug2006['Open'].mean()
print("Aug 2006 Mean Opening Price:", Aug2006_mean)
Aug2006.plot(x='Date', y='Open', title='AMD Opening Prices in August 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2006=df.loc[(df['Date'] >= '2006-09-01') & (df['Date'] < '2006-09-30')]
print(Sep2006)

Sep2006_mean=Sep2006['Open'].mean()
print("Sep 2006 Mean Opening Price:", Sep2006_mean)
Sep2006.plot(x='Date', y='Open', title='AMD Opening Prices in September 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2006=df.loc[(df['Date'] >= '2006-10-01') & (df['Date'] < '2006-10-31')]
print(Oct2006)

Oct2006_mean=Oct2006['Open'].mean()
print("Oct 2006 Mean Opening Price:", Oct2006_mean)
Oct2006.plot(x='Date', y='Open', title='AMD Opening Prices in October 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2006=df.loc[(df['Date'] >= '2006-11-01') & (df['Date'] < '2006-11-30')]
print(Nov2006)

Nov2006_mean=Nov2006['Open'].mean()
print("Nov 2006 Mean Opening Price:", Nov2006_mean)
Nov2006.plot(x='Date', y='Open', title='AMD Opening Prices in November 2006')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2006=df.loc[(df['Date'] >= '2006-12-01') & (df['Date'] < '2006-12-31')]
print(Dec2006)

Dec2006_mean=Dec2006['Open'].mean()
print("Dec 2006 Mean Opening Price:", Dec2006_mean)
Dec2006.plot(x='Date', y='Open', title='AMD Opening Prices in December 2006')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2007=df.loc[(df['Date'] >= '2007-01-01') & (df['Date'] < '2007-01-31')]
print(Jan2007)
Jan2007_mean=Jan2007['Open'].mean()
print("Jan 2007 Mean Opening Price:", Jan2007_mean)
Jan2007.plot(x='Date', y='Open', title='AMD Opening Prices in January 2007')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2007=df.loc[(df['Date'] >= '2007-02-01') & (df['Date'] < '2007-02-28')]
print(Feb2007)

Feb2007_mean=Feb2007['Open'].mean()
print("Feb 2007 Mean Opening Price:", Feb2007_mean)
Feb2007.plot(x='Date', y='Open', title='AMD Opening Prices in February 2007')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2007=df.loc[(df['Date'] >= '2007-03-01') & (df['Date'] < '2007-03-31')]
print(Mar2007)

Mar2007_mean=Mar2007['Open'].mean()
print("Mar 2007 Mean Opening Price:", Mar2007_mean)
Mar2007.plot(x='Date', y='Open', title='AMD Opening Prices in March 2007')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2007=df.loc[(df['Date'] >= '2007-04-01') & (df['Date'] < '2007-04-30')]
print(Apr2007)

Apr2007_mean=Apr2007['Open'].mean()
print("Apr 2007 Mean Opening Price:", Apr2007_mean)
Apr2007.plot(x='Date', y='Open', title='AMD Opening Prices in April 2007')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2007=df.loc[(df['Date'] >= '2007-05-01') & (df['Date'] < '2007-05-31')]
print(May2007)

May2007_mean=May2007['Open'].mean()
print("May 2007 Mean Opening Price:", May2007_mean)
May2007.plot(x='Date', y='Open', title='AMD Opening Prices in May 2007')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2007=df.loc[(df['Date'] >= '2007-06-01') & (df['Date'] < '2007-06-30')]
print(Jun2007)

Jun2007_mean=Jun2007['Open'].mean()
print("Jun 2007 Mean Opening Price:", Jun2007_mean)
Jun2007.plot(x='Date', y='Open', title='AMD Opening Prices in June 2007')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2007=df.loc[(df['Date'] >= '2007-07-01') & (df['Date'] < '2007-07-31')]
print(Jul2007)

Jul2007_mean=Jul2007['Open'].mean()
print("Jul 2007 Mean Opening Price:", Jul2007_mean)
Jul2007.plot(x='Date', y='Open', title='AMD Opening Prices in July 2007')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2007=df.loc[(df['Date'] >= '2007-08-01') & (df['Date'] < '2007-08-31')]
print(Aug2007)

Aug2007_mean=Aug2007['Open'].mean()
print("Aug 2007 Mean Opening Price:", Aug2007_mean)
Aug2007.plot(x='Date', y='Open', title='AMD Opening Prices in August 2007')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2007=df.loc[(df['Date'] >= '2007-09-01') & (df['Date'] < '2007-09-30')]
print(Sep2007)

Sep2007_mean=Sep2007['Open'].mean()
print("Sep 2007 Mean Opening Price:", Sep2007_mean)
Sep2007.plot(x='Date', y='Open', title='AMD Opening Prices in September 2007')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2007=df.loc[(df['Date'] >= '2007-10-01') & (df['Date'] < '2007-10-31')]
print(Oct2007)

Oct2007_mean=Oct2007['Open'].mean()
print("Oct 2007 Mean Opening Price:", Oct2007_mean)
Oct2007.plot(x='Date', y='Open', title='AMD Opening Prices in October 2007')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2007=df.loc[(df['Date'] >= '2007-11-01') & (df['Date'] < '2007-11-30')]
print(Nov2007)

Nov2007_mean=Nov2007['Open'].mean()
print("Nov 2007 Mean Opening Price:", Nov2007_mean)
Nov2007.plot(x='Date', y='Open', title='AMD Opening Prices in November 2007')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2007=df.loc[(df['Date'] >= '2007-12-01') & (df['Date'] < '2007-12-31')]
print(Dec2007)

Dec2007_mean=Dec2007['Open'].mean()
print("Dec 2007 Mean Opening Price:", Dec2007_mean)
Dec2007.plot(x='Date', y='Open', title='AMD Opening Prices in December 2007')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2008=df.loc[(df['Date'] >= '2008-01-01') & (df['Date'] < '2008-01-31')]
print(Jan2008)

Jan2008_mean=Jan2008['Open'].mean()
print("Jan 2008 Mean Opening Price:", Jan2008_mean)
Jan2008.plot(x='Date', y='Open', title='AMD Opening Prices in January 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2008=df.loc[(df['Date'] >= '2008-02-01') & (df['Date'] < '2008-02-29')]
print(Feb2008)

Feb2008_mean=Feb2008['Open'].mean()
print("Feb 2008 Mean Opening Price:", Feb2008_mean)
Feb2008.plot(x='Date', y='Open', title='AMD Opening Prices in February 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2008=df.loc[(df['Date'] >= '2008-03-01') & (df['Date'] < '2008-03-31')]
print(Mar2008)

Mar2008_mean=Mar2008['Open'].mean()
print("Mar 2008 Mean Opening Price:", Mar2008_mean)
Mar2008.plot(x='Date', y='Open', title='AMD Opening Prices in March 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2008=df.loc[(df['Date'] >= '2008-04-01') & (df['Date'] < '2008-04-30')]
print(Apr2008)

Apr2008_mean=Apr2008['Open'].mean()
print("Apr 2008 Mean Opening Price:", Apr2008_mean)
Apr2008.plot(x='Date', y='Open', title='AMD Opening Prices in April 2008')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2008=df.loc[(df['Date'] >= '2008-05-01') & (df['Date'] < '2008-05-31')]
print(May2008)

May2008_mean=May2008['Open'].mean()
print("May 2008 Mean Opening Price:", May2008_mean)
May2008.plot(x='Date', y='Open', title='AMD Opening Prices in May 2008')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2008=df.loc[(df['Date'] >= '2008-06-01') & (df['Date'] < '2008-06-30')]
print(Jun2008)

Jun2008_mean=Jun2008['Open'].mean()
print("Jun 2008 Mean Opening Price:", Jun2008_mean)
Jun2008.plot(x='Date', y='Open', title='AMD Opening Prices in June 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2008=df.loc[(df['Date'] >= '2008-07-01') & (df['Date'] < '2008-07-31')]
print(Jul2008)

Jul2008_mean=Jul2008['Open'].mean()
print("Jul 2008 Mean Opening Price:", Jul2008_mean)
Jul2008.plot(x='Date', y='Open', title='AMD Opening Prices in July 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2008=df.loc[(df['Date'] >= '2008-08-01') & (df['Date'] < '2008-08-31')]
print(Aug2008)

Aug2008_mean=Aug2008['Open'].mean()
print("Aug 2008 Mean Opening Price:", Aug2008_mean)
Aug2008.plot(x='Date', y='Open', title='AMD Opening Prices in August 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2008=df.loc[(df['Date'] >= '2008-09-01') & (df['Date'] < '2008-09-30')]
print(Sep2008)

Sep2008_mean=Sep2008['Open'].mean()
print("Sep 2008 Mean Opening Price:", Sep2008_mean)
Sep2008.plot(x='Date', y='Open', title='AMD Opening Prices in September 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2008=df.loc[(df['Date'] >= '2008-10-01') & (df['Date'] < '2008-10-31')]
print(Oct2008)

Oct2008_mean=Oct2008['Open'].mean()
print("Oct 2008 Mean Opening Price:", Oct2008_mean)
Oct2008.plot(x='Date', y='Open', title='AMD Opening Prices in October 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2008=df.loc[(df['Date'] >= '2008-11-01') & (df['Date'] < '2008-11-30')]
print(Nov2008)

Nov2008_mean=Nov2008['Open'].mean()
print("Nov 2008 Mean Opening Price:", Nov2008_mean)
Nov2008.plot(x='Date', y='Open', title='AMD Opening Prices in November 2008')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Dec2008=df.loc[(df['Date'] >= '2008-12-01') & (df['Date'] < '2008-12-31')]
print(Dec2008)

Dec2008_mean=Dec2008['Open'].mean()
print("Dec 2008 Mean Opening Price:", Dec2008_mean)
Dec2008.plot(x='Date', y='Open', title='AMD Opening Prices in December 2008')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2009=df.loc[(df['Date'] >= '2009-01-01') & (df['Date'] < '2009-01-31')]
print(Jan2009)

Jan2009_mean=Jan2009['Open'].mean()
print("Jan 2009 Mean Opening Price:", Jan2009_mean)
Jan2009.plot(x='Date', y='Open', title='AMD Opening Prices in January 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2009=df.loc[(df['Date'] >= '2009-02-01') & (df['Date'] < '2009-02-28')]
print(Feb2009)

Feb2009_mean=Feb2009['Open'].mean()
print("Feb 2009 Mean Opening Price:", Feb2009_mean)
Feb2009.plot(x='Date', y='Open', title='AMD Opening Prices in February 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2009=df.loc[(df['Date'] >= '2009-03-01') & (df['Date'] < '2009-03-31')]
print(Mar2009)

Mar2009_mean=Mar2009['Open'].mean()
print("Mar 2009 Mean Opening Price:", Mar2009_mean)
Mar2009.plot(x='Date', y='Open', title='AMD Opening Prices in March 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2009=df.loc[(df['Date'] >= '2009-04-01') & (df['Date'] < '2009-04-30')]
print(Apr2009)

Apr2009_mean=Apr2009['Open'].mean()
print("Apr 2009 Mean Opening Price:", Apr2009_mean)
Apr2009.plot(x='Date', y='Open', title='AMD Opening Prices in April 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2009=df.loc[(df['Date'] >= '2009-05-01') & (df['Date'] < '2009-05-31')]
print(May2009)

May2009_mean=May2009['Open'].mean()
print("May 2009 Mean Opening Price:", May2009_mean)
May2009.plot(x='Date', y='Open', title='AMD Opening Prices in May 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2009=df.loc[(df['Date'] >= '2009-06-01') & (df['Date'] < '2009-06-30')]
print(Jun2009)

Jun2009_mean=Jun2009['Open'].mean()
print("Jun 2009 Mean Opening Price:", Jun2009_mean)
Jun2009.plot(x='Date', y='Open', title='AMD Opening Prices in June 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2009=df.loc[(df['Date'] >= '2009-07-01') & (df['Date'] < '2009-07-31')]
print(Jul2009)

Jul2009_mean=Jul2009['Open'].mean()
print("Jul 2009 Mean Opening Price:", Jul2009_mean)
Jul2009.plot(x='Date', y='Open', title='AMD Opening Prices in July 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2009=df.loc[(df['Date'] >= '2009-08-01') & (df['Date'] < '2009-08-31')]
print(Aug2009)

Aug2009_mean=Aug2009['Open'].mean()
print("Aug 2009 Mean Opening Price:", Aug2009_mean)
Aug2009.plot(x='Date', y='Open', title='AMD Opening Prices in August 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2009=df.loc[(df['Date'] >= '2009-09-01') & (df['Date'] < '2009-09-30')]
print(Sep2009)

Sep2009_mean=Sep2009['Open'].mean()
print("Sep 2009 Mean Opening Price:", Sep2009_mean)
Sep2009.plot(x='Date', y='Open', title='AMD Opening Prices in September 2009')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2009=df.loc[(df['Date'] >= '2009-10-01') & (df['Date'] < '2009-10-31')]
print(Oct2009)

Oct2009_mean=Oct2009['Open'].mean()
print("Oct 2009 Mean Opening Price:", Oct2009_mean)
Oct2009.plot(x='Date', y='Open', title='AMD Opening Prices in October 2009')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2009=df.loc[(df['Date'] >= '2009-11-01') & (df['Date'] < '2009-11-30')]
print(Nov2009)

Nov2009_mean=Nov2009['Open'].mean()
print("Nov 2009 Mean Opening Price:", Nov2009_mean)
Nov2009.plot(x='Date', y='Open', title='AMD Opening Prices in November 2009')

plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2009=df.loc[(df['Date'] >= '2009-12-01') & (df['Date'] < '2009-12-31')]
print(Dec2009)

Dec2009_mean=Dec2009['Open'].mean()
print("Dec 2009 Mean Opening Price:", Dec2009_mean)
Dec2009.plot(x='Date', y='Open', title='AMD Opening Prices in December 2009')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2010=df.loc[(df['Date'] >= '2010-01-01') & (df['Date'] < '2010-01-31')]
print(Jan2010)

Jan2010_mean=Jan2010['Open'].mean()
print("Jan 2010 Mean Opening Price:", Jan2010_mean)
Jan2010.plot(x='Date', y='Open', title='AMD Opening Prices in January 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2010=df.loc[(df['Date'] >= '2010-02-01') & (df['Date'] < '2010-02-28')]
print(Feb2010)

Feb2010_mean=Feb2010['Open'].mean()
print("Feb 2010 Mean Opening Price:", Feb2010_mean)
Feb2010.plot(x='Date', y='Open', title='AMD Opening Prices in February 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2010=df.loc[(df['Date'] >= '2010-03-01') & (df['Date'] < '2010-03-31')]
print(Mar2010)

Mar2010_mean=Mar2010['Open'].mean()
print("Mar 2010 Mean Opening Price:", Mar2010_mean)
Mar2010.plot(x='Date', y='Open', title='AMD Opening Prices in March 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2010=df.loc[(df['Date'] >= '2010-04-01') & (df['Date'] < '2010-04-30')]
print(Apr2010)

Apr2010_mean=Apr2010['Open'].mean()
print("Apr 2010 Mean Opening Price:", Apr2010_mean)
Apr2010.plot(x='Date', y='Open', title='AMD Opening Prices in April 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2010=df.loc[(df['Date'] >= '2010-05-01') & (df['Date'] < '2010-05-31')]
print(May2010)

May2010_mean=May2010['Open'].mean()
print("May 2010 Mean Opening Price:", May2010_mean)
May2010.plot(x='Date', y='Open', title='AMD Opening Prices in May 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2010=df.loc[(df['Date'] >= '2010-06-01') & (df['Date'] < '2010-06-30')]
print(Jun2010)

Jun2010_mean=Jun2010['Open'].mean()
print("Jun 2010 Mean Opening Price:", Jun2010_mean)
Jun2010.plot(x='Date', y='Open', title='AMD Opening Prices in June 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2010=df.loc[(df['Date'] >= '2010-07-01') & (df['Date'] < '2010-07-31')]
print(Jul2010)

Jul2010_mean=Jul2010['Open'].mean()
print("Jul 2010 Mean Opening Price:", Jul2010_mean)
Jul2010.plot(x='Date', y='Open', title='AMD Opening Prices in July 2010')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2010=df.loc[(df['Date'] >= '2010-08-01') & (df['Date'] < '2010-08-31')]
print(Aug2010)

Aug2010_mean=Aug2010['Open'].mean()
print("Aug 2010 Mean Opening Price:", Aug2010_mean)
Aug2010.plot(x='Date', y='Open', title='AMD Opening Prices in August 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2010=df.loc[(df['Date'] >= '2010-09-01') & (df['Date'] < '2010-09-30')]
print(Sep2010)

Sep2010_mean=Sep2010['Open'].mean()
print("Sep 2010 Mean Opening Price:", Sep2010_mean)
Sep2010.plot(x='Date', y='Open', title='AMD Opening Prices in September 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2010=df.loc[(df['Date'] >= '2010-10-01') & (df['Date'] < '2010-10-31')]
print(Oct2010)

Oct2010_mean=Oct2010['Open'].mean()
print("Oct 2010 Mean Opening Price:", Oct2010_mean)
Oct2010.plot(x='Date', y='Open', title='AMD Opening Prices in October 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2010=df.loc[(df['Date'] >= '2010-11-01') & (df['Date'] < '2010-11-30')]
print(Nov2010)
Nov2010_mean=Nov2010['Open'].mean()
print("Nov 2010 Mean Opening Price:", Nov2010_mean)
Nov2010.plot(x='Date', y='Open', title='AMD Opening Prices in November 2010')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2010=df.loc[(df['Date'] >= '2010-12-01') & (df['Date'] < '2010-12-31')]
print(Dec2010)

Dec2010_mean=Dec2010['Open'].mean()
print("Dec 2010 Mean Opening Price:", Dec2010_mean)
Dec2010.plot(x='Date', y='Open', title='AMD Opening Prices in December 2010')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2011=df.loc[(df['Date'] >= '2011-01-01') & (df['Date'] < '2011-01-31')]
print(Jan2011)

Jan2011_mean=Jan2011['Open'].mean()
print("Jan 2011 Mean Opening Price:", Jan2011_mean)
Jan2011.plot(x='Date', y='Open', title='AMD Opening Prices in January 2011')

plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2011=df.loc[(df['Date'] >= '2011-02-01') & (df['Date'] < '2011-02-28')]
print(Feb2011)

Feb2011_mean=Feb2011['Open'].mean()
print("Feb 2011 Mean Opening Price:", Feb2011_mean)
Feb2011.plot(x='Date', y='Open', title='AMD Opening Prices in February 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2011=df.loc[(df['Date'] >= '2011-03-01') & (df['Date'] < '2011-03-31')]
print(Mar2011)

Mar2011_mean=Mar2011['Open'].mean()
print("Mar 2011 Mean Opening Price:", Mar2011_mean)
Mar2011.plot(x='Date', y='Open', title='AMD Opening Prices in March 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2011=df.loc[(df['Date'] >= '2011-04-01') & (df['Date'] < '2011-04-30')]
print(Apr2011)

Apr2011_mean=Apr2011['Open'].mean()
print("Apr 2011 Mean Opening Price:", Apr2011_mean)
Apr2011.plot(x='Date', y='Open', title='AMD Opening Prices in April 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2011=df.loc[(df['Date'] >= '2011-05-01') & (df['Date'] < '2011-05-31')]
print(May2011)

May2011_mean=May2011['Open'].mean()
print("May 2011 Mean Opening Price:", May2011_mean)
May2011.plot(x='Date', y='Open', title='AMD Opening Prices in May 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2011=df.loc[(df['Date'] >= '2011-06-01') & (df['Date'] < '2011-06-30')]
print(Jun2011)

Jun2011_mean=Jun2011['Open'].mean()
print("Jun 2011 Mean Opening Price:", Jun2011_mean)
Jun2011.plot(x='Date', y='Open', title='AMD Opening Prices in June 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2011=df.loc[(df['Date'] >= '2011-07-01') & (df['Date'] < '2011-07-31')]
print(Jul2011)

Jul2011_mean=Jul2011['Open'].mean()
print("Jul 2011 Mean Opening Price:", Jul2011_mean)
Jul2011.plot(x='Date', y='Open', title='AMD Opening Prices in July 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2011=df.loc[(df['Date'] >= '2011-08-01') & (df['Date'] < '2011-08-31')]
print(Aug2011)

Aug2011_mean=Aug2011['Open'].mean()
print("Aug 2011 Mean Opening Price:", Aug2011_mean)
Aug2011.plot(x='Date', y='Open', title='AMD Opening Prices in August 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2011=df.loc[(df['Date'] >= '2011-09-01') & (df['Date'] < '2011-09-30')]
print(Sep2011)
Sep2011_mean=Sep2011['Open'].mean()
print("Sep 2011 Mean Opening Price:", Sep2011_mean)
Sep2011.plot(x='Date', y='Open', title='AMD Opening Prices in September 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])

Oct2011=df.loc[(df['Date'] >= '2011-10-01') & (df['Date'] < '2011-10-31')]
print(Oct2011)
Oct2011_mean=Oct2011['Open'].mean()
print("Oct 2011 Mean Opening Price:", Oct2011_mean)
Oct2011.plot(x='Date', y='Open', title='AMD Opening Prices in October 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2011=df.loc[(df['Date'] >= '2011-11-01') & (df['Date'] < '2011-11-30')]
print(Nov2011)

Nov2011_mean=Nov2011['Open'].mean()
print("Nov 2011 Mean Opening Price:", Nov2011_mean)
Nov2011.plot(x='Date', y='Open', title='AMD Opening Prices in November 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2011=df.loc[(df['Date'] >= '2011-12-01') & (df['Date'] < '2011-12-31')]
print(Dec2011)

Dec2011_mean=Dec2011['Open'].mean()
print("Dec 2011 Mean Opening Price:", Dec2011_mean)
Dec2011.plot(x='Date', y='Open', title='AMD Opening Prices in December 2011')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2012=df.loc[(df['Date'] >= '2012-01-01') & (df['Date'] < '2012-01-31')]
print(Jan2012)

Jan2012_mean=Jan2012['Open'].mean()
print("Jan 2012 Mean Opening Price:", Jan2012_mean)
Jan2012.plot(x='Date', y='Open', title='AMD Opening Prices in January 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2012=df.loc[(df['Date'] >= '2012-02-01') & (df['Date'] < '2012-02-29')]
print(Feb2012)
Feb2012_mean=Feb2012['Open'].mean()
print("Feb 2012 Mean Opening Price:", Feb2012_mean)
Feb2012.plot(x='Date', y='Open', title='AMD Opening Prices in February 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2012=df.loc[(df['Date'] >= '2012-03-01') & (df['Date'] < '2012-03-31')]
print(Mar2012)

Mar2012_mean=Mar2012['Open'].mean()
print("Mar 2012 Mean Opening Price:", Mar2012_mean)
Mar2012.plot(x='Date', y='Open', title='AMD Opening Prices in March 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Apr2012=df.loc[(df['Date'] >= '2012-04-01') & (df['Date'] < '2012-04-30')]
print(Apr2012)
Apr2012_mean=Apr2012['Open'].mean()
print("Apr 2012 Mean Opening Price:", Apr2012_mean)
Apr2012.plot(x='Date', y='Open', title='AMD Opening Prices in April 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2012=df.loc[(df['Date'] >= '2012-05-01') & (df['Date'] < '2012-05-31')]
print(May2012)

May2012_mean=May2012['Open'].mean()
print("May 2012 Mean Opening Price:", May2012_mean)
May2012.plot(x='Date', y='Open', title='AMD Opening Prices in May 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2012=df.loc[(df['Date'] >= '2012-06-01') & (df['Date'] < '2012-06-30')]
print(Jun2012)

Jun2012_mean=Jun2012['Open'].mean()
print("Jun 2012 Mean Opening Price:", Jun2012_mean)
Jun2012.plot(x='Date', y='Open', title='AMD Opening Prices in June 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2012=df.loc[(df['Date'] >= '2012-07-01') & (df['Date'] < '2012-07-31')]
print(Jul2012)

Jul2012_mean=Jul2012['Open'].mean()
print("Jul 2012 Mean Opening Price:", Jul2012_mean)
Jul2012.plot(x='Date', y='Open', title='AMD Opening Prices in July 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2012=df.loc[(df['Date'] >= '2012-08-01') & (df['Date'] < '2012-08-31')]
print(Aug2012)

Aug2012_mean=Aug2012['Open'].mean()
print("Aug 2012 Mean Opening Price:", Aug2012_mean)
Aug2012.plot(x='Date', y='Open', title='AMD Opening Prices in August 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Sep2012=df.loc[(df['Date'] >= '2012-09-01') & (df['Date'] < '2012-09-30')]
print(Sep2012)

Sep2012_mean=Sep2012['Open'].mean()
print("Sep 2012 Mean Opening Price:", Sep2012_mean)
Sep2012.plot(x='Date', y='Open', title='AMD Opening Prices in September 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2012=df.loc[(df['Date'] >= '2012-10-01') & (df['Date'] < '2012-10-31')]
print(Oct2012)

Oct2012_mean=Oct2012['Open'].mean()
print("Oct 2012 Mean Opening Price:", Oct2012_mean)
Oct2012.plot(x='Date', y='Open', title='AMD Opening Prices in October 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2012=df.loc[(df['Date'] >= '2012-11-01') & (df['Date'] < '2012-11-30')]
print(Nov2012)

Nov2012_mean=Nov2012['Open'].mean()
print("Nov 2012 Mean Opening Price:", Nov2012_mean)
Nov2012.plot(x='Date', y='Open', title='AMD Opening Prices in November 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2012=df.loc[(df['Date'] >= '2012-12-01') & (df['Date'] < '2012-12-31')]
print(Dec2012)

Dec2012_mean=Dec2012['Open'].mean()
print("Dec 2012 Mean Opening Price:", Dec2012_mean)
Dec2012.plot(x='Date', y='Open', title='AMD Opening Prices in December 2012')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2013=df.loc[(df['Date'] >= '2013-01-01') & (df['Date'] < '2013-01-31')]
print(Jan2013)

Jan2013_mean=Jan2013['Open'].mean()
print("Jan 2013 Mean Opening Price:", Jan2013_mean)
Jan2013.plot(x='Date', y='Open', title='AMD Opening Prices in January 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2013=df.loc[(df['Date'] >= '2013-02-01') & (df['Date'] < '2013-02-28')]
print(Feb2013)

Feb2013_mean=Feb2013['Open'].mean()
print("Feb 2013 Mean Opening Price:", Feb2013_mean)
Feb2013.plot(x='Date', y='Open', title='AMD Opening Prices in February 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2013=df.loc[(df['Date'] >= '2013-03-01') & (df['Date'] < '2013-03-31')]
print(Mar2013)

Mar2013_mean=Mar2013['Open'].mean()
print("Mar 2013 Mean Opening Price:", Mar2013_mean)
Mar2013.plot(x='Date', y='Open', title='AMD Opening Prices in March 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2013=df.loc[(df['Date'] >= '2013-04-01') & (df['Date'] < '2013-04-30')]
print(Apr2013)

Apr2013_mean=Apr2013['Open'].mean()
print("Apr 2013 Mean Opening Price:", Apr2013_mean)
Apr2013.plot(x='Date', y='Open', title='AMD Opening Prices in April 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2013=df.loc[(df['Date'] >= '2013-05-01') & (df['Date'] < '2013-05-31')]
print(May2013)

May2013_mean=May2013['Open'].mean()
print("May 2013 Mean Opening Price:", May2013_mean)
May2013.plot(x='Date', y='Open', title='AMD Opening Prices in May 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2013=df.loc[(df['Date'] >= '2013-06-01') & (df['Date'] < '2013-06-30')]
print(Jun2013)

Jun2013_mean=Jun2013['Open'].mean()
print("Jun 2013 Mean Opening Price:", Jun2013_mean)
Jun2013.plot(x='Date', y='Open', title='AMD Opening Prices in June 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2013=df.loc[(df['Date'] >= '2013-07-01') & (df['Date'] < '2013-07-31')]
print(Jul2013)

Jul2013_mean=Jul2013['Open'].mean()
print("Jul 2013 Mean Opening Price:", Jul2013_mean)
Jul2013.plot(x='Date', y='Open', title='AMD Opening Prices in July 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2013=df.loc[(df['Date'] >= '2013-08-01') & (df['Date'] < '2013-08-31')]
print(Aug2013)

Aug2013_mean=Aug2013['Open'].mean()
print("Aug 2013 Mean Opening Price:", Aug2013_mean)
Aug2013.plot(x='Date', y='Open', title='AMD Opening Prices in August 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2013=df.loc[(df['Date'] >= '2013-09-01') & (df['Date'] < '2013-09-30')]
print(Sep2013)

Sep2013_mean=Sep2013['Open'].mean()
print("Sep 2013 Mean Opening Price:", Sep2013_mean)
Sep2013.plot(x='Date', y='Open', title='AMD Opening Prices in September 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2013=df.loc[(df['Date'] >= '2013-10-01') & (df['Date'] < '2013-10-31')]
print(Oct2013)

Oct2013_mean=Oct2013['Open'].mean()
print("Oct 2013 Mean Opening Price:", Oct2013_mean)
Oct2013.plot(x='Date', y='Open', title='AMD Opening Prices in October 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov2013=df.loc[(df['Date'] >= '2013-11-01') & (df['Date'] < '2013-11-30')]
print(Nov2013)
Nov2013_mean=Nov2013['Open'].mean()
print("Nov 2013 Mean Opening Price:", Nov2013_mean)
Nov2013.plot(x='Date', y='Open', title='AMD Opening Prices in November 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2013=df.loc[(df['Date'] >= '2013-12-01') & (df['Date'] < '2013-12-31')]
print(Dec2013)

Dec2013_mean=Dec2013['Open'].mean()
print("Dec 2013 Mean Opening Price:", Dec2013_mean)
Dec2013.plot(x='Date', y='Open', title='AMD Opening Prices in December 2013')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2014=df.loc[(df['Date'] >= '2014-01-01') & (df['Date'] < '2014-01-31')]
print(Jan2014)

Jan2014_mean=Jan2014['Open'].mean()
print("Jan 2014 Mean Opening Price:", Jan2014_mean)
Jan2014.plot(x='Date', y='Open', title='AMD Opening Prices in January 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2014=df.loc[(df['Date'] >= '2014-02-01') & (df['Date'] < '2014-02-28')]
print(Feb2014)
Feb2014_mean=Feb2014['Open'].mean()
print("Feb 2014 Mean Opening Price:", Feb2014_mean)
Feb2014.plot(x='Date', y='Open', title='AMD Opening Prices in February 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2014=df.loc[(df['Date'] >= '2014-03-01') & (df['Date'] < '2014-03-31')]
print(Mar2014)

Mar2014_mean=Mar2014['Open'].mean()
print("Mar 2014 Mean Opening Price:", Mar2014_mean)
Mar2014.plot(x='Date', y='Open', title='AMD Opening Prices in March 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2014=df.loc[(df['Date'] >= '2014-04-01') & (df['Date'] < '2014-04-30')]
print(Apr2014)

Apr2014_mean=Apr2014['Open'].mean()
print("Apr 2014 Mean Opening Price:", Apr2014_mean)
Apr2014.plot(x='Date', y='Open', title='AMD Opening Prices in April 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2014=df.loc[(df['Date'] >= '2014-05-01') & (df['Date'] < '2014-05-31')]
print(May2014)

May2014_mean=May2014['Open'].mean()
print("May 2014 Mean Opening Price:", May2014_mean)
May2014.plot(x='Date', y='Open', title='AMD Opening Prices in May 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2014=df.loc[(df['Date'] >= '2014-06-01') & (df['Date'] < '2014-06-30')]
print(Jun2014)

Jun2014_mean=Jun2014['Open'].mean()
print("Jun 2014 Mean Opening Price:", Jun2014_mean)
Jun2014.plot(x='Date', y='Open', title='AMD Opening Prices in June 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2014=df.loc[(df['Date'] >= '2014-07-01') & (df['Date'] < '2014-07-31')]
print(Jul2014)

Jul2014_mean=Jul2014['Open'].mean()
print("Jul 2014 Mean Opening Price:", Jul2014_mean)
Jul2014.plot(x='Date', y='Open', title='AMD Opening Prices in July 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2014=df.loc[(df['Date'] >= '2014-08-01') & (df['Date'] < '2014-08-31')]
print(Aug2014)

Aug2014_mean=Aug2014['Open'].mean()
print("Aug 2014 Mean Opening Price:", Aug2014_mean)
Aug2014.plot(x='Date', y='Open', title='AMD Opening Prices in August 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2014=df.loc[(df['Date'] >= '2014-09-01') & (df['Date'] < '2014-09-30')]
print(Sep2014)

Sep2014_mean=Sep2014['Open'].mean()
print("Sep 2014 Mean Opening Price:", Sep2014_mean)
Sep2014.plot(x='Date', y='Open', title='AMD Opening Prices in September 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2014=df.loc[(df['Date'] >= '2014-10-01') & (df['Date'] < '2014-10-31')]
print(Oct2014)

Oct2014_mean=Oct2014['Open'].mean()
print("Oct 2014 Mean Opening Price:", Oct2014_mean)
Oct2014.plot(x='Date', y='Open', title='AMD Opening Prices in October 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov2014=df.loc[(df['Date'] >= '2014-11-01') & (df['Date'] < '2014-11-30')]
print(Nov2014)

Nov2014_mean=Nov2014['Open'].mean()
print("Nov 2014 Mean Opening Price:", Nov2014_mean)
Nov2014.plot(x='Date', y='Open', title='AMD Opening Prices in November 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2014=df.loc[(df['Date'] >= '2014-12-01') & (df['Date'] < '2014-12-31')]
print(Dec2014)

Dec2014_mean=Dec2014['Open'].mean()
print("Dec 2014 Mean Opening Price:", Dec2014_mean)
Dec2014.plot(x='Date', y='Open', title='AMD Opening Prices in December 2014')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Jan2015=df.loc[(df['Date'] >= '2015-01-01') & (df['Date'] < '2015-01-31')]
print(Jan2015)
Jan2015_mean=Jan2015['Open'].mean()
print("Jan 2015 Mean Opening Price:", Jan2015_mean)
Jan2015.plot(x='Date', y='Open', title='AMD Opening Prices in January 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Feb2015=df.loc[(df['Date'] >= '2015-02-01') & (df['Date'] < '2015-02-28')]
print(Feb2015)
Feb2015_mean=Feb2015['Open'].mean()
print("Feb 2015 Mean Opening Price:", Feb2015_mean)
Feb2015.plot(x='Date', y='Open', title='AMD Opening Prices in February 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2015=df.loc[(df['Date'] >= '2015-03-01') & (df['Date'] < '2015-03-31')]
print(Mar2015)

Mar2015_mean=Mar2015['Open'].mean()
print("Mar 2015 Mean Opening Price:", Mar2015_mean)
Mar2015.plot(x='Date', y='Open', title='AMD Opening Prices in March 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2015=df.loc[(df['Date'] >= '2015-04-01') & (df['Date'] < '2015-04-30')]
print(Apr2015)

Apr2015_mean=Apr2015['Open'].mean()
print("Apr 2015 Mean Opening Price:", Apr2015_mean)
Apr2015.plot(x='Date', y='Open', title='AMD Opening Prices in April 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2015=df.loc[(df['Date'] >= '2015-05-01') & (df['Date'] < '2015-05-31')]
print(May2015)

May2015_mean=May2015['Open'].mean()
print("May 2015 Mean Opening Price:", May2015_mean)
May2015.plot(x='Date', y='Open', title='AMD Opening Prices in May 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2015=df.loc[(df['Date'] >= '2015-06-01') & (df['Date'] < '2015-06-30')]
print(Jun2015)

Jun2015_mean=Jun2015['Open'].mean()
print("Jun 2015 Mean Opening Price:", Jun2015_mean)
Jun2015.plot(x='Date', y='Open', title='AMD Opening Prices in June 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2015=df.loc[(df['Date'] >= '2015-07-01') & (df['Date'] < '2015-07-31')]
print(Jul2015)

Jul2015_mean=Jul2015['Open'].mean()
print("Jul 2015 Mean Opening Price:", Jul2015_mean)
Jul2015.plot(x='Date', y='Open', title='AMD Opening Prices in July 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2015=df.loc[(df['Date'] >= '2015-08-01') & (df['Date'] < '2015-08-31')]
print(Aug2015)

Aug2015_mean=Aug2015['Open'].mean()
print("Aug 2015 Mean Opening Price:", Aug2015_mean)
Aug2015.plot(x='Date', y='Open', title='AMD Opening Prices in August 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2015=df.loc[(df['Date'] >= '2015-09-01') & (df['Date'] < '2015-09-30')]
print(Sep2015)
Sep2015_mean=Sep2015['Open'].mean()
print("Sep 2015 Mean Opening Price:", Sep2015_mean)
Sep2015.plot(x='Date', y='Open', title='AMD Opening Prices in September 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Oct2015=df.loc[(df['Date'] >= '2015-10-01') & (df['Date'] < '2015-10-31')]
print(Oct2015)
Oct2015_mean=Oct2015['Open'].mean()
print("Oct 2015 Mean Opening Price:", Oct2015_mean)
Oct2015.plot(x='Date', y='Open', title='AMD Opening Prices in October 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2015=df.loc[(df['Date'] >= '2015-11-01') & (df['Date'] < '2015-11-30')]
print(Nov2015)

Nov2015_mean=Nov2015['Open'].mean()
print("Nov 2015 Mean Opening Price:", Nov2015_mean)
Nov2015.plot(x='Date', y='Open', title='AMD Opening Prices in November 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2015=df.loc[(df['Date'] >= '2015-12-01') & (df['Date'] < '2015-12-31')]
print(Dec2015)

Dec2015_mean=Dec2015['Open'].mean()
print("Dec 2015 Mean Opening Price:", Dec2015_mean)
Dec2015.plot(x='Date', y='Open', title='AMD Opening Prices in December 2015')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2016=df.loc[(df['Date'] >= '2016-01-01') & (df['Date'] < '2016-01-31')]
print(Jan2016)

Jan2016_mean=Jan2016['Open'].mean()
print("Jan 2016 Mean Opening Price:", Jan2016_mean)
Jan2016.plot(x='Date', y='Open', title='AMD Opening Prices in January 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2016=df.loc[(df['Date'] >= '2016-02-01') & (df['Date'] < '2016-02-29')]
print(Feb2016)

Feb2016_mean=Feb2016['Open'].mean()
print("Feb 2016 Mean Opening Price:", Feb2016_mean)
Feb2016.plot(x='Date', y='Open', title='AMD Opening Prices in February 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2016=df.loc[(df['Date'] >= '2016-03-01') & (df['Date'] < '2016-03-31')]
print(Mar2016)

Mar2016_mean=Mar2016['Open'].mean()
print("Mar 2016 Mean Opening Price:", Mar2016_mean)
Mar2016.plot(x='Date', y='Open', title='AMD Opening Prices in March 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2016=df.loc[(df['Date'] >= '2016-04-01') & (df['Date'] < '2016-04-30')]
print(Apr2016)

Apr2016_mean=Apr2016['Open'].mean()
print("Apr 2016 Mean Opening Price:", Apr2016_mean)
Apr2016.plot(x='Date', y='Open', title='AMD Opening Prices in April 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2016=df.loc[(df['Date'] >= '2016-05-01') & (df['Date'] < '2016-05-31')]
print(May2016)

May2016_mean=May2016['Open'].mean()
print("May 2016 Mean Opening Price:", May2016_mean)
May2016.plot(x='Date', y='Open', title='AMD Opening Prices in May 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2016=df.loc[(df['Date'] >= '2016-06-01') & (df['Date'] < '2016-06-30')]
print(Jun2016)

Jun2016_mean=Jun2016['Open'].mean()
print("Jun 2016 Mean Opening Price:", Jun2016_mean)
Jun2016.plot(x='Date', y='Open', title='AMD Opening Prices in June 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2016=df.loc[(df['Date'] >= '2016-07-01') & (df['Date'] < '2016-07-31')]
print(Jul2016)

Jul2016_mean=Jul2016['Open'].mean()
print("Jul 2016 Mean Opening Price:", Jul2016_mean)
Jul2016.plot(x='Date', y='Open', title='AMD Opening Prices in July 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2016=df.loc[(df['Date'] >= '2016-08-01') & (df['Date'] < '2016-08-31')]
print(Aug2016)

Aug2016_mean=Aug2016['Open'].mean()
print("Aug 2016 Mean Opening Price:", Aug2016_mean)
Aug2016.plot(x='Date', y='Open', title='AMD Opening Prices in August 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2016=df.loc[(df['Date'] >= '2016-09-01') & (df['Date'] < '2016-09-30')]
print(Sep2016)
Sep2016_mean=Sep2016['Open'].mean()
print("Sep 2016 Mean Opening Price:", Sep2016_mean)
Sep2016.plot(x='Date', y='Open', title='AMD Opening Prices in September 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2016=df.loc[(df['Date'] >= '2016-10-01') & (df['Date'] < '2016-10-31')]
print(Oct2016)

Oct2016_mean=Oct2016['Open'].mean()
print("Oct 2016 Mean Opening Price:", Oct2016_mean)
Oct2016.plot(x='Date', y='Open', title='AMD Opening Prices in October 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2016=df.loc[(df['Date'] >= '2016-11-01') & (df['Date'] < '2016-11-30')]
print(Nov2016)

Nov2016_mean=Nov2016['Open'].mean()
print("Nov 2016 Mean Opening Price:", Nov2016_mean)
Nov2016.plot(x='Date', y='Open', title='AMD Opening Prices in November 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2016=df.loc[(df['Date'] >= '2016-12-01') & (df['Date'] < '2016-12-31')]
print(Dec2016)

Dec2016_mean=Dec2016['Open'].mean()
print("Dec 2016 Mean Opening Price:", Dec2016_mean)
Dec2016.plot(x='Date', y='Open', title='AMD Opening Prices in December 2016')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2017=df.loc[(df['Date'] >= '2017-01-01') & (df['Date'] < '2017-01-31')]
print(Jan2017)
Jan2017_mean=Jan2017['Open'].mean()
print("Jan 2017 Mean Opening Price:", Jan2017_mean)
Jan2017.plot(x='Date', y='Open', title='AMD Opening Prices in January 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2017=df.loc[(df['Date'] >= '2017-02-01') & (df['Date'] < '2017-02-28')]
print(Feb2017)
Feb2017_mean=Feb2017['Open'].mean()
print("Feb 2017 Mean Opening Price:", Feb2017_mean)
Feb2017.plot(x='Date', y='Open', title='AMD Opening Prices in February 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2017=df.loc[(df['Date'] >= '2017-03-01') & (df['Date'] < '2017-03-31')]
print(Mar2017)
Mar2017_mean=Mar2017['Open'].mean()
print("Mar 2017 Mean Opening Price:", Mar2017_mean)
Mar2017.plot(x='Date', y='Open', title='AMD Opening Prices in March 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2017=df.loc[(df['Date'] >= '2017-04-01') & (df['Date'] < '2017-04-30')]
print(Apr2017)

Apr2017_mean=Apr2017['Open'].mean()
print("Apr 2017 Mean Opening Price:", Apr2017_mean)
Apr2017.plot(x='Date', y='Open', title='AMD Opening Prices in April 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
May2017=df.loc[(df['Date'] >= '2017-05-01') & (df['Date'] < '2017-05-31')]
print(May2017)
May2017_mean=May2017['Open'].mean()
print("May 2017 Mean Opening Price:", May2017_mean)
May2017.plot(x='Date', y='Open', title='AMD Opening Prices in May 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2017=df.loc[(df['Date'] >= '2017-06-01') & (df['Date'] < '2017-06-30')]
print(Jun2017)
Jun2017_mean=Jun2017['Open'].mean()
print("Jun 2017 Mean Opening Price:", Jun2017_mean)
Jun2017.plot(x='Date', y='Open', title='AMD Opening Prices in June 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2017=df.loc[(df['Date'] >= '2017-07-01') & (df['Date'] < '2017-07-31')]
print(Jul2017)

Jul2017_mean=Jul2017['Open'].mean()
print("Jul 2017 Mean Opening Price:", Jul2017_mean)
Jul2017.plot(x='Date', y='Open', title='AMD Opening Prices in July 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2017=df.loc[(df['Date'] >= '2017-08-01') & (df['Date'] < '2017-08-31')]
print(Aug2017)

Aug2017_mean=Aug2017['Open'].mean()
print("Aug 2017 Mean Opening Price:", Aug2017_mean)
Aug2017.plot(x='Date', y='Open', title='AMD Opening Prices in August 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2017=df.loc[(df['Date'] >= '2017-09-01') & (df['Date'] < '2017-09-30')]
print(Sep2017)

Sep2017_mean=Sep2017['Open'].mean()
print("Sep 2017 Mean Opening Price:", Sep2017_mean)
Sep2017.plot(x='Date', y='Open', title='AMD Opening Prices in September 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2017=df.loc[(df['Date'] >= '2017-10-01') & (df['Date'] < '2017-10-31')]
print(Oct2017)

Oct2017_mean=Oct2017['Open'].mean()
print("Oct 2017 Mean Opening Price:", Oct2017_mean)
Oct2017.plot(x='Date', y='Open', title='AMD Opening Prices in October 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2017=df.loc[(df['Date'] >= '2017-11-01') & (df['Date'] < '2017-11-30')]
print(Nov2017)

Nov2017_mean=Nov2017['Open'].mean()
print("Nov 2017 Mean Opening Price:", Nov2017_mean)
Nov2017.plot(x='Date', y='Open', title='AMD Opening Prices in November 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2017=df.loc[(df['Date'] >= '2017-12-01') & (df['Date'] < '2017-12-31')]
print(Dec2017)

Dec2017_mean=Dec2017['Open'].mean()
print("Dec 2017 Mean Opening Price:", Dec2017_mean)
Dec2017.plot(x='Date', y='Open', title='AMD Opening Prices in December 2017')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2018=df.loc[(df['Date'] >= '2018-01-01') & (df['Date'] < '2018-01-31')]
print(Jan2018)

Jan2018_mean=Jan2018['Open'].mean()
print("Jan 2018 Mean Opening Price:", Jan2018_mean)
Jan2018.plot(x='Date', y='Open', title='AMD Opening Prices in January 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2018=df.loc[(df['Date'] >= '2018-02-01') & (df['Date'] < '2018-02-28')]
print(Feb2018)

Feb2018_mean=Feb2018['Open'].mean()
print("Feb 2018 Mean Opening Price:", Feb2018_mean)
Feb2018.plot(x='Date', y='Open', title='AMD Opening Prices in February 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2018=df.loc[(df['Date'] >= '2018-03-01') & (df['Date'] < '2018-03-31')]
print(Mar2018)

Mar2018_mean=Mar2018['Open'].mean()
print("Mar 2018 Mean Opening Price:", Mar2018_mean)
Mar2018.plot(x='Date', y='Open', title='AMD Opening Prices in March 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2018=df.loc[(df['Date'] >= '2018-04-01') & (df['Date'] < '2018-04-30')]
print(Apr2018)

Apr2018_mean=Apr2018['Open'].mean()
print("Apr 2018 Mean Opening Price:", Apr2018_mean)
Apr2018.plot(x='Date', y='Open', title='AMD Opening Prices in April 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2018=df.loc[(df['Date'] >= '2018-05-01') & (df['Date'] < '2018-05-31')]
print(May2018)
May2018_mean=May2018['Open'].mean()
print("May 2018 Mean Opening Price:", May2018_mean)
May2018.plot(x='Date', y='Open', title='AMD Opening Prices in May 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2018=df.loc[(df['Date'] >= '2018-06-01') & (df['Date'] < '2018-06-30')]
print(Jun2018)

Jun2018_mean=Jun2018['Open'].mean()
print("Jun 2018 Mean Opening Price:", Jun2018_mean)
Jun2018.plot(x='Date', y='Open', title='AMD Opening Prices in June 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2018=df.loc[(df['Date'] >= '2018-07-01') & (df['Date'] < '2018-07-31')]
print(Jul2018)

Jul2018_mean=Jul2018['Open'].mean()
print("Jul 2018 Mean Opening Price:", Jul2018_mean)
Jul2018.plot(x='Date', y='Open', title='AMD Opening Prices in July 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2018=df.loc[(df['Date'] >= '2018-08-01') & (df['Date'] < '2018-08-31')]
print(Aug2018)

Aug2018_mean=Aug2018['Open'].mean()
print("Aug 2018 Mean Opening Price:", Aug2018_mean)
Aug2018.plot(x='Date', y='Open', title='AMD Opening Prices in August 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2018=df.loc[(df['Date'] >= '2018-09-01') & (df['Date'] < '2018-09-30')]
print(Sep2018)
Sep2018_mean=Sep2018['Open'].mean()
print("Sep 2018 Mean Opening Price:", Sep2018_mean)
Sep2018.plot(x='Date', y='Open', title='AMD Opening Prices in September 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2018=df.loc[(df['Date'] >= '2018-10-01') & (df['Date'] < '2018-10-31')]
print(Oct2018)

Oct2018_mean=Oct2018['Open'].mean()
print("Oct 2018 Mean Opening Price:", Oct2018_mean)
Oct2018.plot(x='Date', y='Open', title='AMD Opening Prices in October 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2018=df.loc[(df['Date'] >= '2018-11-01') & (df['Date'] < '2018-11-30')]
print(Nov2018)

Nov2018_mean=Nov2018['Open'].mean()
print("Nov 2018 Mean Opening Price:", Nov2018_mean)
Nov2018.plot(x='Date', y='Open', title='AMD Opening Prices in November 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2018=df.loc[(df['Date'] >= '2018-12-01') & (df['Date'] < '2018-12-31')]
print(Dec2018)
Dec2018_mean=Dec2018['Open'].mean()
print("Dec 2018 Mean Opening Price:", Dec2018_mean)
Dec2018.plot(x='Date', y='Open', title='AMD Opening Prices in December 2018')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2019=df.loc[(df['Date'] >= '2019-01-01') & (df['Date'] < '2019-01-31')]
print(Jan2019)

Jan2019_mean=Jan2019['Open'].mean()
print("Jan 2019 Mean Opening Price:", Jan2019_mean)
Jan2019.plot(x='Date', y='Open', title='AMD Opening Prices in January 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2019=df.loc[(df['Date'] >= '2019-02-01') & (df['Date'] < '2019-02-28')]
print(Feb2019)
Feb2019_mean=Feb2019['Open'].mean()
print("Feb 2019 Mean Opening Price:", Feb2019_mean)
Feb2019.plot(x='Date', y='Open', title='AMD Opening Prices in February 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2019=df.loc[(df['Date'] >= '2019-03-01') & (df['Date'] < '2019-03-31')]
print(Mar2019)

Mar2019_mean=Mar2019['Open'].mean()
print("Mar 2019 Mean Opening Price:", Mar2019_mean)
Mar2019.plot(x='Date', y='Open', title='AMD Opening Prices in March 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2019=df.loc[(df['Date'] >= '2019-04-01') & (df['Date'] < '2019-04-30')]
print(Apr2019)

Apr2019_mean=Apr2019['Open'].mean()
print("Apr 2019 Mean Opening Price:", Apr2019_mean)
Apr2019.plot(x='Date', y='Open', title='AMD Opening Prices in April 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2019=df.loc[(df['Date'] >= '2019-05-01') & (df['Date'] < '2019-05-31')]
print(May2019)

May2019_mean=May2019['Open'].mean()
print("May 2019 Mean Opening Price:", May2019_mean)
May2019.plot(x='Date', y='Open', title='AMD Opening Prices in May 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2019=df.loc[(df['Date'] >= '2019-06-01') & (df['Date'] < '2019-06-30')]
print(Jun2019)

Jun2019_mean=Jun2019['Open'].mean()
print("Jun 2019 Mean Opening Price:", Jun2019_mean)
Jun2019.plot(x='Date', y='Open', title='AMD Opening Prices in June 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2019=df.loc[(df['Date'] >= '2019-07-01') & (df['Date'] < '2019-07-31')]
print(Jul2019)

Jul2019_mean=Jul2019['Open'].mean()
print("Jul 2019 Mean Opening Price:", Jul2019_mean)
Jul2019.plot(x='Date', y='Open', title='AMD Opening Prices in July 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2019=df.loc[(df['Date'] >= '2019-08-01') & (df['Date'] < '2019-08-31')]
print(Aug2019)

Aug2019_mean=Aug2019['Open'].mean()
print("Aug 2019 Mean Opening Price:", Aug2019_mean)
Aug2019.plot(x='Date', y='Open', title='AMD Opening Prices in August 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2019=df.loc[(df['Date'] >= '2019-09-01') & (df['Date'] < '2019-09-30')]
print(Sep2019)

Sep2019_mean=Sep2019['Open'].mean()
print("Sep 2019 Mean Opening Price:", Sep2019_mean)
Sep2019.plot(x='Date', y='Open', title='AMD Opening Prices in September 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2019=df.loc[(df['Date'] >= '2019-10-01') & (df['Date'] < '2019-10-31')]
print(Oct2019)

Oct2019_mean=Oct2019['Open'].mean()
print("Oct 2019 Mean Opening Price:", Oct2019_mean)
Oct2019.plot(x='Date', y='Open', title='AMD Opening Prices in October 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'])
Nov2019=df.loc[(df['Date'] >= '2019-11-01') & (df['Date'] < '2019-11-30')]
print(Nov2019)

Nov2019_mean=Nov2019['Open'].mean()
print("Nov 2019 Mean Opening Price:", Nov2019_mean)
Nov2019.plot(x='Date', y='Open', title='AMD Opening Prices in November 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2019=df.loc[(df['Date'] >= '2019-12-01') & (df['Date'] < '2019-12-31')]
print(Dec2019)

Dec2019_mean=Dec2019['Open'].mean()
print("Dec 2019 Mean Opening Price:", Dec2019_mean)
Dec2019.plot(x='Date', y='Open', title='AMD Opening Prices in December 2019')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2020=df.loc[(df['Date'] >= '2020-01-01') & (df['Date'] < '2020-01-31')]
print(Jan2020)

Jan2020_mean=Jan2020['Open'].mean()
print("Jan 2020 Mean Opening Price:", Jan2020_mean)
Jan2020.plot(x='Date', y='Open', title='AMD Opening Prices in January 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2020=df.loc[(df['Date'] >= '2020-02-01') & (df['Date'] < '2020-02-29')]
print(Feb2020)

Feb2020_mean=Feb2020['Open'].mean()
print("Feb 2020 Mean Opening Price:", Feb2020_mean)
Feb2020.plot(x='Date', y='Open', title='AMD Opening Prices in February 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2020=df.loc[(df['Date'] >= '2020-03-01') & (df['Date'] < '2020-03-31')]
print(Mar2020)

Mar2020_mean=Mar2020['Open'].mean()
print("Mar 2020 Mean Opening Price:", Mar2020_mean)
Mar2020.plot(x='Date', y='Open', title='AMD Opening Prices in March 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2020=df.loc[(df['Date'] >= '2020-04-01') & (df['Date'] < '2020-04-30')]
print(Apr2020)

Apr2020_mean=Apr2020['Open'].mean()
print("Apr 2020 Mean Opening Price:", Apr2020_mean)
Apr2020.plot(x='Date', y='Open', title='AMD Opening Prices in April 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2020=df.loc[(df['Date'] >= '2020-05-01') & (df['Date'] < '2020-05-31')]
print(May2020)

May2020_mean=May2020['Open'].mean()
print("May 2020 Mean Opening Price:", May2020_mean)
May2020.plot(x='Date', y='Open', title='AMD Opening Prices in May 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2020=df.loc[(df['Date'] >= '2020-06-01') & (df['Date'] < '2020-06-30')]
print(Jun2020)

Jun2020_mean=Jun2020['Open'].mean()
print("Jun 2020 Mean Opening Price:", Jun2020_mean)
Jun2020.plot(x='Date', y='Open', title='AMD Opening Prices in June 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2020=df.loc[(df['Date'] >= '2020-07-01') & (df['Date'] < '2020-07-31')]
print(Jul2020)

Jul2020_mean=May2020['Open'].mean()
print("Jul 2020 Mean Opening Price:", Jul2020_mean)
Jul2020.plot(x='Date', y='Open', title='AMD Opening Prices in July 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2020=df.loc[(df['Date'] >= '2020-08-01') & (df['Date'] < '2020-08-31')]
print(Aug2020)

Aug2020_mean=Aug2020['Open'].mean()
print("Aug 2020 Mean Opening Price:", Aug2020_mean)
Aug2020.plot(x='Date', y='Open', title='AMD Opening Prices in August 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2020=df.loc[(df['Date'] >= '2020-09-01') & (df['Date'] < '2020-09-30')]
print(Sep2020)

Sep2020_mean=Sep2020['Open'].mean()
print("Sep 2020 Mean Opening Price:", Sep2020_mean)
Sep2020.plot(x='Date', y='Open', title='AMD Opening Prices in September 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2020=df.loc[(df['Date'] >= '2020-10-01') & (df['Date'] < '2020-10-31')]
print(Oct2020)

Oct2020_mean=Oct2020['Open'].mean()
print("Oct 2020 Mean Opening Price:", Oct2020_mean)
Oct2020.plot(x='Date', y='Open', title='AMD Opening Prices in October 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2020=df.loc[(df['Date'] >= '2020-11-01') & (df['Date'] < '2020-11-30')]
print(Nov2020)

Nov2020_mean=Nov2020['Open'].mean()
print("Nov 2020 Mean Opening Price:", Nov2020_mean)
Nov2020.plot(x='Date', y='Open', title='AMD Opening Prices in November 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2020=df.loc[(df['Date'] >= '2020-12-01') & (df['Date'] < '2020-12-31')]
print(Dec2020)

Dec2020_mean=Dec2020['Open'].mean()
print("Dec 2020 Mean Opening Price:", Dec2020_mean)
Dec2020.plot(x='Date', y='Open', title='AMD Opening Prices in December 2020')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2021=df.loc[(df['Date'] >= '2021-01-01') & (df['Date'] < '2021-01-31')]
print(Jan2021)

Jan2021_mean=Jan2021['Open'].mean()
print("Jan 2021 Mean Opening Price:", Jan2021_mean)
Jan2021.plot(x='Date', y='Open', title='AMD Opening Prices in January 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2021=df.loc[(df['Date'] >= '2021-02-01') & (df['Date'] < '2021-02-28')]
print(Feb2021)

Feb2021_mean=Feb2021['Open'].mean()
print("Feb 2021 Mean Opening Price:", Feb2021_mean)
Feb2021.plot(x='Date', y='Open', title='AMD Opening Prices in February 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2021=df.loc[(df['Date'] >= '2021-03-01') & (df['Date'] < '2021-03-31')]
print(Mar2021)

Mar2021_mean=Mar2021['Open'].mean()
print("Mar 2021 Mean Opening Price:", Mar2021_mean)
Mar2021.plot(x='Date', y='Open', title='AMD Opening Prices in March 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2021=df.loc[(df['Date'] >= '2021-04-01') & (df['Date'] < '2021-04-30')]
print(Apr2021)

Apr2021_mean=Apr2021['Open'].mean()
print("Apr 2021 Mean Opening Price:", Apr2021_mean)
Apr2021.plot(x='Date', y='Open', title='AMD Opening Prices in April 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2021=df.loc[(df['Date'] >= '2021-05-01') & (df['Date'] < '2021-05-31')]
print(May2021)

May2021_mean=May2021['Open'].mean()
print("May 2021 Mean Opening Price:", May2021_mean)
May2021.plot(x='Date', y='Open', title='AMD Opening Prices in May 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2021=df.loc[(df['Date'] >= '2021-06-01') & (df['Date'] < '2021-06-30')]
print(Jun2021)

Jun2021_mean=Jun2021['Open'].mean()
print("Jun 2021 Mean Opening Price:", Jun2021_mean)
Jun2021.plot(x='Date', y='Open', title='AMD Opening Prices in June 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2021=df.loc[(df['Date'] >= '2021-07-01') & (df['Date'] < '2021-07-31')]
print(Jul2021)

Jul2021_mean=Jul2021['Open'].mean()
print("Jul 2021 Mean Opening Price:", Jul2021_mean)
Jul2021.plot(x='Date', y='Open', title='AMD Opening Prices in July 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2021=df.loc[(df['Date'] >= '2021-08-01') & (df['Date'] < '2021-08-31')]
print(Aug2021)

Aug2021_mean=Aug2021['Open'].mean()
print("Aug 2021 Mean Opening Price:", Aug2021_mean)
Aug2021.plot(x='Date', y='Open', title='AMD Opening Prices in August 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2021=df.loc[(df['Date'] >= '2021-09-01') & (df['Date'] < '2021-09-30')]
print(Sep2021)

Sep2021_mean=Sep2021['Open'].mean()
print("Sep 2021 Mean Opening Price:", Sep2021_mean)
Sep2021.plot(x='Date', y='Open', title='AMD Opening Prices in September 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2021=df.loc[(df['Date'] >= '2021-10-01') & (df['Date'] < '2021-10-30')]
print(Oct2021)

Oct2021_mean=Oct2021['Open'].mean()
print("Sep 2021 Mean Opening Price:", Oct2021_mean)
Oct2021.plot(x='Date', y='Open', title='AMD Opening Prices in October 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2021=df.loc[(df['Date'] >= '2021-11-01') & (df['Date'] < '2021-11-30')]
print(Nov2021)

Nov2021_mean=Nov2021['Open'].mean()
print("Nov 2021 Mean Opening Price:", Nov2021_mean)
Nov2021.plot(x='Date', y='Open', title='AMD Opening Prices in November 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2021=df.loc[(df['Date'] >= '2021-12-01') & (df['Date'] < '2021-12-31')]
print(Dec2021)

Dec2021_mean=Dec2021['Open'].mean()
print("Dec 2021 Mean Opening Price:", Dec2021_mean)
Dec2021.plot(x='Date', y='Open', title='AMD Opening Prices in December 2021')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2022=df.loc[(df['Date'] >= '2022-01-01') & (df['Date'] < '2022-01-31')]
print(Jan2022)

Jan2022_mean=Jan2022['Open'].mean()
print("Jan 2022 Mean Opening Price:", Jan2022_mean)
Jan2022.plot(x='Date', y='Open', title='AMD Opening Prices in January 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2022=df.loc[(df['Date'] >= '2022-02-01') & (df['Date'] < '2022-02-28')]
print(Feb2022)

Feb2022_mean=Feb2022['Open'].mean()
print("Feb 2022 Mean Opening Price:", Feb2022_mean)
Feb2022.plot(x='Date', y='Open', title='AMD Opening Prices in February 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2022=df.loc[(df['Date'] >= '2022-03-01') & (df['Date'] < '2022-03-31')]
print(Mar2022)

Mar2022_mean=Mar2022['Open'].mean()
print("Mar 2022 Mean Opening Price:", Mar2022_mean)
Mar2022.plot(x='Date', y='Open', title='AMD Opening Prices in March 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2022=df.loc[(df['Date'] >= '2022-04-01') & (df['Date'] < '2022-04-30')]
print(Apr2022)

Apr2022_mean=Apr2022['Open'].mean()
print("Apr 2022 Mean Opening Price:", Apr2022_mean)
Apr2022.plot(x='Date', y='Open', title='AMD Opening Prices in April 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2022=df.loc[(df['Date'] >= '2022-05-01') & (df['Date'] < '2022-05-31')]
print(May2022)

May2022_mean=May2022['Open'].mean()
print("May 2022 Mean Opening Price:", May2022_mean)
May2022.plot(x='Date', y='Open', title='AMD Opening Prices in May 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2022=df.loc[(df['Date'] >= '2022-06-01') & (df['Date'] < '2022-06-30')]
print(Jun2022)

Jun2022_mean=Jun2022['Open'].mean()
print("Jun 2022 Mean Opening Price:", Jun2022_mean)
Jun2022.plot(x='Date', y='Open', title='AMD Opening Prices in June 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2022=df.loc[(df['Date'] >= '2022-07-01') & (df['Date'] < '2022-07-31')]
print(Jul2022)

Jul2022_mean=Jul2022['Open'].mean()
print("Jul 2022 Mean Opening Price:", Jul2022_mean)
Jul2022.plot(x='Date', y='Open', title='AMD Opening Prices in July 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2022=df.loc[(df['Date'] >= '2022-08-01') & (df['Date'] < '2022-08-31')]
print(Aug2022)

Aug2022_mean=Aug2022['Open'].mean()
print("Aug 2022 Mean Opening Price:", Aug2022_mean)
Aug2022.plot(x='Date', y='Open', title='AMD Opening Prices in August 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2022=df.loc[(df['Date'] >= '2022-09-01') & (df['Date'] < '2022-09-30')]
print(Sep2022)

Sep2022_mean=Sep2022['Open'].mean()
print("Sep 2022 Mean Opening Price:", Sep2022_mean)
Sep2022.plot(x='Date', y='Open', title='AMD Opening Prices in September 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2022=df.loc[(df['Date'] >= '2022-10-01') & (df['Date'] < '2022-10-31')]
print(Oct2022)

Oct2022_mean=Oct2022['Open'].mean()
print("Oct 2022 Mean Opening Price:", Oct2022_mean)
Oct2022.plot(x='Date', y='Open', title='AMD Opening Prices in October 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2022=df.loc[(df['Date'] >= '2022-11-01') & (df['Date'] < '2022-11-30')]
print(Nov2022)

Nov2022_mean=Nov2022['Open'].mean()
print("Nov 2022 Mean Opening Price:", Nov2022_mean)
Nov2022.plot(x='Date', y='Open', title='AMD Opening Prices in November 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2022=df.loc[(df['Date'] >= '2022-12-01') & (df['Date'] < '2022-12-31')]
print(Dec2022)

Dec2022_mean=Dec2022['Open'].mean()
print("Dec 2022 Mean Opening Price:", Dec2022_mean)
Dec2022.plot(x='Date', y='Open', title='AMD Opening Prices in December 2022')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2023=df.loc[(df['Date'] >= '2023-01-01') & (df['Date'] < '2023-01-31')]
print(Jan2023)

Jan2023_mean=Jan2023['Open'].mean()
print("Jan 2023 Mean Opening Price:", Jan2023_mean)
Jan2023.plot(x='Date', y='Open', title='AMD Opening Prices in January 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2023=df.loc[(df['Date'] >= '2023-02-01') & (df['Date'] < '2023-02-28')]
print(Feb2023)

Feb2023_mean=Feb2023['Open'].mean()
print("Feb 2023 Mean Opening Price:", Feb2023_mean)
Feb2023.plot(x='Date', y='Open', title='AMD Opening Prices in February 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2023=df.loc[(df['Date'] >= '2023-03-01') & (df['Date'] < '2023-03-31')]
print(Mar2023)

Mar2023_mean=Mar2023['Open'].mean()
print("Mar 2023 Mean Opening Price:", Mar2023_mean)
Mar2023.plot(x='Date', y='Open', title='AMD Opening Prices in March 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2023=df.loc[(df['Date'] >= '2023-04-01') & (df['Date'] < '2023-04-30')]
print(Apr2023)

Apr2023_mean=Apr2023['Open'].mean()
print("Apr 2023 Mean Opening Price:", Apr2023_mean)
Apr2023.plot(x='Date', y='Open', title='AMD Opening Prices in April 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2023=df.loc[(df['Date'] >= '2023-05-01') & (df['Date'] < '2023-05-31')]
print(May2023)

May2023_mean=May2023['Open'].mean()
print("May 2023 Mean Opening Price:", May2023_mean)
May2023.plot(x='Date', y='Open', title='AMD Opening Prices in May 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2023=df.loc[(df['Date'] >= '2023-06-01') & (df['Date'] < '2023-06-30')]
print(Jun2023)

Jun2023_mean=Jun2023['Open'].mean()
print("Jun 2023 Mean Opening Price:", Jun2023_mean)
Jun2023.plot(x='Date', y='Open', title='AMD Opening Prices in June 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2023=df.loc[(df['Date'] >= '2023-07-01') & (df['Date'] < '2023-07-31')]
print(Jul2023)

Jul2023_mean=Jul2023['Open'].mean()
print("Jul 2023 Mean Opening Price:", Jul2023_mean)
Jul2023.plot(x='Date', y='Open', title='AMD Opening Prices in July 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2023=df.loc[(df['Date'] >= '2023-08-01') & (df['Date'] < '2023-08-31')]
print(Aug2023)

Aug2023_mean=Aug2023['Open'].mean()
print("Aug 2023 Mean Opening Price:", Aug2023_mean)
Aug2023.plot(x='Date', y='Open', title='AMD Opening Prices in August 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2023=df.loc[(df['Date'] >= '2023-09-01') & (df['Date'] < '2023-09-30')]
print(Sep2023)

Sep2023_mean=Sep2023['Open'].mean()
print("Sep 2023 Mean Opening Price:", Sep2023_mean)
Sep2023.plot(x='Date', y='Open', title='AMD Opening Prices in September 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2023=df.loc[(df['Date'] >= '2023-10-01') & (df['Date'] < '2023-10-31')]
print(Oct2023)

Oct2023_mean=Oct2023['Open'].mean()
print("Oct 2023 Mean Opening Price:", Oct2023_mean)
Oct2023.plot(x='Date', y='Open', title='AMD Opening Prices in October 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2023=df.loc[(df['Date'] >= '2023-11-01') & (df['Date'] < '2023-11-30')]
print(Nov2023)

Nov2023_mean=Nov2023['Open'].mean()
print("Nov 2023 Mean Opening Price:", Nov2023_mean)
Nov2023.plot(x='Date', y='Open', title='AMD Opening Prices in November 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2023=df.loc[(df['Date'] >= '2023-12-01') & (df['Date'] < '2023-12-31')]
print(Dec2023)

Dec2023_mean=Dec2023['Open'].mean()
print("Dec 2023 Mean Opening Price:", Dec2023_mean)
Dec2023.plot(x='Date', y='Open', title='AMD Opening Prices in December 2023')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2024=df.loc[(df['Date'] >= '2024-01-01') & (df['Date'] < '2024-01-31')]
print(Jan2024)

Jan2024_mean=Jan2024['Open'].mean()
print("Jan 2024 Mean Opening Price:", Jan2024_mean)
Jan2024.plot(x='Date', y='Open', title='AMD Opening Prices in January 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2024=df.loc[(df['Date'] >= '2024-02-01') & (df['Date'] < '2024-02-29')]
print(Feb2024)

Feb2024_mean=Feb2024['Open'].mean()
print("Feb 2024 Mean Opening Price:", Feb2024_mean)
Feb2024.plot(x='Date', y='Open', title='AMD Opening Prices in February 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2024=df.loc[(df['Date'] >= '2024-03-01') & (df['Date'] < '2024-03-31')]
print(Mar2024)

Mar2024_mean=Mar2024['Open'].mean()
print("Mar 2024 Mean Opening Price:", Mar2024_mean)
Mar2024.plot(x='Date', y='Open', title='AMD Opening Prices in March 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2024=df.loc[(df['Date'] >= '2024-04-01') & (df['Date'] < '2024-04-30')]
print(Apr2024)

Apr2024_mean=Apr2024['Open'].mean()
print("Apr 2024 Mean Opening Price:", Apr2024_mean)
Apr2024.plot(x='Date', y='Open', title='AMD Opening Prices in April 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2024=df.loc[(df['Date'] >= '2024-05-01') & (df['Date'] < '2024-05-31')]
print(May2024)

May2024_mean=May2024['Open'].mean()
print("May 2024 Mean Opening Price:", May2024_mean)
May2024.plot(x='Date', y='Open', title='AMD Opening Prices in May 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2024=df.loc[(df['Date'] >= '2024-06-01') & (df['Date'] < '2024-06-30')]
print(Jun2024)

Jun2024_mean=Jun2024['Open'].mean()
print("Jun 2024 Mean Opening Price:", Jun2024_mean)
Jun2024.plot(x='Date', y='Open', title='AMD Opening Prices in June 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2024=df.loc[(df['Date'] >= '2024-07-01') & (df['Date'] < '2024-07-31')]
print(Jul2024)

Jul2024_mean=Jul2024['Open'].mean()
print("Jul 2024 Mean Opening Price:", Jul2024_mean)
Jul2024.plot(x='Date', y='Open', title='AMD Opening Prices in July 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2024=df.loc[(df['Date'] >= '2024-08-01') & (df['Date'] < '2024-08-31')]
print(Aug2024)

Aug2024_mean=Aug2024['Open'].mean()
print("Aug 2024 Mean Opening Price:", Aug2024_mean)
Aug2024.plot(x='Date', y='Open', title='AMD Opening Prices in August 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep2024=df.loc[(df['Date'] >= '2024-09-01') & (df['Date'] < '2024-09-30')]
print(Sep2024)

Sep2024_mean=Sep2024['Open'].mean()
print("Sep 2024 Mean Opening Price:", Sep2024_mean)
Sep2024.plot(x='Date', y='Open', title='AMD Opening Prices in September 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Oct2024=df.loc[(df['Date'] >= '2024-10-01') & (df['Date'] < '2024-10-31')]
print(Oct2024)

Oct2024_mean=Oct2024['Open'].mean()
print("Oct 2024 Mean Opening Price:", Oct2024_mean)
Oct2024.plot(x='Date', y='Open', title='AMD Opening Prices in October 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Nov2024=df.loc[(df['Date'] >= '2024-11-01') & (df['Date'] < '2024-11-30')]
print(Nov2024)

Nov2024_mean=Nov2024['Open'].mean()
print("Nov 2024 Mean Opening Price:", Nov2024_mean)
Nov2024.plot(x='Date', y='Open', title='AMD Opening Prices in November 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Dec2024=df.loc[(df['Date'] >= '2024-12-01') & (df['Date'] < '2024-12-31')]
print(Dec2024)

Dec2024_mean=Dec2024['Open'].mean()
print("Dec 2024 Mean Opening Price:", Dec2024_mean)
Dec2024.plot(x='Date', y='Open', title='AMD Opening Prices in December 2024')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jan2025=df.loc[(df['Date'] >= '2025-01-01') & (df['Date'] < '2025-01-31')]
print(Jan2025)

Jan2025_mean=Jan2025['Open'].mean()
print("Jan 2025 Mean Opening Price:", Jan2025_mean)
Jan2025.plot(x='Date', y='Open', title='AMD Opening Prices in January 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Feb2025=df.loc[(df['Date'] >= '2025-02-01') & (df['Date'] < '2025-02-28')]
print(Feb2025)

Feb2025_mean=Feb2025['Open'].mean()
print("Feb 2025 Mean Opening Price:", Feb2025_mean)
Feb2025.plot(x='Date', y='Open', title='AMD Opening Prices in February 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Mar2025=df.loc[(df['Date'] >= '2025-03-01') & (df['Date'] < '2025-03-31')]
print(Mar2025)

Mar2025_mean=Mar2025['Open'].mean()
print("Mar 2025 Mean Opening Price:", Mar2025_mean)
Mar2025.plot(x='Date', y='Open', title='AMD Opening Prices in March 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Apr2025=df.loc[(df['Date'] >= '2025-04-01') & (df['Date'] < '2025-04-30')]
print(Apr2025)

Apr2025_mean=Apr2025['Open'].mean()
print("Apr 2025 Mean Opening Price:", Apr2025_mean)
Apr2025.plot(x='Date', y='Open', title='AMD Opening Prices in April 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
May2025=df.loc[(df['Date'] >= '2025-05-01') & (df['Date'] < '2025-05-31')]
print(May2025)

May2025_mean=May2025['Open'].mean()
print("May 2025 Mean Opening Price:", May2025_mean)
May2025.plot(x='Date', y='Open', title='AMD Opening Prices in May 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jun2025=df.loc[(df['Date'] >= '2025-06-01') & (df['Date'] < '2025-06-30')]
print(Jun2025)

Jun2025_mean=Jun2025['Open'].mean()
print("Jun 2025 Mean Opening Price:", Jun2025_mean)
Jun2025.plot(x='Date', y='Open', title='AMD Opening Prices in June 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Jul2025=df.loc[(df['Date'] >= '2025-07-01') & (df['Date'] < '2025-07-31')]
print(Jul2025)

Jul2025_mean=Jul2025['Open'].mean()
print("Jul 2025 Mean Opening Price:", Jul2025_mean)
Jul2025.plot(x='Date', y='Open', title='AMD Opening Prices in July 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Aug2025=df.loc[(df['Date'] >= '2025-08-01') & (df['Date'] < '2025-08-31')]
print(Aug2025)

Aug2025_mean=Aug2025['Open'].mean()
print("Aug 2025 Mean Opening Price:", Aug2025_mean)
Aug2025.plot(x='Date', y='Open', title='AMD Opening Prices in August 2025')
plt.xlabel('Date')
plt.ylabel('Open Price')

plt.show()


#Closing Prices of AMD Stocks

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1992=df.loc[(df['Date'] >= '1992-02-01') & (df['Date'] < '1992-02-28')]
print(Feb1992)
Feb1992_mean=Feb1992['Close'].mean()
print("Feb 1992 Mean Closing Price:", Feb1992_mean)
Feb1992.plot(x='Date', y='Close', title='AMD Closing Prices in February 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1992=df.loc[(df['Date'] >= '1992-03-01') & (df['Date'] < '1992-03-31')]
print(Mar1992)
Mar1992_mean=Mar1992['Close'].mean()
print("Mar 1992 Mean Closing Price:", Mar1992_mean)
Mar1992.plot(x='Date', y='Close', title='AMD Closing Prices in March 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1992=df.loc[(df['Date'] >= '1992-04-01') & (df['Date'] < '1992-04-30')]
print(Apr1992)
Apr1992_mean=Apr1992['Close'].mean()
print("Apr 1992 Mean Closing Price:", Apr1992_mean)
Apr1992.plot(x='Date', y='Close', title='AMD Closing Prices in April 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1992=df.loc[(df['Date'] >= '1992-05-01') & (df['Date'] < '1992-05-31')]
print(May1992)
May1992_mean=May1992['Close'].mean()
print("May 1992 Mean Closing Price:", May1992_mean)
May1992.plot(x='Date', y='Close', title='AMD Closing Prices in May 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1992=df.loc[(df['Date'] >= '1992-06-01') & (df['Date'] < '1992-06-30')]
print(Jun1992)
Jun1992_mean=Jun1992['Close'].mean()
print("May 1992 Mean Closing Price:", Jun1992_mean)
Jun1992.plot(x='Date', y='Close', title='AMD Closing Prices in June 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1992=df.loc[(df['Date'] >= '1992-07-01') & (df['Date'] < '1992-07-31')]
print(Jul1992)
Jul1992_mean=Jul1992['Close'].mean()
print("July 1992 Mean Closing Price:", Jul1992_mean)
Jul1992.plot(x='Date', y='Close', title='AMD Closing Prices in July 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1992=df.loc[(df['Date'] >= '1992-08-01') & (df['Date'] < '1992-08-31')]
print(Aug1992)
Aug1992_mean=Aug1992['Close'].mean()
print("August 1992 Mean Closing Price:", Aug1992_mean)
Aug1992.plot(x='Date', y='Close', title='AMD Closing Prices in August 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1992=df.loc[(df['Date'] >= '1992-09-01') & (df['Date'] < '1992-09-30')]
print(Sep1992)
Sep1992_mean=Sep1992['Close'].mean()
print("Sep 1992 Mean Closing Price:", Sep1992_mean)
Sep1992.plot(x='Date', y='Close', title='AMD Closing Prices in September 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1992=df.loc[(df['Date'] >= '1992-10-01') & (df['Date'] < '1992-10-31')]
print(Oct1992)
Oct1992_mean=Oct1992['Close'].mean()
print("Oct 1992 Mean Closing Price:", Oct1992_mean)
Oct1992.plot(x='Date', y='Close', title='AMD Closing Prices in October 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1992=df.loc[(df['Date'] >= '1992-11-01') & (df['Date'] < '1992-11-30')]
print(Nov1992)
Nov1992_mean=Nov1992['Close'].mean()
print("Nov 1992 Mean Closing Price:", Nov1992_mean)
Nov1992.plot(x='Date', y='Close', title='AMD Closing Prices in November 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1992=df.loc[(df['Date'] >= '1992-12-01') & (df['Date'] < '1992-12-31')]
print(Dec1992)
Dec1992_mean=Dec1992['Close'].mean()
print("Dec 1992 Mean Closing Price:", Dec1992_mean)
Dec1992.plot(x='Date', y='Close', title='AMD Closing Prices in December 1992')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1993=df.loc[(df['Date'] >= '1993-01-01') & (df['Date'] < '1993-01-31')]
print(Jan1993)
Jan1993_mean=Jan1993['Close'].mean()
print("Jan 1993 Mean Closing Price:", Jan1993_mean)
Jun1993.plot(x='Date', y='Close', title='AMD Closing Prices in January 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1993=df.loc[(df['Date'] >= '1993-02-01') & (df['Date'] < '1993-02-28')]
print(Feb1993)
Feb1993_mean=Feb1993['Close'].mean()
print("Feb 1993 Mean Closing Price:", Feb1993_mean)
Feb1993.plot(x='Date', y='Close', title='AMD Closing Prices in February 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1993=df.loc[(df['Date'] >= '1993-03-01') & (df['Date'] < '1993-03-31')]
print(Mar1993)
Mar1993_mean=Mar1993['Close'].mean()
print("Mar 1993 Mean Closing Price:", Mar1993_mean)
Mar1993.plot(x='Date', y='Close', title='AMD Closing Prices in March 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1993=df.loc[(df['Date'] >= '1993-04-01') & (df['Date'] < '1993-04-30')]
print(Apr1993)
Apr1993_mean=Apr1993['Close'].mean()
print("Apr 1993 Mean Closing Price:", Apr1993_mean)
Apr1993.plot(x='Date', y='Close', title='AMD Closing Prices in April 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1993=df.loc[(df['Date'] >= '1993-05-01') & (df['Date'] < '1993-05-31')]
print(May1993)
May1993_mean=May1993['Close'].mean()
print("May 1993 Mean Closing Price:", May1993_mean)
May1993.plot(x='Date', y='Close', title='AMD Closing Prices in May 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1993=df.loc[(df['Date'] >= '1993-06-01') & (df['Date'] < '1993-06-30')]
print(Jun1993)
Jun1993_mean=Jun1993['Close'].mean()
print("Jun 1993 Mean Closing Price:", Jun1993_mean)
Jun1993.plot(x='Date', y='Close', title='AMD Closing Prices in June 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1993=df.loc[(df['Date'] >= '1993-07-01') & (df['Date'] < '1993-07-31')]
print(Jul1993)
Jul1993_mean=Jul1993['Close'].mean()
print("Jul 1993 Mean Closing Price:", Jul1993_mean)
Jul1993.plot(x='Date', y='Close', title='AMD Closing Prices in July 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1993=df.loc[(df['Date'] >= '1993-08-01') & (df['Date'] < '1993-08-31')]
print(Aug1993)
Aug1993_mean=Aug1993['Close'].mean()
print("Aug 1993 Mean Closing Price:", Aug1993_mean)
Aug1993.plot(x='Date', y='Close', title='AMD Closing Prices in August 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])
Sep1993=df.loc[(df['Date'] >= '1993-09-01') & (df['Date'] < '1993-09-30')]
print(Sep1993)
Sep1993_mean=Sep1993['Close'].mean()
print("Sep 1993 Mean Closing Price:", Sep1993_mean)
Sep1993.plot(x='Date', y='Close', title='AMD Closing Prices in September 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1993=df.loc[(df['Date'] >= '1993-10-01') & (df['Date'] < '1993-10-31')]
print(Oct1993)
Oct1993_mean=Oct1993['Close'].mean()
print("Oct 1993 Mean Closing Price:", Oct1993_mean)
Oct1993.plot(x='Date', y='Close', title='AMD Closing Prices in October 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1993=df.loc[(df['Date'] >= '1993-11-01') & (df['Date'] < '1993-11-31')]
print(Nov1993)
Nov1993_mean=Nov1993['Close'].mean()
print("Nov 1993 Mean Closing Price:", Nov1993_mean)
Nov1993.plot(x='Date', y='Close', title='AMD Closing Prices in November 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1993=df.loc[(df['Date'] >= '1993-12-01') & (df['Date'] < '1993-12-31')]
print(Dec1993)
Dec1993_mean=Dec1993['Close'].mean()
print("Dec 1993 Mean Closing Price:", Dec1993_mean)
Dec1993.plot(x='Date', y='Close', title='AMD Closing Prices in December 1993')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1994=df.loc[(df['Date'] >= '1994-01-01') & (df['Date'] < '1994-01-31')]
print(Jan1994)
Jan1994_mean=Jan1994['Close'].mean()
print("Jan 1994 Mean Closing Price:", Jan1994_mean)
Jan1994.plot(x='Date', y='Close', title='AMD Closing Prices in January 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1994=df.loc[(df['Date'] >= '1994-02-01') & (df['Date'] < '1994-02-28')]
print(Feb1994)
Feb1994_mean=Feb1994['Close'].mean()
print("Feb 1994 Mean Closing Price:", Feb1994_mean)
Feb1994.plot(x='Date', y='Close', title='AMD Closing Prices in February 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1994=df.loc[(df['Date'] >= '1994-03-01') & (df['Date'] < '1994-03-31')]
print(Mar1994)
Mar1994_mean=Mar1994['Close'].mean()
print("Mar 1994 Mean Closing Price:", Mar1994_mean)
Mar1994.plot(x='Date', y='Close', title='AMD Closing Prices in March 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1994=df.loc[(df['Date'] >= '1994-04-01') & (df['Date'] < '1994-04-30')]
print(Apr1994)
Apr1994_mean=Apr1994['Close'].mean()
print("Apr 1994 Mean Closing Price:", Apr1994_mean)
Apr1994.plot(x='Date', y='Close', title='AMD Closing Prices in April 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1994=df.loc[(df['Date'] >= '1994-05-01') & (df['Date'] < '1994-05-31')]
print(May1994)
May1994_mean=May1994['Close'].mean()
print("May 1994 Mean Closing Price:", May1994_mean)
May1994.plot(x='Date', y='Close', title='AMD Closing Prices in May 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1994=df.loc[(df['Date'] >= '1994-06-01') & (df['Date'] < '1994-06-30')]
print(Jun1994)
Jun1994_mean=Jun1994['Close'].mean()
print("Jun 1994 Mean Closing Price:", Jun1994_mean)
Jun1994.plot(x='Date', y='Close', title='AMD Closing Prices in June 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1994=df.loc[(df['Date'] >= '1994-07-01') & (df['Date'] < '1994-07-31')]
print(Jul1994)
Jul1994_mean=Jul1994['Close'].mean()
print("Jul 1994 Mean Closing Price:", Jul1994_mean)
Jul1994.plot(x='Date', y='Close', title='AMD Closing Prices in July 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1994=df.loc[(df['Date'] >= '1994-08-01') & (df['Date'] < '1994-08-31')]
print(Aug1994)
Aug1994_mean=Aug1994['Close'].mean()
print("Aug 1994 Mean Closing Price:", Aug1994_mean)
Aug1994.plot(x='Date', y='Close', title='AMD Closing Prices in August 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1994=df.loc[(df['Date'] >= '1994-09-01') & (df['Date'] < '1994-09-30')]
print(Sep1994)
Sep1994_mean=Sep1994['Close'].mean()
print("Sep 1994 Mean Closing Price:", Sep1994_mean)
Sep1994.plot(x='Date', y='Close', title='AMD Closing Prices in September 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1994=df.loc[(df['Date'] >= '1994-10-01') & (df['Date'] < '1994-10-31')]
print(Oct1994)
Oct1994_mean=Oct1994['Close'].mean()
print("Oct 1994 Mean Closing Price:", Oct1994_mean)
Oct1994.plot(x='Date', y='Close', title='AMD Closing Prices in October 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1994=df.loc[(df['Date'] >= '1994-11-01') & (df['Date'] < '1994-11-30')]
print(Nov1994)
Nov1994_mean=Nov1994['Close'].mean()
print("Nov 1994 Mean Closing Price:", Nov1994_mean)
Nov1994.plot(x='Date', y='Close', title='AMD Closing Prices in November 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df['Date'] = pd.to_datetime(df['Date'])

Dec1994=df.loc[(df['Date'] >= '1994-12-01') & (df['Date'] < '1994-12-31')]
print(Dec1994)
Dec1994_mean=Dec1994['Close'].mean()
print("Dec 1994 Mean Closing Price:", Dec1994_mean)
Dec1994.plot(x='Date', y='Close', title='AMD Closing Prices in December 1994')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1995=df.loc[(df['Date'] >= '1995-01-01') & (df['Date'] < '1995-01-31')]
print(Jan1995)
Jan1995_mean=Jan1995['Close'].mean()
print("Jan 1995 Mean Closing Price:", Jan1995_mean)
Jan1995.plot(x='Date', y='Close', title='AMD Closing Prices in January 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1995=df.loc[(df['Date'] >= '1995-02-01') & (df['Date'] < '1995-02-28')]
print(Feb1995)
Feb1995_mean=Feb1995['Close'].mean()
print("Feb 1995 Mean Closing Price:", Feb1995_mean)
Feb1995.plot(x='Date', y='Close', title='AMD Closing Prices in February 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1995=df.loc[(df['Date'] >= '1995-03-01') & (df['Date'] < '1995-03-31')]
print(Mar1995)
Mar1995_mean=Mar1995['Close'].mean()
print("Mar 1995 Mean Closing Price:", Mar1995_mean)
Mar1995.plot(x='Date', y='Close', title='AMD Closing Prices in March 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1995=df.loc[(df['Date'] >= '1995-04-01') & (df['Date'] < '1995-04-30')]
print(Apr1995)
Apr1995_mean=Apr1995['Close'].mean()
print("Apr 1995 Mean Closing Price:", Apr1995_mean)
Apr1995.plot(x='Date', y='Close', title='AMD Closing Prices in April 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1995=df.loc[(df['Date'] >= '1995-05-01') & (df['Date'] < '1995-05-31')]
print(May1995)
May1995_mean=May1995['Close'].mean()
print("May 1995 Mean Closing Price:", May1995_mean)
May1995.plot(x='Date', y='Close', title='AMD Closing Prices in May 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1995=df.loc[(df['Date'] >= '1995-06-01') & (df['Date'] < '1995-06-30')]
print(Jun1995)
Jun1995_mean=Jun1995['Close'].mean()
print("Jun 1995 Mean Closing Price:", Jun1995_mean)
Jun1995.plot(x='Date', y='Close', title='AMD Closing Prices in June 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1995=df.loc[(df['Date'] >= '1995-07-01') & (df['Date'] < '1995-07-31')]
print(Jul1995)
Jul1995_mean=Jul1995['Close'].mean()
print("Jul 1995 Mean Closing Price:", Jul1995_mean)
Jul1995.plot(x='Date', y='Close', title='AMD Closing Prices in July 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1995=df.loc[(df['Date'] >= '1995-08-01') & (df['Date'] < '1995-08-31')]
print(Aug1995)
Aug1995_mean=Aug1995['Close'].mean()
print("Aug 1995 Mean Closing Price:", Aug1995_mean)
Aug1995.plot(x='Date', y='Close', title='AMD Closing Prices in August 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1995=df.loc[(df['Date'] >= '1995-09-01') & (df['Date'] < '1995-09-30')]
print(Sep1995)
Sep1995_mean=Sep1995['Close'].mean()
print("Sep 1995 Mean Closing Price:", Sep1995_mean)
Sep1995.plot(x='Date', y='Close', title='AMD Closing Prices in September 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1995=df.loc[(df['Date'] >= '1995-10-01') & (df['Date'] < '1995-10-31')]
print(Oct1995)
Oct1995_mean=Oct1995['Close'].mean()
print("Oct 1995 Mean Closing Price:", Oct1995_mean)
Oct1995.plot(x='Date', y='Close', title='AMD Closing Prices in October 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1995=df.loc[(df['Date'] >= '1995-11-01') & (df['Date'] < '1995-11-30')]
print(Nov1995)
Nov1995_mean=Nov1995['Close'].mean()
print("Nov 1995 Mean Closing Price:", Nov1995_mean)
Nov1995.plot(x='Date', y='Close', title='AMD Closing Prices in November 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1995=df.loc[(df['Date'] >= '1995-12-01') & (df['Date'] < '1995-12-31')]
print(Dec1995)
Dec1995_mean=Dec1995['Close'].mean()
print("Dec 1995 Mean Closing Price:", Dec1995_mean)
Dec1995.plot(x='Date', y='Close', title='AMD Closing Prices in December 1995')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1996=df.loc[(df['Date'] >= '1996-01-01') & (df['Date'] < '1996-01-31')]
print(Jan1996)
Jan1996_mean=Jan1996['Close'].mean()
print("Jan 1996 Mean Closing Price:", Jan1996_mean)
Jan1996.plot(x='Date', y='Close', title='AMD Closing Prices in January 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1996=df.loc[(df['Date'] >= '1996-02-01') & (df['Date'] < '1996-02-29')]
print(Feb1996)
Feb1996_mean=Feb1996['Close'].mean()
print("Feb 1996 Mean Closing Price:", Feb1996_mean)
Feb1996.plot(x='Date', y='Close', title='AMD Closing Prices in February 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1996=df.loc[(df['Date'] >= '1996-03-01') & (df['Date'] < '1996-03-31')]
print(Mar1996)
Mar1996_mean=Mar1996['Close'].mean()
print("Mar 1996 Mean Closing Price:", Mar1996_mean)
Mar1996.plot(x='Date', y='Close', title='AMD Closing Prices in March 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1996=df.loc[(df['Date'] >= '1996-04-01') & (df['Date'] < '1996-04-30')]
print(Apr1996)
Apr1996_mean=Apr1996['Close'].mean()
print("Apr 1996 Mean Closing Price:", Apr1996_mean)
Apr1996.plot(x='Date', y='Close', title='AMD Closing Prices in April 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1996=df.loc[(df['Date'] >= '1996-05-01') & (df['Date'] < '1996-05-31')]
print(May1996)
May1996_mean=May1996['Close'].mean()
print("May 1996 Mean Closing Price:", May1996_mean)
May1996.plot(x='Date', y='Close', title='AMD Closing Prices in May 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1996=df.loc[(df['Date'] >= '1996-06-01') & (df['Date'] < '1996-06-30')]
print(Jun1996)
Jun1996_mean=Jun1996['Close'].mean()
print("Jun 1996 Mean Closing Price:", Jun1996_mean)
Jun1996.plot(x='Date', y='Close', title='AMD Closing Prices in June 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1996=df.loc[(df['Date'] >= '1996-07-01') & (df['Date'] < '1996-07-31')]
print(Jul1996)
Jul1996_mean=Jul1996['Close'].mean()
print("Jul 1996 Mean Closing Price:", Jul1996_mean)
Jul1996.plot(x='Date', y='Close', title='AMD Closing Prices in July 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1996=df.loc[(df['Date'] >= '1996-08-01') & (df['Date'] < '1996-08-31')]
print(Aug1996)
Aug1996_mean=Aug1996['Close'].mean()
print("Aug 1996 Mean Closing Price:", Aug1996_mean)
Aug1996.plot(x='Date', y='Close', title='AMD Closing Prices in August 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1996=df.loc[(df['Date'] >= '1996-09-01') & (df['Date'] < '1996-09-30')]
print(Sep1996)
Sep1996_mean=Sep1996['Close'].mean()
print("Sep 1996 Mean Closing Price:", Sep1996_mean)
Sep1996.plot(x='Date', y='Close', title='AMD Closing Prices in September 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1996=df.loc[(df['Date'] >= '1996-10-01') & (df['Date'] < '1996-10-31')]
print(Oct1996)
Oct1996_mean=Oct1996['Close'].mean()
print("Oct 1996 Mean Closing Price:", Oct1996_mean)
Oct1996.plot(x='Date', y='Close', title='AMD Closing Prices in October 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1996=df.loc[(df['Date'] >= '1996-11-01') & (df['Date'] < '1996-11-30')]
print(Nov1996)
Nov1996_mean=Nov1996['Close'].mean()
print("Nov 1996 Mean Closing Price:", Nov1996_mean)
Nov1996.plot(x='Date', y='Close', title='AMD Closing Prices in November 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1996=df.loc[(df['Date'] >= '1996-12-01') & (df['Date'] < '1996-12-31')]
print(Dec1996)
Dec1996_mean=Dec1996['Close'].mean()
print("Dec 1996 Mean Closing Price:", Dec1996_mean)
Dec1996.plot(x='Date', y='Close', title='AMD Closing Prices in December 1996')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1997=df.loc[(df['Date'] >= '1997-01-01') & (df['Date'] < '1997-01-31')]
print(Jan1997)
Jan1997_mean=Jan1997['Close'].mean()
print("Jan 1997 Mean Closing Price:", Jan1997_mean)
Jan1997.plot(x='Date', y='Close', title='AMD Closing Prices in January 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1997=df.loc[(df['Date'] >= '1997-02-01') & (df['Date'] < '1997-02-28')]
print(Feb1997)
Feb1997_mean=Feb1997['Close'].mean()
print("Feb 1997 Mean Closing Price:", Feb1997_mean)
Feb1997.plot(x='Date', y='Close', title='AMD Closing Prices in February 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1997=df.loc[(df['Date'] >= '1997-03-01') & (df['Date'] < '1997-03-31')]
print(Mar1997)
Mar1997_mean=Mar1997['Close'].mean()
print("Mar 1997 Mean Closing Price:", Mar1997_mean)
Mar1997.plot(x='Date', y='Close', title='AMD Closing Prices in March 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1997=df.loc[(df['Date'] >= '1997-04-01') & (df['Date'] < '1997-04-30')]
print(Apr1997)
Apr1997_mean=Apr1997['Close'].mean()
print("Apr 1997 Mean Closing Price:", Apr1997_mean)
Apr1997.plot(x='Date', y='Close', title='AMD Closing Prices in April 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1997=df.loc[(df['Date'] >= '1997-05-01') & (df['Date'] < '1997-05-31')]
print(May1997)
May1997_mean=May1997['Close'].mean()
print("May 1997 Mean Closing Price:", May1997_mean)
May1997.plot(x='Date', y='Close', title='AMD Closing Prices in May 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1997=df.loc[(df['Date'] >= '1997-06-01') & (df['Date'] < '1997-06-30')]
print(Jun1997)
Jun1997_mean=Jun1997['Close'].mean()
print("Jun 1997 Mean Closing Price:", Jun1997_mean)
Jun1997.plot(x='Date', y='Close', title='AMD Closing Prices in June 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1997=df.loc[(df['Date'] >= '1997-07-01') & (df['Date'] < '1997-07-31')]
print(Jul1997)
Jul1997_mean=Jul1997['Close'].mean()
print("Jul 1997 Mean Closing Price:", Jul1997_mean)
Jul1997.plot(x='Date', y='Close', title='AMD Closing Prices in July 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1997=df.loc[(df['Date'] >= '1997-08-01') & (df['Date'] < '1997-08-31')]
print(Aug1997)
Aug1997_mean=Aug1997['Close'].mean()
print("Aug 1997 Mean Closing Price:", Aug1997_mean)
Aug1997.plot(x='Date', y='Close', title='AMD Closing Prices in August 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1997=df.loc[(df['Date'] >= '1997-09-01') & (df['Date'] < '1997-09-30')]
print(Sep1997)
Sep1997_mean=Sep1997['Close'].mean()
print("Sep 1997 Mean Closing Price:", Sep1997_mean)
Sep1997.plot(x='Date', y='Close', title='AMD Closing Prices in September 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1997=df.loc[(df['Date'] >= '1997-11-01') & (df['Date'] < '1997-11-30')]
print(Oct1997)
Oct1997_mean=Oct1997['Close'].mean()
print("Oct 1997 Mean Closing Price:", Oct1997_mean)
Oct1997.plot(x='Date', y='Close', title='AMD Closing Prices in October 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1997=df.loc[(df['Date'] >= '1997-11-01') & (df['Date'] < '1997-11-30')]
print(Nov1997)
Nov1997_mean=Nov1997['Close'].mean()
print("Nov 1997 Mean Closing Price:", Nov1997_mean)
Nov1997.plot(x='Date', y='Close', title='AMD Closing Prices in November 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1997=df.loc[(df['Date'] >= '1997-12-01') & (df['Date'] < '1997-12-31')]
print(Dec1997)
Dec1997_mean=Dec1997['Close'].mean()
print("Dec 1997 Mean Closing Price:", Dec1997_mean)
Dec1997.plot(x='Date', y='Close', title='AMD Closing Prices in December 1997')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1998=df.loc[(df['Date'] >= '1998-01-01') & (df['Date'] < '1998-01-31')]
print(Jan1998)
Jan1998_mean=Jan1998['Close'].mean()
print("Jan 1998 Mean Closing Price:", Jan1998_mean)
Jan1998.plot(x='Date', y='Close', title='AMD Closing Prices in Janauary 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1998=df.loc[(df['Date'] >= '1998-02-01') & (df['Date'] < '1998-02-28')]
print(Feb1998)
Feb1998_mean=Feb1998['Close'].mean()
print("Feb 1998 Mean Closing Price:", Feb1998_mean)
Feb1998.plot(x='Date', y='Close', title='AMD Closing Prices in February 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1998=df.loc[(df['Date'] >= '1998-03-01') & (df['Date'] < '1998-03-31')]
print(Mar1998)
Mar1998_mean=Mar1998['Close'].mean()
print("Mar 1998 Mean Closing Price:", Mar1998_mean)
Mar1998.plot(x='Date', y='Close', title='AMD Closing Prices in March 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1998=df.loc[(df['Date'] >= '1998-04-01') & (df['Date'] < '1998-04-30')]
print(Apr1998)
Apr1998_mean=Apr1998['Close'].mean()
print("Apr 1998 Mean Closing Price:", Apr1998_mean)
Apr1998.plot(x='Date', y='Close', title='AMD Closing Prices in April 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1998=df.loc[(df['Date'] >= '1998-05-01') & (df['Date'] < '1998-05-31')]
print(May1998)
May1998_mean=May1998['Close'].mean()
print("May 1998 Mean Closing Price:", May1998_mean)
May1998.plot(x='Date', y='Close', title='AMD Closing Prices in May 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1998=df.loc[(df['Date'] >= '1998-06-01') & (df['Date'] < '1998-06-30')]
print(Jun1998)
Jun1998_mean=Jun1998['Close'].mean()
print("Jun 1998 Mean Closing Price:", Jun1998_mean)
Jun1998.plot(x='Date', y='Close', title='AMD Closing Prices in June 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1998=df.loc[(df['Date'] >= '1998-07-01') & (df['Date'] < '1998-07-31')]
print(Jul1998)
Jul1998_mean=Jul1998['Close'].mean()
print("Jul 1998 Mean Closing Price:", Jul1998_mean)
Jul1998.plot(x='Date', y='Close', title='AMD Closing Prices in July 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1998=df.loc[(df['Date'] >= '1998-08-01') & (df['Date'] < '1998-08-31')]
print(Aug1998)
Aug1998_mean=Aug1998['Close'].mean()
print("Aug 1998 Mean Closing Price:", Aug1998_mean)
Aug1998.plot(x='Date', y='Close', title='AMD Closing Prices in August 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1998=df.loc[(df['Date'] >= '1998-09-01') & (df['Date'] < '1998-09-30')]
print(Sep1998)
Sep1998_mean=Sep1998['Close'].mean()
print("Sep 1998 Mean Closing Price:", Sep1998_mean)
Sep1998.plot(x='Date', y='Close', title='AMD Closing Prices in September 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1998=df.loc[(df['Date'] >= '1998-10-01') & (df['Date'] < '1998-10-31')]
print(Oct1998)
Oct1998_mean=Oct1998['Close'].mean()
print("Oct 1998 Mean Closing Price:", Oct1998_mean)
Oct1998.plot(x='Date', y='Close', title='AMD Closing Prices in October 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1998=df.loc[(df['Date'] >= '1998-11-01') & (df['Date'] < '1998-11-30')]
print(Nov1998)
Nov1998_mean=Nov1998['Close'].mean()
print("Nov 1998 Mean Closing Price:", Nov1998_mean)
Nov1998.plot(x='Date', y='Close', title='AMD Closing Prices in November 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1998=df.loc[(df['Date'] >= '1998-12-01') & (df['Date'] < '1998-12-31')]
print(Dec1998)
Dec1998_mean=Dec1998['Close'].mean()
print("Dec 1998 Mean Closing Price:", Dec1998_mean)
Dec1998.plot(x='Date', y='Close', title='AMD Closing Prices in December 1998')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1999=df.loc[(df['Date'] >= '1999-01-01') & (df['Date'] < '1999-01-31')]
print(Jan1999)
Jan1999_mean=Jan1999['Close'].mean()
print("Jan 1999 Mean Closing Price:", Jan1999_mean)
Jan1999.plot(x='Date', y='Close', title='AMD Closing Prices in January 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1999=df.loc[(df['Date'] >= '1999-02-01') & (df['Date'] < '1999-02-28')]
print(Feb1999)
Feb1999_mean=Feb1999['Close'].mean()
print("Feb 1999 Mean Closing Price:", Feb1999_mean)
Feb1999.plot(x='Date', y='Close', title='AMD Closing Prices in February 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1999=df.loc[(df['Date'] >= '1999-03-01') & (df['Date'] < '1999-03-31')]
print(Mar1999)
Mar1999_mean=Mar1999['Close'].mean()
print("Mar 1999 Mean Closing Price:", Mar1999_mean)
Mar1999.plot(x='Date', y='Close', title='AMD Closing Prices in March 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1999=df.loc[(df['Date'] >= '1999-04-01') & (df['Date'] < '1999-04-30')]
print(Apr1999)
Apr1999_mean=Apr1999['Close'].mean()
print("Apr 1999 Mean Closing Price:", Apr1999_mean)
Apr1999.plot(x='Date', y='Close', title='AMD Closing Prices in April 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1999=df.loc[(df['Date'] >= '1999-05-01') & (df['Date'] < '1999-05-31')]
print(May1999)
May1999_mean=May1999['Close'].mean()
print("May 1999 Mean Closing Price:", May1999_mean)
May1999.plot(x='Date', y='Close', title='AMD Closing Prices in May 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1999=df.loc[(df['Date'] >= '1999-06-01') & (df['Date'] < '1999-06-30')]
print(Jun1999)
Jun1999_mean=Jun1999['Close'].mean()
print("Jun 1999 Mean Closing Price:", Jun1999_mean)
Jun1999.plot(x='Date', y='Close', title='AMD Closing Prices in June 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1999=df.loc[(df['Date'] >= '1999-07-01') & (df['Date'] < '1999-07-31')]
print(Jul1999)
Jul1999_mean=Jul1999['Close'].mean()
print("Jul 1999 Mean Closing Price:", Jul1999_mean)
Jul1999.plot(x='Date', y='Close', title='AMD Closing Prices in July 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1999=df.loc[(df['Date'] >= '1999-08-01') & (df['Date'] < '1999-08-31')]
print(Aug1999)
Aug1999_mean=Aug1999['Close'].mean()
print("Aug 1999 Mean Closing Price:", Aug1999_mean)
Aug1999.plot(x='Date', y='Close', title='AMD Closing Prices in August 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1999=df.loc[(df['Date'] >= '1999-09-01') & (df['Date'] < '1999-09-30')]
print(Sep1999)
Sep1999_mean=Sep1999['Close'].mean()
print("Sep 1999 Mean Closing Price:", Jul1999_mean)
Sep1999.plot(x='Date', y='Close', title='AMD Closing Prices in September 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1999=df.loc[(df['Date'] >= '1999-10-01') & (df['Date'] < '1999-10-31')]
print(Oct1999)
Oct1999_mean=Oct1999['Close'].mean()
print("Oct 1999 Mean Closing Price:", Oct1999_mean)
Oct1999.plot(x='Date', y='Close', title='AMD Closing Prices in October 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1999=df.loc[(df['Date'] >= '1999-11-01') & (df['Date'] < '1999-11-30')]
print(Nov1999)
Nov1999_mean=Nov1999['Close'].mean()
print("Nov 1999 Mean Closing Price:", Nov1999_mean)
Nov1999.plot(x='Date', y='Close', title='AMD Closing Prices in November 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1999=df.loc[(df['Date'] >= '1999-12-01') & (df['Date'] < '1999-12-31')]
print(Dec1999)
Dec1999_mean=Dec1999['Close'].mean()
print("Dec 1999 Mean Closing Price:", Dec1999_mean)
Dec1999.plot(x='Date', y='Close', title='AMD Closing Prices in December 1999')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2000=df.loc[(df['Date'] >= '2000-01-01') & (df['Date'] < '2000-01-31')]
print(Jan2000)
Jan2000_mean=Jan2000['Close'].mean()
print("Jan 2000 Mean Closing Price:", Jan2000_mean)
Jan2000.plot(x='Date', y='Close', title='AMD Closing Prices in January 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2000=df.loc[(df['Date'] >= '2000-02-01') & (df['Date'] < '2000-02-29')]
print(Feb2000)
Feb2000_mean=Feb2000['Close'].mean()
print("Feb 2000 Mean Closing Price:", Feb2000_mean)
Feb2000.plot(x='Date', y='Close', title='AMD Closing Prices in February 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2000=df.loc[(df['Date'] >= '2000-03-01') & (df['Date'] < '2000-03-31')]
print(Mar2000)
Mar2000_mean=Mar2000['Close'].mean()
print("Mar 2000 Mean Closing Price:", Mar2000_mean)
Mar2000.plot(x='Date', y='Close', title='AMD Closing Prices in March 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2000=df.loc[(df['Date'] >= '2000-04-01') & (df['Date'] < '2000-04-30')]
print(Apr2000)
Apr2000_mean=Apr2000['Close'].mean()
print("Apr 2000 Mean Closing Price:", Apr2000_mean)
Apr2000.plot(x='Date', y='Close', title='AMD Closing Prices in April 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2000=df.loc[(df['Date'] >= '2000-05-01') & (df['Date'] < '2000-05-31')]
print(May2000)
May2000_mean=May2000['Close'].mean()
print("May 2000 Mean Closing Price:", May2000_mean)
May2000.plot(x='Date', y='Close', title='AMD Closing Prices in May 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2000=df.loc[(df['Date'] >= '2000-06-01') & (df['Date'] < '2000-06-30')]
print(Jun2000)
Jun2000_mean=Jun2000['Close'].mean()
print("Jun 2000 Mean Closing Price:", Jun2000_mean)
Jun2000.plot(x='Date', y='Close', title='AMD Closing Prices in June 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2000=df.loc[(df['Date'] >= '2000-07-01') & (df['Date'] < '2000-07-31')]
print(Mar2000)
Jul2000_mean=Jul2000['Close'].mean()
print("Jul 2000 Mean Closing Price:", Jul2000_mean)
Jul2000.plot(x='Date', y='Close', title='AMD Closing Prices in July 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2000=df.loc[(df['Date'] >= '2000-08-01') & (df['Date'] < '2000-08-31')]
print(Aug2000)
Aug2000_mean=Aug2000['Close'].mean()
print("Aug 2000 Mean Closing Price:", Aug2000_mean)
Aug2000.plot(x='Date', y='Close', title='AMD Closing Prices in August 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2000=df.loc[(df['Date'] >= '2000-09-01') & (df['Date'] < '2000-09-30')]
print(Sep2000)
Sep2000_mean=Sep2000['Close'].mean()
print("Sep 2000 Mean Closing Price:", Sep2000_mean)
Sep2000.plot(x='Date', y='Close', title='AMD Closing Prices in September 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2000=df.loc[(df['Date'] >= '2000-10-01') & (df['Date'] < '2000-10-31')]
print(Oct2000)
Oct2000_mean=Oct2000['Close'].mean()
print("Oct 2000 Mean Closing Price:", Oct2000_mean)
Oct2000.plot(x='Date', y='Close', title='AMD Closing Prices in October 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2000=df.loc[(df['Date'] >= '2000-11-01') & (df['Date'] < '2000-11-30')]
print(Nov2000)
Nov2000_mean=Nov2000['Close'].mean()
print("Nov 2000 Mean Closing Price:", Nov2000_mean)
Nov2000.plot(x='Date', y='Close', title='AMD Closing Prices in November 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2000=df.loc[(df['Date'] >= '2000-12-01') & (df['Date'] < '2000-12-31')]
print(Dec2000)
Dec2000_mean=Dec2000['Close'].mean()
print("Dec 2000 Mean Closing Price:", Dec2000_mean)
Dec2000.plot(x='Date', y='Close', title='AMD Closing Prices in December 2000')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2001=df.loc[(df['Date'] >= '2001-01-01') & (df['Date'] < '2001-01-31')]
print(Jan2001)
Jan2001_mean=Jan2001['Close'].mean()
print("Jan 2001 Mean Closing Price:", Jan2001_mean)
Jan2001.plot(x='Date', y='Close', title='AMD Closing Prices in January 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2001=df.loc[(df['Date'] >= '2001-02-01') & (df['Date'] < '2001-02-28')]
print(Feb2001)
Feb2001_mean=Feb2001['Close'].mean()
print("Feb 2001 Mean Closing Price:", Feb2001_mean)
Feb2001.plot(x='Date', y='Close', title='AMD Closing Prices in February 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2001=df.loc[(df['Date'] >= '2001-03-01') & (df['Date'] < '2001-03-31')]
print(Mar2001)
Mar2001_mean=Mar2001['Close'].mean()
print("Mar 2001 Mean Closing Price:", Mar2001_mean)
Mar2001.plot(x='Date', y='Close', title='AMD Closing Prices in March 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2001=df.loc[(df['Date'] >= '2001-04-01') & (df['Date'] < '2001-04-30')]
print(Apr2001)
Apr2001_mean=Apr2001['Close'].mean()
print("Apr 2001 Mean Closing Price:", Apr2001_mean)
Apr2001.plot(x='Date', y='Close', title='AMD Closing Prices in April 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2001=df.loc[(df['Date'] >= '2001-05-01') & (df['Date'] < '2001-05-31')]
print(May2001)
May2001_mean=May2001['Close'].mean()
print("May 2001 Mean Closing Price:", May2001_mean)
May2001.plot(x='Date', y='Close', title='AMD Closing Prices in May 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2001=df.loc[(df['Date'] >= '2001-06-01') & (df['Date'] < '2001-06-30')]
print(Jun2001)
Jun2001_mean=Jun2001['Close'].mean()
print("Jun 2001 Mean Closing Price:", Jun2001_mean)
Jun2001.plot(x='Date', y='Close', title='AMD Closing Prices in June 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2001=df.loc[(df['Date'] >= '2001-07-01') & (df['Date'] < '2001-07-31')]
print(Jul2001)
Jul2001_mean=Jul2001['Close'].mean()
print("Jul 2001 Mean Closing Price:", Jul2001_mean)
Jul2001.plot(x='Date', y='Close', title='AMD Closing Prices in July 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2001=df.loc[(df['Date'] >= '2001-08-01') & (df['Date'] < '2001-08-31')]
print(Aug2001)
Aug2001_mean=Aug2001['Close'].mean()
print("Aug 2001 Mean Closing Price:", Aug2001_mean)
Aug2001.plot(x='Date', y='Close', title='AMD Closing Prices in August 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2001=df.loc[(df['Date'] >= '2001-09-01') & (df['Date'] < '2001-09-30')]
print(Sep2001)
Sep2001_mean=Sep2001['Close'].mean()
print("Sep 2001 Mean Closing Price:", Sep2001_mean)
Sep2001.plot(x='Date', y='Close', title='AMD Closing Prices in September 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2001=df.loc[(df['Date'] >= '2001-10-01') & (df['Date'] < '2001-10-31')]
print(Oct2001)
Oct2001_mean=Oct2001['Close'].mean()
print("Oct 2001 Mean Closing Price:", Oct2001_mean)
Oct2001.plot(x='Date', y='Close', title='AMD Closing Prices in October 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2001=df.loc[(df['Date'] >= '2001-11-01') & (df['Date'] < '2001-11-30')]
print(Nov2001)
Nov2001_mean=Nov2001['Close'].mean()
print("Nov 2001 Mean Closing Price:", Nov2001_mean)
Nov2001.plot(x='Date', y='Close', title='AMD Closing Prices in November 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2001=df.loc[(df['Date'] >= '2001-12-01') & (df['Date'] < '2001-12-31')]
print(Dec2001)
Dec2001_mean=Dec2001['Close'].mean()
print("Dec 2001 Mean Closing Price:", Dec2001_mean)
Dec2001.plot(x='Date', y='Close', title='AMD Closing Prices in December 2001')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2002=df.loc[(df['Date'] >= '2002-01-01') & (df['Date'] < '2002-01-31')]
print(Jan2002)
Jan2002_mean=Jan2002['Close'].mean()
print("Jan 2002 Mean Closing Price:", Jan2002_mean)
Jan2002.plot(x='Date', y='Close', title='AMD Closing Prices in January 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2002=df.loc[(df['Date'] >= '2002-02-01') & (df['Date'] < '2002-02-28')]
print(Feb2002)
Feb2002_mean=Feb2002['Close'].mean()
print("Feb 2002 Mean Closing Price:", Feb2002_mean)
Feb2002.plot(x='Date', y='Close', title='AMD Closing Prices in February 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2002=df.loc[(df['Date'] >= '2002-03-01') & (df['Date'] < '2002-03-31')]
print(Mar2002)
Mar2002_mean=Mar2002['Close'].mean()
print("Mar 2002 Mean Closing Price:", Mar2002_mean)
Mar2002.plot(x='Date', y='Close', title='AMD Closing Prices in March 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2002=df.loc[(df['Date'] >= '2002-04-01') & (df['Date'] < '2002-04-30')]
print(Apr2002)
Apr2002_mean=Apr2002['Close'].mean()
print("Apr 2002 Mean Closing Price:", Apr2002_mean)
Apr2002.plot(x='Date', y='Close', title='AMD Closing Prices in April 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2002=df.loc[(df['Date'] >= '2002-05-01') & (df['Date'] < '2002-05-31')]
print(May2002)
May2002_mean=May2002['Close'].mean()
print("May 2002 Mean Closing Price:", May2002_mean)
May2002.plot(x='Date', y='Close', title='AMD Closing Prices in May 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2002=df.loc[(df['Date'] >= '2002-06-01') & (df['Date'] < '2002-06-30')]
print(Jun2002)
Jun2002_mean=Jan2002['Close'].mean()
print("Jun 2002 Mean Closing Price:", Jun2002_mean)
Jun2002.plot(x='Date', y='Close', title='AMD Closing Prices in June 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2002=df.loc[(df['Date'] >= '2002-07-01') & (df['Date'] < '2002-07-31')]
print(Jul2002)
Jul2002_mean=Jul2002['Close'].mean()
print("Jul 2002 Mean Closing Price:", Jul2002_mean)
Jul2002.plot(x='Date', y='Close', title='AMD Closing Prices in July 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2002=df.loc[(df['Date'] >= '2002-08-01') & (df['Date'] < '2002-08-31')]
print(Aug2002)
Aug2002_mean=Aug2002['Close'].mean()
print("Aug 2002 Mean Closing Price:", Aug2002_mean)
Aug2002.plot(x='Date', y='Close', title='AMD Closing Prices in August 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2002=df.loc[(df['Date'] >= '2002-09-01') & (df['Date'] < '2002-09-30')]
print(Sep2002)
Sep2002_mean=Sep2002['Close'].mean()
print("Sep 2002 Mean Closing Price:", Sep2002_mean)
Sep2002.plot(x='Date', y='Close', title='AMD Closing Prices in September 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2002=df.loc[(df['Date'] >= '2002-10-01') & (df['Date'] < '2002-10-31')]
print(Oct2002)
Oct2002_mean=Oct2002['Close'].mean()
print("Oct 2002 Mean Closing Price:", Oct2002_mean)
Oct2002.plot(x='Date', y='Close', title='AMD Closing Prices in October 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2002=df.loc[(df['Date'] >= '2002-11-01') & (df['Date'] < '2002-11-30')]
print(Nov2002)
Nov2002_mean=Nov2002['Close'].mean()
print("Nov 2002 Mean Closing Price:", Nov2002_mean)
Nov2002.plot(x='Date', y='Close', title='AMD Closing Prices in November 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2002=df.loc[(df['Date'] >= '2002-12-01') & (df['Date'] < '2002-12-31')]
print(Dec2002)
Dec2002_mean=Dec2002['Close'].mean()
print("Dec 2002 Mean Closing Price:", Dec2002_mean)
Dec2002.plot(x='Date', y='Close', title='AMD Closing Prices in December 2002')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2003=df.loc[(df['Date'] >= '2003-01-01') & (df['Date'] < '2003-01-31')]
print(Jan2003)
Jan2003_mean=Jan2003['Close'].mean()
print("Jan 2003 Mean Closing Price:", Jan2003_mean)
Jan2003.plot(x='Date', y='Close', title='AMD Closing Prices in January 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2003=df.loc[(df['Date'] >= '2003-02-01') & (df['Date'] < '2003-02-28')]
print(Feb2003)
Feb2003_mean=Feb2003['Close'].mean()
print("Feb 2003 Mean Closing Price:", Feb2003_mean)
Feb2003.plot(x='Date', y='Close', title='AMD Closing Prices in February 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2003=df.loc[(df['Date'] >= '2003-03-01') & (df['Date'] < '2003-03-31')]
print(Mar2003)
Mar2003_mean=Mar2003['Close'].mean()
print("Mar 2003 Mean Closing Price:", Mar2003_mean)
Mar2003.plot(x='Date', y='Close', title='AMD Closing Prices in March 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2003=df.loc[(df['Date'] >= '2003-04-01') & (df['Date'] < '2003-04-30')]
print(Apr2003)
Apr2003_mean=Apr2003['Close'].mean()
print("Apr 2003 Mean Closing Price:", Apr2003_mean)
Apr2003.plot(x='Date', y='Close', title='AMD Closing Prices in April 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2003=df.loc[(df['Date'] >= '2003-05-01') & (df['Date'] < '2003-05-31')]
print(May2003)
May2003_mean=May2003['Close'].mean()
print("May 2003 Mean Closing Price:", May2003_mean)
May2003.plot(x='Date', y='Close', title='AMD Closing Prices in May 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2003=df.loc[(df['Date'] >= '2003-06-01') & (df['Date'] < '2003-06-30')]
print(Jun2003)
Jun2003_mean=Jun2003['Close'].mean()
print("Jun 2003 Mean Closing Price:", Jun2003_mean)
Jun2003.plot(x='Date', y='Close', title='AMD Closing Prices in June 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2003=df.loc[(df['Date'] >= '2003-07-01') & (df['Date'] < '2003-07-31')]
print(Jul2003)
Jul2003_mean=Jul2003['Close'].mean()
print("Jul 2003 Mean Closing Price:", Jul2003_mean)
Jul2003.plot(x='Date', y='Close', title='AMD Closing Prices in July 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2003=df.loc[(df['Date'] >= '2003-08-01') & (df['Date'] < '2003-08-31')]
print(Aug2003)
Aug2003_mean=Aug2003['Close'].mean()
print("Aug 2003 Mean Closing Price:", Aug2003_mean)
Aug2003.plot(x='Date', y='Close', title='AMD Closing Prices in August 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2003=df.loc[(df['Date'] >= '2003-09-01') & (df['Date'] < '2003-09-30')]
print(Sep2003)
Sep2003_mean=Sep2003['Close'].mean()
print("Sep 2003 Mean Closing Price:", Sep2003_mean)
Sep2003.plot(x='Date', y='Close', title='AMD Closing Prices in September 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2003=df.loc[(df['Date'] >= '2003-10-01') & (df['Date'] < '2003-10-31')]
print(Oct2003)
Oct2003_mean=Oct2003['Close'].mean()
print("Oct 2003 Mean Closing Price:", Oct2003_mean)
Oct2003.plot(x='Date', y='Close', title='AMD Closing Prices in October 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2003=df.loc[(df['Date'] >= '2003-11-01') & (df['Date'] < '2003-11-30')]
print(Nov2003)
Nov2003_mean=Nov2003['Close'].mean()
print("Nov 2003 Mean Closing Price:", Nov2003_mean)
Nov2003.plot(x='Date', y='Close', title='AMD Closing Prices in November 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2003=df.loc[(df['Date'] >= '2003-12-01') & (df['Date'] < '2003-12-31')]
print(Dec2003)
Dec2003_mean=Dec2003['Close'].mean()
print("Dec 2003 Mean Closing Price:", Dec2003_mean)
Dec2003.plot(x='Date', y='Close', title='AMD Closing Prices in December 2003')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2004=df.loc[(df['Date'] >= '2004-01-01') & (df['Date'] < '2004-01-31')]
print(Jan2004)
Jan2004_mean=Jan2004['Close'].mean()
print("Jan 2004 Mean Closing Price:", Jan2004_mean)
Jan2004.plot(x='Date', y='Close', title='AMD Closing Prices in January 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2004=df.loc[(df['Date'] >= '2004-02-01') & (df['Date'] < '2004-02-29')]
print(Feb2004)
Feb2004_mean=Feb2004['Close'].mean()
print("Feb 2004 Mean Closing Price:", Feb2004_mean)
Feb2004.plot(x='Date', y='Close', title='AMD Closing Prices in February 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2004=df.loc[(df['Date'] >= '2004-03-01') & (df['Date'] < '2004-03-31')]
print(Mar2004)
Mar2004_mean=Mar2004['Close'].mean()
print("Mar 2004 Mean Closing Price:", Mar2004_mean)
Mar2004.plot(x='Date', y='Close', title='AMD Closing Prices in March 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2004=df.loc[(df['Date'] >= '2004-04-01') & (df['Date'] < '2004-04-30')]
print(Apr2004)
Apr2004_mean=Apr2004['Close'].mean()
print("Apr 2004 Mean Closing Price:", Apr2004_mean)
Apr2004.plot(x='Date', y='Close', title='AMD Closing Prices in April 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2004=df.loc[(df['Date'] >= '2004-05-01') & (df['Date'] < '2004-05-31')]
print(May2004)
May2004_mean=May2004['Close'].mean()
print("May 2004 Mean Closing Price:", May2004_mean)
May2004.plot(x='Date', y='Close', title='AMD Closing Prices in May 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2004=df.loc[(df['Date'] >= '2004-06-01') & (df['Date'] < '2004-06-30')]
print(Jun2004)
Jun2004_mean=Jun2004['Close'].mean()
print("Jun 2004 Mean Closing Price:", Jun2004_mean)
Jun2004.plot(x='Date', y='Close', title='AMD Closing Prices in June 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2004=df.loc[(df['Date'] >= '2004-07-01') & (df['Date'] < '2004-07-31')]
print(Jul2004)
Jul2004_mean=Jul2004['Close'].mean()
print("Jul 2004 Mean Closing Price:", Jul2004_mean)
Jul2004.plot(x='Date', y='Close', title='AMD Closing Prices in July 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2004=df.loc[(df['Date'] >= '2004-08-01') & (df['Date'] < '2004-08-31')]
print(Aug2004)
Aug2004_mean=Aug2004['Close'].mean()
print("Aug 2004 Mean Closing Price:", Aug2004_mean)
Aug2004.plot(x='Date', y='Close', title='AMD Closing Prices in August 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2004=df.loc[(df['Date'] >= '2004-09-01') & (df['Date'] < '2004-09-30')]
print(Sep2004)
Sep2004_mean=Sep2004['Close'].mean()
print("Sep 2004 Mean Closing Price:", Sep2004_mean)
Sep2004.plot(x='Date', y='Close', title='AMD Closing Prices in September 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2004=df.loc[(df['Date'] >= '2004-10-01') & (df['Date'] < '2004-10-31')]
print(Oct2004)
Oct2004_mean=Oct2004['Close'].mean()
print("Oct 2004 Mean Closing Price:", Oct2004_mean)
Oct2004.plot(x='Date', y='Close', title='AMD Closing Prices in October 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2004=df.loc[(df['Date'] >= '2004-11-01') & (df['Date'] < '2004-11-30')]
print(Nov2004)
Nov2004_mean=Nov2004['Close'].mean()
print("Nov 2004 Mean Closing Price:", Nov2004_mean)
Nov2004.plot(x='Date', y='Close', title='AMD Closing Prices in November 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2004=df.loc[(df['Date'] >= '2004-12-01') & (df['Date'] < '2004-12-31')]
print(Dec2004)
Dec2004_mean=Dec2004['Close'].mean()
print("Dec 2004 Mean Closing Price:", Dec2004_mean)
Dec2004.plot(x='Date', y='Close', title='AMD Closing Prices in December 2004')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2005=df.loc[(df['Date'] >= '2005-01-01') & (df['Date'] < '2005-01-31')]
print(Jan2005)
Jan2005_mean=Jan2005['Close'].mean()
print("Jan 2005 Mean Closing Price:", Jan2005_mean)
Jan2005.plot(x='Date', y='Close', title='AMD Closing Prices in January 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2005=df.loc[(df['Date'] >= '2005-02-01') & (df['Date'] < '2005-02-28')]
print(Feb2005)
Feb2005_mean=Feb2005['Close'].mean()
print("Feb 2005 Mean Closing Price:", Feb2005_mean)
Feb2005.plot(x='Date', y='Close', title='AMD Closing Prices in February 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2005=df.loc[(df['Date'] >= '2005-03-01') & (df['Date'] < '2005-03-31')]
print(Mar2005)
Mar2005_mean=Mar2005['Close'].mean()
print("Mar 2005 Mean Closing Price:", Mar2005_mean)
Mar2005.plot(x='Date', y='Close', title='AMD Closing Prices in March 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2005=df.loc[(df['Date'] >= '2005-04-01') & (df['Date'] < '2005-04-30')]
print(Apr2005)
Apr2005_mean=Apr2005['Close'].mean()
print("Apr 2005 Mean Closing Price:", Apr2005_mean)
Apr2005.plot(x='Date', y='Close', title='AMD Closing Prices in April 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2005=df.loc[(df['Date'] >= '2005-05-01') & (df['Date'] < '2005-05-31')]
print(May2005)
May2005_mean=May2005['Close'].mean()
print("May 2005 Mean Closing Price:", May2005_mean)
May2005.plot(x='Date', y='Close', title='AMD Closing Prices in May 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2005=df.loc[(df['Date'] >= '2005-06-01') & (df['Date'] < '2005-06-30')]
print(Jun2005)
Jun2005_mean=Jun2005['Close'].mean()
print("Jun 2005 Mean Closing Price:", Jun2005_mean)
Jun2005.plot(x='Date', y='Close', title='AMD Closing Prices in June 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2005=df.loc[(df['Date'] >= '2005-07-01') & (df['Date'] < '2005-07-31')]
print(Jul2005)
Jul2005_mean=Jul2005['Close'].mean()
print("Jul 2005 Mean Closing Price:", Jul2005_mean)
Jul2005.plot(x='Date', y='Close', title='AMD Closing Prices in July 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2005=df.loc[(df['Date'] >= '2005-08-01') & (df['Date'] < '2005-08-31')]
print(Aug2005)
Aug2005_mean=Aug2005['Close'].mean()
print("Aug 2005 Mean Closing Price:", Aug2005_mean)
Aug2005.plot(x='Date', y='Close', title='AMD Closing Prices in August 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2005=df.loc[(df['Date'] >= '2005-09-01') & (df['Date'] < '2005-09-30')]
print(Sep2005)
Sep2005_mean=Sep2005['Close'].mean()
print("Sep 2005 Mean Closing Price:", Sep2005_mean)
Sep2005.plot(x='Date', y='Close', title='AMD Closing Prices in September 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2005=df.loc[(df['Date'] >= '2005-10-01') & (df['Date'] < '2005-10-31')]
print(Oct2005)
Oct2005_mean=Oct2005['Close'].mean()
print("Oct 2005 Mean Closing Price:", Oct2005_mean)
Oct2005.plot(x='Date', y='Close', title='AMD Closing Prices in October 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2005=df.loc[(df['Date'] >= '2005-11-01') & (df['Date'] < '2005-11-30')]
print(Nov2005)
Nov2005_mean=Nov2005['Close'].mean()
print("Nov 2005 Mean Closing Price:", Nov2005_mean)
Nov2005.plot(x='Date', y='Close', title='AMD Closing Prices in November 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2005=df.loc[(df['Date'] >= '2005-12-01') & (df['Date'] < '2005-12-31')]
print(Dec2005)
Dec2005_mean=Dec2005['Close'].mean()
print("Dec 2005 Mean Closing Price:", Dec2005_mean)
Dec2005.plot(x='Date', y='Close', title='AMD Closing Prices in December 2005')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2006=df.loc[(df['Date'] >= '2006-01-01') & (df['Date'] < '2006-01-31')]
print(Jan2006)
Jan2006_mean=Jan2006['Close'].mean()
print("Jan 2006 Mean Closing Price:", Jan2006_mean)
Jan2006.plot(x='Date', y='Close', title='AMD Closing Prices in January 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2006=df.loc[(df['Date'] >= '2006-02-01') & (df['Date'] < '2006-02-28')]
print(Feb2006)
Feb2006_mean=Feb2006['Close'].mean()
print("Feb 2006 Mean Closing Price:", Feb2006_mean)
Feb2006.plot(x='Date', y='Close', title='AMD Closing Prices in February 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2006=df.loc[(df['Date'] >= '2006-03-01') & (df['Date'] < '2006-03-31')]
print(Mar2006)
Mar2006_mean=Mar2006['Close'].mean()
print("Mar 2006 Mean Closing Price:", Mar2006_mean)
Mar2006.plot(x='Date', y='Close', title='AMD Closing Prices in March 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2006=df.loc[(df['Date'] >= '2006-04-01') & (df['Date'] < '2006-04-30')]
print(Apr2006)
Apr2006_mean=Apr2006['Close'].mean()
print("Apr 2006 Mean Closing Price:", Apr2006_mean)
Apr2006.plot(x='Date', y='Close', title='AMD Closing Prices in April 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2006=df.loc[(df['Date'] >= '2006-05-01') & (df['Date'] < '2006-05-31')]
print(May2006)
May2006_mean=May2006['Close'].mean()
print("May 2006 Mean Closing Price:", May2006_mean)
May2006.plot(x='Date', y='Close', title='AMD Closing Prices in May 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2006=df.loc[(df['Date'] >= '2006-06-01') & (df['Date'] < '2006-06-30')]
print(Jun2006)
Jun2006_mean=Jun2006['Close'].mean()
print("Jun 2006 Mean Closing Price:", Jun2006_mean)
Jun2006.plot(x='Date', y='Close', title='AMD Closing Prices in January 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2006=df.loc[(df['Date'] >= '2006-07-01') & (df['Date'] < '2006-07-31')]
print(Jul2006)
Jul2006_mean=Jul2006['Close'].mean()
print("Jul 2006 Mean Closing Price:", Jul2006_mean)
Jul2006.plot(x='Date', y='Close', title='AMD Closing Prices in July 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2006=df.loc[(df['Date'] >= '2006-08-01') & (df['Date'] < '2006-08-31')]
print(Aug2006)
Aug2006_mean=Aug2006['Close'].mean()
print("Aug 2006 Mean Closing Price:", Aug2006_mean)
Aug2006.plot(x='Date', y='Close', title='AMD Closing Prices in August 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2006=df.loc[(df['Date'] >= '2006-09-01') & (df['Date'] < '2006-09-30')]
print(Sep2006)
Sep2006_mean=Sep2006['Close'].mean()
print("Sep 2006 Mean Closing Price:", Sep2006_mean)
Sep2006.plot(x='Date', y='Close', title='AMD Closing Prices in September 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2006=df.loc[(df['Date'] >= '2006-10-01') & (df['Date'] < '2006-10-31')]
print(Oct2006)
Oct2006_mean=Oct2006['Close'].mean()
print("Oct 2006 Mean Closing Price:", Oct2006_mean)
Oct2006.plot(x='Date', y='Close', title='AMD Closing Prices in October 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2006=df.loc[(df['Date'] >= '2006-11-01') & (df['Date'] < '2006-11-30')]
print(Nov2006)
Nov2006_mean=Nov2006['Close'].mean()
print("Nov 2006 Mean Closing Price:", Nov2006_mean)
Nov2006.plot(x='Date', y='Close', title='AMD Closing Prices in November 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2006=df.loc[(df['Date'] >= '2006-12-01') & (df['Date'] < '2006-12-31')]
print(Dec2006)
Dec2006_mean=Dec2006['Close'].mean()
print("Dec 2006 Mean Closing Price:", Dec2006_mean)
Dec2006.plot(x='Date', y='Close', title='AMD Closing Prices in December 2006')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2007=df.loc[(df['Date'] >= '2007-01-01') & (df['Date'] < '2007-01-31')]
print(Jan2007)
Jan2007_mean=Jan2007['Close'].mean()
print("Jan 2007 Mean Closing Price:", Jan2007_mean)
Jan2007.plot(x='Date', y='Close', title='AMD Closing Prices in January 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2007=df.loc[(df['Date'] >= '2007-02-01') & (df['Date'] < '2007-02-28')]
print(Feb2007)
Feb2007_mean=Feb2007['Close'].mean()
print("Feb 2007 Mean Closing Price:", Feb2007_mean)
Feb2007.plot(x='Date', y='Close', title='AMD Closing Prices in February 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2007=df.loc[(df['Date'] >= '2007-03-01') & (df['Date'] < '2007-03-31')]
print(Mar2007)
Mar2007_mean=Mar2007['Close'].mean()
print("Mar 2007 Mean Closing Price:", Mar2007_mean)
Mar2007.plot(x='Date', y='Close', title='AMD Closing Prices in March 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2007=df.loc[(df['Date'] >= '2007-04-01') & (df['Date'] < '2007-04-30')]
print(Apr2007)
Apr2007_mean=Apr2007['Close'].mean()
print("Apr 2007 Mean Closing Price:", Apr2007_mean)
Apr2007.plot(x='Date', y='Close', title='AMD Closing Prices in April 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2007=df.loc[(df['Date'] >= '2007-05-01') & (df['Date'] < '2007-05-31')]
print(May2007)
May2007_mean=May2007['Close'].mean()
print("May 2007 Mean Closing Price:", May2007_mean)
May2007.plot(x='Date', y='Close', title='AMD Closing Prices in May 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2007=df.loc[(df['Date'] >= '2007-06-01') & (df['Date'] < '2007-06-30')]
print(Jun2007)
Jun2007_mean=Jun2007['Close'].mean()
print("Jun 2007 Mean Closing Price:", Jun2007_mean)
Jun2007.plot(x='Date', y='Close', title='AMD Closing Prices in June 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2007=df.loc[(df['Date'] >= '2007-07-01') & (df['Date'] < '2007-07-31')]
print(Jul2007)
Jul2007_mean=Jul2007['Close'].mean()
print("Jul 2007 Mean Closing Price:", Jul2007_mean)
Jul2007.plot(x='Date', y='Close', title='AMD Closing Prices in July 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2007=df.loc[(df['Date'] >= '2007-08-01') & (df['Date'] < '2007-08-31')]
print(Aug2007)
Aug2007_mean=Aug2007['Close'].mean()
print("Aug 2007 Mean Closing Price:", Aug2007_mean)
Aug2007.plot(x='Date', y='Close', title='AMD Closing Prices in August 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2007=df.loc[(df['Date'] >= '2007-09-01') & (df['Date'] < '2007-09-30')]
print(Sep2007)
Sep2007_mean=Sep2007['Close'].mean()
print("Sep 2007 Mean Closing Price:", Sep2007_mean)
Sep2007.plot(x='Date', y='Close', title='AMD Closing Prices in September 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2007=df.loc[(df['Date'] >= '2007-10-01') & (df['Date'] < '2007-10-31')]
print(Oct2007)
Oct2007_mean=Oct2007['Close'].mean()
print("Oct 2007 Mean Closing Price:", Oct2007_mean)
Oct2007.plot(x='Date', y='Close', title='AMD Closing Prices in October 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2007=df.loc[(df['Date'] >= '2007-11-01') & (df['Date'] < '2007-11-30')]
print(Nov2007)
Nov2007_mean=Nov2007['Close'].mean()
print("Nov 2007 Mean Closing Price:", Nov2007_mean)
Nov2007.plot(x='Date', y='Close', title='AMD Closing Prices in November 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2007=df.loc[(df['Date'] >= '2007-12-01') & (df['Date'] < '2007-12-31')]
print(Dec2007)
Dec2007_mean=Dec2007['Close'].mean()
print("Dec 2007 Mean Closing Price:", Dec2007_mean)
Dec2007.plot(x='Date', y='Close', title='AMD Closing Prices in December 2007')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2008=df.loc[(df['Date'] >= '2008-01-01') & (df['Date'] < '2008-01-31')]
print(Jan2008)
Jan2008_mean=Jan2008['Close'].mean()
print("Jan 2008 Mean Closing Price:", Jan2008_mean)
Jan2008.plot(x='Date', y='Close', title='AMD Closing Prices in January 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2008=df.loc[(df['Date'] >= '2008-02-01') & (df['Date'] < '2008-02-29')]
print(Feb2008)
Feb2008_mean=Feb2008['Close'].mean()
print("Feb 2008 Mean Closing Price:", Feb2008_mean)
Feb2008.plot(x='Date', y='Close', title='AMD Closing Prices in February 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2008=df.loc[(df['Date'] >= '2008-03-01') & (df['Date'] < '2008-03-31')]
print(Mar2008)
Mar2008_mean=Mar2008['Close'].mean()
print("Mar 2008 Mean Closing Price:", Mar2008_mean)
Mar2008.plot(x='Date', y='Close', title='AMD Closing Prices in March 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2008=df.loc[(df['Date'] >= '2008-04-01') & (df['Date'] < '2008-04-30')]
print(Apr2008)
Apr2008_mean=Apr2008['Close'].mean()
print("Apr 2008 Mean Closing Price:", Apr2008_mean)
Apr2008.plot(x='Date', y='Close', title='AMD Closing Prices in April 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2008=df.loc[(df['Date'] >= '2008-05-01') & (df['Date'] < '2008-05-31')]
print(May2008)
May2008_mean=May2008['Close'].mean()
print("May 2008 Mean Closing Price:", May2008_mean)
May2008.plot(x='Date', y='Close', title='AMD Closing Prices in May 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2008=df.loc[(df['Date'] >= '2008-06-01') & (df['Date'] < '2008-06-30')]
print(Jun2008)
Jun2008_mean=Jun2008['Close'].mean()
print("Jun 2008 Mean Closing Price:", Jun2008_mean)
Jun2008.plot(x='Date', y='Close', title='AMD Closing Prices in June 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2008=df.loc[(df['Date'] >= '2008-07-01') & (df['Date'] < '2008-07-31')]
print(Jul2008)
Jul2008_mean=Jul2008['Close'].mean()
print("Jul 2008 Mean Closing Price:", Jul2008_mean)
Jul2008.plot(x='Date', y='Close', title='AMD Closing Prices in July 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2008=df.loc[(df['Date'] >= '2008-08-01') & (df['Date'] < '2008-08-31')]
print(Aug2008)
Aug2008_mean=Aug2008['Close'].mean()
print("Aug 2008 Mean Closing Price:", Aug2008_mean)
Aug2008.plot(x='Date', y='Close', title='AMD Closing Prices in August 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2008=df.loc[(df['Date'] >= '2008-09-01') & (df['Date'] < '2008-09-30')]
print(Sep2008)
Sep2008_mean=Sep2008['Close'].mean()
print("Sep 2008 Mean Closing Price:", Sep2008_mean)
Sep2008.plot(x='Date', y='Close', title='AMD Closing Prices in September 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2008=df.loc[(df['Date'] >= '2008-10-01') & (df['Date'] < '2008-10-31')]
print(Oct2008)
Oct2008_mean=Oct2008['Close'].mean()
print("Oct 2008 Mean Closing Price:", Oct2008_mean)
Oct2008.plot(x='Date', y='Close', title='AMD Closing Prices in October 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2008=df.loc[(df['Date'] >= '2008-11-01') & (df['Date'] < '2008-11-30')]
print(Nov2008)
Nov2008_mean=Nov2008['Close'].mean()
print("Nov 2008 Mean Closing Price:", Nov2008_mean)
Nov2008.plot(x='Date', y='Close', title='AMD Closing Prices in November 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2008=df.loc[(df['Date'] >= '2008-12-01') & (df['Date'] < '2008-12-31')]
print(Dec2008)
Dec2008_mean=Dec2008['Close'].mean()
print("Dec 2008 Mean Closing Price:", Dec2008_mean)
Dec2008.plot(x='Date', y='Close', title='AMD Closing Prices in December 2008')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2009=df.loc[(df['Date'] >= '2009-01-01') & (df['Date'] < '2009-01-31')]
print(Jan2009)
Jan2009_mean=Jan2009['Close'].mean()
print("Jan 2009 Mean Closing Price:", Jan2009_mean)
Jan2009.plot(x='Date', y='Close', title='AMD Closing Prices in January 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2009=df.loc[(df['Date'] >= '2009-02-01') & (df['Date'] < '2009-02-28')]
print(Feb2009)
Feb2009_mean=Feb2009['Close'].mean()
print("Feb 2009 Mean Closing Price:", Feb2009_mean)
Feb2009.plot(x='Date', y='Close', title='AMD Closing Prices in February 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2009=df.loc[(df['Date'] >= '2009-03-01') & (df['Date'] < '2009-03-31')]
print(Mar2009)
Mar2009_mean=Mar2009['Close'].mean()
print("Mar 2009 Mean Closing Price:", Mar2009_mean)
Mar2009.plot(x='Date', y='Close', title='AMD Closing Prices in March 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2009=df.loc[(df['Date'] >= '2009-04-01') & (df['Date'] < '2009-04-30')]
print(Apr2009)
Apr2009_mean=Apr2009['Close'].mean()
print("Apr 2009 Mean Closing Price:", Apr2009_mean)
Apr2009.plot(x='Date', y='Close', title='AMD Closing Prices in April 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2009=df.loc[(df['Date'] >= '2009-05-01') & (df['Date'] < '2009-05-31')]
print(May2009)
May2009_mean=May2009['Close'].mean()
print("May 2009 Mean Closing Price:", May2009_mean)
May2009.plot(x='Date', y='Close', title='AMD Closing Prices in May 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2009=df.loc[(df['Date'] >= '2009-06-01') & (df['Date'] < '2009-06-30')]
print(Jun2009)
Jun2009_mean=Jun2009['Close'].mean()
print("Jun 2009 Mean Closing Price:", Jun2009_mean)
Jun2009.plot(x='Date', y='Close', title='AMD Closing Prices in June 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2009=df.loc[(df['Date'] >= '2009-07-01') & (df['Date'] < '2009-07-31')]
print(Jul2009)
Jul2009_mean=Jul2009['Close'].mean()
print("Jul 2009 Mean Closing Price:", Jul2009_mean)
Jul2009.plot(x='Date', y='Close', title='AMD Closing Prices in July 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2009=df.loc[(df['Date'] >= '2009-08-01') & (df['Date'] < '2009-08-31')]
print(Aug2009)
Aug2009_mean=Aug2009['Close'].mean()
print("Aug 2009 Mean Closing Price:", Aug2009_mean)
Aug2009.plot(x='Date', y='Close', title='AMD Closing Prices in August 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2009=df.loc[(df['Date'] >= '2009-09-01') & (df['Date'] < '2009-09-30')]
print(Sep2009)
Sep2009_mean=Sep2009['Close'].mean()
print("Sep 2009 Mean Closing Price:", Sep2009_mean)
Sep2009.plot(x='Date', y='Close', title='AMD Closing Prices in September 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2009=df.loc[(df['Date'] >= '2009-10-01') & (df['Date'] < '2009-10-31')]
print(Oct2009)
Oct2009_mean=Oct2009['Close'].mean()
print("Oct 2009 Mean Closing Price:", Oct2009_mean)
Oct2009.plot(x='Date', y='Close', title='AMD Closing Prices in October 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2009=df.loc[(df['Date'] >= '2009-11-01') & (df['Date'] < '2009-11-30')]
print(Nov2009)
Nov2009_mean=Nov2009['Close'].mean()
print("Nov 2009 Mean Closing Price:", Nov2009_mean)
Nov2009.plot(x='Date', y='Close', title='AMD Closing Prices in November 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2009=df.loc[(df['Date'] >= '2009-12-01') & (df['Date'] < '2009-12-31')]
print(Dec2009)
Dec2009_mean=Dec2009['Close'].mean()
print("Dec 2009 Mean Closing Price:", Dec2009_mean)
Dec2009.plot(x='Date', y='Close', title='AMD Closing Prices in December 2009')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2010=df.loc[(df['Date'] >= '2010-01-01') & (df['Date'] < '2010-01-31')]
print(Jan2010)
Jan2010_mean=Jan2010['Close'].mean()
print("Jan 2010 Mean Closing Price:", Jan2010_mean)
Jan2010.plot(x='Date', y='Close', title='AMD Closing Prices in January 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2010=df.loc[(df['Date'] >= '2010-02-01') & (df['Date'] < '2010-02-28')]
print(Feb2010)
Feb2010_mean=Feb2010['Close'].mean()
print("Feb 2010 Mean Closing Price:", Feb2010_mean)
Feb2010.plot(x='Date', y='Close', title='AMD Closing Prices in February 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2010=df.loc[(df['Date'] >= '2010-03-01') & (df['Date'] < '2010-03-31')]
print(Mar2010)
Mar2010_mean=Mar2010['Close'].mean()
print("Mar 2010 Mean Closing Price:", Mar2010_mean)
Mar2010.plot(x='Date', y='Close', title='AMD Closing Prices in March 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2010=df.loc[(df['Date'] >= '2010-04-01') & (df['Date'] < '2010-04-30')]
print(Apr2010)
Apr2010_mean=Apr2010['Close'].mean()
print("Apr 2010 Mean Closing Price:", Apr2010_mean)
Apr2010.plot(x='Date', y='Close', title='AMD Closing Prices in April 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2010=df.loc[(df['Date'] >= '2010-05-01') & (df['Date'] < '2010-05-31')]
print(May2010)
May2010_mean=May2010['Close'].mean()
print("May 2010 Mean Closing Price:", May2010_mean)
May2010.plot(x='Date', y='Close', title='AMD Closing Prices in May 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2010=df.loc[(df['Date'] >= '2010-06-01') & (df['Date'] < '2010-06-30')]
print(Jun2010)
Jun2010_mean=Jun2010['Close'].mean()
print("Jun 2010 Mean Closing Price:", Jun2010_mean)
Jun2010.plot(x='Date', y='Close', title='AMD Closing Prices in June 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2010=df.loc[(df['Date'] >= '2010-07-01') & (df['Date'] < '2010-07-31')]
print(Jul2010)
Jul2010_mean=Jul2010['Close'].mean()
print("Jul 2010 Mean Closing Price:", Jul2010_mean)
Jul2010.plot(x='Date', y='Close', title='AMD Closing Prices in July 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2010=df.loc[(df['Date'] >= '2010-08-01') & (df['Date'] < '2010-08-31')]
print(Aug2010)
Aug2010_mean=Aug2010['Close'].mean()
print("Aug 2010 Mean Closing Price:", Aug2010_mean)
Aug2010.plot(x='Date', y='Close', title='AMD Closing Prices in August 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2010=df.loc[(df['Date'] >= '2010-09-01') & (df['Date'] < '2010-09-30')]
print(Sep2010)
Sep2010_mean=Sep2010['Close'].mean()
print("Sep 2010 Mean Closing Price:", Sep2010_mean)
Sep2010.plot(x='Date', y='Close', title='AMD Closing Prices in September 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2010=df.loc[(df['Date'] >= '2010-10-01') & (df['Date'] < '2010-10-31')]
print(Oct2010)
Oct2010_mean=Oct2010['Close'].mean()
print("Oct 2010 Mean Closing Price:", Oct2010_mean)
Oct2010.plot(x='Date', y='Close', title='AMD Closing Prices in October 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2010=df.loc[(df['Date'] >= '2010-11-01') & (df['Date'] < '2010-11-30')]
print(Nov2010)
Nov2010_mean=Nov2010['Close'].mean()
print("Nov 2010 Mean Closing Price:", Nov2010_mean)
Nov2010.plot(x='Date', y='Close', title='AMD Closing Prices in November 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2010=df.loc[(df['Date'] >= '2010-12-01') & (df['Date'] < '2010-12-31')]
print(Dec2010)
Dec2010_mean=Dec2010['Close'].mean()
print("Dec 2010 Mean Closing Price:", Dec2010_mean)
Dec2010.plot(x='Date', y='Close', title='AMD Closing Prices in December 2010')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2011=df.loc[(df['Date'] >= '2011-01-01') & (df['Date'] < '2011-01-31')]
print(Jan2011)
Jan2011_mean=Jan2011['Close'].mean()
print("Jan 2011 Mean Closing Price:", Jan2011_mean)
Jan2011.plot(x='Date', y='Close', title='AMD Closing Prices in January 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2011=df.loc[(df['Date'] >= '2011-02-01') & (df['Date'] < '2011-02-28')]
print(Feb2011)
Feb2011_mean=Feb2011['Close'].mean()
print("Feb 2011 Mean Closing Price:", Feb2011_mean)
Feb2011.plot(x='Date', y='Close', title='AMD Closing Prices in February 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2011=df.loc[(df['Date'] >= '2011-03-01') & (df['Date'] < '2011-03-31')]
print(Mar2011)
Mar2011_mean=Mar2011['Close'].mean()
print("Mar 2011 Mean Closing Price:", Mar2011_mean)
Mar2011.plot(x='Date', y='Close', title='AMD Closing Prices in March 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2011=df.loc[(df['Date'] >= '2011-04-01') & (df['Date'] < '2011-04-30')]
print(Apr2011)
Apr2011_mean=Apr2011['Close'].mean()
print("Apr 2011 Mean Closing Price:", Apr2011_mean)
Apr2011.plot(x='Date', y='Close', title='AMD Closing Prices in April 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2011=df.loc[(df['Date'] >= '2011-05-01') & (df['Date'] < '2011-05-31')]
print(May2011)
May2011_mean=May2011['Close'].mean()
print("May 2011 Mean Closing Price:", May2011_mean)
May2011.plot(x='Date', y='Close', title='AMD Closing Prices in May 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2011=df.loc[(df['Date'] >= '2011-06-01') & (df['Date'] < '2011-06-30')]
print(Jun2011)
Jun2011_mean=Jun2011['Close'].mean()
print("Jun 2011 Mean Closing Price:", Jun2011_mean)
Jun2011.plot(x='Date', y='Close', title='AMD Closing Prices in June 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2011=df.loc[(df['Date'] >= '2011-07-01') & (df['Date'] < '2011-07-31')]
print(Jul2011)
Jul2011_mean=Jul2011['Close'].mean()
print("Jul 2011 Mean Closing Price:", Jul2011_mean)
Jul2011.plot(x='Date', y='Close', title='AMD Closing Prices in July 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2011=df.loc[(df['Date'] >= '2011-08-01') & (df['Date'] < '2011-08-31')]
print(Aug2011)
Aug2011_mean=Aug2011['Close'].mean()
print("Aug 2011 Mean Closing Price:", Aug2011_mean)
Aug2011.plot(x='Date', y='Close', title='AMD Closing Prices in August 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2011=df.loc[(df['Date'] >= '2011-09-01') & (df['Date'] < '2011-09-30')]
print(Sep2011)
Sep2011_mean=Sep2011['Close'].mean()
print("Sep 2011 Mean Closing Price:", Sep2011_mean)
Sep2011.plot(x='Date', y='Close', title='AMD Closing Prices in September 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2011=df.loc[(df['Date'] >= '2011-10-01') & (df['Date'] < '2011-10-31')]
print(Oct2011)
Oct2011_mean=Oct2011['Close'].mean()
print("Oct 2011 Mean Closing Price:", Oct2011_mean)
Oct2011.plot(x='Date', y='Close', title='AMD Closing Prices in October 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2011=df.loc[(df['Date'] >= '2011-11-01') & (df['Date'] < '2011-11-30')]
print(Nov2011)
Nov2011_mean=Nov2011['Close'].mean()
print("Nov 2011 Mean Closing Price:", Nov2011_mean)
Nov2011.plot(x='Date', y='Close', title='AMD Closing Prices in November 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2011=df.loc[(df['Date'] >= '2011-12-01') & (df['Date'] < '2011-12-31')]
print(Dec2011)
Dec2011_mean=Dec2011['Close'].mean()
print("Dec 2011 Mean Closing Price:", Dec2011_mean)
Dec2011.plot(x='Date', y='Close', title='AMD Closing Prices in December 2011')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2012=df.loc[(df['Date'] >= '2012-01-01') & (df['Date'] < '2012-01-31')]
print(Jan2012)
Jan2012_mean=Jan2012['Close'].mean()
print("Jan 2012 Mean Closing Price:", Jan2012_mean)
Jan2012.plot(x='Date', y='Close', title='AMD Closing Prices in January 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2012=df.loc[(df['Date'] >= '2012-02-01') & (df['Date'] < '2012-02-29')]
print(Feb2012)
Feb2012_mean=Feb2012['Close'].mean()
print("Feb 2012 Mean Closing Price:", Feb2012_mean)
Feb2012.plot(x='Date', y='Close', title='AMD Closing Prices in February 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2012=df.loc[(df['Date'] >= '2012-03-01') & (df['Date'] < '2012-03-31')]
print(Mar2012)
Mar2012_mean=Mar2012['Close'].mean()
print("Mar 2012 Mean Closing Price:", Mar2012_mean)
Mar2012.plot(x='Date', y='Close', title='AMD Closing Prices in March 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2012=df.loc[(df['Date'] >= '2012-04-01') & (df['Date'] < '2012-04-30')]
print(Apr2012)
Apr2012_mean=Apr2012['Close'].mean()
print("Apr 2012 Mean Closing Price:", Apr2012_mean)
Apr2012.plot(x='Date', y='Close', title='AMD Closing Prices in April 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2012=df.loc[(df['Date'] >= '2012-05-01') & (df['Date'] < '2012-05-31')]
print(May2012)
May2012_mean=May2012['Close'].mean()
print("May 2012 Mean Closing Price:", May2012_mean)
May2012.plot(x='Date', y='Close', title='AMD Closing Prices in May 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2012=df.loc[(df['Date'] >= '2012-06-01') & (df['Date'] < '2012-06-30')]
print(Jun2012)
Jun2012_mean=Jun2012['Close'].mean()
print("Jun 2012 Mean Closing Price:", Jun2012_mean)
Jun2012.plot(x='Date', y='Close', title='AMD Closing Prices in June 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2012=df.loc[(df['Date'] >= '2012-07-01') & (df['Date'] < '2012-07-31')]
print(Jul2012)
Jul2012_mean=Jul2012['Close'].mean()
print("Jul 2012 Mean Closing Price:", Jul2012_mean)
Jul2012.plot(x='Date', y='Close', title='AMD Closing Prices in July 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2012=df.loc[(df['Date'] >= '2012-08-01') & (df['Date'] < '2012-08-31')]
print(Aug2012)
Aug2012_mean=Aug2012['Close'].mean()
print("Aug 2012 Mean Closing Price:", Aug2012_mean)
Aug2012.plot(x='Date', y='Close', title='AMD Closing Prices in August 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2012=df.loc[(df['Date'] >= '2012-09-01') & (df['Date'] < '2012-09-30')]
print(Sep2012)
Sep2012_mean=Sep2012['Close'].mean()
print("Sep 2012 Mean Closing Price:", Sep2012_mean)
Sep2012.plot(x='Date', y='Close', title='AMD Closing Prices in September 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2012=df.loc[(df['Date'] >= '2012-10-01') & (df['Date'] < '2012-10-31')]
print(Oct2012)
Oct2012_mean=Oct2012['Close'].mean()
print("Oct 2012 Mean Closing Price:", Oct2012_mean)
Oct2012.plot(x='Date', y='Close', title='AMD Closing Prices in October 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2012=df.loc[(df['Date'] >= '2012-11-01') & (df['Date'] < '2012-11-30')]
print(Nov2012)
Nov2012_mean=Nov2012['Close'].mean()
print("Nov 2012 Mean Closing Price:", Nov2012_mean)
Nov2012.plot(x='Date', y='Close', title='AMD Closing Prices in November 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2012=df.loc[(df['Date'] >= '2012-12-01') & (df['Date'] < '2012-12-31')]
print(Dec2012)
Dec2012_mean=Dec2012['Close'].mean()
print("Dec 2012 Mean Closing Price:", Dec2012_mean)
Dec2012.plot(x='Date', y='Close', title='AMD Closing Prices in December 2012')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2013=df.loc[(df['Date'] >= '2013-01-01') & (df['Date'] < '2013-01-31')]
print(Jan2013)
Jan2013_mean=Jan2013['Close'].mean()
print("Jan 2013 Mean Closing Price:", Jan2013_mean)
Jan2013.plot(x='Date', y='Close', title='AMD Closing Prices in January 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2013=df.loc[(df['Date'] >= '2013-02-01') & (df['Date'] < '2013-02-28')]
print(Feb2013)
Feb2013_mean=Feb2013['Close'].mean()
print("Feb 2013 Mean Closing Price:", Jan2013_mean)
Feb2013.plot(x='Date', y='Close', title='AMD Closing Prices in February 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2013=df.loc[(df['Date'] >= '2013-03-01') & (df['Date'] < '2013-03-31')]
print(Mar2013)
Mar2013_mean=Mar2013['Close'].mean()
print("Mar 2013 Mean Closing Price:", Mar2013_mean)
Mar2013.plot(x='Date', y='Close', title='AMD Closing Prices in March 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2013=df.loc[(df['Date'] >= '2013-04-01') & (df['Date'] < '2013-04-30')]
print(Apr2013)
Apr2013_mean=Apr2013['Close'].mean()
print("Apr 2013 Mean Closing Price:", Apr2013_mean)
Apr2013.plot(x='Date', y='Close', title='AMD Closing Prices in April 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2013=df.loc[(df['Date'] >= '2013-05-01') & (df['Date'] < '2013-05-31')]
print(May2013)
May2013_mean=May2013['Close'].mean()
print("May 2013 Mean Closing Price:", May2013_mean)
May2013.plot(x='Date', y='Close', title='AMD Closing Prices in May 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2013=df.loc[(df['Date'] >= '2013-06-01') & (df['Date'] < '2013-06-30')]
print(Jun2013)
Jun2013_mean=Jun2013['Close'].mean()
print("Jun 2013 Mean Closing Price:", Jun2013_mean)
Jun2013.plot(x='Date', y='Close', title='AMD Closing Prices in June 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2013=df.loc[(df['Date'] >= '2013-07-01') & (df['Date'] < '2013-07-31')]
print(Jul2013)
Jul2013_mean=Jul2013['Close'].mean()
print("Jul 2013 Mean Closing Price:", Jul2013_mean)
Jul2013.plot(x='Date', y='Close', title='AMD Closing Prices in July 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2013=df.loc[(df['Date'] >= '2013-08-01') & (df['Date'] < '2013-08-31')]
print(Aug2013)
Aug2013_mean=Aug2013['Close'].mean()
print("Aug 2013 Mean Closing Price:", Aug2013_mean)
Aug2013.plot(x='Date', y='Close', title='AMD Closing Prices in August 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2013=df.loc[(df['Date'] >= '2013-09-01') & (df['Date'] < '2013-09-30')]
print(Sep2013)
Sep2013_mean=Sep2013['Close'].mean()
print("Sep 2013 Mean Closing Price:", Sep2013_mean)
Sep2013.plot(x='Date', y='Close', title='AMD Closing Prices in September 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2013=df.loc[(df['Date'] >= '2013-10-01') & (df['Date'] < '2013-10-31')]
print(Oct2013)
Oct2013_mean=Oct2013['Close'].mean()
print("Oct 2013 Mean Closing Price:", Oct2013_mean)
Oct2013.plot(x='Date', y='Close', title='AMD Closing Prices in October 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2013=df.loc[(df['Date'] >= '2013-11-01') & (df['Date'] < '2013-11-30')]
print(Nov2013)
Nov2013_mean=Nov2013['Close'].mean()
print("Nov 2013 Mean Closing Price:", Nov2013_mean)
Nov2013.plot(x='Date', y='Close', title='AMD Closing Prices in November 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2013=df.loc[(df['Date'] >= '2013-12-01') & (df['Date'] < '2013-12-31')]
print(Dec2013)
Dec2013_mean=Dec2013['Close'].mean()
print("Dec 2013 Mean Closing Price:", Dec2013_mean)
Dec2013.plot(x='Date', y='Close', title='AMD Closing Prices in December 2013')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2014=df.loc[(df['Date'] >= '2014-01-01') & (df['Date'] < '2014-01-31')]
print(Jan2014)
Jan2014_mean=Jan2014['Close'].mean()
print("Jan 2014 Mean Closing Price:", Jan2014_mean)
Jan2014.plot(x='Date', y='Close', title='AMD Closing Prices in January 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2014=df.loc[(df['Date'] >= '2014-02-01') & (df['Date'] < '2014-02-28')]
print(Feb2014)
Feb2014_mean=Feb2014['Close'].mean()
print("Feb 2014 Mean Closing Price:", Feb2014_mean)
Feb2014.plot(x='Date', y='Close', title='AMD Closing Prices in February 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2014=df.loc[(df['Date'] >= '2014-03-01') & (df['Date'] < '2014-03-31')]
print(Mar2014)
Mar2014_mean=Mar2014['Close'].mean()
print("Mar 2014 Mean Closing Price:", Mar2014_mean)
Mar2014.plot(x='Date', y='Close', title='AMD Closing Prices in March 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2014=df.loc[(df['Date'] >= '2014-04-01') & (df['Date'] < '2014-04-30')]
print(Apr2014)
Apr2014_mean=Apr2014['Close'].mean()
print("Apr 2014 Mean Closing Price:", Apr2014_mean)
Apr2014.plot(x='Date', y='Close', title='AMD Closing Prices in April 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2014=df.loc[(df['Date'] >= '2014-05-01') & (df['Date'] < '2014-05-31')]
print(May2014)
May2014_mean=May2014['Close'].mean()
print("May 2014 Mean Closing Price:", May2014_mean)
May2014.plot(x='Date', y='Close', title='AMD Closing Prices in May 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2014=df.loc[(df['Date'] >= '2014-06-01') & (df['Date'] < '2014-06-30')]
print(Jun2014)
Jun2014_mean=Jun2014['Close'].mean()
print("Jun 2014 Mean Closing Price:", Jun2014_mean)
Jun2014.plot(x='Date', y='Close', title='AMD Closing Prices in June 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2014=df.loc[(df['Date'] >= '2014-07-01') & (df['Date'] < '2014-07-31')]
print(Jul2014)
Jul2014_mean=Jul2014['Close'].mean()
print("Jul 2014 Mean Closing Price:", Jul2014_mean)
Jul2014.plot(x='Date', y='Close', title='AMD Closing Prices in July 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2014=df.loc[(df['Date'] >= '2014-08-01') & (df['Date'] < '2014-08-31')]
print(Aug2014)
Aug2014_mean=Aug2014['Close'].mean()
print("Aug 2014 Mean Closing Price:", Aug2014_mean)
Aug2014.plot(x='Date', y='Close', title='AMD Closing Prices in August 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2014=df.loc[(df['Date'] >= '2014-09-01') & (df['Date'] < '2014-09-30')]
print(Sep2014)
Sep2014_mean=Sep2014['Close'].mean()
print("Sep 2014 Mean Closing Price:", Sep2014_mean)
Sep2014.plot(x='Date', y='Close', title='AMD Closing Prices in September 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2014=df.loc[(df['Date'] >= '2014-10-01') & (df['Date'] < '2014-10-31')]
print(Oct2014)
Oct2014_mean=Oct2014['Close'].mean()
print("Oct 2014 Mean Closing Price:", Oct2014_mean)
Oct2014.plot(x='Date', y='Close', title='AMD Closing Prices in October 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2014=df.loc[(df['Date'] >= '2014-11-01') & (df['Date'] < '2014-11-30')]
print(Nov2014)
Nov2014_mean=Nov2014['Close'].mean()
print("Nov 2014 Mean Closing Price:", Nov2014_mean)
Nov2014.plot(x='Date', y='Close', title='AMD Closing Prices in November 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2014=df.loc[(df['Date'] >= '2014-12-01') & (df['Date'] < '2014-12-31')]
print(Dec2014)
Dec2014_mean=Dec2014['Close'].mean()
print("Dec 2014 Mean Closing Price:", Dec2014_mean)
Dec2014.plot(x='Date', y='Close', title='AMD Closing Prices in December 2014')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2015=df.loc[(df['Date'] >= '2015-01-01') & (df['Date'] < '2015-01-31')]
print(Jan2015)
Jan2015_mean=Jan2015['Close'].mean()
print("Jan 2015 Mean Closing Price:", Jan2015_mean)
Jan2015.plot(x='Date', y='Close', title='AMD Closing Prices in January 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2015=df.loc[(df['Date'] >= '2015-02-01') & (df['Date'] < '2015-02-28')]
print(Feb2015)
Feb2015_mean=Feb2015['Close'].mean()
print("Feb 2015 Mean Closing Price:", Feb2015_mean)
Feb2015.plot(x='Date', y='Close', title='AMD Closing Prices in February 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2015=df.loc[(df['Date'] >= '2015-03-01') & (df['Date'] < '2015-03-31')]
print(Mar2015)
Mar2015_mean=Mar2015['Close'].mean()
print("Mar 2015 Mean Closing Price:", Mar2015_mean)
Mar2015.plot(x='Date', y='Close', title='AMD Closing Prices in March 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2015=df.loc[(df['Date'] >= '2015-04-01') & (df['Date'] < '2015-04-30')]
print(Apr2015)
Apr2015_mean=Apr2015['Close'].mean()
print("Apr 2015 Mean Closing Price:", Apr2015_mean)
Apr2015.plot(x='Date', y='Close', title='AMD Closing Prices in April 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2015=df.loc[(df['Date'] >= '2015-05-01') & (df['Date'] < '2015-05-31')]
print(May2015)
May2015_mean=May2015['Close'].mean()
print("May 2015 Mean Closing Price:", May2015_mean)
May2015.plot(x='Date', y='Close', title='AMD Closing Prices in May 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2015=df.loc[(df['Date'] >= '2015-06-01') & (df['Date'] < '2015-06-30')]
print(Jun2015)
Jun2015_mean=Jun2015['Close'].mean()
print("Jun 2015 Mean Closing Price:", Jun2015_mean)
Jun2015.plot(x='Date', y='Close', title='AMD Closing Prices in June 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2015=df.loc[(df['Date'] >= '2015-07-01') & (df['Date'] < '2015-07-31')]
print(Jul2015)
Jul2015_mean=Jul2015['Close'].mean()
print("Jul 2015 Mean Closing Price:", Jul2015_mean)
Jul2015.plot(x='Date', y='Close', title='AMD Closing Prices in July 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2015=df.loc[(df['Date'] >= '2015-08-01') & (df['Date'] < '2015-08-31')]
print(Aug2015)
Aug2015_mean=Aug2015['Close'].mean()
print("Aug 2015 Mean Closing Price:", Aug2015_mean)
Aug2015.plot(x='Date', y='Close', title='AMD Closing Prices in August 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2015=df.loc[(df['Date'] >= '2015-09-01') & (df['Date'] < '2015-09-30')]
print(Sep2015)
Sep2015_mean=Sep2015['Close'].mean()
print("Sep 2015 Mean Closing Price:", Sep2015_mean)
Sep2015.plot(x='Date', y='Close', title='AMD Closing Prices in September 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2015=df.loc[(df['Date'] >= '2015-10-01') & (df['Date'] < '2015-10-31')]
print(Oct2015)
Oct2015_mean=Oct2015['Close'].mean()
print("Oct 2015 Mean Closing Price:", Oct2015_mean)
Oct2015.plot(x='Date', y='Close', title='AMD Closing Prices in October 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2015=df.loc[(df['Date'] >= '2015-11-01') & (df['Date'] < '2015-11-30')]
print(Nov2015)
Nov2015_mean=Nov2015['Close'].mean()
print("Nov 2015 Mean Closing Price:", Nov2015_mean)
Nov2015.plot(x='Date', y='Close', title='AMD Closing Prices in November 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2015=df.loc[(df['Date'] >= '2015-12-01') & (df['Date'] < '2015-12-31')]
print(Dec2015)
Dec2015_mean=Dec2015['Close'].mean()
print("Dec 2015 Mean Closing Price:", Dec2015_mean)
Dec2015.plot(x='Date', y='Close', title='AMD Closing Prices in December 2015')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2016=df.loc[(df['Date'] >= '2016-01-01') & (df['Date'] < '2016-01-31')]
print(Jan2016)
Jan2016_mean=Jan2016['Close'].mean()
print("Jan 2016 Mean Closing Price:", Jan2016_mean)
Jan2016.plot(x='Date', y='Close', title='AMD Closing Prices in January 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2016=df.loc[(df['Date'] >= '2016-02-01') & (df['Date'] < '2016-02-29')]
print(Feb2016)
Feb2016_mean=Feb2016['Close'].mean()
print("Feb 2016 Mean Closing Price:", Feb2016_mean)
Feb2016.plot(x='Date', y='Close', title='AMD Closing Prices in February 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2016=df.loc[(df['Date'] >= '2016-03-01') & (df['Date'] < '2016-03-31')]
print(Mar2016)
Mar2016_mean=Mar2016['Close'].mean()
print("Mar 2016 Mean Closing Price:", Mar2016_mean)
Mar2016.plot(x='Date', y='Close', title='AMD Closing Prices in March 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2016=df.loc[(df['Date'] >= '2016-04-01') & (df['Date'] < '2016-04-30')]
print(Apr2016)
Apr2016_mean=Apr2016['Close'].mean()
print("Apr 2016 Mean Closing Price:", Apr2016_mean)
Apr2016.plot(x='Date', y='Close', title='AMD Closing Prices in April 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2016=df.loc[(df['Date'] >= '2016-05-01') & (df['Date'] < '2016-05-31')]
print(May2016)
May2016_mean=May2016['Close'].mean()
print("May 2016 Mean Closing Price:", May2016_mean)
May2016.plot(x='Date', y='Close', title='AMD Closing Prices in May 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2016=df.loc[(df['Date'] >= '2016-06-01') & (df['Date'] < '2016-06-30')]
print(Jun2016)
Jun2016_mean=Jun2016['Close'].mean()
print("Jun 2016 Mean Closing Price:", Jun2016_mean)
Jun2016.plot(x='Date', y='Close', title='AMD Closing Prices in June 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2016=df.loc[(df['Date'] >= '2016-07-01') & (df['Date'] < '2016-07-31')]
print(Jul2016)
Jul2016_mean=Jul2016['Close'].mean()
print("Jul 2016 Mean Closing Price:", Jul2016_mean)
Jul2016.plot(x='Date', y='Close', title='AMD Closing Prices in July 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2016=df.loc[(df['Date'] >= '2016-08-01') & (df['Date'] < '2016-08-31')]
print(Aug2016)
Aug2016_mean=Aug2016['Close'].mean()
print("Aug 2016 Mean Closing Price:", Aug2016_mean)
Aug2016.plot(x='Date', y='Close', title='AMD Closing Prices in August 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2016=df.loc[(df['Date'] >= '2016-09-01') & (df['Date'] < '2016-09-30')]
print(Sep2016)
Sep2016_mean=Sep2016['Close'].mean()
print("Sep 2016 Mean Closing Price:", Sep2016_mean)
Sep2016.plot(x='Date', y='Close', title='AMD Closing Prices in September 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2016=df.loc[(df['Date'] >= '2016-10-01') & (df['Date'] < '2016-10-31')]
print(Oct2016)
Oct2016_mean=Oct2016['Close'].mean()
print("Oct 2016 Mean Closing Price:", Oct2016_mean)
Oct2016.plot(x='Date', y='Close', title='AMD Closing Prices in October 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2016=df.loc[(df['Date'] >= '2016-11-01') & (df['Date'] < '2016-11-30')]
print(Nov2016)
Nov2016_mean=Nov2016['Close'].mean()
print("Nov 2016 Mean Closing Price:", Nov2016_mean)
Nov2016.plot(x='Date', y='Close', title='AMD Closing Prices in November 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2016=df.loc[(df['Date'] >= '2016-12-01') & (df['Date'] < '2016-12-31')]
print(Dec2016)
Dec2016_mean=Dec2016['Close'].mean()
print("Dec 2016 Mean Closing Price:", Dec2016_mean)
Dec2016.plot(x='Date', y='Close', title='AMD Closing Prices in December 2016')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2017=df.loc[(df['Date'] >= '2017-01-01') & (df['Date'] < '2017-01-31')]
print(Jan2017)
Jan2017_mean=Jan2017['Close'].mean()
print("Jan 2017 Mean Closing Price:", Jan2017_mean)
Jan2017.plot(x='Date', y='Close', title='AMD Closing Prices in January 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2017=df.loc[(df['Date'] >= '2017-02-01') & (df['Date'] < '2017-02-28')]
print(Feb2017)
Feb2017_mean=Feb2017['Close'].mean()
print("Feb 2017 Mean Closing Price:", Feb2017_mean)
Feb2017.plot(x='Date', y='Close', title='AMD Closing Prices in February 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2017=df.loc[(df['Date'] >= '2017-03-01') & (df['Date'] < '2017-03-31')]
print(Mar2017)
Mar2017_mean=Mar2017['Close'].mean()
print("Mar 2017 Mean Closing Price:", Mar2017_mean)
Mar2017.plot(x='Date', y='Close', title='AMD Closing Prices in March 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2017=df.loc[(df['Date'] >= '2017-04-01') & (df['Date'] < '2017-04-30')]
print(Apr2017)
Apr2017_mean=Apr2017['Close'].mean()
print("Apr 2017 Mean Closing Price:", Apr2017_mean)
Apr2017.plot(x='Date', y='Close', title='AMD Closing Prices in April 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2017=df.loc[(df['Date'] >= '2017-05-01') & (df['Date'] < '2017-05-31')]
print(May2017)
May2017_mean=May2017['Close'].mean()
print("May 2017 Mean Closing Price:", May2017_mean)
May2017.plot(x='Date', y='Close', title='AMD Closing Prices in May 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2017=df.loc[(df['Date'] >= '2017-06-01') & (df['Date'] < '2017-06-30')]
print(Jun2017)
Jun2017_mean=Jun2017['Close'].mean()
print("Jun 2017 Mean Closing Price:", Jun2017_mean)
Jun2017.plot(x='Date', y='Close', title='AMD Closing Prices in June 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2017=df.loc[(df['Date'] >= '2017-07-01') & (df['Date'] < '2017-07-31')]
print(Jul2017)
Jul2017_mean=Jul2017['Close'].mean()
print("Jul 2017 Mean Closing Price:", Jul2017_mean)
Jul2017.plot(x='Date', y='Close', title='AMD Closing Prices in July 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2017=df.loc[(df['Date'] >= '2017-08-01') & (df['Date'] < '2017-08-31')]
print(Aug2017)
Aug2017_mean=Aug2017['Close'].mean()
print("Aug 2017 Mean Closing Price:", Aug2017_mean)
Aug2017.plot(x='Date', y='Close', title='AMD Closing Prices in August 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2017=df.loc[(df['Date'] >= '2017-09-01') & (df['Date'] < '2017-09-30')]
print(Sep2017)
Sep2017_mean=Sep2017['Close'].mean()
print("Sep 2017 Mean Closing Price:", Sep2017_mean)
Sep2017.plot(x='Date', y='Close', title='AMD Closing Prices in September 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2017=df.loc[(df['Date'] >= '2017-10-01') & (df['Date'] < '2017-10-31')]
print(Oct2017)
Oct2017_mean=Oct2017['Close'].mean()
print("Oct 2017 Mean Closing Price:", Oct2017_mean)
Oct2017.plot(x='Date', y='Close', title='AMD Closing Prices in October 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2017=df.loc[(df['Date'] >= '2017-11-01') & (df['Date'] < '2017-11-31')]
print(Nov2017)
Nov2017_mean=Nov2017['Close'].mean()
print("Nov 2017 Mean Closing Price:", Nov2017_mean)
Nov2017.plot(x='Date', y='Close', title='AMD Closing Prices in November 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2017=df.loc[(df['Date'] >= '2017-12-01') & (df['Date'] < '2017-12-31')]
print(Dec2017)
Dec2017_mean=Dec2017['Close'].mean()
print("Dec 2017 Mean Closing Price:", Dec2017_mean)
Dec2017.plot(x='Date', y='Close', title='AMD Closing Prices in December 2017')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2018=df.loc[(df['Date'] >= '2018-01-01') & (df['Date'] < '2018-01-31')]
print(Jan2018)
Jan2018_mean=Jan2018['Close'].mean()
print("Jan 2018 Mean Closing Price:", Jan2018_mean)
Jan2018.plot(x='Date', y='Close', title='AMD Closing Prices in January 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2018=df.loc[(df['Date'] >= '2018-02-01') & (df['Date'] < '2018-02-28')]
print(Feb2018)
Feb2018_mean=Feb2018['Close'].mean()
print("Feb 2018 Mean Closing Price:", Feb2018_mean)
Feb2018.plot(x='Date', y='Close', title='AMD Closing Prices in February 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2018=df.loc[(df['Date'] >= '2018-03-01') & (df['Date'] < '2018-03-31')]
print(Mar2018)
Mar2018_mean=Mar2018['Close'].mean()
print("Mar 2018 Mean Closing Price:", Mar2018_mean)
Mar2018.plot(x='Date', y='Close', title='AMD Closing Prices in March 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2018=df.loc[(df['Date'] >= '2018-04-01') & (df['Date'] < '2018-04-30')]
print(Apr2018)
Apr2018_mean=Apr2018['Close'].mean()
print("Apr 2018 Mean Closing Price:", Apr2018_mean)
Apr2018.plot(x='Date', y='Close', title='AMD Closing Prices in April 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2018=df.loc[(df['Date'] >= '2018-05-01') & (df['Date'] < '2018-05-31')]
print(May2018)
May2018_mean=May2018['Close'].mean()
print("May 2018 Mean Closing Price:", May2018_mean)
May2018.plot(x='Date', y='Close', title='AMD Closing Prices in May 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2018=df.loc[(df['Date'] >= '2018-06-01') & (df['Date'] < '2018-06-30')]
print(Jun2018)
Jun2018_mean=Jun2018['Close'].mean()
print("Jun 2018 Mean Closing Price:", Jun2018_mean)
Jun2018.plot(x='Date', y='Close', title='AMD Closing Prices in June 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2018=df.loc[(df['Date'] >= '2018-07-01') & (df['Date'] < '2018-07-31')]
print(Jul2018)
Jul2018_mean=Jul2018['Close'].mean()
print("Jul 2018 Mean Closing Price:", Jul2018_mean)
Jul2018.plot(x='Date', y='Close', title='AMD Closing Prices in July 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2018=df.loc[(df['Date'] >= '2018-08-01') & (df['Date'] < '2018-08-31')]
print(Aug2018)
Aug2018_mean=Aug2018['Close'].mean()
print("Aug 2018 Mean Closing Price:", Aug2018_mean)
Aug2018.plot(x='Date', y='Close', title='AMD Closing Prices in August 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2018=df.loc[(df['Date'] >= '2018-09-01') & (df['Date'] < '2018-09-30')]
print(Sep2018)
Sep2018_mean=Sep2018['Close'].mean()
print("Sep 2018 Mean Closing Price:", Sep2018_mean)
Sep2018.plot(x='Date', y='Close', title='AMD Closing Prices in September 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2018=df.loc[(df['Date'] >= '2018-10-01') & (df['Date'] < '2018-10-31')]
print(Oct2018)
Oct2018_mean=Oct2018['Close'].mean()
print("Oct 2018 Mean Closing Price:", Oct2018_mean)
Oct2018.plot(x='Date', y='Close', title='AMD Closing Prices in October 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2018=df.loc[(df['Date'] >= '2018-11-01') & (df['Date'] < '2018-11-30')]
print(Nov2018)
Nov2018_mean=Nov2018['Close'].mean()
print("Nov 2018 Mean Closing Price:", Nov2018_mean)
Nov2018.plot(x='Date', y='Close', title='AMD Closing Prices in November 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2018=df.loc[(df['Date'] >= '2018-12-01') & (df['Date'] < '2018-12-31')]
print(Dec2018)
Dec2018_mean=Dec2018['Close'].mean()
print("Dec 2018 Mean Closing Price:", Dec2018_mean)
Dec2018.plot(x='Date', y='Close', title='AMD Closing Prices in December 2018')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2019=df.loc[(df['Date'] >= '2019-01-01') & (df['Date'] < '2019-01-31')]
print(Jan2019)
Jan2019_mean=Jan2019['Close'].mean()
print("Jan 2019 Mean Closing Price:", Jan2019_mean)
Jan2019.plot(x='Date', y='Close', title='AMD Closing Prices in January 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2019=df.loc[(df['Date'] >= '2019-02-01') & (df['Date'] < '2019-02-28')]
print(Feb2019)
Feb2019_mean=Feb2019['Close'].mean()
print("Feb 2019 Mean Closing Price:", Feb2019_mean)
Feb2019.plot(x='Date', y='Close', title='AMD Closing Prices in February 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2019=df.loc[(df['Date'] >= '2019-03-01') & (df['Date'] < '2019-03-31')]
print(Mar2019)
Mar2019_mean=Mar2019['Close'].mean()
print("Mar 2019 Mean Closing Price:", Mar2019_mean)
Mar2019.plot(x='Date', y='Close', title='AMD Closing Prices in March 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2019=df.loc[(df['Date'] >= '2019-04-01') & (df['Date'] < '2019-04-30')]
print(Apr2019)
Apr2019_mean=Apr2019['Close'].mean()
print("Apr 2019 Mean Closing Price:", Apr2019_mean)
Apr2019.plot(x='Date', y='Close', title='AMD Closing Prices in April 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2019=df.loc[(df['Date'] >= '2019-05-01') & (df['Date'] < '2019-05-31')]
print(May2019)
May2019_mean=May2019['Close'].mean()
print("May 2019 Mean Closing Price:", May2019_mean)
May2019.plot(x='Date', y='Close', title='AMD Closing Prices in May 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2019=df.loc[(df['Date'] >= '2019-06-01') & (df['Date'] < '2019-06-30')]
print(Jun2019)
Jun2019_mean=Jun2019['Close'].mean()
print("Jun 2019 Mean Closing Price:", Jun2019_mean)
Jun2019.plot(x='Date', y='Close', title='AMD Closing Prices in June 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2019=df.loc[(df['Date'] >= '2019-07-01') & (df['Date'] < '2019-07-31')]
print(Jul2019)
Jul2019_mean=Jul2019['Close'].mean()
print("Jul 2019 Mean Closing Price:", Jul2019_mean)
Jul2019.plot(x='Date', y='Close', title='AMD Closing Prices in July 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2019=df.loc[(df['Date'] >= '2019-08-01') & (df['Date'] < '2019-08-31')]
print(Aug2019)
Aug2019_mean=Aug2019['Close'].mean()
print("Aug 2019 Mean Closing Price:", Aug2019_mean)
Aug2019.plot(x='Date', y='Close', title='AMD Closing Prices in August 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2019=df.loc[(df['Date'] >= '2019-09-01') & (df['Date'] < '2019-09-30')]
print(Sep2019)
Sep2019_mean=Sep2019['Close'].mean()
print("Sep 2019 Mean Closing Price:", Sep2019_mean)
Sep2019.plot(x='Date', y='Close', title='AMD Closing Prices in September 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2019=df.loc[(df['Date'] >= '2019-10-01') & (df['Date'] < '2019-10-31')]
print(Oct2019)
Oct2019_mean=Oct2019['Close'].mean()
print("Oct 2019 Mean Closing Price:", Oct2019_mean)
Oct2019.plot(x='Date', y='Close', title='AMD Closing Prices in October 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2019=df.loc[(df['Date'] >= '2019-11-01') & (df['Date'] < '2019-11-31')]
print(Nov2019)
Nov2019_mean=Nov2019['Close'].mean()
print("Nov 2019 Mean Closing Price:", Nov2019_mean)
Nov2019.plot(x='Date', y='Close', title='AMD Closing Prices in November 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2019=df.loc[(df['Date'] >= '2019-12-01') & (df['Date'] < '2019-12-31')]
print(Dec2019)
Dec2019_mean=Dec2019['Close'].mean()
print("Dec 2019 Mean Closing Price:", Dec2019_mean)
Dec2019.plot(x='Date', y='Close', title='AMD Closing Prices in December 2019')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2020=df.loc[(df['Date'] >= '2020-01-01') & (df['Date'] < '2020-01-31')]
print(Jan2020)
Jan2020_mean=Jan2020['Close'].mean()
print("Jan 2020 Mean Closing Price:", Jan2020_mean)
Jan2020.plot(x='Date', y='Close', title='AMD Closing Prices in January 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2020=df.loc[(df['Date'] >= '2020-02-01') & (df['Date'] < '2020-02-29')]
print(Feb2020)
Feb2020_mean=Feb2020['Close'].mean()
print("Feb 2020 Mean Closing Price:", Feb2020_mean)
Feb2020.plot(x='Date', y='Close', title='AMD Closing Prices in February 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2020=df.loc[(df['Date'] >= '2020-03-01') & (df['Date'] < '2020-03-31')]
print(Mar2020)
Mar2020_mean=Mar2020['Close'].mean()
print("Mar 2020 Mean Closing Price:", Mar2020_mean)
Mar2020.plot(x='Date', y='Close', title='AMD Closing Prices in March 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2020=df.loc[(df['Date'] >= '2020-04-01') & (df['Date'] < '2020-04-30')]
print(Apr2020)
Apr2020_mean=Apr2020['Close'].mean()
print("Apr 2020 Mean Closing Price:", Apr2020_mean)
Apr2020.plot(x='Date', y='Close', title='AMD Closing Prices in April 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2020=df.loc[(df['Date'] >= '2020-05-01') & (df['Date'] < '2020-05-31')]
print(May2020)
May2020_mean=May2020['Close'].mean()
print("May 2020 Mean Closing Price:", May2020_mean)
May2020.plot(x='Date', y='Close', title='AMD Closing Prices in May 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2020=df.loc[(df['Date'] >= '2020-06-01') & (df['Date'] < '2020-06-30')]
print(Jun2020)
Jun2020_mean=Jun2020['Close'].mean()
print("Jun 2020 Mean Closing Price:", Jun2020_mean)
Jun2020.plot(x='Date', y='Close', title='AMD Closing Prices in June 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2020=df.loc[(df['Date'] >= '2020-07-01') & (df['Date'] < '2020-07-31')]
print(Jul2020)
Jul2020_mean=Jul2020['Close'].mean()
print("Jul 2020 Mean Closing Price:", Jul2020_mean)
Jul2020.plot(x='Date', y='Close', title='AMD Closing Prices in July 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2020=df.loc[(df['Date'] >= '2020-08-01') & (df['Date'] < '2020-08-31')]
print(Aug2020)
Aug2020_mean=Aug2020['Close'].mean()
print("Aug 2020 Mean Closing Price:", Aug2020_mean)
Aug2020.plot(x='Date', y='Close', title='AMD Closing Prices in August 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2020=df.loc[(df['Date'] >= '2020-09-01') & (df['Date'] < '2020-09-30')]
print(Sep2020)
Sep2020_mean=Sep2020['Close'].mean()
print("Sep 2020 Mean Closing Price:", Sep2020_mean)
Sep2020.plot(x='Date', y='Close', title='AMD Closing Prices in September 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2020=df.loc[(df['Date'] >= '2020-10-01') & (df['Date'] < '2020-10-31')]
print(Oct2020)
Oct2020_mean=Oct2020['Close'].mean()
print("Oct 2020 Mean Closing Price:",Oct2020_mean)
Oct2020.plot(x='Date', y='Close', title='AMD Closing Prices in October 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2020=df.loc[(df['Date'] >= '2020-11-01') & (df['Date'] < '2020-11-30')]
print(Nov2020)
Nov2020_mean=Nov2020['Close'].mean()
print("Nov 2020 Mean Closing Price:", Nov2020_mean)
Nov2020.plot(x='Date', y='Close', title='AMD Closing Prices in November 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2020=df.loc[(df['Date'] >= '2020-12-01') & (df['Date'] < '2020-12-31')]
print(Dec2020)
Dec2020_mean=Dec2020['Close'].mean()
print("Dec 2020 Mean Closing Price:", Dec2020_mean)
Dec2020.plot(x='Date', y='Close', title='AMD Closing Prices in December 2020')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2021=df.loc[(df['Date'] >= '2021-01-01') & (df['Date'] < '2021-01-31')]
print(Jan2021)
Jan2021_mean=Jan2021['Close'].mean()
print("Jan 2021 Mean Closing Price:", Jan2021_mean)
Jan2021.plot(x='Date', y='Close', title='AMD Closing Prices in January 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2021=df.loc[(df['Date'] >= '2021-02-01') & (df['Date'] < '2021-02-28')]
print(Feb2021)
Feb2021_mean=Feb2021['Close'].mean()
print("Feb2021 Mean Closing Price:", Feb2021_mean)
Feb2021.plot(x='Date', y='Close', title='AMD Closing Prices in February 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2021=df.loc[(df['Date'] >= '2021-03-01') & (df['Date'] < '2021-03-31')]
print(Mar2021)
Mar2021_mean=Mar2021['Close'].mean()
print("Mar 2021 Mean Closing Price:", Mar2021_mean)
Mar2021.plot(x='Date', y='Close', title='AMD Closing Prices in March 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2021=df.loc[(df['Date'] >= '2021-04-01') & (df['Date'] < '2021-04-30')]
print(Apr2021)
Apr2021_mean=Apr2021['Close'].mean()
print("Apr 2021 Mean Closing Price:", Apr2021_mean)
Apr2021.plot(x='Date', y='Close', title='AMD Closing Prices in April 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2021=df.loc[(df['Date'] >= '2021-05-01') & (df['Date'] < '2021-05-31')]
print(May2021)
May2021_mean=May2021['Close'].mean()
print("May 2021 Mean Closing Price:", May2021_mean)
May2021.plot(x='Date', y='Close', title='AMD Closing Prices in May 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2021=df.loc[(df['Date'] >= '2021-06-01') & (df['Date'] < '2021-06-30')]
print(Jun2021)
Jun2021_mean=Jun2021['Close'].mean()
print("Jun 2021 Mean Closing Price:", Jun2021_mean)
Jun2021.plot(x='Date', y='Close', title='AMD Closing Prices in June 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2021=df.loc[(df['Date'] >= '2021-07-01') & (df['Date'] < '2021-07-31')]
print(Jul2021)
Jul2021_mean=Jul2021['Close'].mean()
print("Jul 2021 Mean Closing Price:", Jul2021_mean)
Jul2021.plot(x='Date', y='Close', title='AMD Closing Prices in July 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2021=df.loc[(df['Date'] >= '2021-08-01') & (df['Date'] < '2021-08-31')]
print(Aug2021)
Aug2021_mean=Aug2021['Close'].mean()
print("Aug 2021 Mean Closing Price:", Aug2021_mean)
Aug2021.plot(x='Date', y='Close', title='AMD Closing Prices in August 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2021=df.loc[(df['Date'] >= '2021-09-01') & (df['Date'] < '2021-09-30')]
print(Sep2021)
Sep2021_mean=Sep2021['Close'].mean()
print("Sep 2021 Mean Closing Price:", Sep2021_mean)
Sep2021.plot(x='Date', y='Close', title='AMD Closing Prices in September 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2021=df.loc[(df['Date'] >= '2021-10-01') & (df['Date'] < '2021-10-31')]
print(Oct2021)
Oct2021_mean=Oct2021['Close'].mean()
print("Oct 2021 Mean Closing Price:", Oct2021_mean)
Oct2021.plot(x='Date', y='Close', title='AMD Closing Prices in October 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2021=df.loc[(df['Date'] >= '2021-11-01') & (df['Date'] < '2021-11-30')]
print(Nov2021)
Nov2021_mean=Nov2021['Close'].mean()
print("Nov 2021 Mean Closing Price:", Nov2021_mean)
Nov2021.plot(x='Date', y='Close', title='AMD Closing Prices in November 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2021=df.loc[(df['Date'] >= '2021-12-01') & (df['Date'] < '2021-12-31')]
print(Dec2021)
Dec2021_mean=Dec2021['Close'].mean()
print("Dec 2021 Mean Closing Price:", Dec2021_mean)
Dec2021.plot(x='Date', y='Close', title='AMD Closing Prices in December 2021')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2022=df.loc[(df['Date'] >= '2022-01-01') & (df['Date'] < '2022-01-31')]
print(Jan2022)
Jan2022_mean=Jan2022['Close'].mean()
print("Jan 2022 Mean Closing Price:", Jan2022_mean)
Jan2022.plot(x='Date', y='Close', title='AMD Closing Prices in January 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2022=df.loc[(df['Date'] >= '2022-02-01') & (df['Date'] < '2022-02-28')]
print(Feb2022)
Feb2022_mean=Feb2022['Close'].mean()
print("Feb 2022 Mean Closing Price:", Feb2022_mean)
Feb2022.plot(x='Date', y='Close', title='AMD Closing Prices in February 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2022=df.loc[(df['Date'] >= '2022-03-01') & (df['Date'] < '2022-03-31')]
print(Mar2022)
Mar2022_mean=Mar2022['Close'].mean()
print("Mar 2022 Mean Closing Price:", Mar2022_mean)
Mar2022.plot(x='Date', y='Close', title='AMD Closing Prices in March 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2022=df.loc[(df['Date'] >= '2022-04-01') & (df['Date'] < '2022-04-30')]
print(Apr2022)
Apr2022_mean=Apr2022['Close'].mean()
print("Apr 2022 Mean Closing Price:", Apr2022_mean)
Apr2022.plot(x='Date', y='Close', title='AMD Closing Prices in April 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2022=df.loc[(df['Date'] >= '2022-05-01') & (df['Date'] < '2022-05-31')]
print(May2022)
May2022_mean=May2022['Close'].mean()
print("May 2022 Mean Closing Price:", May2022_mean)
May2022.plot(x='Date', y='Close', title='AMD Closing Prices in May 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2022=df.loc[(df['Date'] >= '2022-06-01') & (df['Date'] < '2022-06-30')]
print(Jun2022)
Jun2022_mean=Jun2022['Close'].mean()
print("Jun 2022 Mean Closing Price:", Jun2022_mean)
Jun2022.plot(x='Date', y='Close', title='AMD Closing Prices in June 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2022=df.loc[(df['Date'] >= '2022-07-01') & (df['Date'] < '2022-07-31')]
print(Jul2022)
Jul2022_mean=Jul2022['Close'].mean()
print("Jul 2022 Mean Closing Price:", Jul2022_mean)
Jul2022.plot(x='Date', y='Close', title='AMD Closing Prices in July 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2022=df.loc[(df['Date'] >= '2022-08-01') & (df['Date'] < '2022-08-31')]
print(Aug2022)
Aug2022_mean=Aug2022['Close'].mean()
print("Aug 2022 Mean Closing Price:", Aug2022_mean)
Aug2022.plot(x='Date', y='Close', title='AMD Closing Prices in August 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2022=df.loc[(df['Date'] >= '2022-09-01') & (df['Date'] < '2022-09-30')]
print(Sep2022)
Sep2022_mean=Sep2022['Close'].mean()
print("Sep 2022 Mean Closing Price:", Sep2022_mean)
Sep2022.plot(x='Date', y='Close', title='AMD Closing Prices in September 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2022=df.loc[(df['Date'] >= '2022-10-01') & (df['Date'] < '2022-10-31')]
print(Oct2022)
Oct2022_mean=Oct2022['Close'].mean()
print("Oct 2022 Mean Closing Price:", Oct2022_mean)
Oct2022.plot(x='Date', y='Close', title='AMD Closing Prices in October 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2022=df.loc[(df['Date'] >= '2022-11-01') & (df['Date'] < '2022-11-30')]
print(Nov2022)
Nov2022_mean=Nov2022['Close'].mean()
print("Nov 2022 Mean Closing Price:", Nov2022_mean)
Nov2022.plot(x='Date', y='Close', title='AMD Closing Prices in November 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2022=df.loc[(df['Date'] >= '2022-12-01') & (df['Date'] < '2022-12-31')]
print(Dec2022)
Dec2022_mean=Dec2022['Close'].mean()
print("Dec 2022 Mean Closing Price:", Dec2022_mean)
Dec2022.plot(x='Date', y='Close', title='AMD Closing Prices in December 2022')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2023=df.loc[(df['Date'] >= '2023-01-01') & (df['Date'] < '2023-01-31')]
print(Jan2023)
Jan2023_mean=Jan2023['Close'].mean()
print("Jan 2023 Mean Closing Price:", Jan2023_mean)
Jan2023.plot(x='Date', y='Close', title='AMD Closing Prices in January 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2023=df.loc[(df['Date'] >= '2023-02-01') & (df['Date'] < '2023-02-28')]
print(Feb2023)
Feb2023_mean=Feb2023['Close'].mean()
print("Feb 2023 Mean Closing Price:", Feb2023_mean)
Feb2023.plot(x='Date', y='Close', title='AMD Closing Prices in February 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2023=df.loc[(df['Date'] >= '2023-03-01') & (df['Date'] < '2023-03-31')]
print(Mar2023)
Mar2023_mean=Mar2023['Close'].mean()
print("Mar 2023 Mean Closing Price:", Mar2023_mean)
Mar2023.plot(x='Date', y='Close', title='AMD Closing Prices in March 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2023=df.loc[(df['Date'] >= '2023-04-01') & (df['Date'] < '2023-04-30')]
print(Apr2023)
Apr2023_mean=Apr2023['Close'].mean()
print("Apr 2023 Mean Closing Price:", Apr2023_mean)
Apr2023.plot(x='Date', y='Close', title='AMD Closing Prices in April 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2023=df.loc[(df['Date'] >= '2023-05-01') & (df['Date'] < '2023-05-31')]
print(May2023)
May2023_mean=May2023['Close'].mean()
print("May 2023 Mean Closing Price:", May2023_mean)
May2023.plot(x='Date', y='Close', title='AMD Closing Prices in May 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2023=df.loc[(df['Date'] >= '2023-06-01') & (df['Date'] < '2023-06-30')]
print(Jun2023)
Jun2023_mean=Jun2023['Close'].mean()
print("Jun 2023 Mean Closing Price:", Jun2023_mean)
Jun2023.plot(x='Date', y='Close', title='AMD Closing Prices in June 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2023=df.loc[(df['Date'] >= '2023-07-01') & (df['Date'] < '2023-07-31')]
print(Jul2023)
Jul2023_mean=Jul2023['Close'].mean()
print("Jul 2023 Mean Closing Price:", Jul2023_mean)
Jul2023.plot(x='Date', y='Close', title='AMD Closing Prices in July 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2023=df.loc[(df['Date'] >= '2023-08-01') & (df['Date'] < '2023-08-31')]
print(Aug2023)
Aug2023_mean=Aug2023['Close'].mean()
print("Aug 2023 Mean Closing Price:", Aug2023_mean)
Aug2023.plot(x='Date', y='Close', title='AMD Closing Prices in August 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2023=df.loc[(df['Date'] >= '2023-09-01') & (df['Date'] < '2023-09-30')]
print(Sep2023)
Sep2023_mean=Sep2023['Close'].mean()
print("Sep 2023 Mean Closing Price:", Sep2023_mean)
Sep2023.plot(x='Date', y='Close', title='AMD Closing Prices in September 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2023=df.loc[(df['Date'] >= '2023-10-01') & (df['Date'] < '2023-10-31')]
print(Oct2023)
Oct2023_mean=Oct2023['Close'].mean()
print("Oct 2023 Mean Closing Price:", Oct2023_mean)
Oct2023.plot(x='Date', y='Close', title='AMD Closing Prices in October 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2023=df.loc[(df['Date'] >= '2023-11-01') & (df['Date'] < '2023-11-30')]
print(Nov2023)
Nov2023_mean=Nov2023['Close'].mean()
print("Nov 2023 Mean Closing Price:", Nov2023_mean)
Nov2023.plot(x='Date', y='Close', title='AMD Closing Prices in November 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2023=df.loc[(df['Date'] >= '2023-12-01') & (df['Date'] < '2023-12-31')]
print(Dec2023)
Dec2023_mean=Dec2023['Close'].mean()
print("Dec 2023 Mean Closing Price:", Dec2023_mean)
Dec2023.plot(x='Date', y='Close', title='AMD Closing Prices in December 2023')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2024=df.loc[(df['Date'] >= '2024-01-01') & (df['Date'] < '2024-01-31')]
print(Jan2024)
Jan2024_mean=Jan2024['Close'].mean()
print("Jan 2024 Mean Closing Price:", Jan2024_mean)
Jan2024.plot(x='Date', y='Close', title='AMD Closing Prices in January 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2024=df.loc[(df['Date'] >= '2024-02-01') & (df['Date'] < '2024-02-29')]
print(Feb2024)
Feb2024_mean=Feb2024['Close'].mean()
print("Feb 2024 Mean Closing Price:", Feb2024_mean)
Feb2024.plot(x='Date', y='Close', title='AMD Closing Prices in February 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2024=df.loc[(df['Date'] >= '2024-03-01') & (df['Date'] < '2024-03-31')]
print(Mar2024)
Mar2024_mean=Mar2024['Close'].mean()
print("Mar 2024 Mean Closing Price:", Mar2024_mean)
Mar2024.plot(x='Date', y='Close', title='AMD Closing Prices in March 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2024=df.loc[(df['Date'] >= '2024-04-01') & (df['Date'] < '2024-04-30')]
print(Apr2024)
Apr2024_mean=Apr2024['Close'].mean()
print("Apr 2024 Mean Closing Price:", Apr2024_mean)
Apr2024.plot(x='Date', y='Close', title='AMD Closing Prices in April 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2024=df.loc[(df['Date'] >= '2024-05-01') & (df['Date'] < '2024-05-31')]
print(May2024)
May2024_mean=May2024['Close'].mean()
print("May 2024 Mean Closing Price:", May2024_mean)
May2024.plot(x='Date', y='Close', title='AMD Closing Prices in May 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2024=df.loc[(df['Date'] >= '2024-06-01') & (df['Date'] < '2024-06-30')]
print(Jun2024)
Jun2024_mean=Jun2024['Close'].mean()
print("Jun 2024 Mean Closing Price:", Jun2024_mean)
Jun2024.plot(x='Date', y='Close', title='AMD Closing Prices in June 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2024=df.loc[(df['Date'] >= '2024-07-01') & (df['Date'] < '2024-07-31')]
print(Jul2024)
Jul2024_mean=Jul2024['Close'].mean()
print("Jul 2024 Mean Closing Price:", Jul2024_mean)
Jul2024.plot(x='Date', y='Close', title='AMD Closing Prices in July 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2024=df.loc[(df['Date'] >= '2024-08-01') & (df['Date'] < '2024-08-31')]
print(Aug2024)
Aug2024_mean=Aug2024['Close'].mean()
print("Aug 2024 Mean Closing Price:", Aug2024_mean)
Aug2024.plot(x='Date', y='Close', title='AMD Closing Prices in August 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2024=df.loc[(df['Date'] >= '2024-09-01') & (df['Date'] < '2024-09-30')]
print(Sep2024)
Sep2024_mean=Sep2024['Close'].mean()
print("Sep 2024 Mean Closing Price:", Sep2024_mean)
Sep2024.plot(x='Date', y='Close', title='AMD Closing Prices in September 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2024=df.loc[(df['Date'] >= '2024-10-01') & (df['Date'] < '2024-10-31')]
print(Oct2024)
Oct2024_mean=Oct2024['Close'].mean()
print("Oct 2024 Mean Closing Price:", Oct2024_mean)
Oct2024.plot(x='Date', y='Close', title='AMD Closing Prices in October 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2024=df.loc[(df['Date'] >= '2024-11-01') & (df['Date'] < '2024-11-30')]
print(Nov2024)
Nov2024_mean=Nov2024['Close'].mean()
print("Nov 2024 Mean Closing Price:", Nov2024_mean)
Nov2024.plot(x='Date', y='Close', title='AMD Closing Prices in November 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2024=df.loc[(df['Date'] >= '2024-12-01') & (df['Date'] < '2024-12-31')]
print(Dec2024)
Dec2024_mean=Dec2024['Close'].mean()
print("Dec 2024 Mean Closing Price:", Dec2024_mean)
Dec2024.plot(x='Date', y='Close', title='AMD Closing Prices in December 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2025=df.loc[(df['Date'] >= '2025-01-01') & (df['Date'] < '2025-01-31')]
print(Jan2025)
Jan2025_mean=Jan2025['Close'].mean()
print("Jan 2025 Mean Closing Price:", Jan2025_mean)
Jan2025.plot(x='Date', y='Close', title='AMD Closing Prices in January 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2025=df.loc[(df['Date'] >= '2025-02-01') & (df['Date'] < '2025-02-28')]
print(Feb2025)
Feb2025_mean=Feb2025['Close'].mean()
print("Feb 2025 Mean Closing Price:", Feb2025_mean)
Feb2025.plot(x='Date', y='Close', title='AMD Closing Prices in February 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2025=df.loc[(df['Date'] >= '2025-03-01') & (df['Date'] < '2025-03-31')]
print(Mar2025)
Mar2025_mean=Mar2025['Close'].mean()
print("Mar 2025 Mean Closing Price:", Mar2025_mean)
Mar2025.plot(x='Date', y='Close', title='AMD Closing Prices in March 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2025=df.loc[(df['Date'] >= '2025-04-01') & (df['Date'] < '2025-04-30')]
print(Apr2025)
Apr2025_mean=Apr2025['Close'].mean()
print("Apr 2025 Mean Closing Price:", Apr2025_mean)
Apr2025.plot(x='Date', y='Close', title='AMD Closing Prices in April 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2025=df.loc[(df['Date'] >= '2025-05-01') & (df['Date'] < '2025-05-31')]
print(May2025)
May2025_mean=May2025['Close'].mean()
print("May 2025 Mean Closing Price:", May2025_mean)
May2025.plot(x='Date', y='Close', title='AMD Closing Prices in May 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2025=df.loc[(df['Date'] >= '2025-06-01') & (df['Date'] < '2025-06-30')]
print(Jun2025)
Jun2025_mean=Jun2025['Close'].mean()
print("Jun 2025 Mean Closing Price:", Jun2025_mean)
Jun2025.plot(x='Date', y='Close', title='AMD Closing Prices in June 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2025=df.loc[(df['Date'] >= '2025-07-01') & (df['Date'] < '2025-07-31')]
print(Jul2025)
Jul2025_mean=Jul2025['Close'].mean()
print("Jul 2025 Mean Closing Price:", Jul2025_mean)
Jul2025.plot(x='Date', y='Close', title='AMD Closing Prices in July 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2025=df.loc[(df['Date'] >= '2025-08-01') & (df['Date'] < '2025-08-31')]
print(Aug2025)
Aug2025_mean=Aug2025['Close'].mean()
print("Aug 2025 Mean Closing Price:", Aug2025_mean)
Aug2025.plot(x='Date', y='Close', title='AMD Closing Prices in August 2025')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.show()

#Month wise High Prices are mentioned below 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1992=df.loc[(df['Date'] >= '1992-02-01') & (df['Date'] < '1992-02-29')]
print(Feb1992)
Feb1992_mean=Feb1992['High'].mean()
print("Feb 1992 Mean High Price:", Feb1992_mean)
Feb1992.plot(x='Date', y='High', title='AMD High Prices in February 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1992=df.loc[(df['Date'] >= '1992-03-01') & (df['Date'] < '1992-03-31')]
print(Mar1992)
Mar1992_mean=Mar1992['High'].mean()
print("Mar 1992 Mean High Price:", Mar1992_mean)
Mar1992.plot(x='Date', y='High', title='AMD High Prices in March 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1992=df.loc[(df['Date'] >= '1992-04-01') & (df['Date'] < '1992-04-30')]
print(Apr1992)
Apr1992_mean=Apr1992['High'].mean()
print("Apr 1992 Mean High Price:", Apr1992_mean)
Apr1992.plot(x='Date', y='High', title='AMD High Prices in April 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1992=df.loc[(df['Date'] >= '1992-05-01') & (df['Date'] < '1992-05-31')]
print(May1992)
May1992_mean=May1992['High'].mean()
print("May 1992 Mean High Price:", May1992_mean)
May1992.plot(x='Date', y='High', title='AMD High Prices in May 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1992=df.loc[(df['Date'] >= '1992-06-01') & (df['Date'] < '1992-06-30')]
print(Jun1992)
Jun1992_mean=Jun1992['High'].mean()
print("Jun 1992 Mean High Price:", Jun1992_mean)
Jun1992.plot(x='Date', y='High', title='AMD High Prices in June 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1992=df.loc[(df['Date'] >= '1992-07-01') & (df['Date'] < '1992-07-31')]
print(Jul1992)
Jul1992_mean=Jul1992['High'].mean()
print("Jul 1992 Mean High Price:", Jul1992_mean)
Jul1992.plot(x='Date', y='High', title='AMD High Prices in July 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1992=df.loc[(df['Date'] >= '1992-08-01') & (df['Date'] < '1992-08-31')]
print(Aug1992)
Aug1992_mean=Aug1992['High'].mean()
print("Aug 1992 Mean High Price:", Aug1992_mean)
Aug1992.plot(x='Date', y='High', title='AMD High Prices in August 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1992=df.loc[(df['Date'] >= '1992-09-01') & (df['Date'] < '1992-09-30')]
print(Sep1992)
Sep1992_mean=Sep1992['High'].mean()
print("Sep 1992 Mean High Price:", Sep1992_mean)
Sep1992.plot(x='Date', y='High', title='AMD High Prices in September 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1992=df.loc[(df['Date'] >= '1992-10-01') & (df['Date'] < '1992-10-31')]
print(Oct1992)
Oct1992_mean=Oct1992['High'].mean()
print("Oct 1992 Mean High Price:", Oct1992_mean)
Oct1992.plot(x='Date', y='High', title='AMD High Prices in October 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1992=df.loc[(df['Date'] >= '1992-11-01') & (df['Date'] < '1992-11-30')]
print(Nov1992)
Nov1992_mean=Nov1992['High'].mean()
print("Nov 1992 Mean High Price:", Nov1992_mean)
Nov1992.plot(x='Date', y='High', title='AMD High Prices in November 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1992=df.loc[(df['Date'] >= '1992-12-01') & (df['Date'] < '1992-12-31')]
print(Dec1992)
Dec1992_mean=Dec1992['High'].mean()
print("Dec 1992 Mean High Price:", Dec1992_mean)
Dec1992.plot(x='Date', y='High', title='AMD High Prices in December 1992')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1993=df.loc[(df['Date'] >= '1993-01-01') & (df['Date'] < '1993-01-31')]
print(Jan1993)
Jan1993_mean=Jan1993['High'].mean()
print("Jan 1993 Mean High Price:", Jan1993_mean)
Jan1993.plot(x='Date', y='High', title='AMD High Prices in January 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1993=df.loc[(df['Date'] >= '1993-02-01') & (df['Date'] < '1993-02-28')]
print(Feb1993)
Feb1993_mean=Feb1993['High'].mean()
print("Feb 1993 Mean High Price:", Feb1993_mean)
Feb1993.plot(x='Date', y='High', title='AMD High Prices in February 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1993=df.loc[(df['Date'] >= '1993-03-01') & (df['Date'] < '1993-03-31')]
print(Mar1993)
Mar1993_mean=Mar1993['High'].mean()
print("Mar 1993 Mean High Price:", Mar1993_mean)
Mar1993.plot(x='Date', y='High', title='AMD High Prices in March 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1993=df.loc[(df['Date'] >= '1993-04-01') & (df['Date'] < '1993-04-30')]
print(Apr1993)
Apr1993_mean=Apr1993['High'].mean()
print("Apr 1993 Mean High Price:", Apr1993_mean)
Apr1993.plot(x='Date', y='High', title='AMD High Prices in April 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1993=df.loc[(df['Date'] >= '1993-05-01') & (df['Date'] < '1993-05-31')]
print(May1993)
May1993_mean=May1993['High'].mean()
print("May 1993 Mean High Price:", May1993_mean)
May1993.plot(x='Date', y='High', title='AMD High Prices in May 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1993=df.loc[(df['Date'] >= '1993-06-01') & (df['Date'] < '1993-06-30')]
print(Jun1993)
Jun1993_mean=Jun1993['High'].mean()
print("Jun 1993 Mean High Price:", Jun1993_mean)
Jun1993.plot(x='Date', y='High', title='AMD High Prices in June 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1993=df.loc[(df['Date'] >= '1993-07-01') & (df['Date'] < '1993-07-31')]
print(Jul1993)
Jul1993_mean=Jul1993['High'].mean()
print("Jul 1993 Mean High Price:", Jul1993_mean)
Jul1993.plot(x='Date', y='High', title='AMD High Prices in July 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1993=df.loc[(df['Date'] >= '1993-08-01') & (df['Date'] < '1993-08-31')]
print(Aug1993)
Aug1993_mean=Aug1993['High'].mean()
print("Aug 1993 Mean High Price:", Aug1993_mean)
Aug1993.plot(x='Date', y='High', title='AMD High Prices in August 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1993=df.loc[(df['Date'] >= '1993-09-01') & (df['Date'] < '1993-09-30')]
print(Sep1993)
Sep1993_mean=Sep1993['High'].mean()
print("Sep 1993 Mean High Price:", Sep1993_mean)
Sep1993.plot(x='Date', y='High', title='AMD High Prices in September 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1993=df.loc[(df['Date'] >= '1993-10-01') & (df['Date'] < '1993-10-31')]
print(Oct1993)
Oct1993_mean=Oct1993['High'].mean()
print("Oct 1993 Mean High Price:", Oct1993_mean)
Oct1993.plot(x='Date', y='High', title='AMD High Prices in October 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1993=df.loc[(df['Date'] >= '1993-11-01') & (df['Date'] < '1993-11-30')]
print(Nov1993)
Nov1993_mean=Nov1993['High'].mean()
print("Nov 1993 Mean High Price:", Nov1993_mean)
Nov1993.plot(x='Date', y='High', title='AMD High Prices in November 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1993=df.loc[(df['Date'] >= '1993-12-01') & (df['Date'] < '1993-12-31')]
print(Dec1993)
Dec1993_mean=Dec1993['High'].mean()
print("Dec 1993 Mean High Price:", Dec1993_mean)
Dec1993.plot(x='Date', y='High', title='AMD High Prices in December 1993')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1994=df.loc[(df['Date'] >= '1994-01-01') & (df['Date'] < '1994-01-31')]
print(Jan1994)
Jan1994_mean=Jan1994['High'].mean()
print("Jan 1994 Mean High Price:", Jan1994_mean)
Jan1994.plot(x='Date', y='High', title='AMD High Prices in January 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1994=df.loc[(df['Date'] >= '1994-02-01') & (df['Date'] < '1994-02-28')]
print(Feb1994)
Feb1994_mean=Feb1994['High'].mean()
print("Feb 1994 Mean High Price:", Feb1994_mean)
Feb1994.plot(x='Date', y='High', title='AMD High Prices in February 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1994=df.loc[(df['Date'] >= '1994-03-01') & (df['Date'] < '1994-03-31')]
print(Mar1994)
Mar1994_mean=Mar1994['High'].mean()
print("Mar 1994 Mean High Price:", Mar1994_mean)
Mar1994.plot(x='Date', y='High', title='AMD High Prices in March 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1994=df.loc[(df['Date'] >= '1994-04-01') & (df['Date'] < '1994-04-30')]
print(Apr1994)
Apr1994_mean=Apr1994['High'].mean()
print("Apr 1994 Mean High Price:", Apr1994_mean)
Apr1994.plot(x='Date', y='High', title='AMD High Prices in April 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1994=df.loc[(df['Date'] >= '1994-05-01') & (df['Date'] < '1994-05-31')]
print(May1994)
May1994_mean=May1994['High'].mean()
print("May 1994 Mean High Price:", May1994_mean)
May1994.plot(x='Date', y='High', title='AMD High Prices in May 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1994=df.loc[(df['Date'] >= '1994-06-01') & (df['Date'] < '1994-06-30')]
print(Jun1994)
Jun1994_mean=Jun1994['High'].mean()
print("Jun 1994 Mean High Price:", Jun1994_mean)
Jun1994.plot(x='Date', y='High', title='AMD High Prices in June 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1994=df.loc[(df['Date'] >= '1994-07-01') & (df['Date'] < '1994-07-31')]
print(Jul1994)
Jul1994_mean=Jul1994['High'].mean()
print("Jul 1994 Mean High Price:", Jul1994_mean)
Jul1994.plot(x='Date', y='High', title='AMD High Prices in July 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1994=df.loc[(df['Date'] >= '1994-08-01') & (df['Date'] < '1994-08-31')]
print(Aug1994)
Aug1994_mean=Aug1994['High'].mean()
print("Aug 1994 Mean High Price:", Aug1994_mean)
Aug1994.plot(x='Date', y='High', title='AMD High Prices in August 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1994=df.loc[(df['Date'] >= '1994-09-01') & (df['Date'] < '1994-09-30')]
print(Sep1994)
Sep1994_mean=Sep1994['High'].mean()
print("Sep 1994 Mean High Price:", Sep1994_mean)
Sep1994.plot(x='Date', y='High', title='AMD High Prices in September 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1994=df.loc[(df['Date'] >= '1994-10-01') & (df['Date'] < '1994-10-31')]
print(Oct1994)
Oct1994_mean=Oct1994['High'].mean()
print("Oct 1994 Mean High Price:", Oct1994_mean)
Oct1994.plot(x='Date', y='High', title='AMD High Prices in October 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1994=df.loc[(df['Date'] >= '1994-11-01') & (df['Date'] < '1994-11-30')]
print(Nov1994)
Nov1994_mean=Nov1994['High'].mean()
print("Nov 1994 Mean High Price:", Nov1994_mean)
Nov1994.plot(x='Date', y='High', title='AMD High Prices in November 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1994=df.loc[(df['Date'] >= '1994-12-01') & (df['Date'] < '1994-12-31')]
print(Dec1994)
Dec1994_mean=Dec1994['High'].mean()
print("Dec 1994 Mean High Price:", Dec1994_mean)
Dec1994.plot(x='Date', y='High', title='AMD High Prices in December 1994')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1995=df.loc[(df['Date'] >= '1995-01-01') & (df['Date'] < '1995-01-31')]
print(Jan1995)
Jan1995_mean=Jan1995['High'].mean()
print("Jan 1995 Mean High Price:", Jan1995_mean)
Jan1995.plot(x='Date', y='High', title='AMD High Prices in January 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1995=df.loc[(df['Date'] >= '1995-02-01') & (df['Date'] < '1995-02-28')]
print(Feb1995)
Feb1995_mean=Feb1995['High'].mean()
print("Feb 1995 Mean High Price:", Feb1995_mean)
Feb1995.plot(x='Date', y='High', title='AMD High Prices in February 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1995=df.loc[(df['Date'] >= '1995-03-01') & (df['Date'] < '1995-03-31')]
print(Mar1995)
Mar1995_mean=Mar1995['High'].mean()
print("Mar 1995 Mean High Price:", Mar1995_mean)
Mar1995.plot(x='Date', y='High', title='AMD High Prices in March 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1995=df.loc[(df['Date'] >= '1995-04-01') & (df['Date'] < '1995-04-30')]
print(Apr1995)
Apr1995_mean=Apr1995['High'].mean()
print("Apr 1995 Mean High Price:", Apr1995_mean)
Apr1995.plot(x='Date', y='High', title='AMD High Prices in April 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1995=df.loc[(df['Date'] >= '1995-05-01') & (df['Date'] < '1995-05-31')]
print(May1995)
May1995_mean=May1995['High'].mean()
print("May 1995 Mean High Price:", May1995_mean)
May1995.plot(x='Date', y='High', title='AMD High Prices in May 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1995=df.loc[(df['Date'] >= '1995-06-01') & (df['Date'] < '1995-06-30')]
print(Jun1995)
Jun1995_mean=Jun1995['High'].mean()
print("Jun 1995 Mean High Price:", Jun1995_mean)
Jun1995.plot(x='Date', y='High', title='AMD High Prices in June 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1995=df.loc[(df['Date'] >= '1995-06-01') & (df['Date'] < '1995-06-30')]
print(Jul1995)
Jul1995_mean=Jul1995['High'].mean()
print("Jul 1995 Mean High Price:", Jul1995_mean)
Jul1995.plot(x='Date', y='High', title='AMD High Prices in July 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1995=df.loc[(df['Date'] >= '1995-08-01') & (df['Date'] < '1995-08-31')]
print(Aug1995)
Aug1995_mean=Aug1995['High'].mean()
print("Aug 1995 Mean High Price:", Aug1995_mean)
Aug1995.plot(x='Date', y='High', title='AMD High Prices in August 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1995=df.loc[(df['Date'] >= '1995-09-01') & (df['Date'] < '1995-09-30')]
print(Sep1995)
Sep1995_mean=Sep1995['High'].mean()
print("Sep 1995 Mean High Price:", Sep1995_mean)
Sep1995.plot(x='Date', y='High', title='AMD High Prices in September 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1995=df.loc[(df['Date'] >= '1995-10-01') & (df['Date'] < '1995-10-31')]
print(Oct1995)
Oct1995_mean=Oct1995['High'].mean()
print("Oct 1995 Mean High Price:", Oct1995_mean)
Oct1995.plot(x='Date', y='High', title='AMD High Prices in October 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1995=df.loc[(df['Date'] >= '1995-11-01') & (df['Date'] < '1995-11-30')]
print(Nov1995)
Nov1995_mean=Nov1995['High'].mean()
print("Nov 1995 Mean High Price:", Nov1995_mean)
Nov1995.plot(x='Date', y='High', title='AMD High Prices in November 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1995=df.loc[(df['Date'] >= '1995-12-01') & (df['Date'] < '1995-12-31')]
print(Dec1995)
Dec1995_mean=Dec1995['High'].mean()
print("Dec 1995 Mean High Price:", Dec1995_mean)
Dec1995.plot(x='Date', y='High', title='AMD High Prices in December 1995')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1996=df.loc[(df['Date'] >= '1996-01-01') & (df['Date'] < '1996-01-31')]
print(Jan1996)
Jan1996_mean=Jan1996['High'].mean()
print("Jan 1996 Mean High Price:", Jan1996_mean)
Jan1996.plot(x='Date', y='High', title='AMD High Prices in January 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1996=df.loc[(df['Date'] >= '1996-02-01') & (df['Date'] < '1996-02-29')]
print(Feb1996)
Feb1996_mean=Feb1996['High'].mean()
print("Feb 1996 Mean High Price:", Feb1996_mean)
Feb1996.plot(x='Date', y='High', title='AMD High Prices in February 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1996=df.loc[(df['Date'] >= '1996-03-01') & (df['Date'] < '1996-03-31')]
print(Mar1996)
Mar1996_mean=Mar1996['High'].mean()
print("Mar 1996 Mean High Price:", Mar1996_mean)
Mar1996.plot(x='Date', y='High', title='AMD High Prices in March 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1996=df.loc[(df['Date'] >= '1996-04-01') & (df['Date'] < '1996-04-30')]
print(Apr1996)
Apr1996_mean=Apr1996['High'].mean()
print("Apr 1996 Mean High Price:", Apr1996_mean)
Apr1996.plot(x='Date', y='High', title='AMD High Prices in April 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1996=df.loc[(df['Date'] >= '1996-05-01') & (df['Date'] < '1996-05-31')]
print(May1996)
May1996_mean=May1996['High'].mean()
print("May 1996 Mean High Price:", May1996_mean)
May1996.plot(x='Date', y='High', title='AMD High Prices in May 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1996=df.loc[(df['Date'] >= '1996-06-01') & (df['Date'] < '1996-06-30')]
print(Jun1996)
Jun1996_mean=Jun1996['High'].mean()
print("Jun 1996 Mean High Price:", Jun1996_mean)
Jun1996.plot(x='Date', y='High', title='AMD High Prices in June 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1996=df.loc[(df['Date'] >= '1996-07-01') & (df['Date'] < '1996-07-31')]
print(Jul1996)
Jul1996_mean=Jul1996['High'].mean()
print("Jul 1996 Mean High Price:", Jul1996_mean)
Jul1996.plot(x='Date', y='High', title='AMD High Prices in July 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1996=df.loc[(df['Date'] >= '1996-08-01') & (df['Date'] < '1996-08-31')]
print(Aug1996)
Aug1996_mean=Aug1996['High'].mean()
print("Aug 1996 Mean High Price:", Aug1996_mean)
Aug1996.plot(x='Date', y='High', title='AMD High Prices in August 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1996=df.loc[(df['Date'] >= '1996-09-01') & (df['Date'] < '1996-09-30')]
print(Sep1996)
Sep1996_mean=Sep1996['High'].mean()
print("Sep 1996 Mean High Price:", Sep1996_mean)
Sep1996.plot(x='Date', y='High', title='AMD High Prices in September 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1996=df.loc[(df['Date'] >= '1996-10-01') & (df['Date'] < '1996-10-31')]
print(Oct1996)
Oct1996_mean=Oct1996['High'].mean()
print("Oct 1996 Mean High Price:", Oct1996_mean)
Oct1996.plot(x='Date', y='High', title='AMD High Prices in October 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1996=df.loc[(df['Date'] >= '1996-11-01') & (df['Date'] < '1996-11-30')]
print(Nov1996)
Nov1996_mean=Nov1996['High'].mean()
print("Nov 1996 Mean High Price:", Nov1996_mean)
Nov1996.plot(x='Date', y='High', title='AMD High Prices in November 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1996=df.loc[(df['Date'] >= '1996-12-01') & (df['Date'] < '1996-12-31')]
print(Dec1996)
Dec1996_mean=Dec1996['High'].mean()
print("Dec 1996 Mean High Price:", Dec1996_mean)
Dec1996.plot(x='Date', y='High', title='AMD High Prices in December 1996')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1997=df.loc[(df['Date'] >= '1997-01-01') & (df['Date'] < '1997-01-31')]
print(Jan1997)
Jan1997_mean=Jan1997['High'].mean()
print("Jan 1997 Mean High Price:", Jan1997_mean)
Jan1997.plot(x='Date', y='High', title='AMD High Prices in January 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1997=df.loc[(df['Date'] >= '1997-02-01') & (df['Date'] < '1997-02-28')]
print(Feb1997)
Feb1997_mean=Feb1997['High'].mean()
print("Feb 1997 Mean High Price:", Feb1997_mean)
Feb1997.plot(x='Date', y='High', title='AMD High Prices in February 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1997=df.loc[(df['Date'] >= '1997-03-01') & (df['Date'] < '1997-03-31')]
print(Mar1997)
Mar1997_mean=Mar1997['High'].mean()
print("Mar 1997 Mean High Price:", Mar1997_mean)
Mar1997.plot(x='Date', y='High', title='AMD High Prices in March 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1997=df.loc[(df['Date'] >= '1997-04-01') & (df['Date'] < '1997-04-30')]
print(Apr1997)
Apr1997_mean=Apr1997['High'].mean()
print("Apr 1997 Mean High Price:", Apr1997_mean)
Apr1997.plot(x='Date', y='High', title='AMD High Prices in April 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1997=df.loc[(df['Date'] >= '1997-05-01') & (df['Date'] < '1997-05-31')]
print(May1997)
May1997_mean=May1997['High'].mean()
print("May 1997 Mean High Price:", May1997_mean)
May1997.plot(x='Date', y='High', title='AMD High Prices in May 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1997=df.loc[(df['Date'] >= '1997-06-01') & (df['Date'] < '1997-06-30')]
print(Jun1997)
Jun1997_mean=Jun1997['High'].mean()
print("Jun 1997 Mean High Price:", Jun1997_mean)
Jun1997.plot(x='Date', y='High', title='AMD High Prices in June 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1997=df.loc[(df['Date'] >= '1997-07-01') & (df['Date'] < '1997-07-31')]
print(Jul1997)
Jul1997_mean=Jul1997['High'].mean()
print("Jul 1997 Mean High Price:", Jul1997_mean)
Jul1997.plot(x='Date', y='High', title='AMD High Prices in July 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1997=df.loc[(df['Date'] >= '1997-08-01') & (df['Date'] < '1997-08-31')]
print(Aug1997)
Aug1997_mean=Aug1997['High'].mean()
print("Aug 1997 Mean High Price:", Aug1997_mean)
Aug1997.plot(x='Date', y='High', title='AMD High Prices in August 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1997=df.loc[(df['Date'] >= '1997-09-01') & (df['Date'] < '1997-09-30')]
print(Sep1997)
Sep1997_mean=Sep1997['High'].mean()
print("Sep 1997 Mean High Price:", Sep1997_mean)
Sep1997.plot(x='Date', y='High', title='AMD High Prices in September 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1997=df.loc[(df['Date'] >= '1997-10-01') & (df['Date'] < '1997-10-31')]
print(Oct1997)
Oct1997_mean=Oct1997['High'].mean()
print("Oct 1997 Mean High Price:", Oct1997_mean)
Oct1997.plot(x='Date', y='High', title='AMD High Prices in October 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1997=df.loc[(df['Date'] >= '1997-11-01') & (df['Date'] < '1997-11-30')]
print(Nov1997)
Nov1997_mean=Nov1997['High'].mean()
print("Nov 1997 Mean High Price:", Nov1997_mean)
Nov1997.plot(x='Date', y='High', title='AMD High Prices in November 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1997=df.loc[(df['Date'] >= '1997-12-01') & (df['Date'] < '1997-12-31')]
print(Dec1997)
Dec1997_mean=Dec1997['High'].mean()
print("Dec 1997 Mean High Price:", Dec1997_mean)
Dec1997.plot(x='Date', y='High', title='AMD High Prices in December 1997')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1998=df.loc[(df['Date'] >= '1998-01-01') & (df['Date'] < '1998-01-31')]
print(Jan1998)
Jan1998_mean=Jan1998['High'].mean()
print("Jan 1998 Mean High Price:", Jan1998_mean)
Jan1998.plot(x='Date', y='High', title='AMD High Prices in January 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1998=df.loc[(df['Date'] >= '1998-02-01') & (df['Date'] < '1998-02-28')]
print(Feb1998)
Feb1998_mean=Feb1998['High'].mean()
print("Feb 1998 Mean High Price:", Feb1998_mean)
Feb1998.plot(x='Date', y='High', title='AMD High Prices in February 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1998=df.loc[(df['Date'] >= '1998-03-01') & (df['Date'] < '1998-03-31')]
print(Mar1998)
Mar1998_mean=Mar1998['High'].mean()
print("Mar 1998 Mean High Price:", Mar1998_mean)
Mar1998.plot(x='Date', y='High', title='AMD High Prices in March 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1998=df.loc[(df['Date'] >= '1998-04-01') & (df['Date'] < '1998-04-30')]
print(Apr1998)
Apr1998_mean=Apr1998['High'].mean()
print("Apr 1998 Mean High Price:", Apr1998_mean)
Apr1998.plot(x='Date', y='High', title='AMD High Prices in April 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1998=df.loc[(df['Date'] >= '1998-05-01') & (df['Date'] < '1998-05-31')]
print(May1998)
May1998_mean=May1998['High'].mean()
print("May 1998 Mean High Price:", May1998_mean)
May1998.plot(x='Date', y='High', title='AMD High Prices in May 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1998=df.loc[(df['Date'] >= '1998-06-01') & (df['Date'] < '1998-06-30')]
print(Jun1998)
Jun1998_mean=Jun1998['High'].mean()
print("Jun 1998 Mean High Price:", Jun1998_mean)
Jun1998.plot(x='Date', y='High', title='AMD High Prices in June 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1998=df.loc[(df['Date'] >= '1998-07-01') & (df['Date'] < '1998-07-31')]
print(Jul1998)
Jul1998_mean=Jul1998['High'].mean()
print("Jul 1998 Mean High Price:", Jul1998_mean)
Jul1998.plot(x='Date', y='High', title='AMD High Prices in July 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1998=df.loc[(df['Date'] >= '1998-08-01') & (df['Date'] < '1998-08-31')]
print(Aug1998)
Aug1998_mean=Aug1998['High'].mean()
print("Aug 1998 Mean High Price:", Aug1998_mean)
Aug1998.plot(x='Date', y='High', title='AMD High Prices in August 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1998=df.loc[(df['Date'] >= '1998-09-01') & (df['Date'] < '1998-09-30')]
print(Sep1998)
Sep1998_mean=Sep1998['High'].mean()
print("Sep 1998 Mean High Price:", Jan1998_mean)
Sep1998.plot(x='Date', y='High', title='AMD High Prices in September 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1998=df.loc[(df['Date'] >= '1998-10-01') & (df['Date'] < '1998-10-31')]
print(Oct1998)
Oct1998_mean=Oct1998['High'].mean()
print("Oct 1998 Mean High Price:", Oct1998_mean)
Oct1998.plot(x='Date', y='High', title='AMD High Prices in October 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1998=df.loc[(df['Date'] >= '1998-11-01') & (df['Date'] < '1998-11-30')]
print(Nov1998)
Nov1998_mean=Nov1998['High'].mean()
print("Nov 1998 Mean High Price:", Nov1998_mean)
Nov1998.plot(x='Date', y='High', title='AMD High Prices in November 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1998=df.loc[(df['Date'] >= '1998-12-01') & (df['Date'] < '1998-12-31')]
print(Dec1998)
Dec1998_mean=Dec1998['High'].mean()
print("Dec 1998 Mean High Price:", Dec1998_mean)
Dec1998.plot(x='Date', y='High', title='AMD High Prices in December 1998')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1999=df.loc[(df['Date'] >= '1999-01-01') & (df['Date'] < '1999-01-31')]
print(Jan1999)
Jan1999_mean=Jan1999['High'].mean()
print("Jan 1999 Mean High Price:", Jan1999_mean)
Jan1999.plot(x='Date', y='High', title='AMD High Prices in January 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1999=df.loc[(df['Date'] >= '1999-02-01') & (df['Date'] < '1999-02-28')]
print(Feb1999)
Feb1999_mean=Feb1999['High'].mean()
print("Feb 1999 Mean High Price:", Feb1999_mean)
Feb1999.plot(x='Date', y='High', title='AMD High Prices in February 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1999=df.loc[(df['Date'] >= '1999-03-01') & (df['Date'] < '1999-03-31')]
print(Mar1999)
Mar1999_mean=Mar1999['High'].mean()
print("Mar 1999 Mean High Price:", Mar1999_mean)
Mar1999.plot(x='Date', y='High', title='AMD High Prices in March 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1999=df.loc[(df['Date'] >= '1999-04-01') & (df['Date'] < '1999-04-30')]
print(Apr1999)
Apr1999_mean=Apr1999['High'].mean()
print("Apr 1999 Mean High Price:", Apr1999_mean)
Apr1999.plot(x='Date', y='High', title='AMD High Prices in April 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1999=df.loc[(df['Date'] >= '1999-05-01') & (df['Date'] < '1999-05-31')]
print(May1999)
May1999_mean=May1999['High'].mean()
print("May 1999 Mean High Price:", May1999_mean)
May1999.plot(x='Date', y='High', title='AMD High Prices in May 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1999=df.loc[(df['Date'] >= '1999-06-01') & (df['Date'] < '1999-06-30')]
print(Jun1999)
Jun1999_mean=Jun1999['High'].mean()
print("Jun 1999 Mean High Price:", Jun1999_mean)
Jun1999.plot(x='Date', y='High', title='AMD High Prices in June 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1999=df.loc[(df['Date'] >= '1999-07-01') & (df['Date'] < '1999-07-31')]
print(Jul1999)
Jul1999_mean=Jul1999['High'].mean()
print("Jul 1999 Mean High Price:", Jul1999_mean)
Jul1999.plot(x='Date', y='High', title='AMD High Prices in July 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1999=df.loc[(df['Date'] >= '1999-08-01') & (df['Date'] < '1999-08-31')]
print(Aug1999)
Aug1999_mean=Aug1999['High'].mean()
print("Aug 1999 Mean High Price:", Aug1999_mean)
Aug1999.plot(x='Date', y='High', title='AMD High Prices in August 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1999=df.loc[(df['Date'] >= '1999-09-01') & (df['Date'] < '1999-09-30')]
print(Sep1999)
Sep1999_mean=Sep1999['High'].mean()
print("Sep 1999 Mean High Price:", Sep1999_mean)
Sep1999.plot(x='Date', y='High', title='AMD High Prices in September 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1999=df.loc[(df['Date'] >= '1999-10-01') & (df['Date'] < '1999-10-31')]
print(Oct1999)
Oct1999_mean=Oct1999['High'].mean()
print("Oct 1999 Mean High Price:", Oct1999_mean)
Oct1999.plot(x='Date', y='High', title='AMD High Prices in October 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1999=df.loc[(df['Date'] >= '1999-11-01') & (df['Date'] < '1999-11-30')]
print(Nov1999)
Nov1999_mean=Nov1999['High'].mean()
print("Nov 1999 Mean High Price:", Nov1999_mean)
Nov1999.plot(x='Date', y='High', title='AMD High Prices in November 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1999=df.loc[(df['Date'] >= '1999-12-01') & (df['Date'] < '1999-12-31')]
print(Dec1999)
Dec1999_mean=Dec1999['High'].mean()
print("Dec 1999 Mean High Price:", Dec1999_mean)
Dec1999.plot(x='Date', y='High', title='AMD High Prices in December 1999')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2000=df.loc[(df['Date'] >= '2000-01-01') & (df['Date'] < '2000-01-31')]
print(Jan2000)
Jan2000_mean=Jan2000['High'].mean()
print("Jan 2000 Mean High Price:", Jan2000_mean)
Jan2000.plot(x='Date', y='High', title='AMD High Prices in January 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2000=df.loc[(df['Date'] >= '2000-02-01') & (df['Date'] < '2000-02-29')]
print(Feb2000)
Feb2000_mean=Feb2000['High'].mean()
print("Feb 2000 Mean High Price:", Feb2000_mean)
Feb2000.plot(x='Date', y='High', title='AMD High Prices in February 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2000=df.loc[(df['Date'] >= '2000-03-01') & (df['Date'] < '2000-03-31')]
print(Mar2000)
Mar2000_mean=Mar2000['High'].mean()
print("Mar 2000 Mean High Price:", Mar2000_mean)
Mar2000.plot(x='Date', y='High', title='AMD High Prices in March 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2000=df.loc[(df['Date'] >= '2000-04-01') & (df['Date'] < '2000-04-30')]
print(Apr2000)
Apr2000_mean=Apr2000['High'].mean()
print("Apr 2000 Mean High Price:", Apr2000_mean)
Apr2000.plot(x='Date', y='High', title='AMD High Prices in April 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2000=df.loc[(df['Date'] >= '2000-05-01') & (df['Date'] < '2000-05-31')]
print(May2000)
May2000_mean=May2000['High'].mean()
print("May 2000 Mean High Price:", May2000_mean)
May2000.plot(x='Date', y='High', title='AMD High Prices in May 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2000=df.loc[(df['Date'] >= '2000-06-01') & (df['Date'] < '2000-06-30')]
print(Jun2000)
Jun2000_mean=Jun2000['High'].mean()
print("Jun 2000 Mean High Price:", Jun2000_mean)
Jun2000.plot(x='Date', y='High', title='AMD High Prices in June 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2000=df.loc[(df['Date'] >= '2000-07-01') & (df['Date'] < '2000-07-31')]
print(Jul2000)
Jul2000_mean=Jul2000['High'].mean()
print("Jul 2000 Mean High Price:", Jul2000_mean)
Jul2000.plot(x='Date', y='High', title='AMD High Prices in July 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2000=df.loc[(df['Date'] >= '2000-08-01') & (df['Date'] < '2000-08-31')]
print(Aug2000)
Aug2000_mean=Aug2000['High'].mean()
print("Aug 2000 Mean High Price:", Aug2000_mean)
Aug2000.plot(x='Date', y='High', title='AMD High Prices in August 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2000=df.loc[(df['Date'] >= '2000-09-01') & (df['Date'] < '2000-09-30')]
print(Sep2000)
Sep2000_mean=Sep2000['High'].mean()
print("Sep 2000 Mean High Price:", Sep2000_mean)
Sep2000.plot(x='Date', y='High', title='AMD High Prices in September 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2000=df.loc[(df['Date'] >= '2000-10-01') & (df['Date'] < '2000-10-31')]
print(Oct2000)
Oct2000_mean=Oct2000['High'].mean()
print("Oct 2000 Mean High Price:", Oct2000_mean)
Oct2000.plot(x='Date', y='High', title='AMD High Prices in October 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2000=df.loc[(df['Date'] >= '2000-11-01') & (df['Date'] < '2000-11-30')]
print(Nov2000)
Nov2000_mean=Nov2000['High'].mean()
print("Nov 2000 Mean High Price:", Nov2000_mean)
Nov2000.plot(x='Date', y='High', title='AMD High Prices in November 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2000=df.loc[(df['Date'] >= '2000-12-01') & (df['Date'] < '2000-12-31')]
print(Dec2000)
Dec2000_mean=Dec2000['High'].mean()
print("Dec 2000 Mean High Price:", Dec2000_mean)
Dec2000.plot(x='Date', y='High', title='AMD High Prices in December 2000')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2001=df.loc[(df['Date'] >= '2001-01-01') & (df['Date'] < '2001-01-31')]
print(Jan2001)
Jan2001_mean=Jan2001['High'].mean()
print("Jan 2001 Mean High Price:", Jan2001_mean)
Jan2001.plot(x='Date', y='High', title='AMD High Prices in January 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2001=df.loc[(df['Date'] >= '2001-02-01') & (df['Date'] < '2001-02-28')]
print(Feb2001)
Feb2001_mean=Feb2001['High'].mean()
print("Feb 2001 Mean High Price:", Feb2001_mean)
Feb2001.plot(x='Date', y='High', title='AMD High Prices in February 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2001=df.loc[(df['Date'] >= '2001-03-01') & (df['Date'] < '2001-03-31')]
print(Mar2001)
Mar2001_mean=Mar2001['High'].mean()
print("Mar 2001 Mean High Price:", Mar2001_mean)
Mar2001.plot(x='Date', y='High', title='AMD High Prices in March 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2001=df.loc[(df['Date'] >= '2001-04-01') & (df['Date'] < '2001-04-30')]
print(Apr2001)
Apr2001_mean=Apr2001['High'].mean()
print("Apr 2001 Mean High Price:", Apr2001_mean)
Apr2001.plot(x='Date', y='High', title='AMD High Prices in April 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2001=df.loc[(df['Date'] >= '2001-05-01') & (df['Date'] < '2001-05-31')]
print(May2001)
May2001_mean=May2001['High'].mean()
print("May 2001 Mean High Price:", May2001_mean)
May2001.plot(x='Date', y='High', title='AMD High Prices in May 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2001=df.loc[(df['Date'] >= '2001-06-01') & (df['Date'] < '2001-06-30')]
print(Jun2001)
Jun2001_mean=Jun2001['High'].mean()
print("Jun 2001 Mean High Price:", Jun2001_mean)
Jun2001.plot(x='Date', y='High', title='AMD High Prices in June 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2001=df.loc[(df['Date'] >= '2001-07-01') & (df['Date'] < '2001-07-31')]
print(Jul2001)
Jul2001_mean=Jul2001['High'].mean()
print("Jul 2001 Mean High Price:", Jul2001_mean)
Jul2001.plot(x='Date', y='High', title='AMD High Prices in July 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2001=df.loc[(df['Date'] >= '2001-08-01') & (df['Date'] < '2001-08-31')]
print(Aug2001)
Aug2001_mean=Aug2001['High'].mean()
print("Aug 2001 Mean High Price:", Aug2001_mean)
Aug2001.plot(x='Date', y='High', title='AMD High Prices in August 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2001=df.loc[(df['Date'] >= '2001-09-01') & (df['Date'] < '2001-09-30')]
print(Sep2001)
Sep2001_mean=Sep2001['High'].mean()
print("Sep 2001 Mean High Price:", Sep2001_mean)
Sep2001.plot(x='Date', y='High', title='AMD High Prices in September 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2001=df.loc[(df['Date'] >= '2001-10-01') & (df['Date'] < '2001-10-31')]
print(Oct2001)
Oct2001_mean=Oct2001['High'].mean()
print("Oct 2001 Mean High Price:", Oct2001_mean)
Oct2001.plot(x='Date', y='High', title='AMD High Prices in October 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2001=df.loc[(df['Date'] >= '2001-11-01') & (df['Date'] < '2001-11-30')]
print(Nov2001)
Nov2001_mean=Nov2001['High'].mean()
print("Nov 2001 Mean High Price:", Nov2001_mean)
Nov2001.plot(x='Date', y='High', title='AMD High Prices in November 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2001=df.loc[(df['Date'] >= '2001-12-01') & (df['Date'] < '2001-12-31')]
print(Dec2001)
Dec2001_mean=Dec2001['High'].mean()
print("Dec 2001 Mean High Price:", Dec2001_mean)
Dec2001.plot(x='Date', y='High', title='AMD High Prices in December 2001')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2002=df.loc[(df['Date'] >= '2002-01-01') & (df['Date'] < '2002-01-31')]
print(Jan2002)
Jan2002_mean=Jan2002['High'].mean()
print("Jan 2002 Mean High Price:", Jan2002_mean)
Jan2002.plot(x='Date', y='High', title='AMD High Prices in January 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2002=df.loc[(df['Date'] >= '2002-02-01') & (df['Date'] < '2002-02-28')]
print(Feb2002)
Feb2002_mean=Feb2002['High'].mean()
print("Feb 2002 Mean High Price:", Feb2002_mean)
Feb2002.plot(x='Date', y='High', title='AMD High Prices in February 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2002=df.loc[(df['Date'] >= '2002-03-01') & (df['Date'] < '2002-03-31')]
print(Mar2002)
Mar2002_mean=Mar2002['High'].mean()
print("Mar 2002 Mean High Price:", Mar2002_mean)
Mar2002.plot(x='Date', y='High', title='AMD High Prices in March 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2002=df.loc[(df['Date'] >= '2002-04-01') & (df['Date'] < '2002-04-30')]
print(Apr2002)
Apr2002_mean=Apr2002['High'].mean()
print("Apr 2002 Mean High Price:", Apr2002_mean)
Apr2002.plot(x='Date', y='High', title='AMD High Prices in April 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2002=df.loc[(df['Date'] >= '2002-05-01') & (df['Date'] < '2002-05-31')]
print(May2002)
May2002_mean=May2002['High'].mean()
print("May 2002 Mean High Price:", May2002_mean)
May2002.plot(x='Date', y='High', title='AMD High Prices in May 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2002=df.loc[(df['Date'] >= '2002-06-01') & (df['Date'] < '2002-06-30')]
print(Jun2002)
Jun2002_mean=Jun2002['High'].mean()
print("Jun 2002 Mean High Price:", Jun2002_mean)
Jun2002.plot(x='Date', y='High', title='AMD High Prices in June 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2002=df.loc[(df['Date'] >= '2002-07-01') & (df['Date'] < '2002-07-31')]
print(Jul2002)
Jul2002_mean=Jul2002['High'].mean()
print("Jul 2002 Mean High Price:", Jul2002_mean)
Jul2002.plot(x='Date', y='High', title='AMD High Prices in July 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2002=df.loc[(df['Date'] >= '2002-01-01') & (df['Date'] < '2002-01-31')]
print(Aug2002)
Aug2002_mean=Aug2002['High'].mean()
print("Aug 2002 Mean High Price:", Aug2002_mean)
Aug2002.plot(x='Date', y='High', title='AMD High Prices in August 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2002=df.loc[(df['Date'] >= '2002-09-01') & (df['Date'] < '2002-09-30')]
print(Sep2002)
Sep2002_mean=Sep2002['High'].mean()
print("Sep 2002 Mean High Price:", Sep2002_mean)
Sep2002.plot(x='Date', y='High', title='AMD High Prices in September 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2002=df.loc[(df['Date'] >= '2002-10-01') & (df['Date'] < '2002-10-31')]
print(Oct2002)
Oct2002_mean=Oct2002['High'].mean()
print("Oct 2002 Mean High Price:", Oct2002_mean)
Oct2002.plot(x='Date', y='High', title='AMD High Prices in October 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2002=df.loc[(df['Date'] >= '2002-11-01') & (df['Date'] < '2002-11-30')]
print(Nov2002)
Nov2002_mean=Nov2002['High'].mean()
print("Nov 2002 Mean High Price:", Nov2002_mean)
Nov2002.plot(x='Date', y='High', title='AMD High Prices in November 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2002=df.loc[(df['Date'] >= '2002-12-01') & (df['Date'] < '2002-12-31')]
print(Dec2002)
Dec2002_mean=Dec2002['High'].mean()
print("Dec 2002 Mean High Price:", Dec2002_mean)
Dec2002.plot(x='Date', y='High', title='AMD High Prices in December 2002')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2003=df.loc[(df['Date'] >= '2003-01-01') & (df['Date'] < '2003-01-31')]
print(Jan2003)
Jan2003_mean=Jan2003['High'].mean()
print("Jan 2003 Mean High Price:", Jan2003_mean)
Jan2003.plot(x='Date', y='High', title='AMD High Prices in January 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2003=df.loc[(df['Date'] >= '2003-02-01') & (df['Date'] < '2003-02-28')]
print(Feb2003)
Feb2003_mean=Feb2003['High'].mean()
print("Feb 2003 Mean High Price:", Feb2003_mean)
Feb2003.plot(x='Date', y='High', title='AMD High Prices in February 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2003=df.loc[(df['Date'] >= '2003-03-01') & (df['Date'] < '2003-03-31')]
print(Mar2003)
Mar2003_mean=Mar2003['High'].mean()
print("Mar 2003 Mean High Price:", Mar2003_mean)
Mar2003.plot(x='Date', y='High', title='AMD High Prices in March 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2003=df.loc[(df['Date'] >= '2003-04-01') & (df['Date'] < '2003-04-30')]
print(Apr2003)
Apr2003_mean=Apr2003['High'].mean()
print("Apr 2003 Mean High Price:", Apr2003_mean)
Apr2003.plot(x='Date', y='High', title='AMD High Prices in January 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2003=df.loc[(df['Date'] >= '2003-05-01') & (df['Date'] < '2003-05-31')]
print(May2003)
May2003_mean=May2003['High'].mean()
print("May 2003 Mean High Price:", May2003_mean)
May2003.plot(x='Date', y='High', title='AMD High Prices in May 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2003=df.loc[(df['Date'] >= '2003-06-01') & (df['Date'] < '2003-06-30')]
print(Jun2003)
Jun2003_mean=Jun2003['High'].mean()
print("Jun 2003 Mean High Price:", Jun2003_mean)
Jun2003.plot(x='Date', y='High', title='AMD High Prices in June 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2003=df.loc[(df['Date'] >= '2003-07-01') & (df['Date'] < '2003-07-31')]
print(Jul2003)
Jul2003_mean=Jul2003['High'].mean()
print("Jul 2003 Mean High Price:", Jul2003_mean)
Jul2003.plot(x='Date', y='High', title='AMD High Prices in July 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2003=df.loc[(df['Date'] >= '2003-08-01') & (df['Date'] < '2003-08-31')]
print(Aug2003)
Aug2003_mean=Aug2003['High'].mean()
print("Aug 2003 Mean High Price:", Aug2003_mean)
Aug2003.plot(x='Date', y='High', title='AMD High Prices in August 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2003=df.loc[(df['Date'] >= '2003-09-01') & (df['Date'] < '2003-09-30')]
print(Sep2003)
Sep2003_mean=Sep2003['High'].mean()
print("Sep 2003 Mean High Price:", Sep2003_mean)
Sep2003.plot(x='Date', y='High', title='AMD High Prices in September 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2003=df.loc[(df['Date'] >= '2003-10-01') & (df['Date'] < '2003-10-31')]
print(Oct2003)
Oct2003_mean=Oct2003['High'].mean()
print("Oct 2003 Mean High Price:", Oct2003_mean)
Oct2003.plot(x='Date', y='High', title='AMD High Prices in October 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2003=df.loc[(df['Date'] >= '2003-01-01') & (df['Date'] < '2003-01-31')]
print(Jan2003)
Jan2003_mean=Jan2003['High'].mean()
print("Jan 2003 Mean High Price:", Jan2003_mean)
Jan2003.plot(x='Date', y='High', title='AMD High Prices in January 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2003=df.loc[(df['Date'] >= '2003-11-01') & (df['Date'] < '2003-11-30')]
print(Nov2003)
Nov2003_mean=Nov2003['High'].mean()
print("Nov 2003 Mean High Price:", Nov2003_mean)
Nov2003.plot(x='Date', y='High', title='AMD High Prices in November 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2003=df.loc[(df['Date'] >= '2003-12-01') & (df['Date'] < '2003-12-31')]
print(Dec2003)
Dec2003_mean=Dec2003['High'].mean()
print("Dec 2003 Mean High Price:", Dec2003_mean)
Dec2003.plot(x='Date', y='High', title='AMD High Prices in December 2003')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2004=df.loc[(df['Date'] >= '2004-01-01') & (df['Date'] < '2004-01-31')]
print(Jan2004)
Jan2004_mean=Jan2004['High'].mean()
print("Jan 2004 Mean High Price:", Jan2004_mean)
Jan2004.plot(x='Date', y='High', title='AMD High Prices in January 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2004=df.loc[(df['Date'] >= '2004-02-01') & (df['Date'] < '2004-02-29')]
print(Feb2004)
Feb2004_mean=Feb2004['High'].mean()
print("Feb 2004 Mean High Price:", Feb2004_mean)
Feb2004.plot(x='Date', y='High', title='AMD High Prices in February 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2004=df.loc[(df['Date'] >= '2004-03-01') & (df['Date'] < '2004-03-31')]
print(Mar2004)
Mar2004_mean=Mar2004['High'].mean()
print("Mar 2004 Mean High Price:", Mar2004_mean)
Mar2004.plot(x='Date', y='High', title='AMD High Prices in March 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2004=df.loc[(df['Date'] >= '2004-04-01') & (df['Date'] < '2004-04-30')]
print(Apr2004)
Apr2004_mean=Apr2004['High'].mean()
print("Apr 2004 Mean High Price:", Apr2004_mean)
Apr2004.plot(x='Date', y='High', title='AMD High Prices in April 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2004=df.loc[(df['Date'] >= '2004-05-01') & (df['Date'] < '2004-05-31')]
print(May2004)
May2004_mean=May2004['High'].mean()
print("May 2004 Mean High Price:", May2004_mean)
May2004.plot(x='Date', y='High', title='AMD High Prices in May 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2004=df.loc[(df['Date'] >= '2004-06-01') & (df['Date'] < '2004-06-30')]
print(Jun2004)
Jun2004_mean=Jun2004['High'].mean()
print("Jun 2004 Mean High Price:", Jun2004_mean)
Jun2004.plot(x='Date', y='High', title='AMD High Prices in June 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2004=df.loc[(df['Date'] >= '2004-07-01') & (df['Date'] < '2004-07-31')]
print(Jul2004)
Jul2004_mean=Jul2004['High'].mean()
print("Jul 2004 Mean High Price:", Jul2004_mean)
Jul2004.plot(x='Date', y='High', title='AMD High Prices in July 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2004=df.loc[(df['Date'] >= '2004-08-01') & (df['Date'] < '2004-08-31')]
print(Aug2004)
Aug2004_mean=Aug2004['High'].mean()
print("Aug 2004 Mean High Price:", Aug2004_mean)
Aug2004.plot(x='Date', y='High', title='AMD High Prices in August 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2004=df.loc[(df['Date'] >= '2004-09-01') & (df['Date'] < '2004-09-30')]
print(Sep2004)
Sep2004_mean=Sep2004['High'].mean()
print("Sep 2004 Mean High Price:", Sep2004_mean)
Sep2004.plot(x='Date', y='High', title='AMD High Prices in September 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2004=df.loc[(df['Date'] >= '2004-10-01') & (df['Date'] < '2004-10-31')]
print(Oct2004)
Oct2004_mean=Oct2004['High'].mean()
print("Oct 2004 Mean High Price:", Oct2004_mean)
Oct2004.plot(x='Date', y='High', title='AMD High Prices in October 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2004=df.loc[(df['Date'] >= '2004-11-01') & (df['Date'] < '2004-11-30')]
print(Nov2004)
Nov2004_mean=Nov2004['High'].mean()
print("Nov 2004 Mean High Price:", Nov2004_mean)
Nov2004.plot(x='Date', y='High', title='AMD High Prices in November 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2004=df.loc[(df['Date'] >= '2004-12-01') & (df['Date'] < '2004-12-31')]
print(Dec2004)
Dec2004_mean=Dec2004['High'].mean()
print("Dec 2004 Mean High Price:", Dec2004_mean)
Dec2004.plot(x='Date', y='High', title='AMD High Prices in December 2004')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2005=df.loc[(df['Date'] >= '2005-01-01') & (df['Date'] < '2005-01-31')]
print(Jan2005)
Jan2005_mean=Jan2005['High'].mean()
print("Jan 2005 Mean High Price:", Jan2005_mean)
Jan2005.plot(x='Date', y='High', title='AMD High Prices in January 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2005=df.loc[(df['Date'] >= '2005-02-01') & (df['Date'] < '2005-02-28')]
print(Feb2005)
Feb2005_mean=Feb2005['High'].mean()
print("Feb 2005 Mean High Price:", Feb2005_mean)
Feb2005.plot(x='Date', y='High', title='AMD High Prices in February 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2005=df.loc[(df['Date'] >= '2005-03-01') & (df['Date'] < '2005-03-31')]
print(Mar2005)
Mar2005_mean=Mar2005['High'].mean()
print("Mar 2005 Mean High Price:", Mar2005_mean)
Mar2005.plot(x='Date', y='High', title='AMD High Prices in March 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2005=df.loc[(df['Date'] >= '2005-04-01') & (df['Date'] < '2005-04-30')]
print(Apr2005)
Apr2005_mean=Apr2005['High'].mean()
print("Apr 2005 Mean High Price:", Apr2005_mean)
Apr2005.plot(x='Date', y='High', title='AMD High Prices in April 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2005=df.loc[(df['Date'] >= '2005-05-01') & (df['Date'] < '2005-05-31')]
print(May2005)
May2005_mean=May2005['High'].mean()
print("May 2005 Mean High Price:", May2005_mean)
May2005.plot(x='Date', y='High', title='AMD High Prices in May 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2005=df.loc[(df['Date'] >= '2005-06-01') & (df['Date'] < '2005-06-30')]
print(Jun2005)
Jun2005_mean=Jun2005['High'].mean()
print("Jun 2005 Mean High Price:", Jun2005_mean)
Jun2005.plot(x='Date', y='High', title='AMD High Prices in June 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2005=df.loc[(df['Date'] >= '2005-07-01') & (df['Date'] < '2005-07-31')]
print(Jul2005)
Jul2005_mean=Jul2005['High'].mean()
print("Jul 2005 Mean High Price:", Jul2005_mean)
Jul2005.plot(x='Date', y='High', title='AMD High Prices in July 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2005=df.loc[(df['Date'] >= '2005-08-01') & (df['Date'] < '2005-08-31')]
print(Aug2005)
Aug2005_mean=Aug2005['High'].mean()
print("Aug 2005 Mean High Price:", Aug2005_mean)
Aug2005.plot(x='Date', y='High', title='AMD High Prices in August 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2005=df.loc[(df['Date'] >= '2005-09-01') & (df['Date'] < '2005-09-30')]
print(Sep2005)
Sep2005_mean=Sep2005['High'].mean()
print("Sep 2005 Mean High Price:", Sep2005_mean)
Sep2005.plot(x='Date', y='High', title='AMD High Prices in September 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2005=df.loc[(df['Date'] >= '2005-10-01') & (df['Date'] < '2005-10-31')]
print(Oct2005)
Oct2005_mean=Oct2005['High'].mean()
print("Oct 2005 Mean High Price:", Oct2005_mean)
Oct2005.plot(x='Date', y='High', title='AMD High Prices in October 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2005=df.loc[(df['Date'] >= '2005-11-01') & (df['Date'] < '2005-11-30')]
print(Nov2005)
Nov2005_mean=Nov2005['High'].mean()
print("Nov 2005 Mean High Price:", Nov2005_mean)
Nov2005.plot(x='Date', y='High', title='AMD High Prices in November 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2005=df.loc[(df['Date'] >= '2005-12-01') & (df['Date'] < '2005-12-31')]
print(Dec2005)
Dec2005_mean=Dec2005['High'].mean()
print("Dec 2005 Mean High Price:", Dec2005_mean)
Dec2005.plot(x='Date', y='High', title='AMD High Prices in December 2005')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2006=df.loc[(df['Date'] >= '2006-01-01') & (df['Date'] < '2006-01-31')]
print(Jan2006)
Jan2006_mean=Jan2006['High'].mean()
print("Jan 2006 Mean High Price:", Jan2006_mean)
Jan2006.plot(x='Date', y='High', title='AMD High Prices in January 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2006=df.loc[(df['Date'] >= '2006-02-01') & (df['Date'] < '2006-02-28')]
print(Feb2006)
Feb2006_mean=Feb2005['High'].mean()
print("Feb 2006 Mean High Price:", Feb2006_mean)
Feb2006.plot(x='Date', y='High', title='AMD High Prices in February 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2006=df.loc[(df['Date'] >= '2006-03-01') & (df['Date'] < '2006-03-31')]
print(Mar2006)
Mar2006_mean=Mar2006['High'].mean()
print("Mar 2006 Mean High Price:", Mar2006_mean)
Mar2006.plot(x='Date', y='High', title='AMD High Prices in March 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2006=df.loc[(df['Date'] >= '2006-04-01') & (df['Date'] < '2006-04-30')]
print(Apr2006)
Apr2006_mean=Apr2006['High'].mean()
print("Apr 2006 Mean High Price:", Apr2006_mean)
Apr2006.plot(x='Date', y='High', title='AMD High Prices in April 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2006=df.loc[(df['Date'] >= '2006-05-01') & (df['Date'] < '2006-05-31')]
print(May2006)
May2006_mean=May2006['High'].mean()
print("May 2006 Mean High Price:", May2006_mean)
May2006.plot(x='Date', y='High', title='AMD High Prices in May 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2006=df.loc[(df['Date'] >= '2006-06-01') & (df['Date'] < '2006-06-30')]
print(Jun2006)
Jun2006_mean=Jun2006['High'].mean()
print("Jun 2006 Mean High Price:", Jun2006_mean)
Jun2006.plot(x='Date', y='High', title='AMD High Prices in June 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2006=df.loc[(df['Date'] >= '2006-07-01') & (df['Date'] < '2006-07-31')]
print(Jul2006)
Jul2006_mean=Jul2006['High'].mean()
print("Jul 2006 Mean High Price:", Jul2006_mean)
Jul2006.plot(x='Date', y='High', title='AMD High Prices in July 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2006=df.loc[(df['Date'] >= '2006-08-01') & (df['Date'] < '2006-08-31')]
print(Aug2006)
Aug2006_mean=Aug2006['High'].mean()
print("Aug 2006 Mean High Price:", Aug2006_mean)
Aug2006.plot(x='Date', y='High', title='AMD High Prices in August 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2006=df.loc[(df['Date'] >= '2006-09-01') & (df['Date'] < '2006-09-30')]
print(Sep2006)
Sep2006_mean=Sep2006['High'].mean()
print("Sep 2006 Mean High Price:", Sep2006_mean)
Sep2006.plot(x='Date', y='High', title='AMD High Prices in September 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2006=df.loc[(df['Date'] >= '2006-10-01') & (df['Date'] < '2006-10-31')]
print(Oct2006)
Oct2006_mean=Oct2006['High'].mean()
print("Oct 2006 Mean High Price:", Oct2006_mean)
Oct2006.plot(x='Date', y='High', title='AMD High Prices in October 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2006=df.loc[(df['Date'] >= '2006-11-01') & (df['Date'] < '2006-11-30')]
print(Nov2006)
Nov2006_mean=Nov2006['High'].mean()
print("Nov 2006 Mean High Price:", Nov2006_mean)
Nov2006.plot(x='Date', y='High', title='AMD High Prices in November 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2006=df.loc[(df['Date'] >= '2006-12-01') & (df['Date'] < '2006-12-31')]
print(Dec2006)
Dec2006_mean=Dec2006['High'].mean()
print("Dec 2006 Mean High Price:", Dec2006_mean)
Dec2006.plot(x='Date', y='High', title='AMD High Prices in December 2006')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2007=df.loc[(df['Date'] >= '2007-01-01') & (df['Date'] < '2007-01-31')]
print(Jan2007)
Jan2007_mean=Jan2007['High'].mean()
print("Jan 2007 Mean High Price:", Jan2007_mean)
Jan2007.plot(x='Date', y='High', title='AMD High Prices in January 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2007=df.loc[(df['Date'] >= '2007-02-01') & (df['Date'] < '2007-02-28')]
print(Feb2007)
Feb2007_mean=Feb2007['High'].mean()
print("Feb 2007 Mean High Price:", Feb2007_mean)
Feb2007.plot(x='Date', y='High', title='AMD High Prices in February 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2007=df.loc[(df['Date'] >= '2007-03-01') & (df['Date'] < '2007-03-31')]
print(Mar2007)
Mar2007_mean=Mar2007['High'].mean()
print("Mar 2007 Mean High Price:", Mar2007_mean)
Mar2007.plot(x='Date', y='High', title='AMD High Prices in March 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2007=df.loc[(df['Date'] >= '2007-04-01') & (df['Date'] < '2007-04-30')]
print(Apr2007)
Apr2007_mean=Apr2007['High'].mean()
print("Apr 2007 Mean High Price:", Apr2007_mean)
Apr2007.plot(x='Date', y='High', title='AMD High Prices in April 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2007=df.loc[(df['Date'] >= '2007-05-01') & (df['Date'] < '2007-05-31')]
print(May2007)
May2007_mean=May2007['High'].mean()
print("May 2007 Mean High Price:", May2007_mean)
May2007.plot(x='Date', y='High', title='AMD High Prices in May 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2007=df.loc[(df['Date'] >= '2007-06-01') & (df['Date'] < '2007-06-30')]
print(Jun2007)
Jun2007_mean=Jun2007['High'].mean()
print("Jun 2007 Mean High Price:", Jun2007_mean)
Jun2007.plot(x='Date', y='High', title='AMD High Prices in June 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2007=df.loc[(df['Date'] >= '2007-07-01') & (df['Date'] < '2007-07-31')]
print(Jul2007)
Jul2007_mean=Jul2007['High'].mean()
print("Jul 2007 Mean High Price:", Jul2007_mean)
Jul2007.plot(x='Date', y='High', title='AMD High Prices in July 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2007=df.loc[(df['Date'] >= '2007-08-01') & (df['Date'] < '2007-08-31')]
print(Aug2007)
Aug2007_mean=Aug2007['High'].mean()
print("Aug 2007 Mean High Price:", Aug2007_mean)
Aug2007.plot(x='Date', y='High', title='AMD High Prices in August 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2007=df.loc[(df['Date'] >= '2007-09-01') & (df['Date'] < '2007-09-30')]
print(Sep2007)
Sep2007_mean=Sep2007['High'].mean()
print("Sep 2007 Mean High Price:", Sep2007_mean)
Sep2007.plot(x='Date', y='High', title='AMD High Prices in September 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2007=df.loc[(df['Date'] >= '2007-10-01') & (df['Date'] < '2007-10-31')]
print(Oct2007)
Oct2007_mean=Oct2007['High'].mean()
print("Oct 2007 Mean High Price:", Oct2007_mean)
Oct2007.plot(x='Date', y='High', title='AMD High Prices in October 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2007=df.loc[(df['Date'] >= '2007-11-01') & (df['Date'] < '2007-11-30')]
print(Nov2007)
Nov2007_mean=Nov2007['High'].mean()
print("Nov 2007 Mean High Price:", Nov2007_mean)
Nov2007.plot(x='Date', y='High', title='AMD High Prices in November 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2007=df.loc[(df['Date'] >= '2007-12-01') & (df['Date'] < '2007-12-31')]
print(Dec2007)
Dec2007_mean=Dec2007['High'].mean()
print("Dec 2007 Mean High Price:", Dec2007_mean)
Dec2007.plot(x='Date', y='High', title='AMD High Prices in December 2007')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2008=df.loc[(df['Date'] >= '2008-01-01') & (df['Date'] < '2008-01-31')]
print(Jan2008)
Jan2008_mean=Jan2008['High'].mean()
print("Jan 2008 Mean High Price:", Jan2008_mean)
Jan2008.plot(x='Date', y='High', title='AMD High Prices in January 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2008=df.loc[(df['Date'] >= '2008-02-01') & (df['Date'] < '2008-02-29')]
print(Feb2008)
Feb2008_mean=Feb2008['High'].mean()
print("Feb 2008 Mean High Price:", Feb2008_mean)
Feb2008.plot(x='Date', y='High', title='AMD High Prices in February 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2008=df.loc[(df['Date'] >= '2008-03-01') & (df['Date'] < '2008-03-31')]
print(Mar2008)
Mar2008_mean=Mar2008['High'].mean()
print("Mar 2008 Mean High Price:", Mar2008_mean)
Mar2008.plot(x='Date', y='High', title='AMD High Prices in March 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2008=df.loc[(df['Date'] >= '2008-04-01') & (df['Date'] < '2008-04-30')]
print(Apr2008)
Apr2008_mean=Apr2008['High'].mean()
print("Apr 2008 Mean High Price:", Apr2008_mean)
Apr2008.plot(x='Date', y='High', title='AMD High Prices in April 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2008=df.loc[(df['Date'] >= '2008-05-01') & (df['Date'] < '2008-05-31')]
print(May2008)
May2008_mean=May2008['High'].mean()
print("May 2008 Mean High Price:", May2008_mean)
May2008.plot(x='Date', y='High', title='AMD High Prices in May 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2008=df.loc[(df['Date'] >= '2008-06-01') & (df['Date'] < '2008-06-30')]
print(Jun2008)
Jun2008_mean=Jun2008['High'].mean()
print("Jun 2008 Mean High Price:", Jun2008_mean)
Jun2008.plot(x='Date', y='High', title='AMD High Prices in June 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2008=df.loc[(df['Date'] >= '2008-07-01') & (df['Date'] < '2008-07-31')]
print(Jul2008)
Jul2008_mean=Jul2008['High'].mean()
print("Jul 2008 Mean High Price:", Jul2008_mean)
Jul2008.plot(x='Date', y='High', title='AMD High Prices in July 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2008=df.loc[(df['Date'] >= '2008-08-01') & (df['Date'] < '2008-08-31')]
print(Aug2008)
Aug2008_mean=Aug2008['High'].mean()
print("Aug 2008 Mean High Price:", Aug2008_mean)
Aug2008.plot(x='Date', y='High', title='AMD High Prices in August 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2008=df.loc[(df['Date'] >= '2008-09-01') & (df['Date'] < '2008-09-30')]
print(Sep2008)
Sep2008_mean=Sep2008['High'].mean()
print("Sep 2008 Mean High Price:", Sep2008_mean)
Sep2008.plot(x='Date', y='High', title='AMD High Prices in September 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2008=df.loc[(df['Date'] >= '2008-10-01') & (df['Date'] < '2008-10-31')]
print(Oct2008)
Oct2008_mean=Oct2008['High'].mean()
print("Oct 2008 Mean High Price:", Oct2008_mean)
Oct2008.plot(x='Date', y='High', title='AMD High Prices in October 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2008=df.loc[(df['Date'] >= '2008-11-01') & (df['Date'] < '2008-11-30')]
print(Nov2008)
Nov2008_mean=Nov2008['High'].mean()
print("Nov 2008 Mean High Price:", Nov2008_mean)
Nov2008.plot(x='Date', y='High', title='AMD High Prices in November 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2008=df.loc[(df['Date'] >= '2008-12-01') & (df['Date'] < '2008-12-31')]
print(Dec2008)
Dec2008_mean=Dec2008['High'].mean()
print("Dec 2008 Mean High Price:", Dec2008_mean)
Dec2008.plot(x='Date', y='High', title='AMD High Prices in December 2008')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2009=df.loc[(df['Date'] >= '2009-01-01') & (df['Date'] < '2009-01-31')]
print(Jan2009)
Jan2009_mean=Jan2009['High'].mean()
print("Jan 2009 Mean High Price:", Jan2009_mean)
Jan2009.plot(x='Date', y='High', title='AMD High Prices in January 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2009=df.loc[(df['Date'] >= '2009-02-01') & (df['Date'] < '2009-02-28')]
print(Feb2009)
Feb2009_mean=Feb2009['High'].mean()
print("Feb 2009 Mean High Price:", Feb2009_mean)
Feb2009.plot(x='Date', y='High', title='AMD High Prices in February 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2009=df.loc[(df['Date'] >= '2009-03-01') & (df['Date'] < '2009-03-31')]
print(Mar2009)
Mar2009_mean=Mar2009['High'].mean()
print("Mar 2009 Mean High Price:", Mar2009_mean)
Mar2009.plot(x='Date', y='High', title='AMD High Prices in March 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2009=df.loc[(df['Date'] >= '2009-04-01') & (df['Date'] < '2009-04-30')]
print(Apr2009)
Apr2009_mean=Apr2009['High'].mean()
print("Apr 2009 Mean High Price:", Apr2009_mean)
Apr2009.plot(x='Date', y='High', title='AMD High Prices in April 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2009=df.loc[(df['Date'] >= '2009-05-01') & (df['Date'] < '2009-05-31')]
print(May2009)
May2009_mean=May2009['High'].mean()
print("May 2009 Mean High Price:", May2009_mean)
May2009.plot(x='Date', y='High', title='AMD High Prices in May 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2009=df.loc[(df['Date'] >= '2009-06-01') & (df['Date'] < '2009-06-30')]
print(Jun2009)
Jun2009_mean=Jun2009['High'].mean()
print("Jun 2009 Mean High Price:", Jun2009_mean)
Jun2009.plot(x='Date', y='High', title='AMD High Prices in June 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2009=df.loc[(df['Date'] >= '2009-07-01') & (df['Date'] < '2009-07-31')]
print(Jul2009)
Jul2009_mean=Jul2009['High'].mean()
print("Jul 2009 Mean High Price:", Jul2009_mean)
Jul2009.plot(x='Date', y='High', title='AMD High Prices in July 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2009=df.loc[(df['Date'] >= '2009-08-01') & (df['Date'] < '2009-08-31')]
print(Aug2009)
Aug2009_mean=Aug2009['High'].mean()
print("Aug 2009 Mean High Price:", Aug2009_mean)
Aug2009.plot(x='Date', y='High', title='AMD High Prices in August 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2009=df.loc[(df['Date'] >= '2009-09-01') & (df['Date'] < '2009-09-30')]
print(Sep2009)
Sep2009_mean=Sep2009['High'].mean()
print("Sep 2009 Mean High Price:", Sep2009_mean)
Sep2009.plot(x='Date', y='High', title='AMD High Prices in September 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2009=df.loc[(df['Date'] >= '2009-10-01') & (df['Date'] < '2009-10-31')]
print(Oct2009)
Oct2009_mean=Oct2009['High'].mean()
print("Oct 2009 Mean High Price:", Oct2009_mean)
Oct2009.plot(x='Date', y='High', title='AMD High Prices in October 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2009=df.loc[(df['Date'] >= '2009-11-01') & (df['Date'] < '2009-11-30')]
print(Nov2009)
Nov2009_mean=Nov2009['High'].mean()
print("Nov 2009 Mean High Price:", Nov2009_mean)
Nov2009.plot(x='Date', y='High', title='AMD High Prices in November 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2009=df.loc[(df['Date'] >= '2009-12-01') & (df['Date'] < '2009-12-31')]
print(Dec2009)
Dec2009_mean=Dec2009['High'].mean()
print("Dec 2009 Mean High Price:", Dec2009_mean)
Dec2009.plot(x='Date', y='High', title='AMD High Prices in December 2009')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2010=df.loc[(df['Date'] >= '2010-01-01') & (df['Date'] < '2010-01-31')]
print(Jan2010)
Jan2010_mean=Jan2010['High'].mean()
print("Jan 2010 Mean High Price:", Jan2010_mean)
Jan2010.plot(x='Date', y='High', title='AMD High Prices in January 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2010=df.loc[(df['Date'] >= '2010-02-01') & (df['Date'] < '2010-02-28')]
print(Feb2010)
Feb2010_mean=Feb2010['High'].mean()
print("Feb 2010 Mean High Price:", Feb2010_mean)
Feb2010.plot(x='Date', y='High', title='AMD High Prices in February 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2010=df.loc[(df['Date'] >= '2010-03-01') & (df['Date'] < '2010-03-31')]
print(Mar2010)
Mar2010_mean=Mar2010['High'].mean()
print("Mar 2010 Mean High Price:", Mar2010_mean)
Mar2010.plot(x='Date', y='High', title='AMD High Prices in March 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2010=df.loc[(df['Date'] >= '2010-04-01') & (df['Date'] < '2010-04-30')]
print(Apr2010)
Apr2010_mean=Apr2010['High'].mean()
print("Apr 2010 Mean High Price:", Apr2010_mean)
Apr2010.plot(x='Date', y='High', title='AMD High Prices in April 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2010=df.loc[(df['Date'] >= '2010-05-01') & (df['Date'] < '2010-05-31')]
print(May2010)
May2010_mean=May2010['High'].mean()
print("May 2010 Mean High Price:", May2010_mean)
May2010.plot(x='Date', y='High', title='AMD High Prices in May 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2010=df.loc[(df['Date'] >= '2010-06-01') & (df['Date'] < '2010-06-30')]
print(Jun2010)
Jun2010_mean=Jun2010['High'].mean()
print("Jun 2010 Mean High Price:", Jun2010_mean)
Jun2010.plot(x='Date', y='High', title='AMD High Prices in June 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2010=df.loc[(df['Date'] >= '2010-07-01') & (df['Date'] < '2010-07-31')]
print(Jul2010)
Jul2010_mean=Jul2010['High'].mean()
print("Jul 2010 Mean High Price:", Jul2010_mean)
Jul2010.plot(x='Date', y='High', title='AMD High Prices in July 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2010=df.loc[(df['Date'] >= '2010-08-01') & (df['Date'] < '2010-08-31')]
print(Aug2010)
Aug2010_mean=Aug2010['High'].mean()
print("Aug 2010 Mean High Price:", Aug2010_mean)
Aug2010.plot(x='Date', y='High', title='AMD High Prices in August 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2010=df.loc[(df['Date'] >= '2010-09-01') & (df['Date'] < '2010-09-30')]
print(Sep2010)
Sep2010_mean=Sep2010['High'].mean()
print("Sep 2010 Mean High Price:", Sep2010_mean)
Sep2010.plot(x='Date', y='High', title='AMD High Prices in September 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2010=df.loc[(df['Date'] >= '2010-10-01') & (df['Date'] < '2010-10-31')]
print(Oct2010)
Oct2010_mean=Oct2010['High'].mean()
print("Oct 2010 Mean High Price:", Oct2010_mean)
Oct2010.plot(x='Date', y='High', title='AMD High Prices in October 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2010=df.loc[(df['Date'] >= '2010-11-01') & (df['Date'] < '2010-11-30')]
print(Nov2010)
Nov2010_mean=Nov2010['High'].mean()
print("Nov 2010 Mean High Price:", Nov2010_mean)
Nov2010.plot(x='Date', y='High', title='AMD High Prices in November 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2010=df.loc[(df['Date'] >= '2010-12-01') & (df['Date'] < '2010-12-31')]
print(Dec2010)
Dec2010_mean=Dec2010['High'].mean()
print("Dec 2010 Mean High Price:", Dec2010_mean)
Dec2010.plot(x='Date', y='High', title='AMD High Prices in December 2010')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2011=df.loc[(df['Date'] >= '2011-01-01') & (df['Date'] < '2011-01-31')]
print(Jan2011)
Jan2011_mean=Jan2011['High'].mean()
print("Jan 2011 Mean High Price:", Jan2011_mean)
Jan2011.plot(x='Date', y='High', title='AMD High Prices in January 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2011=df.loc[(df['Date'] >= '2011-02-01') & (df['Date'] < '2011-02-28')]
print(Feb2011)
Feb2011_mean=Feb2011['High'].mean()
print("Feb 2011 Mean High Price:", Feb2011_mean)
Feb2011.plot(x='Date', y='High', title='AMD High Prices in February 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2011=df.loc[(df['Date'] >= '2011-03-01') & (df['Date'] < '2011-03-31')]
print(Mar2011)
Mar2011_mean=Mar2011['High'].mean()
print("Mar 2011 Mean High Price:", Mar2011_mean)
Mar2011.plot(x='Date', y='High', title='AMD High Prices in March 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2011=df.loc[(df['Date'] >= '2011-04-01') & (df['Date'] < '2011-04-30')]
print(Apr2011)
Apr2011_mean=Apr2011['High'].mean()
print("Apr 2011 Mean High Price:", Apr2011_mean)
Apr2011.plot(x='Date', y='High', title='AMD High Prices in April 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2011=df.loc[(df['Date'] >= '2011-05-01') & (df['Date'] < '2011-05-31')]
print(May2011)
May2011_mean=May2011['High'].mean()
print("May 2011 Mean High Price:", May2011_mean)
May2011.plot(x='Date', y='High', title='AMD High Prices in May 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2011=df.loc[(df['Date'] >= '2011-06-01') & (df['Date'] < '2011-06-31')]
print(Jun2011)
Jun2011_mean=Jun2011['High'].mean()
print("Jun 2011 Mean High Price:", Jun2011_mean)
Jun2011.plot(x='Date', y='High', title='AMD High Prices in June 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2011=df.loc[(df['Date'] >= '2011-07-01') & (df['Date'] < '2011-07-31')]
print(Jul2011)
Jul2011_mean=Jul2011['High'].mean()
print("Jul 2011 Mean High Price:", Jul2011_mean)
Jul2011.plot(x='Date', y='High', title='AMD High Prices in July 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2011=df.loc[(df['Date'] >= '2011-08-01') & (df['Date'] < '2011-08-31')]
print(Aug2011)
Aug2011_mean=Aug2011['High'].mean()
print("Aug 2011 Mean High Price:", Aug2011_mean)
Aug2011.plot(x='Date', y='High', title='AMD High Prices in August 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2011=df.loc[(df['Date'] >= '2011-09-01') & (df['Date'] < '2011-09-30')]
print(Sep2011)
Sep2011_mean=Sep2011['High'].mean()
print("Sep 2011 Mean High Price:", Sep2011_mean)
Sep2011.plot(x='Date', y='High', title='AMD High Prices in September 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2011=df.loc[(df['Date'] >= '2011-10-01') & (df['Date'] < '2011-10-31')]
print(Oct2011)
Oct2011_mean=Oct2011['High'].mean()
print("Oct 2011 Mean High Price:", Oct2011_mean)
Oct2011.plot(x='Date', y='High', title='AMD High Prices in October 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2011=df.loc[(df['Date'] >= '2011-11-01') & (df['Date'] < '2011-11-30')]
print(Nov2011)
Nov2011_mean=Nov2011['High'].mean()
print("Nov 2011 Mean High Price:", Nov2011_mean)
Nov2011.plot(x='Date', y='High', title='AMD High Prices in November 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2011=df.loc[(df['Date'] >= '2011-12-01') & (df['Date'] < '2011-12-31')]
print(Dec2011)
Dec2011_mean=Dec2011['High'].mean()
print("Dec 2011 Mean High Price:", Dec2011_mean)
Dec2011.plot(x='Date', y='High', title='AMD High Prices in December 2011')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2012=df.loc[(df['Date'] >= '2012-01-01') & (df['Date'] < '2012-01-31')]
print(Jan2012)
Jan2012_mean=Jan2012['High'].mean()
print("Jan 2012 Mean High Price:", Jan2012_mean)
Jan2012.plot(x='Date', y='High', title='AMD High Prices in January 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2012=df.loc[(df['Date'] >= '2012-02-01') & (df['Date'] < '2012-02-29')]
print(Feb2012)
Feb2012_mean=Feb2012['High'].mean()
print("Feb 2012 Mean High Price:", Feb2012_mean)
Feb2012.plot(x='Date', y='High', title='AMD High Prices in February 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2012=df.loc[(df['Date'] >= '2012-03-01') & (df['Date'] < '2012-03-31')]
print(Mar2012)
Mar2012_mean=Mar2012['High'].mean()
print("Mar 2012 Mean High Price:", Mar2012_mean)
Mar2012.plot(x='Date', y='High', title='AMD High Prices in March 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2012=df.loc[(df['Date'] >= '2012-04-01') & (df['Date'] < '2012-04-30')]
print(Apr2012)
Apr2012_mean=Apr2012['High'].mean()
print("Apr 2012 Mean High Price:", Apr2012_mean)
Apr2012.plot(x='Date', y='High', title='AMD High Prices in April 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2012=df.loc[(df['Date'] >= '2012-05-01') & (df['Date'] < '2012-05-31')]
print(May2012)
May2012_mean=May2012['High'].mean()
print("May 2012 Mean High Price:", May2012_mean)
May2012.plot(x='Date', y='High', title='AMD High Prices in May 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2012=df.loc[(df['Date'] >= '2012-06-01') & (df['Date'] < '2012-06-30')]
print(Jun2012)
Jun2012_mean=Jun2012['High'].mean()
print("Jun 2012 Mean High Price:", Jun2012_mean)
Jun2012.plot(x='Date', y='High', title='AMD High Prices in June 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2012=df.loc[(df['Date'] >= '2012-07-01') & (df['Date'] < '2012-07-31')]
print(Jul2012)
Jul2012_mean=Jul2012['High'].mean()
print("Jul 2012 Mean High Price:", Jul2012_mean)
Jul2012.plot(x='Date', y='High', title='AMD High Prices in July 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2012=df.loc[(df['Date'] >= '2012-08-01') & (df['Date'] < '2012-08-31')]
print(Aug2012)
Aug2012_mean=Aug2012['High'].mean()
print("Aug 2012 Mean High Price:", Aug2012_mean)
Aug2012.plot(x='Date', y='High', title='AMD High Prices in August 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2012=df.loc[(df['Date'] >= '2012-09-01') & (df['Date'] < '2012-09-30')]
print(Sep2012)
Sep2012_mean=Sep2012['High'].mean()
print("Sep 2012 Mean High Price:", Sep2012_mean)
Sep2012.plot(x='Date', y='High', title='AMD High Prices in September 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2012=df.loc[(df['Date'] >= '2012-10-01') & (df['Date'] < '2012-10-31')]
print(Oct2012)
Oct2012_mean=Oct2012['High'].mean()
print("Oct 2012 Mean High Price:", Oct2012_mean)
Oct2012.plot(x='Date', y='High', title='AMD High Prices in October 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2012=df.loc[(df['Date'] >= '2012-11-01') & (df['Date'] < '2012-11-30')]
print(Nov2012)
Nov2012_mean=Nov2012['High'].mean()
print("Nov 2012 Mean High Price:", Nov2012_mean)
Nov2012.plot(x='Date', y='High', title='AMD High Prices in November 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2012=df.loc[(df['Date'] >= '2012-12-01') & (df['Date'] < '2012-12-31')]
print(Dec2012)
Dec2012_mean=Dec2012['High'].mean()
print("Dec 2012 Mean High Price:", Dec2012_mean)
Dec2012.plot(x='Date', y='High', title='AMD High Prices in December 2012')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2013=df.loc[(df['Date'] >= '2013-01-01') & (df['Date'] < '2013-01-31')]
print(Jan2013)
Jan2013_mean=Jan2013['High'].mean()
print("Jan 2013 Mean High Price:", Jan2013_mean)
Jan2013.plot(x='Date', y='High', title='AMD High Prices in January 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2013=df.loc[(df['Date'] >= '2013-02-01') & (df['Date'] < '2013-02-28')]
print(Feb2013)
Feb2013_mean=Feb2013['High'].mean()
print("Feb 2013 Mean High Price:", Feb2013_mean)
Feb2013.plot(x='Date', y='High', title='AMD High Prices in February 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2013=df.loc[(df['Date'] >= '2013-03-01') & (df['Date'] < '2013-03-31')]
print(Mar2013)
Mar2013_mean=Mar2013['High'].mean()
print("Mar 2013 Mean High Price:", Mar2013_mean)
Mar2013.plot(x='Date', y='High', title='AMD High Prices in March 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2013=df.loc[(df['Date'] >= '2013-04-01') & (df['Date'] < '2013-04-30')]
print(Apr2013)
Apr2013_mean=Apr2013['High'].mean()
print("Apr 2013 Mean High Price:", Apr2013_mean)
Apr2013.plot(x='Date', y='High', title='AMD High Prices in April 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2013=df.loc[(df['Date'] >= '2013-05-01') & (df['Date'] < '2013-05-31')]
print(May2013)
May2013_mean=May2013['High'].mean()
print("May 2013 Mean High Price:", May2013_mean)
May2013.plot(x='Date', y='High', title='AMD High Prices in May 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2013=df.loc[(df['Date'] >= '2013-06-01') & (df['Date'] < '2013-06-30')]
print(Jun2013)
Jun2013_mean=Jun2013['High'].mean()
print("Jun 2013 Mean High Price:", Jun2013_mean)
Jun2013.plot(x='Date', y='High', title='AMD High Prices in June 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2013=df.loc[(df['Date'] >= '2013-07-01') & (df['Date'] < '2013-07-31')]
print(Jul2013)
Jul2013_mean=Jul2013['High'].mean()
print("Jul 2013 Mean High Price:", Jul2013_mean)
Jul2013.plot(x='Date', y='High', title='AMD High Prices in July 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2013=df.loc[(df['Date'] >= '2013-08-01') & (df['Date'] < '2013-08-31')]
print(Aug2013)
Aug2013_mean=Aug2013['High'].mean()
print("Aug 2013 Mean High Price:", Aug2013_mean)
Aug2013.plot(x='Date', y='High', title='AMD High Prices in August 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2013=df.loc[(df['Date'] >= '2013-09-01') & (df['Date'] < '2013-09-30')]
print(Sep2013)
Sep2013_mean=Sep2013['High'].mean()
print("Sep 2013 Mean High Price:", Sep2013_mean)
Sep2013.plot(x='Date', y='High', title='AMD High Prices in September 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2013=df.loc[(df['Date'] >= '2013-10-01') & (df['Date'] < '2013-10-31')]
print(Oct2013)
Oct2013_mean=Oct2013['High'].mean()
print("Oct 2013 Mean High Price:", Oct2013_mean)
Oct2013.plot(x='Date', y='High', title='AMD High Prices in October 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2013=df.loc[(df['Date'] >= '2013-11-01') & (df['Date'] < '2013-11-30')]
print(Nov2013)
Nov2013_mean=Nov2013['High'].mean()
print("Nov 2013 Mean High Price:", Nov2013_mean)
Nov2013.plot(x='Date', y='High', title='AMD High Prices in November 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2013=df.loc[(df['Date'] >= '2013-12-01') & (df['Date'] < '2013-12-31')]
print(Dec2013)
Dec2013_mean=Dec2013['High'].mean()
print("Dec 2013 Mean High Price:", Dec2013_mean)
Dec2013.plot(x='Date', y='High', title='AMD High Prices in December 2013')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2014=df.loc[(df['Date'] >= '2014-01-01') & (df['Date'] < '2014-01-31')]
print(Jan2014)
Jan2014_mean=Jan2014['High'].mean()
print("Jan 2014 Mean High Price:", Jan2014_mean)
Jan2014.plot(x='Date', y='High', title='AMD High Prices in January 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2014=df.loc[(df['Date'] >= '2014-02-01') & (df['Date'] < '2014-02-28')]
print(Feb2014)
Feb2014_mean=Feb2014['High'].mean()
print("Feb 2014 Mean High Price:", Feb2014_mean)
Feb2014.plot(x='Date', y='High', title='AMD High Prices in February 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2014=df.loc[(df['Date'] >= '2014-03-01') & (df['Date'] < '2014-03-31')]
print(Mar2014)
Mar2014_mean=Mar2014['High'].mean()
print("Mar 2014 Mean High Price:", Mar2014_mean)
Mar2014.plot(x='Date', y='High', title='AMD High Prices in March 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2014=df.loc[(df['Date'] >= '2014-04-01') & (df['Date'] < '2014-04-30')]
print(Apr2014)
Apr2014_mean=Apr2014['High'].mean()
print("Apr 2014 Mean High Price:", Apr2014_mean)
Apr2014.plot(x='Date', y='High', title='AMD High Prices in April 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2014=df.loc[(df['Date'] >= '2014-05-01') & (df['Date'] < '2014-05-31')]
print(May2014)
May2014_mean=May2014['High'].mean()
print("May 2014 Mean High Price:", May2014_mean)
May2014.plot(x='Date', y='High', title='AMD High Prices in May 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2014=df.loc[(df['Date'] >= '2014-06-01') & (df['Date'] < '2014-06-30')]
print(Jun2014)
Jun2014_mean=Jun2014['High'].mean()
print("Jun 2014 Mean High Price:", Jun2014_mean)
Jun2014.plot(x='Date', y='High', title='AMD High Prices in June 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2014=df.loc[(df['Date'] >= '2014-07-01') & (df['Date'] < '2014-07-31')]
print(Jul2014)
Jul2014_mean=Jul2014['High'].mean()
print("Jul 2014 Mean High Price:", Jul2014_mean)
Jul2014.plot(x='Date', y='High', title='AMD High Prices in July 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2014=df.loc[(df['Date'] >= '2014-08-01') & (df['Date'] < '2014-08-31')]
print(Aug2014)
Aug2014_mean=Aug2014['High'].mean()
print("Aug 2014 Mean High Price:", Aug2014_mean)
Aug2014.plot(x='Date', y='High', title='AMD High Prices in August 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2014=df.loc[(df['Date'] >= '2014-09-01') & (df['Date'] < '2014-09-30')]
print(Sep2014)
Sep2014_mean=Sep2014['High'].mean()
print("Sep 2014 Mean High Price:", Sep2014_mean)
Sep2014.plot(x='Date', y='High', title='AMD High Prices in September 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2014=df.loc[(df['Date'] >= '2014-10-01') & (df['Date'] < '2014-10-31')]
print(Oct2014)
Oct2014_mean=Oct2014['High'].mean()
print("Oct 2014 Mean High Price:", Oct2014_mean)
Oct2014.plot(x='Date', y='High', title='AMD High Prices in October 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2014=df.loc[(df['Date'] >= '2014-11-01') & (df['Date'] < '2014-11-30')]
print(Nov2014)
Nov2014_mean=Nov2014['High'].mean()
print("Nov 2014 Mean High Price:", Nov2014_mean)
Nov2014.plot(x='Date', y='High', title='AMD High Prices in November 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2014=df.loc[(df['Date'] >= '2014-12-01') & (df['Date'] < '2014-12-31')]
print(Dec2014)
Dec2014_mean=Dec2014['High'].mean()
print("Dec 2014 Mean High Price:", Dec2014_mean)
Dec2014.plot(x='Date', y='High', title='AMD High Prices in December 2014')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2015=df.loc[(df['Date'] >= '2015-01-01') & (df['Date'] < '2015-01-31')]
print(Jan2015)
Jan2015_mean=Jan2015['High'].mean()
print("Jan 2015 Mean High Price:", Jan2015_mean)
Jan2015.plot(x='Date', y='High', title='AMD High Prices in January 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2015=df.loc[(df['Date'] >= '2015-02-01') & (df['Date'] < '2015-02-28')]
print(Feb2015)
Feb2015_mean=Feb2015['High'].mean()
print("Feb 2015 Mean High Price:", Feb2015_mean)
Feb2015.plot(x='Date', y='High', title='AMD High Prices in February 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2015=df.loc[(df['Date'] >= '2015-03-01') & (df['Date'] < '2015-03-31')]
print(Mar2015)
Mar2015_mean=Mar2015['High'].mean()
print("Mar 2015 Mean High Price:", Mar2015_mean)
Mar2015.plot(x='Date', y='High', title='AMD High Prices in March 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2015=df.loc[(df['Date'] >= '2015-04-01') & (df['Date'] < '2015-04-30')]
print(Apr2015)
Apr2015_mean=Apr2015['High'].mean()
print("Apr 2015 Mean High Price:", Apr2015_mean)
Apr2015.plot(x='Date', y='High', title='AMD High Prices in April 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2015=df.loc[(df['Date'] >= '2015-05-01') & (df['Date'] < '2015-05-31')]
print(May2015)
May2015_mean=May2015['High'].mean()
print("May 2015 Mean High Price:", May2015_mean)
May2015.plot(x='Date', y='High', title='AMD High Prices in May 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2015=df.loc[(df['Date'] >= '2015-06-01') & (df['Date'] < '2015-06-30')]
print(Jun2015)
Jun2015_mean=Jun2015['High'].mean()
print("Jun 2015 Mean High Price:", Jun2015_mean)
Jun2015.plot(x='Date', y='High', title='AMD High Prices in June 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2015=df.loc[(df['Date'] >= '2015-07-01') & (df['Date'] < '2015-07-31')]
print(Jul2015)
Jul2015_mean=Jul2015['High'].mean()
print("Jul 2015 Mean High Price:", Jul2015_mean)
Jul2015.plot(x='Date', y='High', title='AMD High Prices in July 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2015=df.loc[(df['Date'] >= '2015-08-01') & (df['Date'] < '2015-08-31')]
print(Aug2015)
Aug2015_mean=Aug2015['High'].mean()
print("Aug 2015 Mean High Price:", Aug2015_mean)
Aug2015.plot(x='Date', y='High', title='AMD High Prices in August 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2015=df.loc[(df['Date'] >= '2015-09-01') & (df['Date'] < '2015-09-30')]
print(Sep2015)
Sep2015_mean=Sep2015['High'].mean()
print("Sep 2015 Mean High Price:", Sep2015_mean)
Sep2015.plot(x='Date', y='High', title='AMD High Prices in September 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2015=df.loc[(df['Date'] >= '2015-10-01') & (df['Date'] < '2015-10-31')]
print(Oct2015)
Oct2015_mean=Oct2015['High'].mean()
print("Oct 2015 Mean High Price:", Oct2015_mean)
Oct2015.plot(x='Date', y='High', title='AMD High Prices in October 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2015=df.loc[(df['Date'] >= '2015-11-01') & (df['Date'] < '2015-11-30')]
print(Nov2015)
Nov2015_mean=Nov2015['High'].mean()
print("Nov 2015 Mean High Price:", Nov2015_mean)
Nov2015.plot(x='Date', y='High', title='AMD High Prices in November 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2015=df.loc[(df['Date'] >= '2015-12-01') & (df['Date'] < '2015-12-31')]
print(Dec2015)
Dec2015_mean=Dec2015['High'].mean()
print("Dec 2015 Mean High Price:", Dec2015_mean)
Dec2015.plot(x='Date', y='High', title='AMD High Prices in December 2015')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2016=df.loc[(df['Date'] >= '2016-01-01') & (df['Date'] < '2016-01-31')]
print(Jan2016)
Jan2016_mean=Jan2016['High'].mean()
print("Jan 2016 Mean High Price:", Jan2016_mean)
Jan2016.plot(x='Date', y='High', title='AMD High Prices in January 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2016=df.loc[(df['Date'] >= '2016-02-01') & (df['Date'] < '2016-02-29')]
print(Feb2016)
Feb2016_mean=Feb2016['High'].mean()
print("Feb 2016 Mean High Price:", Feb2016_mean)
Feb2016.plot(x='Date', y='High', title='AMD High Prices in February 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2016=df.loc[(df['Date'] >= '2016-03-01') & (df['Date'] < '2016-03-31')]
print(Mar2016)
Mar2016_mean=Mar2016['High'].mean()
print("Mar 2016 Mean High Price:", Mar2016_mean)
Mar2016.plot(x='Date', y='High', title='AMD High Prices in March 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2016=df.loc[(df['Date'] >= '2016-04-01') & (df['Date'] < '2016-04-30')]
print(Apr2016)
Apr2016_mean=Apr2016['High'].mean()
print("Apr 2016 Mean High Price:", Apr2016_mean)
Apr2016.plot(x='Date', y='High', title='AMD High Prices in April 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2016=df.loc[(df['Date'] >= '2016-05-01') & (df['Date'] < '2016-05-31')]
print(May2016)
May2016_mean=May2016['High'].mean()
print("May 2016 Mean High Price:", May2016_mean)
May2016.plot(x='Date', y='High', title='AMD High Prices in May 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2016=df.loc[(df['Date'] >= '2016-06-01') & (df['Date'] < '2016-06-30')]
print(Jun2016)
Jun2016_mean=Jun2016['High'].mean()
print("Jun 2016 Mean High Price:", Jun2016_mean)
Jun2016.plot(x='Date', y='High', title='AMD High Prices in June 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2016=df.loc[(df['Date'] >= '2016-07-01') & (df['Date'] < '2016-07-31')]
print(Jul2016)
Jul2016_mean=Jul2016['High'].mean()
print("Jul 2016 Mean High Price:", Jul2016_mean)
Jul2016.plot(x='Date', y='High', title='AMD High Prices in July 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2016=df.loc[(df['Date'] >= '2016-08-01') & (df['Date'] < '2016-08-31')]
print(Aug2016)
Aug2016_mean=Aug2016['High'].mean()
print("Aug 2016 Mean High Price:", Aug2016_mean)
Aug2016.plot(x='Date', y='High', title='AMD High Prices in August 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2016=df.loc[(df['Date'] >= '2016-09-01') & (df['Date'] < '2016-09-30')]
print(Sep2016)
Sep2016_mean=Sep2016['High'].mean()
print("Sep 2016 Mean High Price:", Sep2016_mean)
Sep2016.plot(x='Date', y='High', title='AMD High Prices in September 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2016=df.loc[(df['Date'] >= '2016-10-01') & (df['Date'] < '2016-10-31')]
print(Oct2016)
Oct2016_mean=Oct2016['High'].mean()
print("Oct 2016 Mean High Price:", Oct2016_mean)
Oct2016.plot(x='Date', y='High', title='AMD High Prices in October 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2016=df.loc[(df['Date'] >= '2016-11-01') & (df['Date'] < '2016-11-30')]
print(Nov2016)
Nov2016_mean=Nov2016['High'].mean()
print("Nov 2016 Mean High Price:", Nov2016_mean)
Nov2016.plot(x='Date', y='High', title='AMD High Prices in November 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2016=df.loc[(df['Date'] >= '2016-12-01') & (df['Date'] < '2016-12-31')]
print(Dec2016)
Dec2016_mean=Dec2016['High'].mean()
print("Dec 2016 Mean High Price:", Dec2016_mean)
Dec2016.plot(x='Date', y='High', title='AMD High Prices in December 2016')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2017=df.loc[(df['Date'] >= '2017-01-01') & (df['Date'] < '2017-01-31')]
print(Jan2017)
Jan2017_mean=Jan2017['High'].mean()
print("Jan 2017 Mean High Price:", Jan2017_mean)
Jan2017.plot(x='Date', y='High', title='AMD High Prices in January 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2017=df.loc[(df['Date'] >= '2017-02-01') & (df['Date'] < '2017-02-28')]
print(Feb2017)
Feb2017_mean=Feb2017['High'].mean()
print("Feb 2017 Mean High Price:", Feb2017_mean)
Feb2017.plot(x='Date', y='High', title='AMD High Prices in February 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2017=df.loc[(df['Date'] >= '2017-03-01') & (df['Date'] < '2017-03-31')]
print(Mar2017)
Mar2017_mean=Mar2017['High'].mean()
print("Mar 2017 Mean High Price:", Mar2017_mean)
Mar2017.plot(x='Date', y='High', title='AMD High Prices in March 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2017=df.loc[(df['Date'] >= '2017-04-01') & (df['Date'] < '2017-04-30')]
print(Apr2017)
Apr2017_mean=Apr2017['High'].mean()
print("Apr 2017 Mean High Price:", Apr2017_mean)
Apr2017.plot(x='Date', y='High', title='AMD High Prices in April 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2017=df.loc[(df['Date'] >= '2017-05-01') & (df['Date'] < '2017-05-31')]
print(May2017)
May2017_mean=May2017['High'].mean()
print("May 2017 Mean High Price:", May2017_mean)
May2017.plot(x='Date', y='High', title='AMD High Prices in May 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2017=df.loc[(df['Date'] >= '2017-06-01') & (df['Date'] < '2017-06-30')]
print(Jun2017)
Jun2017_mean=Jun2017['High'].mean()
print("Jun 2017 Mean High Price:", Jun2017_mean)
Jun2017.plot(x='Date', y='High', title='AMD High Prices in June 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2017=df.loc[(df['Date'] >= '2017-07-01') & (df['Date'] < '2017-07-31')]
print(Jul2017)
Jul2017_mean=Jul2017['High'].mean()
print("Jul 2017 Mean High Price:", Jul2017_mean)
Jul2017.plot(x='Date', y='High', title='AMD High Prices in July 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2017=df.loc[(df['Date'] >= '2017-08-01') & (df['Date'] < '2017-08-31')]
print(Aug2017)
Aug2017_mean=Aug2017['High'].mean()
print("Aug 2017 Mean High Price:", Aug2017_mean)
Aug2017.plot(x='Date', y='High', title='AMD High Prices in August 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2017=df.loc[(df['Date'] >= '2017-09-01') & (df['Date'] < '2017-09-30')]
print(Sep2017)
Sep2017_mean=Sep2017['High'].mean()
print("Sep 2017 Mean High Price:", Sep2017_mean)
Sep2017.plot(x='Date', y='High', title='AMD High Prices in September 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2017=df.loc[(df['Date'] >= '2017-10-01') & (df['Date'] < '2017-10-31')]
print(Oct2017)
Oct2017_mean=Oct2017['High'].mean()
print("Oct 2017 Mean High Price:", Oct2017_mean)
Oct2017.plot(x='Date', y='High', title='AMD High Prices in October 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2017=df.loc[(df['Date'] >= '2017-11-01') & (df['Date'] < '2017-11-30')]
print(Nov2017)
Nov2017_mean=Nov2017['High'].mean()
print("Nov 2017 Mean High Price:", Nov2017_mean)
Nov2017.plot(x='Date', y='High', title='AMD High Prices in November 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2017=df.loc[(df['Date'] >= '2017-12-01') & (df['Date'] < '2017-12-31')]
print(Dec2017)
Dec2017_mean=Dec2017['High'].mean()
print("Dec 2017 Mean High Price:", Dec2017_mean)
Dec2017.plot(x='Date', y='High', title='AMD High Prices in December 2017')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2018=df.loc[(df['Date'] >= '2018-01-01') & (df['Date'] < '2018-01-31')]
print(Jan2018)
Jan2018_mean=Jan2018['High'].mean()
print("Jan 2018 Mean High Price:", Jan2018_mean)
Jan2018.plot(x='Date', y='High', title='AMD High Prices in January 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2018=df.loc[(df['Date'] >= '2018-02-01') & (df['Date'] < '2018-02-28')]
print(Feb2018)
Feb2018_mean=Feb2018['High'].mean()
print("Feb 2018 Mean High Price:", Feb2018_mean)
Feb2018.plot(x='Date', y='High', title='AMD High Prices in February 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2018=df.loc[(df['Date'] >= '2018-03-01') & (df['Date'] < '2018-03-31')]
print(Mar2018)
Mar2018_mean=Mar2018['High'].mean()
print("Mar 2018 Mean High Price:", Mar2018_mean)
Mar2018.plot(x='Date', y='High', title='AMD High Prices in March 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2018=df.loc[(df['Date'] >= '2018-04-01') & (df['Date'] < '2018-04-30')]
print(Apr2018)
Apr2018_mean=Apr2018['High'].mean()
print("Apr 2018 Mean High Price:", Apr2018_mean)
Apr2018.plot(x='Date', y='High', title='AMD High Prices in April 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2018=df.loc[(df['Date'] >= '2018-05-01') & (df['Date'] < '2018-05-31')]
print(May2018)
May2018_mean=May2018['High'].mean()
print("May 2018 Mean High Price:", May2018_mean)
May2018.plot(x='Date', y='High', title='AMD High Prices in May 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2018=df.loc[(df['Date'] >= '2018-06-01') & (df['Date'] < '2018-06-30')]
print(Jun2018)
Jun2018_mean=Jun2018['High'].mean()
print("Jun 2018 Mean High Price:", Jun2018_mean)
Jun2018.plot(x='Date', y='High', title='AMD High Prices in June 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2018=df.loc[(df['Date'] >= '2018-07-01') & (df['Date'] < '2018-07-31')]
print(Jul2018)
Jul2018_mean=Jul2018['High'].mean()
print("Jul 2018 Mean High Price:", Jul2018_mean)
Jul2018.plot(x='Date', y='High', title='AMD High Prices in July 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2018=df.loc[(df['Date'] >= '2018-08-01') & (df['Date'] < '2018-08-31')]
print(Aug2018)
Aug2018_mean=Aug2018['High'].mean()
print("Aug 2018 Mean High Price:", Aug2018_mean)
Aug2018.plot(x='Date', y='High', title='AMD High Prices in August 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2018=df.loc[(df['Date'] >= '2018-09-01') & (df['Date'] < '2018-09-30')]
print(Sep2018)
Sep2018_mean=Jan2018['High'].mean()
print("Sep 2018 Mean High Price:", Sep2018_mean)
Sep2018.plot(x='Date', y='High', title='AMD High Prices in September 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2018=df.loc[(df['Date'] >= '2018-10-01') & (df['Date'] < '2018-10-31')]
print(Oct2018)
Oct2018_mean=Oct2018['High'].mean()
print("Oct 2018 Mean High Price:", Oct2018_mean)
Oct2018.plot(x='Date', y='High', title='AMD High Prices in October 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2018=df.loc[(df['Date'] >= '2018-11-01') & (df['Date'] < '2018-11-30')]
print(Nov2018)
Nov2018_mean=Nov2018['High'].mean()
print("Nov 2018 Mean High Price:", Nov2018_mean)
Nov2018.plot(x='Date', y='High', title='AMD High Prices in November 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2018=df.loc[(df['Date'] >= '2018-12-01') & (df['Date'] < '2018-12-31')]
print(Dec2018)
Dec2018_mean=Dec2018['High'].mean()
print("Dec 2018 Mean High Price:", Dec2018_mean)
Dec2018.plot(x='Date', y='High', title='AMD High Prices in December 2018')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2019=df.loc[(df['Date'] >= '2019-01-01') & (df['Date'] < '2019-01-31')]
print(Jan2019)
Jan2019_mean=Jan2019['High'].mean()
print("Jan 2019 Mean High Price:", Jan2019_mean)
Jan2019.plot(x='Date', y='High', title='AMD High Prices in January 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2019=df.loc[(df['Date'] >= '2019-02-01') & (df['Date'] < '2019-02-28')]
print(Feb2019)
Feb2019_mean=Feb2019['High'].mean()
print("Feb 2019 Mean High Price:", Feb2019_mean)
Feb2019.plot(x='Date', y='High', title='AMD High Prices in February 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2019=df.loc[(df['Date'] >= '2019-03-01') & (df['Date'] < '2019-03-31')]
print(Mar2019)
Mar2019_mean=Mar2019['High'].mean()
print("Mar 2019 Mean High Price:", Mar2019_mean)
Mar2019.plot(x='Date', y='High', title='AMD High Prices in March 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2019=df.loc[(df['Date'] >= '2019-04-01') & (df['Date'] < '2019-04-30')]
print(Apr2019)
Apr2019_mean=Apr2019['High'].mean()
print("Apr 2019 Mean High Price:", Apr2019_mean)
Apr2019.plot(x='Date', y='High', title='AMD High Prices in April 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2019=df.loc[(df['Date'] >= '2019-05-01') & (df['Date'] < '2019-05-31')]
print(May2019)
May2019_mean=May2019['High'].mean()
print("May 2019 Mean High Price:", May2019_mean)
May2019.plot(x='Date', y='High', title='AMD High Prices in May 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2019=df.loc[(df['Date'] >= '2019-06-01') & (df['Date'] < '2019-06-30')]
print(Jun2019)
Jun2019_mean=Jun2019['High'].mean()
print("Jun 2019 Mean High Price:", Jun2019_mean)
Jun2019.plot(x='Date', y='High', title='AMD High Prices in June 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2019=df.loc[(df['Date'] >= '2019-07-01') & (df['Date'] < '2019-07-31')]
print(Jul2019)
Jul2019_mean=Jul2019['High'].mean()
print("Jul 2019 Mean High Price:", Jul2019_mean)
Jul2019.plot(x='Date', y='High', title='AMD High Prices in July 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2019=df.loc[(df['Date'] >= '2019-08-01') & (df['Date'] < '2019-08-31')]
print(Aug2019)
Aug2019_mean=Aug2019['High'].mean()
print("Aug 2019 Mean High Price:", Aug2019_mean)
Aug2019.plot(x='Date', y='High', title='AMD High Prices in August 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2019=df.loc[(df['Date'] >= '2019-09-01') & (df['Date'] < '2019-09-30')]
print(Sep2019)
Sep2019_mean=Sep2019['High'].mean()
print("Sep 2019 Mean High Price:", Sep2019_mean)
Sep2019.plot(x='Date', y='High', title='AMD High Prices in September 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2019=df.loc[(df['Date'] >= '2019-10-01') & (df['Date'] < '2019-10-31')]
print(Oct2019)
Oct2019_mean=Oct2019['High'].mean()
print("Oct 2019 Mean High Price:", Oct2019_mean)
Oct2019.plot(x='Date', y='High', title='AMD High Prices in October 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2019=df.loc[(df['Date'] >= '2019-11-01') & (df['Date'] < '2019-11-30')]
print(Nov2019)
Nov2019_mean=Nov2019['High'].mean()
print("Nov 2019 Mean High Price:", Nov2019_mean)
Nov2019.plot(x='Date', y='High', title='AMD High Prices in November 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2019=df.loc[(df['Date'] >= '2019-12-01') & (df['Date'] < '2019-12-31')]
print(Dec2019)
Dec2019_mean=Dec2019['High'].mean()
print("Dec 2019 Mean High Price:", Dec2019_mean)
Dec2019.plot(x='Date', y='High', title='AMD High Prices in December 2019')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2020=df.loc[(df['Date'] >= '2020-01-01') & (df['Date'] < '2020-01-31')]
print(Jan2020)
Jan2020_mean=Jan2020['High'].mean()
print("Jan 2020 Mean High Price:", Jan2020_mean)
Jan2020.plot(x='Date', y='High', title='AMD High Prices in January 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2020=df.loc[(df['Date'] >= '2020-02-01') & (df['Date'] < '2020-02-29')]
print(Feb2020)
Feb2020_mean=Feb2020['High'].mean()
print("Feb 2020 Mean High Price:", Feb2020_mean)
Feb2020.plot(x='Date', y='High', title='AMD High Prices in February 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2020=df.loc[(df['Date'] >= '2020-03-01') & (df['Date'] < '2020-03-31')]
print(Mar2020)
Mar2020_mean=Mar2020['High'].mean()
print("Mar 2020 Mean High Price:", Mar2020_mean)
Mar2020.plot(x='Date', y='High', title='AMD High Prices in March 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2020=df.loc[(df['Date'] >= '2020-04-01') & (df['Date'] < '2020-04-30')]
print(Apr2020)
Apr2020_mean=Apr2020['High'].mean()
print("Apr 2020 Mean High Price:", Apr2020_mean)
Apr2020.plot(x='Date', y='High', title='AMD High Prices in April 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2020=df.loc[(df['Date'] >= '2020-05-01') & (df['Date'] < '2020-05-31')]
print(May2020)
May2020_mean=May2020['High'].mean()
print("May 2020 Mean High Price:", May2020_mean)
May2020.plot(x='Date', y='High', title='AMD High Prices in May 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2020=df.loc[(df['Date'] >= '2020-06-01') & (df['Date'] < '2020-06-30')]
print(Jun2020)
Jun2020_mean=Jun2020['High'].mean()
print("Jun 2020 Mean High Price:", Jun2020_mean)
Jun2020.plot(x='Date', y='High', title='AMD High Prices in June 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2020=df.loc[(df['Date'] >= '2020-07-01') & (df['Date'] < '2020-07-31')]
print(Jul2020)
Jul2020_mean=Jul2020['High'].mean()
print("Jul 2020 Mean High Price:", Jul2020_mean)
Jul2020.plot(x='Date', y='High', title='AMD High Prices in July 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2020=df.loc[(df['Date'] >= '2020-08-01') & (df['Date'] < '2020-08-31')]
print(Aug2020)
Aug2020_mean=Aug2020['High'].mean()
print("Aug 2020 Mean High Price:", Aug2020_mean)
Aug2020.plot(x='Date', y='High', title='AMD High Prices in August 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2020=df.loc[(df['Date'] >= '2020-09-01') & (df['Date'] < '2020-09-30')]
print(Sep2020)
Sep2020_mean=Sep2020['High'].mean()
print("Sep 2020 Mean High Price:", Sep2020_mean)
Sep2020.plot(x='Date', y='High', title='AMD High Prices in September 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2020=df.loc[(df['Date'] >= '2020-10-01') & (df['Date'] < '2020-10-31')]
print(Oct2020)
Oct2020_mean=Oct2020['High'].mean()
print("Oct 2020 Mean High Price:", Oct2020_mean)
Oct2020.plot(x='Date', y='High', title='AMD High Prices in October 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2020=df.loc[(df['Date'] >= '2020-11-01') & (df['Date'] < '2020-11-30')]
print(Nov2020)
Nov2020_mean=Nov2020['High'].mean()
print("Nov 2020 Mean High Price:", Nov2020_mean)
Nov2020.plot(x='Date', y='High', title='AMD High Prices in November 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2020=df.loc[(df['Date'] >= '2020-12-01') & (df['Date'] < '2020-12-31')]
print(Dec2020)
Dec2020_mean=Dec2020['High'].mean()
print("Dec 2020 Mean High Price:", Dec2020_mean)
Dec2020.plot(x='Date', y='High', title='AMD High Prices in December 2020')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2021=df.loc[(df['Date'] >= '2021-01-01') & (df['Date'] < '2021-01-31')]
print(Jan2021)
Jan2021_mean=Jan2021['High'].mean()
print("Jan 2021 Mean High Price:", Jan2021_mean)
Jan2021.plot(x='Date', y='High', title='AMD High Prices in January 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2021=df.loc[(df['Date'] >= '2021-02-01') & (df['Date'] < '2021-02-28')]
print(Feb2021)
Feb2021_mean=Feb2021['High'].mean()
print("Feb 2021 Mean High Price:", Feb2021_mean)
Feb2021.plot(x='Date', y='High', title='AMD High Prices in February 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2021=df.loc[(df['Date'] >= '2021-03-01') & (df['Date'] < '2021-03-31')]
print(Mar2021)
Mar2021_mean=Mar2021['High'].mean()
print("Mar 2021 Mean High Price:", Mar2021_mean)
Mar2021.plot(x='Date', y='High', title='AMD High Prices in March 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2021=df.loc[(df['Date'] >= '2021-04-01') & (df['Date'] < '2021-04-30')]
print(Apr2021)
Apr2021_mean=Apr2021['High'].mean()
print("Apr 2021 Mean High Price:", Apr2021_mean)
Apr2021.plot(x='Date', y='High', title='AMD High Prices in April 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2021=df.loc[(df['Date'] >= '2021-05-01') & (df['Date'] < '2021-05-31')]
print(May2021)
May2021_mean=May2021['High'].mean()
print("May 2021 Mean High Price:", May2021_mean)
May2021.plot(x='Date', y='High', title='AMD High Prices in May 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2021=df.loc[(df['Date'] >= '2021-06-01') & (df['Date'] < '2021-06-30')]
print(Jun2021)
Jun2021_mean=Jun2021['High'].mean()
print("Jun 2021 Mean High Price:", Jun2021_mean)
Jun2021.plot(x='Date', y='High', title='AMD High Prices in June 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2021=df.loc[(df['Date'] >= '2021-07-01') & (df['Date'] < '2021-07-31')]
print(Jul2021)
Jul2021_mean=Jul2021['High'].mean()
print("Jul 2021 Mean High Price:", Jul2021_mean)
Jul2021.plot(x='Date', y='High', title='AMD High Prices in July 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2021=df.loc[(df['Date'] >= '2021-08-01') & (df['Date'] < '2021-08-31')]
print(Aug2021)
Aug2021_mean=Aug2021['High'].mean()
print("Aug 2021 Mean High Price:", Aug2021_mean)
Aug2021.plot(x='Date', y='High', title='AMD High Prices in August 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2021=df.loc[(df['Date'] >= '2021-09-01') & (df['Date'] < '2021-09-30')]
print(Sep2021)
Sep2021_mean=Sep2021['High'].mean()
print("Sep 2021 Mean High Price:", Sep2021_mean)
Sep2021.plot(x='Date', y='High', title='AMD High Prices in September 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2021=df.loc[(df['Date'] >= '2021-10-01') & (df['Date'] < '2021-10-31')]
print(Oct2021)
Oct2021_mean=Oct2021['High'].mean()
print("Oct 2021 Mean High Price:", Oct2021_mean)
Oct2021.plot(x='Date', y='High', title='AMD High Prices in October 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2021=df.loc[(df['Date'] >= '2021-11-01') & (df['Date'] < '2021-11-30')]
print(Nov2021)
Nov2021_mean=Nov2021['High'].mean()
print("Nov 2021 Mean High Price:", Nov2021_mean)
Nov2021.plot(x='Date', y='High', title='AMD High Prices in November 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2021=df.loc[(df['Date'] >= '2021-12-01') & (df['Date'] < '2021-12-31')]
print(Dec2021)
Dec2021_mean=Dec2021['High'].mean()
print("Dec 2021 Mean High Price:", Dec2021_mean)
Dec2021.plot(x='Date', y='High', title='AMD High Prices in December 2021')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2022=df.loc[(df['Date'] >= '2022-01-01') & (df['Date'] < '2022-01-31')]
print(Jan2022)
Jan2022_mean=Jan2022['High'].mean()
print("Jan 2022 Mean High Price:", Jan2022_mean)
Jan2022.plot(x='Date', y='High', title='AMD High Prices in January 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2022=df.loc[(df['Date'] >= '2022-02-01') & (df['Date'] < '2022-02-28')]
print(Feb2022)
Feb2022_mean=Feb2022['High'].mean()
print("Feb 2022 Mean High Price:", Feb2022_mean)
Feb2022.plot(x='Date', y='High', title='AMD High Prices in February 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2022=df.loc[(df['Date'] >= '2022-03-01') & (df['Date'] < '2022-03-31')]
print(Mar2022)
Mar2022_mean=Mar2022['High'].mean()
print("Mar 2022 Mean High Price:", Mar2022_mean)
Mar2022.plot(x='Date', y='High', title='AMD High Prices in March 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2022=df.loc[(df['Date'] >= '2022-04-01') & (df['Date'] < '2022-04-30')]
print(Apr2022)
Apr2022_mean=Apr2022['High'].mean()
print("Apr 2022 Mean High Price:", Apr2022_mean)
Apr2022.plot(x='Date', y='High', title='AMD High Prices in April 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2022=df.loc[(df['Date'] >= '2022-05-01') & (df['Date'] < '2022-05-31')]
print(May2022)
May2022_mean=May2022['High'].mean()
print("May 2022 Mean High Price:", May2022_mean)
May2022.plot(x='Date', y='High', title='AMD High Prices in May 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2022=df.loc[(df['Date'] >= '2022-06-01') & (df['Date'] < '2022-06-30')]
print(Jun2022)
Jun2022_mean=Jun2022['High'].mean()
print("Jun 2022 Mean High Price:", Jun2022_mean)
Jun2022.plot(x='Date', y='High', title='AMD High Prices in June 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2022=df.loc[(df['Date'] >= '2022-07-01') & (df['Date'] < '2022-07-31')]
print(Jul2022)
Jul2022_mean=Jul2022['High'].mean()
print("Jul 2022 Mean High Price:", Jul2022_mean)
Jul2022.plot(x='Date', y='High', title='AMD High Prices in July 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2022=df.loc[(df['Date'] >= '2022-08-01') & (df['Date'] < '2022-08-31')]
print(Aug2022)
Aug2022_mean=Aug2022['High'].mean()
print("Aug 2022 Mean High Price:", Aug2022_mean)
Aug2022.plot(x='Date', y='High', title='AMD High Prices in August 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2022=df.loc[(df['Date'] >= '2022-09-01') & (df['Date'] < '2022-09-30')]
print(Sep2022)
Sep2022_mean=Sep2022['High'].mean()
print("Sep 2022 Mean High Price:", Sep2022_mean)
Sep2022.plot(x='Date', y='High', title='AMD High Prices in September 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2022=df.loc[(df['Date'] >= '2022-10-01') & (df['Date'] < '2022-10-31')]
print(Oct2022)
Oct2022_mean=Oct2022['High'].mean()
print("Oct 2022 Mean High Price:", Oct2022_mean)
Oct2022.plot(x='Date', y='High', title='AMD High Prices in October 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2022=df.loc[(df['Date'] >= '2022-11-01') & (df['Date'] < '2022-11-30')]
print(Nov2022)
Nov2022_mean=Nov2022['High'].mean()
print("Nov 2022 Mean High Price:", Nov2022_mean)
Nov2022.plot(x='Date', y='High', title='AMD High Prices in November 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2022=df.loc[(df['Date'] >= '2022-12-01') & (df['Date'] < '2022-12-31')]
print(Dec2022)
Dec2022_mean=Dec2022['High'].mean()
print("Dec 2022 Mean High Price:", Dec2022_mean)
Dec2022.plot(x='Date', y='High', title='AMD High Prices in December 2022')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2023=df.loc[(df['Date'] >= '2023-01-01') & (df['Date'] < '2023-01-31')]
print(Jan2023)
Jan2023_mean=Jan2023['High'].mean()
print("Jan 2023 Mean High Price:", Jan2023_mean)
Jan2023.plot(x='Date', y='High', title='AMD High Prices in January 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2023=df.loc[(df['Date'] >= '2023-02-01') & (df['Date'] < '2023-02-28')]
print(Feb2023)
Feb2023_mean=Feb2023['High'].mean()
print("Feb 2023 Mean High Price:", Feb2023_mean)
Feb2023.plot(x='Date', y='High', title='AMD High Prices in February 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2023=df.loc[(df['Date'] >= '2023-03-01') & (df['Date'] < '2023-03-31')]
print(Mar2023)
Mar2023_mean=Mar2023['High'].mean()
print("Mar 2023 Mean High Price:", Mar2023_mean)
Mar2023.plot(x='Date', y='High', title='AMD High Prices in March 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2023=df.loc[(df['Date'] >= '2023-04-01') & (df['Date'] < '2023-04-30')]
print(Apr2023)
Apr2023_mean=Apr2023['High'].mean()
print("Apr 2023 Mean High Price:", Apr2023_mean)
Apr2023.plot(x='Date', y='High', title='AMD High Prices in April 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2023=df.loc[(df['Date'] >= '2023-05-01') & (df['Date'] < '2023-05-31')]
print(May2023)
May2023_mean=May2023['High'].mean()
print("May 2023 Mean High Price:", May2023_mean)
May2023.plot(x='Date', y='High', title='AMD High Prices in May 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2023=df.loc[(df['Date'] >= '2023-06-01') & (df['Date'] < '2023-06-30')]
print(Jun2023)
Jun2023_mean=Jun2023['High'].mean()
print("Jun 2023 Mean High Price:", Jun2023_mean)
Jun2023.plot(x='Date', y='High', title='AMD High Prices in June 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2023=df.loc[(df['Date'] >= '2023-07-01') & (df['Date'] < '2023-07-31')]
print(Jul2023)
Jul2023_mean=Jul2023['High'].mean()
print("Jul 2023 Mean High Price:", Jul2023_mean)
Jul2023.plot(x='Date', y='High', title='AMD High Prices in July 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2023=df.loc[(df['Date'] >= '2023-08-01') & (df['Date'] < '2023-08-31')]
print(Aug2023)
Aug2023_mean=Aug2023['High'].mean()
print("Aug 2023 Mean High Price:", Aug2023_mean)
Aug2023.plot(x='Date', y='High', title='AMD High Prices in August 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2023=df.loc[(df['Date'] >= '2023-09-01') & (df['Date'] < '2023-09-30')]
print(Sep2023)
Sep2023_mean=Sep2023['High'].mean()
print("Sep 2023 Mean High Price:", Sep2023_mean)
Sep2023.plot(x='Date', y='High', title='AMD High Prices in September 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2023=df.loc[(df['Date'] >= '2023-10-01') & (df['Date'] < '2023-10-31')]
print(Oct2023)
Oct2023_mean=Oct2023['High'].mean()
print("Oct 2023 Mean High Price:", Oct2023_mean)
Oct2023.plot(x='Date', y='High', title='AMD High Prices in October 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2023=df.loc[(df['Date'] >= '2023-11-01') & (df['Date'] < '2023-11-30')]
print(Nov2023)
Nov2023_mean=Nov2023['High'].mean()
print("Nov 2023 Mean High Price:", Nov2023_mean)
Nov2023.plot(x='Date', y='High', title='AMD High Prices in November 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2023=df.loc[(df['Date'] >= '2023-12-01') & (df['Date'] < '2023-12-31')]
print(Dec2023)
Dec2023_mean=Dec2023['High'].mean()
print("Dec 2023 Mean High Price:", Dec2023_mean)
Dec2023.plot(x='Date', y='High', title='AMD High Prices in December 2023')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2024=df.loc[(df['Date'] >= '2024-01-01') & (df['Date'] < '2024-01-31')]
print(Jan2024)
Jan2024_mean=Jan2024['High'].mean()
print("Jan 2024 Mean High Price:", Jan2024_mean)
Jan2024.plot(x='Date', y='High', title='AMD High Prices in January 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2024=df.loc[(df['Date'] >= '2024-02-01') & (df['Date'] < '2024-02-29')]
print(Feb2024)
Feb2024_mean=Feb2024['High'].mean()
print("Feb 2024 Mean High Price:", Feb2024_mean)
Feb2024.plot(x='Date', y='High', title='AMD High Prices in February 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2024=df.loc[(df['Date'] >= '2024-03-01') & (df['Date'] < '2024-03-31')]
print(Mar2024)
Mar2024_mean=Mar2024['High'].mean()
print("Mar 2024 Mean High Price:", Mar2024_mean)
Mar2024.plot(x='Date', y='High', title='AMD High Prices in March 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2024=df.loc[(df['Date'] >= '2024-04-01') & (df['Date'] < '2024-04-30')]
print(Apr2024)
Apr2024_mean=Apr2024['High'].mean()
print("Apr 2024 Mean High Price:", Apr2024_mean)
Apr2024.plot(x='Date', y='High', title='AMD High Prices in April 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2024=df.loc[(df['Date'] >= '2024-05-01') & (df['Date'] < '2024-05-31')]
print(May2024)
May2024_mean=May2024['High'].mean()
print("May 2024 Mean High Price:", May2024_mean)
May2024.plot(x='Date', y='High', title='AMD High Prices in May 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2024=df.loc[(df['Date'] >= '2024-06-01') & (df['Date'] < '2024-06-30')]
print(Jun2024)
Jun2024_mean=Jun2024['High'].mean()
print("Jun 2024 Mean High Price:", Jun2024_mean)
Jun2024.plot(x='Date', y='High', title='AMD High Prices in June 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2024=df.loc[(df['Date'] >= '2024-07-01') & (df['Date'] < '2024-07-31')]
print(Jul2024)
Jul2024_mean=Jul2024['High'].mean()
print("Jul 2024 Mean High Price:", Jul2024_mean)
Jul2024.plot(x='Date', y='High', title='AMD High Prices in July 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2024=df.loc[(df['Date'] >= '2024-08-01') & (df['Date'] < '2024-08-31')]
print(Aug2024)
Aug2024_mean=Aug2024['High'].mean()
print("Aug 2024 Mean High Price:", Aug2024_mean)
Aug2024.plot(x='Date', y='High', title='AMD High Prices in August 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2024=df.loc[(df['Date'] >= '2024-09-01') & (df['Date'] < '2024-09-30')]
print(Sep2024)
Sep2024_mean=Sep2024['High'].mean()
print("Sep 2024 Mean High Price:", Sep2024_mean)
Sep2024.plot(x='Date', y='High', title='AMD High Prices in September 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2024=df.loc[(df['Date'] >= '2024-10-01') & (df['Date'] < '2024-10-31')]
print(Oct2024)
Oct2024_mean=Oct2024['High'].mean()
print("Oct 2024 Mean High Price:", Oct2024_mean)
Oct2024.plot(x='Date', y='High', title='AMD High Prices in October 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2024=df.loc[(df['Date'] >= '2024-11-01') & (df['Date'] < '2024-11-30')]
print(Nov2024)
Nov2024_mean=Nov2024['High'].mean()
print("Nov 2024 Mean High Price:", Nov2024_mean)
Nov2024.plot(x='Date', y='High', title='AMD High Prices in November 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2024=df.loc[(df['Date'] >= '2024-12-01') & (df['Date'] < '2024-12-31')]
print(Dec2024)
Dec2024_mean=Dec2024['High'].mean()
print("Dec 2024 Mean High Price:", Dec2024_mean)
Dec2024.plot(x='Date', y='High', title='AMD High Prices in December 2024')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2025=df.loc[(df['Date'] >= '2025-01-01') & (df['Date'] < '2025-01-31')]
print(Jan2025)
Jan2025_mean=Jan2025['High'].mean()
print("Jan 2025 Mean High Price:", Jan2025_mean)
Jan2025.plot(x='Date', y='High', title='AMD High Prices in January 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2025=df.loc[(df['Date'] >= '2025-02-01') & (df['Date'] < '2025-02-28')]
print(Feb2025)
Feb2025_mean=Feb2025['High'].mean()
print("Feb 2025 Mean High Price:", Feb2025_mean)
Feb2025.plot(x='Date', y='High', title='AMD High Prices in February 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2025=df.loc[(df['Date'] >= '2025-03-01') & (df['Date'] < '2025-03-31')]
print(Mar2025)
Mar2025_mean=Mar2025['High'].mean()
print("Mar 2025 Mean High Price:", Mar2025_mean)
Mar2025.plot(x='Date', y='High', title='AMD High Prices in March 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2025=df.loc[(df['Date'] >= '2025-04-01') & (df['Date'] < '2025-04-30')]
print(Apr2025)
Apr2025_mean=Apr2025['High'].mean()
print("Apr 2025 Mean High Price:", Apr2025_mean)
Apr2025.plot(x='Date', y='High', title='AMD High Prices in April 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2025=df.loc[(df['Date'] >= '2025-05-01') & (df['Date'] < '2025-05-31')]
print(May2025)
May2025_mean=May2025['High'].mean()
print("May 2025 Mean High Price:", May2025_mean)
May2025.plot(x='Date', y='High', title='AMD High Prices in May 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2025=df.loc[(df['Date'] >= '2025-06-01') & (df['Date'] < '2025-06-30')]
print(Jun2025)
Jun2025_mean=Jun2025['High'].mean()
print("Jun 2025 Mean High Price:", Jun2025_mean)
Jun2025.plot(x='Date', y='High', title='AMD High Prices in June 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2025=df.loc[(df['Date'] >= '2025-07-01') & (df['Date'] < '2025-07-31')]
print(Jul2025)
Jul2025_mean=Jul2025['High'].mean()
print("Jul 2025 Mean High Price:", Jul2025_mean)
Jul2025.plot(x='Date', y='High', title='AMD High Prices in July 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2025=df.loc[(df['Date'] >= '2025-08-01') & (df['Date'] < '2025-08-31')]
print(Aug2025)
Aug2025_mean=Aug2025['High'].mean()
print("Aug 2025 Mean High Price:", Aug2025_mean)
Aug2025.plot(x='Date', y='High', title='AMD High Prices in August 2025')
plt.xlabel('Date')
plt.ylabel('High Price')

plt.show()

#Month wise Low Prices are mentioned below

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1992=df.loc[(df['Date'] >= '1992-02-01') & (df['Date'] < '1992-02-29')]
print(Feb1992)
Feb1992_mean=Feb1992['Low'].mean()
print("Feb 1992 Mean Low Price:", Feb1992_mean)
Feb1992.plot(x='Date', y='Low', title='AMD Low Prices in February 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1992=df.loc[(df['Date'] >= '1992-03-01') & (df['Date'] < '1992-03-31')]
print(Mar1992)
Mar1992_mean=Mar1992['Low'].mean()
print("Mar 1992 Mean Low Price:", Mar1992_mean)
Mar1992.plot(x='Date', y='Low', title='AMD Low Prices in March 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1992=df.loc[(df['Date'] >= '1992-04-01') & (df['Date'] < '1992-04-30')]
print(Apr1992)
Apr1992_mean=Apr1992['Low'].mean()
print("Apr 1992 Mean Low Price:", Apr1992_mean)
Apr1992.plot(x='Date', y='Low', title='AMD Low Prices in April 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1992=df.loc[(df['Date'] >= '1992-05-01') & (df['Date'] < '1992-05-31')]
print(May1992)
May1992_mean=May1992['Low'].mean()
print("May 1992 Mean Low Price:", May1992_mean)
May1992.plot(x='Date', y='Low', title='AMD Low Prices in May 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1992=df.loc[(df['Date'] >= '1992-06-01') & (df['Date'] < '1992-06-30')]
print(Jun1992)
Jun1992_mean=Jun1992['Low'].mean()
print("Jun 1992 Mean Low Price:", Jun1992_mean)
Jun1992.plot(x='Date', y='Low', title='AMD Low Prices in June 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1992=df.loc[(df['Date'] >= '1992-07-01') & (df['Date'] < '1992-07-31')]
print(Jul1992)
Jul1992_mean=Jul1992['Low'].mean()
print("Jul 1992 Mean Low Price:", Jul1992_mean)
Jul1992.plot(x='Date', y='Low', title='AMD Low Prices in July 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1992=df.loc[(df['Date'] >= '1992-08-01') & (df['Date'] < '1992-08-31')]
print(Aug1992)
Aug1992_mean=Aug1992['Low'].mean()
print("Aug 1992 Mean Low Price:", Aug1992_mean)
Aug1992.plot(x='Date', y='Low', title='AMD Low Prices in August 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1992=df.loc[(df['Date'] >= '1992-09-01') & (df['Date'] < '1992-09-30')]
print(Sep1992)
Sep1992_mean=Sep1992['Low'].mean()
print("Sep 1992 Mean Low Price:", Sep1992_mean)
Sep1992.plot(x='Date', y='Low', title='AMD Low Prices in September 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1992=df.loc[(df['Date'] >= '1992-10-01') & (df['Date'] < '1992-10-31')]
print(Oct1992)
Oct1992_mean=Oct1992['Low'].mean()
print("Oct 1992 Mean Low Price:", Oct1992_mean)
Oct1992.plot(x='Date', y='Low', title='AMD Low Prices in October 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1992=df.loc[(df['Date'] >= '1992-11-01') & (df['Date'] < '1992-11-30')]
print(Nov1992)
Nov1992_mean=Nov1992['Low'].mean()
print("Nov 1992 Mean Low Price:", Nov1992_mean)
Nov1992.plot(x='Date', y='Low', title='AMD Low Prices in November 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1992=df.loc[(df['Date'] >= '1992-12-01') & (df['Date'] < '1992-12-31')]
print(Dec1992)
Dec1992_mean=Dec1992['Low'].mean()
print("Dec 1992 Mean Low Price:", Dec1992_mean)
Dec1992.plot(x='Date', y='Low', title='AMD Low Prices in December 1992')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1993=df.loc[(df['Date'] >= '1993-01-01') & (df['Date'] < '1993-01-31')]
print(Jan1993)
Jan1993_mean=Jan1993['Low'].mean()
print("Jan 1993 Mean Low Price:", Jan1993_mean)
Jan1993.plot(x='Date', y='Low', title='AMD Low Prices in January 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1993=df.loc[(df['Date'] >= '1993-02-01') & (df['Date'] < '1993-02-28')]
print(Feb1993)
Feb1993_mean=Feb1993['Low'].mean()
print("Feb 1993 Mean Low Price:", Feb1993_mean)
Feb1993.plot(x='Date', y='Low', title='AMD Low Prices in February 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1993=df.loc[(df['Date'] >= '1993-03-01') & (df['Date'] < '1993-03-31')]
print(Mar1993)
Mar1993_mean=Mar1993['Low'].mean()
print("Mar 1993 Mean Low Price:", Mar1993_mean)
Mar1993.plot(x='Date', y='Low', title='AMD Low Prices in March 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1993=df.loc[(df['Date'] >= '1993-04-01') & (df['Date'] < '1993-04-30')]
print(Apr1993)
Apr1993_mean=Apr1993['Low'].mean()
print("Apr 1993 Mean Low Price:", Apr1993_mean)
Apr1993.plot(x='Date', y='Low', title='AMD Low Prices in April 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1993=df.loc[(df['Date'] >= '1993-05-01') & (df['Date'] < '1993-05-31')]
print(May1993)
May1993_mean=May1993['Low'].mean()
print("May 1993 Mean Low Price:", May1993_mean)
May1993.plot(x='Date', y='Low', title='AMD Low Prices in May 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1993=df.loc[(df['Date'] >= '1993-06-01') & (df['Date'] < '1993-06-30')]
print(Jun1993)
Jun1993_mean=Jun1993['Low'].mean()
print("Jun 1993 Mean Low Price:", Jun1993_mean)
Jun1993.plot(x='Date', y='Low', title='AMD Low Prices in June 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1993=df.loc[(df['Date'] >= '1993-07-01') & (df['Date'] < '1993-07-31')]
print(Jul1993)
Jul1993_mean=Jul1993['Low'].mean()
print("Jul 1993 Mean Low Price:", Jul1993_mean)
Jul1993.plot(x='Date', y='Low', title='AMD Low Prices in July 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1993=df.loc[(df['Date'] >= '1993-08-01') & (df['Date'] < '1993-08-31')]
print(Aug1993)
Aug1993_mean=Aug1993['Low'].mean()
print("Aug 1993 Mean Low Price:", Aug1993_mean)
Aug1993.plot(x='Date', y='Low', title='AMD Low Prices in August 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1993=df.loc[(df['Date'] >= '1993-09-01') & (df['Date'] < '1993-09-30')]
print(Sep1993)
Sep1993_mean=Sep1993['Low'].mean()
print("Sep 1993 Mean Low Price:", Sep1993_mean)
Sep1993.plot(x='Date', y='Low', title='AMD Low Prices in September 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1993=df.loc[(df['Date'] >= '1993-10-01') & (df['Date'] < '1993-10-31')]
print(Oct1993)
Oct1993_mean=Oct1993['Low'].mean()
print("Oct 1993 Mean Low Price:", Oct1993_mean)
Oct1993.plot(x='Date', y='Low', title='AMD Low Prices in October 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1993=df.loc[(df['Date'] >= '1993-11-01') & (df['Date'] < '1993-11-30')]
print(Nov1993)
Nov1993_mean=Nov1993['Low'].mean()
print("Nov 1993 Mean Low Price:", Nov1993_mean)
Nov1993.plot(x='Date', y='Low', title='AMD Low Prices in November 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1993=df.loc[(df['Date'] >= '1993-12-01') & (df['Date'] < '1993-12-31')]
print(Dec1993)
Dec1993_mean=Dec1993['Low'].mean()
print("Dec 1993 Mean Low Price:", Dec1993_mean)
Dec1993.plot(x='Date', y='Low', title='AMD Low Prices in December 1993')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1994=df.loc[(df['Date'] >= '1994-01-01') & (df['Date'] < '1994-01-31')]
print(Jan1994)
Jan1994_mean=Jan1994['Low'].mean()
print("Jan 1994 Mean Low Price:", Jan1994_mean)
Jan1994.plot(x='Date', y='Low', title='AMD Low Prices in January 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1994=df.loc[(df['Date'] >= '1994-02-01') & (df['Date'] < '1994-02-28')]
print(Feb1994)
Feb1994_mean=Feb1994['Low'].mean()
print("Feb 1994 Mean Low Price:", Feb1994_mean)
Feb1994.plot(x='Date', y='Low', title='AMD Low Prices in February 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1994=df.loc[(df['Date'] >= '1994-03-01') & (df['Date'] < '1994-03-31')]
print(Mar1994)
Mar1994_mean=Mar1994['Low'].mean()
print("Mar 1994 Mean Low Price:", Mar1994_mean)
Mar1994.plot(x='Date', y='Low', title='AMD Low Prices in March 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1994=df.loc[(df['Date'] >= '1994-04-01') & (df['Date'] < '1994-04-30')]
print(Apr1994)
Apr1994_mean=Apr1994['Low'].mean()
print("Apr 1994 Mean Low Price:", Apr1994_mean)
Apr1994.plot(x='Date', y='Low', title='AMD Low Prices in April 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1994=df.loc[(df['Date'] >= '1994-05-01') & (df['Date'] < '1994-05-31')]
print(May1994)
May1994_mean=May1994['Low'].mean()
print("May 1994 Mean Low Price:", May1994_mean)
May1994.plot(x='Date', y='Low', title='AMD Low Prices in May 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1994=df.loc[(df['Date'] >= '1994-06-01') & (df['Date'] < '1994-06-30')]
print(Jun1994)
Jun1994_mean=Jun1994['Low'].mean()
print("Jun 1994 Mean Low Price:", Jun1994_mean)
Jun1994.plot(x='Date', y='Low', title='AMD Low Prices in June 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1994=df.loc[(df['Date'] >= '1994-07-01') & (df['Date'] < '1994-07-31')]
print(Jul1994)
Jul1994_mean=Jul1994['Low'].mean()
print("Jul 1994 Mean Low Price:", Jul1994_mean)
Jul1994.plot(x='Date', y='Low', title='AMD Low Prices in July 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1994=df.loc[(df['Date'] >= '1994-08-01') & (df['Date'] < '1994-08-31')]
print(Aug1994)
Aug1994_mean=Aug1994['Low'].mean()
print("Aug 1994 Mean Low Price:", Aug1994_mean)
Aug1994.plot(x='Date', y='Low', title='AMD Low Prices in August 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1994=df.loc[(df['Date'] >= '1994-09-01') & (df['Date'] < '1994-09-30')]
print(Sep1994)
Sep1994_mean=Sep1994['Low'].mean()
print("Sep 1994 Mean Low Price:", Sep1994_mean)
Sep1994.plot(x='Date', y='Low', title='AMD Low Prices in September 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1994=df.loc[(df['Date'] >= '1994-10-01') & (df['Date'] < '1994-10-31')]
print(Oct1994)
Oct1994_mean=Oct1994['Low'].mean()
print("Oct 1994 Mean Low Price:", Oct1994_mean)
Oct1994.plot(x='Date', y='Low', title='AMD Low Prices in October 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1994=df.loc[(df['Date'] >= '1994-11-01') & (df['Date'] < '1994-11-30')]
print(Nov1994)
Nov1994_mean=Nov1994['Low'].mean()
print("Nov 1994 Mean Low Price:", Nov1994_mean)
Nov1994.plot(x='Date', y='Low', title='AMD Low Prices in November 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1994=df.loc[(df['Date'] >= '1994-12-01') & (df['Date'] < '1994-12-31')]
print(Dec1994)
Dec1994_mean=Dec1994['Low'].mean()
print("Dec 1994 Mean Low Price:", Dec1994_mean)
Dec1994.plot(x='Date', y='Low', title='AMD Low Prices in December 1994')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1995=df.loc[(df['Date'] >= '1995-01-01') & (df['Date'] < '1995-01-31')]
print(Jan1995)
Jan1995_mean=Jan1995['Low'].mean()
print("Jan 1995 Mean Low Price:", Jan1995_mean)
Jan1995.plot(x='Date', y='Low', title='AMD Low Prices in January 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1995=df.loc[(df['Date'] >= '1995-02-01') & (df['Date'] < '1995-02-28')]
print(Feb1995)
Feb1995_mean=Feb1995['Low'].mean()
print("Feb 1995 Mean Low Price:", Feb1995_mean)
Feb1995.plot(x='Date', y='Low', title='AMD Low Prices in February 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1995=df.loc[(df['Date'] >= '1995-03-01') & (df['Date'] < '1995-03-31')]
print(Mar1995)
Mar1995_mean=Mar1995['Low'].mean()
print("Mar 1995 Mean Low Price:", Mar1995_mean)
Mar1995.plot(x='Date', y='Low', title='AMD Low Prices in March 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1995=df.loc[(df['Date'] >= '1995-04-01') & (df['Date'] < '1995-04-30')]
print(Apr1995)
Apr1995_mean=Apr1995['Low'].mean()
print("Apr 1995 Mean Low Price:", Apr1995_mean)
Apr1995.plot(x='Date', y='Low', title='AMD Low Prices in April 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1995=df.loc[(df['Date'] >= '1995-05-01') & (df['Date'] < '1995-05-31')]
print(May1995)
May1995_mean=May1995['Low'].mean()
print("May 1995 Mean Low Price:", May1995_mean)
May1995.plot(x='Date', y='Low', title='AMD Low Prices in May 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1995=df.loc[(df['Date'] >= '1995-06-01') & (df['Date'] < '1995-06-30')]
print(Jun1995)
Jun1995_mean=Jun1995['Low'].mean()
print("Jun 1995 Mean Low Price:", Jun1995_mean)
Jun1995.plot(x='Date', y='Low', title='AMD Low Prices in June 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1995=df.loc[(df['Date'] >= '1995-07-01') & (df['Date'] < '1995-07-31')]
print(Jul1995)
Jul1995_mean=Jul1995['Low'].mean()
print("Jul 1995 Mean Low Price:", Jul1995_mean)
Jul1995.plot(x='Date', y='Low', title='AMD Low Prices in July 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1995=df.loc[(df['Date'] >= '1995-08-01') & (df['Date'] < '1995-08-31')]
print(Aug1995)
Aug1995_mean=Aug1995['Low'].mean()
print("Aug 1995 Mean Low Price:", Aug1995_mean)
Aug1995.plot(x='Date', y='Low', title='AMD Low Prices in August 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1995=df.loc[(df['Date'] >= '1995-09-01') & (df['Date'] < '1995-09-30')]
print(Sep1995)
Sep1995_mean=Sep1995['Low'].mean()
print("Sep 1995 Mean Low Price:", Sep1995_mean)
Sep1995.plot(x='Date', y='Low', title='AMD Low Prices in September 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1995=df.loc[(df['Date'] >= '1995-10-01') & (df['Date'] < '1995-10-31')]
print(Oct1995)
Oct1995_mean=Oct1995['Low'].mean()
print("Oct 1995 Mean Low Price:", Oct1995_mean)
Oct1995.plot(x='Date', y='Low', title='AMD Low Prices in October 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1995=df.loc[(df['Date'] >= '1995-11-01') & (df['Date'] < '1995-11-30')]
print(Nov1995)
Nov1995_mean=Nov1995['Low'].mean()
print("Nov 1995 Mean Low Price:", Nov1995_mean)
Nov1995.plot(x='Date', y='Low', title='AMD Low Prices in November 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1995=df.loc[(df['Date'] >= '1995-12-01') & (df['Date'] < '1995-12-31')]
print(Dec1995)
Dec1995_mean=Dec1995['Low'].mean()
print("Dec 1995 Mean Low Price:", Dec1995_mean)
Dec1995.plot(x='Date', y='Low', title='AMD Low Prices in December 1995')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1996=df.loc[(df['Date'] >= '1996-01-01') & (df['Date'] < '1996-01-31')]
print(Jan1996)
Jan1996_mean=Jan1996['Low'].mean()
print("Jan 1996 Mean Low Price:", Jan1996_mean)
Jan1996.plot(x='Date', y='Low', title='AMD Low Prices in January 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1996=df.loc[(df['Date'] >= '1996-02-01') & (df['Date'] < '1996-02-29')]
print(Feb1996)
Feb1996_mean=Feb1996['Low'].mean()
print("Feb 1996 Mean Low Price:", Feb1996_mean)
Feb1996.plot(x='Date', y='Low', title='AMD Low Prices in February 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1996=df.loc[(df['Date'] >= '1996-03-01') & (df['Date'] < '1996-03-31')]
print(Mar1996)
Mar1996_mean=Mar1996['Low'].mean()
print("Mar 1996 Mean Low Price:", Mar1996_mean)
Mar1996.plot(x='Date', y='Low', title='AMD Low Prices in March 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1996=df.loc[(df['Date'] >= '1996-04-01') & (df['Date'] < '1996-04-30')]
print(Apr1996)
Apr1996_mean=Apr1996['Low'].mean()
print("Apr 1996 Mean Low Price:", Apr1996_mean)
Apr1996.plot(x='Date', y='Low', title='AMD Low Prices in April 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1996=df.loc[(df['Date'] >= '1996-05-01') & (df['Date'] < '1996-05-31')]
print(May1996)
May1996_mean=May1996['Low'].mean()
print("May 1996 Mean Low Price:", May1996_mean)
May1996.plot(x='Date', y='Low', title='AMD Low Prices in May 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1996=df.loc[(df['Date'] >= '1996-06-01') & (df['Date'] < '1996-06-30')]
print(Jun1996)
Jun1996_mean=Jun1996['Low'].mean()
print("Jun 1996 Mean Low Price:", Jun1996_mean)
Jun1996.plot(x='Date', y='Low', title='AMD Low Prices in June 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1996=df.loc[(df['Date'] >= '1996-07-01') & (df['Date'] < '1996-07-31')]
print(Jul1996)
Jul1996_mean=Jul1996['Low'].mean()
print("Jul 1996 Mean Low Price:", Jul1996_mean)
Jul1996.plot(x='Date', y='Low', title='AMD Low Prices in July 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1996=df.loc[(df['Date'] >= '1996-08-01') & (df['Date'] < '1996-08-31')]
print(Aug1996)
Aug1996_mean=Aug1996['Low'].mean()
print("Aug 1996 Mean Low Price:", Aug1996_mean)
Aug1996.plot(x='Date', y='Low', title='AMD Low Prices in August 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1996=df.loc[(df['Date'] >= '1996-09-01') & (df['Date'] < '1996-09-30')]
print(Sep1996)
Sep1996_mean=Sep1996['Low'].mean()
print("Sep 1996 Mean Low Price:", Sep1996_mean)
Sep1996.plot(x='Date', y='Low', title='AMD Low Prices in September 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1996=df.loc[(df['Date'] >= '1996-10-01') & (df['Date'] < '1996-10-31')]
print(Oct1996)
Oct1996_mean=Oct1996['Low'].mean()
print("Oct 1996 Mean Low Price:", Oct1996_mean)
Oct1996.plot(x='Date', y='Low', title='AMD Low Prices in October 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1996=df.loc[(df['Date'] >= '1996-11-01') & (df['Date'] < '1996-11-30')]
print(Nov1996)
Nov1996_mean=Nov1996['Low'].mean()
print("Nov 1996 Mean Low Price:", Nov1996_mean)
Nov1996.plot(x='Date', y='Low', title='AMD Low Prices in November 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1996=df.loc[(df['Date'] >= '1996-12-01') & (df['Date'] < '1996-12-31')]
print(Dec1996)
Dec1996_mean=Dec1996['Low'].mean()
print("Dec 1996 Mean Low Price:", Dec1996_mean)
Dec1996.plot(x='Date', y='Low', title='AMD Low Prices in December 1996')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1997=df.loc[(df['Date'] >= '1997-01-01') & (df['Date'] < '1997-01-31')]
print(Jan1997)
Jan1997_mean=Jan1997['Low'].mean()
print("Jan 1997 Mean Low Price:", Jan1997_mean)
Jan1997.plot(x='Date', y='Low', title='AMD Low Prices in January 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1997=df.loc[(df['Date'] >= '1997-02-01') & (df['Date'] < '1997-02-28')]
print(Feb1997)
Feb1997_mean=Feb1997['Low'].mean()
print("Feb 1997 Mean Low Price:", Feb1997_mean)
Feb1997.plot(x='Date', y='Low', title='AMD Low Prices in February 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1997=df.loc[(df['Date'] >= '1997-03-01') & (df['Date'] < '1997-03-31')]
print(Mar1997)
Mar1997_mean=Mar1997['Low'].mean()
print("Mar 1997 Mean Low Price:", Mar1997_mean)
Mar1997.plot(x='Date', y='Low', title='AMD Low Prices in March 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1997=df.loc[(df['Date'] >= '1997-04-01') & (df['Date'] < '1997-04-30')]
print(Apr1997)
Apr1997_mean=Apr1997['Low'].mean()
print("Apr 1997 Mean Low Price:", Apr1997_mean)
Apr1997.plot(x='Date', y='Low', title='AMD Low Prices in April 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1997=df.loc[(df['Date'] >= '1997-05-01') & (df['Date'] < '1997-05-31')]
print(May1997)
May1997_mean=May1997['Low'].mean()
print("May 1997 Mean Low Price:", May1997_mean)
May1997.plot(x='Date', y='Low', title='AMD Low Prices in May 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1997=df.loc[(df['Date'] >= '1997-06-01') & (df['Date'] < '1997-06-30')]
print(Jun1997)
Jun1997_mean=Jun1997['Low'].mean()
print("Jun 1997 Mean Low Price:", Jun1997_mean)
Jun1997.plot(x='Date', y='Low', title='AMD Low Prices in June 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1997=df.loc[(df['Date'] >= '1997-07-01') & (df['Date'] < '1997-07-31')]
print(Jul1997)
Jul1997_mean=Jul1997['Low'].mean()
print("Jul 1997 Mean Low Price:", Jul1997_mean)
Jul1997.plot(x='Date', y='Low', title='AMD Low Prices in July 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1997=df.loc[(df['Date'] >= '1997-08-01') & (df['Date'] < '1997-08-31')]
print(Aug1997)
Aug1997_mean=Aug1997['Low'].mean()
print("Aug 1997 Mean Low Price:", Aug1997_mean)
Aug1997.plot(x='Date', y='Low', title='AMD Low Prices in August 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1997=df.loc[(df['Date'] >= '1997-09-01') & (df['Date'] < '1997-09-30')]
print(Sep1997)
Sep1997_mean=Sep1997['Low'].mean()
print("Sep 1997 Mean Low Price:", Sep1997_mean)
Sep1997.plot(x='Date', y='Low', title='AMD Low Prices in September 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1997=df.loc[(df['Date'] >= '1997-10-01') & (df['Date'] < '1997-10-31')]
print(Oct1997)
Oct1997_mean=Oct1997['Low'].mean()
print("Oct 1997 Mean Low Price:", Oct1997_mean)
Oct1997.plot(x='Date', y='Low', title='AMD Low Prices in October 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1997=df.loc[(df['Date'] >= '1997-11-01') & (df['Date'] < '1997-11-30')]
print(Nov1997)
Nov1997_mean=Nov1997['Low'].mean()
print("Nov 1997 Mean Low Price:", Nov1997_mean)
Nov1997.plot(x='Date', y='Low', title='AMD Low Prices in November 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1997=df.loc[(df['Date'] >= '1997-12-01') & (df['Date'] < '1997-12-31')]
print(Dec1997)
Dec1997_mean=Dec1997['Low'].mean()
print("Dec 1997 Mean Low Price:", Dec1997_mean)
Dec1997.plot(x='Date', y='Low', title='AMD Low Prices in December 1997')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1998=df.loc[(df['Date'] >= '1998-01-01') & (df['Date'] < '1998-01-31')]
print(Jan1998)
Jan1998_mean=Jan1998['Low'].mean()
print("Jan 1998 Mean Low Price:", Jan1998_mean)
Jan1998.plot(x='Date', y='Low', title='AMD Low Prices in January 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1998=df.loc[(df['Date'] >= '1998-02-01') & (df['Date'] < '1998-02-28')]
print(Feb1998)
Feb1998_mean=Feb1998['Low'].mean()
print("Feb 1998 Mean Low Price:", Feb1998_mean)
Feb1998.plot(x='Date', y='Low', title='AMD Low Prices in February 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1998=df.loc[(df['Date'] >= '1998-03-01') & (df['Date'] < '1998-03-31')]
print(Mar1998)
Mar1998_mean=Mar1998['Low'].mean()
print("Mar 1998 Mean Low Price:", Mar1998_mean)
Mar1998.plot(x='Date', y='Low', title='AMD Low Prices in March 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1998=df.loc[(df['Date'] >= '1998-04-01') & (df['Date'] < '1998-04-30')]
print(Apr1998)
Apr1998_mean=Apr1998['Low'].mean()
print("Apr 1998 Mean Low Price:", Apr1998_mean)
Apr1998.plot(x='Date', y='Low', title='AMD Low Prices in April 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1998=df.loc[(df['Date'] >= '1998-05-01') & (df['Date'] < '1998-05-31')]
print(May1998)
May1998_mean=May1998['Low'].mean()
print("May 1998 Mean Low Price:", May1998_mean)
May1998.plot(x='Date', y='Low', title='AMD Low Prices in May 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1998=df.loc[(df['Date'] >= '1998-06-01') & (df['Date'] < '1998-06-30')]
print(Jun1998)
Jun1998_mean=Jun1998['Low'].mean()
print("Jun 1998 Mean Low Price:", Jun1998_mean)
Jun1998.plot(x='Date', y='Low', title='AMD Low Prices in June 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1998=df.loc[(df['Date'] >= '1998-07-01') & (df['Date'] < '1998-07-31')]
print(Jul1998)
Jul1998_mean=Jul1998['Low'].mean()
print("Jul 1998 Mean Low Price:", Jul1998_mean)
Jul1998.plot(x='Date', y='Low', title='AMD Low Prices in July 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1998=df.loc[(df['Date'] >= '1998-08-01') & (df['Date'] < '1998-08-31')]
print(Aug1998)
Aug1998_mean=Aug1998['Low'].mean()
print("Aug 1998 Mean Low Price:", Aug1998_mean)
Aug1998.plot(x='Date', y='Low', title='AMD Low Prices in August 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1998=df.loc[(df['Date'] >= '1998-09-01') & (df['Date'] < '1998-09-30')]
print(Sep1998)
Sep1998_mean=Sep1998['Low'].mean()
print("Sep 1998 Mean Low Price:", Sep1998_mean)
Sep1998.plot(x='Date', y='Low', title='AMD Low Prices in September 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1998=df.loc[(df['Date'] >= '1998-10-01') & (df['Date'] < '1998-10-31')]
print(Oct1998)
Oct1998_mean=Oct1998['Low'].mean()
print("Oct 1998 Mean Low Price:", Oct1998_mean)
Oct1998.plot(x='Date', y='Low', title='AMD Low Prices in October 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1998=df.loc[(df['Date'] >= '1998-11-01') & (df['Date'] < '1998-11-30')]
print(Nov1998)
Nov1998_mean=Nov1998['Low'].mean()
print("Nov 1998 Mean Low Price:", Nov1998_mean)
Nov1998.plot(x='Date', y='Low', title='AMD Low Prices in November 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1998=df.loc[(df['Date'] >= '1998-12-01') & (df['Date'] < '1998-12-31')]
print(Dec1998)
Dec1998_mean=Dec1998['Low'].mean()
print("Dec 1998 Mean Low Price:", Dec1998_mean)
Dec1998.plot(x='Date', y='Low', title='AMD Low Prices in December 1998')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1999=df.loc[(df['Date'] >= '1999-01-01') & (df['Date'] < '1999-01-31')]
print(Jan1999)
Jan1999_mean=Jan1999['Low'].mean()
print("Jan 1999 Mean Low Price:", Jan1999_mean)
Jan1999.plot(x='Date', y='Low', title='AMD Low Prices in January 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1999=df.loc[(df['Date'] >= '1999-02-01') & (df['Date'] < '1999-02-28')]
print(Feb1999)
Feb1999_mean=Feb1999['Low'].mean()
print("Feb 1999 Mean Low Price:", Feb1999_mean)
Feb1999.plot(x='Date', y='Low', title='AMD Low Prices in February 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1999=df.loc[(df['Date'] >= '1999-03-01') & (df['Date'] < '1999-03-31')]
print(Mar1999)
Mar1999_mean=Mar1999['Low'].mean()
print("Mar 1999 Mean Low Price:", Mar1999_mean)
Mar1999.plot(x='Date', y='Low', title='AMD Low Prices in March 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1999=df.loc[(df['Date'] >= '1999-04-01') & (df['Date'] < '1999-04-30')]
print(Apr1999)
Apr1999_mean=Apr1999['Low'].mean()
print("Apr 1999 Mean Low Price:", Apr1999_mean)
Apr1999.plot(x='Date', y='Low', title='AMD Low Prices in April 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1999=df.loc[(df['Date'] >= '1999-05-01') & (df['Date'] < '1999-05-31')]
print(May1999)
May1999_mean=May1999['Low'].mean()
print("May 1999 Mean Low Price:", May1999_mean)
May1999.plot(x='Date', y='Low', title='AMD Low Prices in May 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1999=df.loc[(df['Date'] >= '1999-06-01') & (df['Date'] < '1999-06-30')]
print(Jun1999)
Jun1999_mean=Jun1999['Low'].mean()
print("Jun 1999 Mean Low Price:", Jun1999_mean)
Jun1999.plot(x='Date', y='Low', title='AMD Low Prices in June 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1999=df.loc[(df['Date'] >= '1999-07-01') & (df['Date'] < '1999-07-31')]
print(Jul1999)
Jul1999_mean=Jul1999['Low'].mean()
print("Jul 1999 Mean Low Price:", Jul1999_mean)
Jul1999.plot(x='Date', y='Low', title='AMD Low Prices in July 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1999=df.loc[(df['Date'] >= '1999-08-01') & (df['Date'] < '1999-08-31')]
print(Aug1999)
Aug1999_mean=Aug1999['Low'].mean()
print("Aug 1999 Mean Low Price:", Aug1999_mean)
Aug1999.plot(x='Date', y='Low', title='AMD Low Prices in August 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1999=df.loc[(df['Date'] >= '1999-09-01') & (df['Date'] < '1999-09-30')]
print(Sep1999)
Sep1999_mean=Sep1999['Low'].mean()
print("Sep 1999 Mean Low Price:", Sep1999_mean)
Sep1999.plot(x='Date', y='Low', title='AMD Low Prices in September 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1999=df.loc[(df['Date'] >= '1999-10-01') & (df['Date'] < '1999-10-31')]
print(Oct1999)
Oct1999_mean=Oct1999['Low'].mean()
print("Oct 1999 Mean Low Price:", Oct1999_mean)
Oct1999.plot(x='Date', y='Low', title='AMD Low Prices in October 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1999=df.loc[(df['Date'] >= '1999-11-01') & (df['Date'] < '1999-11-30')]
print(Nov1999)
Nov1999_mean=Nov1999['Low'].mean()
print("Nov 1999 Mean Low Price:", Nov1999_mean)
Nov1999.plot(x='Date', y='Low', title='AMD Low Prices in November 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1999=df.loc[(df['Date'] >= '1999-12-01') & (df['Date'] < '1999-12-31')]
print(Dec1999)
Dec1999_mean=Dec1999['Low'].mean()
print("Dec 1999 Mean Low Price:", Dec1999_mean)
Dec1999.plot(x='Date', y='Low', title='AMD Low Prices in December 1999')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2000=df.loc[(df['Date'] >= '2000-01-01') & (df['Date'] < '2000-01-31')]
print(Jan2000)
Jan2000_mean=Jan2000['Low'].mean()
print("Jan 2000 Mean Low Price:", Jan2000_mean)
Jan2000.plot(x='Date', y='Low', title='AMD Low Prices in January 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2000=df.loc[(df['Date'] >= '2000-02-01') & (df['Date'] < '2000-02-29')]
print(Feb2000)
Feb2000_mean=Feb2000['Low'].mean()
print("Feb 2000 Mean Low Price:", Feb2000_mean)
Feb2000.plot(x='Date', y='Low', title='AMD Low Prices in February 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2000=df.loc[(df['Date'] >= '2000-03-01') & (df['Date'] < '2000-03-31')]
print(Mar2000)
Mar2000_mean=Mar2000['Low'].mean()
print("Mar 2000 Mean Low Price:", Mar2000_mean)
Mar2000.plot(x='Date', y='Low', title='AMD Low Prices in March 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2000=df.loc[(df['Date'] >= '2000-04-01') & (df['Date'] < '2000-04-30')]
print(Apr2000)
Apr2000_mean=Apr2000['Low'].mean()
print("Apr 2000 Mean Low Price:", Apr2000_mean)
Apr2000.plot(x='Date', y='Low', title='AMD Low Prices in April 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2000=df.loc[(df['Date'] >= '2000-05-01') & (df['Date'] < '2000-05-31')]
print(May2000)
May2000_mean=May2000['Low'].mean()
print("May 2000 Mean Low Price:", May2000_mean)
May2000.plot(x='Date', y='Low', title='AMD Low Prices in May 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2000=df.loc[(df['Date'] >= '2000-06-01') & (df['Date'] < '2000-06-30')]
print(Jun2000)
Jun2000_mean=Jun2000['Low'].mean()
print("Jun 2000 Mean Low Price:", Jun2000_mean)
Jun2000.plot(x='Date', y='Low', title='AMD Low Prices in June 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2000=df.loc[(df['Date'] >= '2000-07-01') & (df['Date'] < '2000-07-31')]
print(Jul2000)
Jul2000_mean=Jul2000['Low'].mean()
print("Jul 2000 Mean Low Price:", Jul2000_mean)
Jul2000.plot(x='Date', y='Low', title='AMD Low Prices in July 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2000=df.loc[(df['Date'] >= '2000-08-01') & (df['Date'] < '2000-08-31')]
print(Aug2000)
Aug2000_mean=Aug2000['Low'].mean()
print("Aug 2000 Mean Low Price:", Aug2000_mean)
Aug2000.plot(x='Date', y='Low', title='AMD Low Prices in August 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2000=df.loc[(df['Date'] >= '2000-09-01') & (df['Date'] < '2000-09-30')]
print(Sep2000)
Sep2000_mean=Sep2000['Low'].mean()
print("Sep 2000 Mean Low Price:", Sep2000_mean)
Sep2000.plot(x='Date', y='Low', title='AMD Low Prices in September 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2000=df.loc[(df['Date'] >= '2000-10-01') & (df['Date'] < '2000-10-31')]
print(Oct2000)
Oct2000_mean=Oct2000['Low'].mean()
print("Oct 2000 Mean Low Price:", Oct2000_mean)
Oct2000.plot(x='Date', y='Low', title='AMD Low Prices in October 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2000=df.loc[(df['Date'] >= '2000-11-01') & (df['Date'] < '2000-11-30')]
print(Nov2000)
Nov2000_mean=Nov2000['Low'].mean()
print("Nov 2000 Mean Low Price:", Nov2000_mean)
Nov2000.plot(x='Date', y='Low', title='AMD Low Prices in November 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2000=df.loc[(df['Date'] >= '2000-12-01') & (df['Date'] < '2000-12-31')]
print(Dec2000)
Dec2000_mean=Dec2000['Low'].mean()
print("Dec 2000 Mean Low Price:", Dec2000_mean)
Dec2000.plot(x='Date', y='Low', title='AMD Low Prices in December 2000')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2001=df.loc[(df['Date'] >= '2001-01-01') & (df['Date'] < '2001-01-31')]
print(Jan2001)
Jan2001_mean=Jan2001['Low'].mean()
print("Jan 2001 Mean Low Price:", Jan2001_mean)
Jan2001.plot(x='Date', y='Low', title='AMD Low Prices in January 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2001=df.loc[(df['Date'] >= '2001-02-01') & (df['Date'] < '2001-02-28')]
print(Feb2001)
Feb2001_mean=Feb2001['Low'].mean()
print("Feb 2001 Mean Low Price:", Feb2001_mean)
Feb2001.plot(x='Date', y='Low', title='AMD Low Prices in February 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2001=df.loc[(df['Date'] >= '2001-03-01') & (df['Date'] < '2001-03-31')]
print(Mar2001)
Mar2001_mean=Mar2001['Low'].mean()
print("Mar 2001 Mean Low Price:", Mar2001_mean)
Mar2001.plot(x='Date', y='Low', title='AMD Low Prices in March 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2001=df.loc[(df['Date'] >= '2001-04-01') & (df['Date'] < '2001-04-30')]
print(Apr2001)
Apr2001_mean=Apr2001['Low'].mean()
print("Apr 2001 Mean Low Price:", Apr2001_mean)
Apr2001.plot(x='Date', y='Low', title='AMD Low Prices in April 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2001=df.loc[(df['Date'] >= '2001-05-01') & (df['Date'] < '2001-05-31')]
print(May2001)
May2001_mean=May2001['Low'].mean()
print("May 2001 Mean Low Price:", May2001_mean)
May2001.plot(x='Date', y='Low', title='AMD Low Prices in May 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2001=df.loc[(df['Date'] >= '2001-06-01') & (df['Date'] < '2001-06-30')]
print(Jun2001)
Jun2001_mean=Jun2001['Low'].mean()
print("Jun 2001 Mean Low Price:", Jun2001_mean)
Jun2001.plot(x='Date', y='Low', title='AMD Low Prices in June 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2001=df.loc[(df['Date'] >= '2001-07-01') & (df['Date'] < '2001-07-31')]
print(Jul2001)
Jul2001_mean=Jul2001['Low'].mean()
print("Jul 2001 Mean Low Price:", Jul2001_mean)
Jul2001.plot(x='Date', y='Low', title='AMD Low Prices in July 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2001=df.loc[(df['Date'] >= '2001-08-01') & (df['Date'] < '2001-08-31')]
print(Aug2001)
Aug2001_mean=Aug2001['Low'].mean()
print("Aug 2001 Mean Low Price:", Aug2001_mean)
Aug2001.plot(x='Date', y='Low', title='AMD Low Prices in August 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2001=df.loc[(df['Date'] >= '2001-07-01') & (df['Date'] < '2001-07-31')]
print(Jul2001)
Jul2001_mean=Jul2001['Low'].mean()
print("Jul 2001 Mean Low Price:", Jul2001_mean)
Jul2001.plot(x='Date', y='Low', title='AMD Low Prices in July 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2001=df.loc[(df['Date'] >= '2001-08-01') & (df['Date'] < '2001-08-31')]
print(Aug2001)
Aug2001_mean=Aug2001['Low'].mean()
print("Aug 2001 Mean Low Price:", Aug2001_mean)
Aug2001.plot(x='Date', y='Low', title='AMD Low Prices in August 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2001=df.loc[(df['Date'] >= '2001-09-01') & (df['Date'] < '2001-09-30')]
print(Sep2001)
Sep2001_mean=Sep2001['Low'].mean()
print("Sep 2001 Mean Low Price:", Sep2001_mean)
Sep2001.plot(x='Date', y='Low', title='AMD Low Prices in September 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2001=df.loc[(df['Date'] >= '2001-10-01') & (df['Date'] < '2001-10-31')]
print(Oct2001)
Oct2001_mean=Oct2001['Low'].mean()
print("Oct 2001 Mean Low Price:", Oct2001_mean)
Oct2001.plot(x='Date', y='Low', title='AMD Low Prices in October 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2001=df.loc[(df['Date'] >= '2001-11-01') & (df['Date'] < '2001-11-30')]
print(Nov2001)
Nov2001_mean=Nov2001['Low'].mean()
print("Nov 2001 Mean Low Price:", Nov2001_mean)
Nov2001.plot(x='Date', y='Low', title='AMD Low Prices in November 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2001=df.loc[(df['Date'] >= '2001-12-01') & (df['Date'] < '2001-12-31')]
print(Dec2001)
Dec2001_mean=Dec2001['Low'].mean()
print("Dec 2001 Mean Low Price:", Dec2001_mean)
Dec2001.plot(x='Date', y='Low', title='AMD Low Prices in December 2001')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2002=df.loc[(df['Date'] >= '2002-01-01') & (df['Date'] < '2002-01-31')]
print(Jan2002)
Jan2002_mean=Jan2002['Low'].mean()
print("Jan 2002 Mean Low Price:", Jan2002_mean)
Jan2002.plot(x='Date', y='Low', title='AMD Low Prices in January 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2002=df.loc[(df['Date'] >= '2002-02-01') & (df['Date'] < '2002-02-28')]
print(Feb2002)
Feb2002_mean=Feb2002['Low'].mean()
print("Feb 2002 Mean Low Price:", Feb2002_mean)
Feb2002.plot(x='Date', y='Low', title='AMD Low Prices in February 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2002=df.loc[(df['Date'] >= '2002-03-01') & (df['Date'] < '2002-03-31')]
print(Mar2002)
Mar2002_mean=Mar2002['Low'].mean()
print("Mar 2002 Mean Low Price:", Mar2002_mean)
Mar2002.plot(x='Date', y='Low', title='AMD Low Prices in March 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2002=df.loc[(df['Date'] >= '2002-04-01') & (df['Date'] < '2002-04-30')]
print(Apr2002)
Apr2002_mean=Apr2002['Low'].mean()
print("Apr 2002 Mean Low Price:", Apr2002_mean)
Apr2002.plot(x='Date', y='Low', title='AMD Low Prices in April 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2002=df.loc[(df['Date'] >= '2002-05-01') & (df['Date'] < '2002-05-31')]
print(May2002)
May2002_mean=May2002['Low'].mean()
print("May 2002 Mean Low Price:", May2002_mean)
May2002.plot(x='Date', y='Low', title='AMD Low Prices in May 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2002=df.loc[(df['Date'] >= '2002-06-01') & (df['Date'] < '2002-06-30')]
print(Jun2002)
Jun2002_mean=Jun2002['Low'].mean()
print("Jun 2002 Mean Low Price:", Jun2002_mean)
Jun2002.plot(x='Date', y='Low', title='AMD Low Prices in June 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2002=df.loc[(df['Date'] >= '2002-07-01') & (df['Date'] < '2002-07-31')]
print(Jul2002)
Jul2002_mean=Jul2002['Low'].mean()
print("Jul 2002 Mean Low Price:", Jul2002_mean)
Jul2002.plot(x='Date', y='Low', title='AMD Low Prices in July 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2002=df.loc[(df['Date'] >= '2002-08-01') & (df['Date'] < '2002-08-31')]
print(Aug2002)
Aug2002_mean=Aug2002['Low'].mean()
print("Aug 2002 Mean Low Price:", Aug2002_mean)
Aug2002.plot(x='Date', y='Low', title='AMD Low Prices in August 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2002=df.loc[(df['Date'] >= '2002-09-01') & (df['Date'] < '2002-09-30')]
print(Sep2002)
Sep2002_mean=Sep2002['Low'].mean()
print("Sep 2002 Mean Low Price:", Sep2002_mean)
Sep2002.plot(x='Date', y='Low', title='AMD Low Prices in September 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2002=df.loc[(df['Date'] >= '2002-10-01') & (df['Date'] < '2002-10-31')]
print(Oct2002)
Oct2002_mean=Oct2002['Low'].mean()
print("Oct 2002 Mean Low Price:", Oct2002_mean)
Oct2002.plot(x='Date', y='Low', title='AMD Low Prices in October 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2002=df.loc[(df['Date'] >= '2002-11-01') & (df['Date'] < '2002-11-30')]
print(Nov2002)
Nov2002_mean=Nov2002['Low'].mean()
print("Nov 2002 Mean Low Price:", Nov2002_mean)
Nov2002.plot(x='Date', y='Low', title='AMD Low Prices in November 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2002=df.loc[(df['Date'] >= '2002-12-01') & (df['Date'] < '2002-12-31')]
print(Dec2002)
Dec2002_mean=Dec2002['Low'].mean()
print("Dec 2002 Mean Low Price:", Dec2002_mean)
Dec2002.plot(x='Date', y='Low', title='AMD Low Prices in December 2002')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2003=df.loc[(df['Date'] >= '2003-01-01') & (df['Date'] < '2003-01-31')]
print(Jan2003)
Jan2003_mean=Jan2003['Low'].mean()
print("Jan 2003 Mean Low Price:", Jan2003_mean)
Jan2003.plot(x='Date', y='Low', title='AMD Low Prices in January 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2003=df.loc[(df['Date'] >= '2003-02-01') & (df['Date'] < '2003-02-28')]
print(Feb2003)
Feb2003_mean=Feb2003['Low'].mean()
print("Feb 2003 Mean Low Price:", Feb2003_mean)
Feb2003.plot(x='Date', y='Low', title='AMD Low Prices in February 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2003=df.loc[(df['Date'] >= '2003-03-01') & (df['Date'] < '2003-03-31')]
print(Mar2003)
Mar2003_mean=Mar2003['Low'].mean()
print("Mar 2003 Mean Low Price:", Mar2003_mean)
Mar2003.plot(x='Date', y='Low', title='AMD Low Prices in March 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2003=df.loc[(df['Date'] >= '2003-04-01') & (df['Date'] < '2003-04-30')]
print(Apr2003)
Apr2003_mean=Apr2003['Low'].mean()
print("Apr 2003 Mean Low Price:", Apr2003_mean)
Apr2003.plot(x='Date', y='Low', title='AMD Low Prices in April 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2003=df.loc[(df['Date'] >= '2003-05-01') & (df['Date'] < '2003-05-31')]
print(May2003)
May2003_mean=May2003['Low'].mean()
print("May 2003 Mean Low Price:", May2003_mean)
May2003.plot(x='Date', y='Low', title='AMD Low Prices in May 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2003=df.loc[(df['Date'] >= '2003-06-01') & (df['Date'] < '2003-06-30')]
print(Jun2003)
Jun2003_mean=Jun2003['Low'].mean()
print("Jun 2003 Mean Low Price:", Jun2003_mean)
Jun2003.plot(x='Date', y='Low', title='AMD Low Prices in June 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2003=df.loc[(df['Date'] >= '2003-07-01') & (df['Date'] < '2003-07-31')]
print(Jul2003)
Jul2003_mean=Jul2003['Low'].mean()
print("Jul 2003 Mean Low Price:", Jul2003_mean)
Jul2003.plot(x='Date', y='Low', title='AMD Low Prices in July 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2003=df.loc[(df['Date'] >= '2003-08-01') & (df['Date'] < '2003-08-31')]
print(Aug2003)
Aug2003_mean=Aug2003['Low'].mean()
print("Aug 2003 Mean Low Price:", Aug2003_mean)
Aug2003.plot(x='Date', y='Low', title='AMD Low Prices in August 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2003=df.loc[(df['Date'] >= '2003-09-01') & (df['Date'] < '2003-09-30')]
print(Sep2003)
Sep2003_mean=Sep2003['Low'].mean()
print("Sep 2003 Mean Low Price:", Sep2003_mean)
Sep2003.plot(x='Date', y='Low', title='AMD Low Prices in September 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2003=df.loc[(df['Date'] >= '2003-10-01') & (df['Date'] < '2003-10-31')]
print(Oct2003)
Oct2003_mean=Oct2003['Low'].mean()
print("Oct 2003 Mean Low Price:", Oct2003_mean)
Oct2003.plot(x='Date', y='Low', title='AMD Low Prices in October 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2003=df.loc[(df['Date'] >= '2003-11-01') & (df['Date'] < '2003-11-30')]
print(Nov2003)
Nov2003_mean=Nov2003['Low'].mean()
print("Nov 2003 Mean Low Price:", Nov2003_mean)
Nov2003.plot(x='Date', y='Low', title='AMD Low Prices in November 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2003=df.loc[(df['Date'] >= '2003-12-01') & (df['Date'] < '2003-12-31')]
print(Dec2003)
Dec2003_mean=Dec2003['Low'].mean()
print("Dec 2003 Mean Low Price:", Dec2003_mean)
Dec2003.plot(x='Date', y='Low', title='AMD Low Prices in December 2003')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2004=df.loc[(df['Date'] >= '2004-01-01') & (df['Date'] < '2004-01-31')]
print(Jan2004)
Jan2004_mean=Jan2004['Low'].mean()
print("Jan 2004 Mean Low Price:", Jan2004_mean)
Jan2004.plot(x='Date', y='Low', title='AMD Low Prices in January 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2004=df.loc[(df['Date'] >= '2004-02-01') & (df['Date'] < '2004-02-29')]
print(Feb2004)
Feb2004_mean=Feb2004['Low'].mean()
print("Feb 2004 Mean Low Price:", Feb2004_mean)
Feb2004.plot(x='Date', y='Low', title='AMD Low Prices in February 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2004=df.loc[(df['Date'] >= '2004-03-01') & (df['Date'] < '2004-03-31')]
print(Mar2004)
Mar2004_mean=Mar2004['Low'].mean()
print("Mar 2004 Mean Low Price:", Mar2004_mean)
Mar2004.plot(x='Date', y='Low', title='AMD Low Prices in March 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2004=df.loc[(df['Date'] >= '2004-04-01') & (df['Date'] < '2004-04-30')]
print(Apr2004)
Apr2004_mean=Apr2004['Low'].mean()
print("Apr 2004 Mean Low Price:", Apr2004_mean)
Apr2004.plot(x='Date', y='Low', title='AMD Low Prices in April 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2004=df.loc[(df['Date'] >= '2004-05-01') & (df['Date'] < '2004-05-31')]
print(May2004)
May2004_mean=May2004['Low'].mean()
print("May 2004 Mean Low Price:", May2004_mean)
May2004.plot(x='Date', y='Low', title='AMD Low Prices in May 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2004=df.loc[(df['Date'] >= '2004-06-01') & (df['Date'] < '2004-06-30')]
print(Jun2004)
Jun2004_mean=Jun2004['Low'].mean()
print("Jun 2004 Mean Low Price:", Jun2004_mean)
Jun2004.plot(x='Date', y='Low', title='AMD Low Prices in June 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2004=df.loc[(df['Date'] >= '2004-07-01') & (df['Date'] < '2004-07-31')]
print(Jul2004)
Jul2004_mean=Jul2004['Low'].mean()
print("Jul 2004 Mean Low Price:", Jul2004_mean)
Jul2004.plot(x='Date', y='Low', title='AMD Low Prices in July 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2004=df.loc[(df['Date'] >= '2004-08-01') & (df['Date'] < '2004-08-31')]
print(Aug2004)
Aug2004_mean=Aug2004['Low'].mean()
print("Aug 2004 Mean Low Price:", Aug2004_mean)
Aug2004.plot(x='Date', y='Low', title='AMD Low Prices in August 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2004=df.loc[(df['Date'] >= '2004-09-01') & (df['Date'] < '2004-09-30')]
print(Sep2004)
Sep2004_mean=Sep2004['Low'].mean()
print("Sep 2004 Mean Low Price:", Sep2004_mean)
Sep2004.plot(x='Date', y='Low', title='AMD Low Prices in September 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2004=df.loc[(df['Date'] >= '2004-10-01') & (df['Date'] < '2004-10-31')]
print(Oct2004)
Oct2004_mean=Oct2004['Low'].mean()
print("Oct 2004 Mean Low Price:", Oct2004_mean)
Oct2004.plot(x='Date', y='Low', title='AMD Low Prices in October 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2004=df.loc[(df['Date'] >= '2004-11-01') & (df['Date'] < '2004-11-30')]
print(Nov2004)
Nov2004_mean=Nov2004['Low'].mean()
print("Nov 2004 Mean Low Price:", Nov2004_mean)
Nov2004.plot(x='Date', y='Low', title='AMD Low Prices in November 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2004=df.loc[(df['Date'] >= '2004-12-01') & (df['Date'] < '2004-12-31')]
print(Dec2004)
Dec2004_mean=Dec2004['Low'].mean()
print("Dec 2004 Mean Low Price:", Dec2004_mean)
Dec2004.plot(x='Date', y='Low', title='AMD Low Prices in December 2004')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2005=df.loc[(df['Date'] >= '2005-01-01') & (df['Date'] < '2005-01-31')]
print(Jan2005)
Jan2005_mean=Jan2005['Low'].mean()
print("Jan 2005 Mean Low Price:", Jan2005_mean)
Jan2005.plot(x='Date', y='Low', title='AMD Low Prices in January 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2005=df.loc[(df['Date'] >= '2005-02-01') & (df['Date'] < '2005-02-28')]
print(Feb2005)
Feb2005_mean=Feb2005['Low'].mean()
print("Feb 2005 Mean Low Price:", Feb2005_mean)
Feb2005.plot(x='Date', y='Low', title='AMD Low Prices in February 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2005=df.loc[(df['Date'] >= '2005-03-01') & (df['Date'] < '2005-03-31')]
print(Mar2005)
Mar2005_mean=Mar2005['Low'].mean()
print("Mar 2005 Mean Low Price:", Mar2005_mean)
Mar2005.plot(x='Date', y='Low', title='AMD Low Prices in March 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2005=df.loc[(df['Date'] >= '2005-04-01') & (df['Date'] < '2005-04-30')]
print(Apr2005)
Apr2005_mean=Apr2005['Low'].mean()
print("Apr 2005 Mean Low Price:", Apr2005_mean)
Apr2005.plot(x='Date', y='Low', title='AMD Low Prices in April 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2005=df.loc[(df['Date'] >= '2005-05-01') & (df['Date'] < '2005-05-31')]
print(May2005)
May2005_mean=May2005['Low'].mean()
print("May 2005 Mean Low Price:", May2005_mean)
May2005.plot(x='Date', y='Low', title='AMD Low Prices in May 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2005=df.loc[(df['Date'] >= '2005-06-01') & (df['Date'] < '2005-06-30')]
print(Jun2005)
Jun2005_mean=Jun2005['Low'].mean()
print("Jun 2005 Mean Low Price:", Jun2005_mean)
Jun2005.plot(x='Date', y='Low', title='AMD Low Prices in June 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2005=df.loc[(df['Date'] >= '2005-07-01') & (df['Date'] < '2005-07-31')]
print(Jul2005)
Jul2005_mean=Jul2005['Low'].mean()
print("Jul 2005 Mean Low Price:", Jul2005_mean)
Jul2005.plot(x='Date', y='Low', title='AMD Low Prices in July 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2005=df.loc[(df['Date'] >= '2005-08-01') & (df['Date'] < '2005-08-31')]
print(Aug2005)
Aug2005_mean=Aug2005['Low'].mean()
print("Aug 2005 Mean Low Price:", Aug2005_mean)
Aug2005.plot(x='Date', y='Low', title='AMD Low Prices in August 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2005=df.loc[(df['Date'] >= '2005-09-01') & (df['Date'] < '2005-09-30')]
print(Sep2005)
Sep2005_mean=Sep2005['Low'].mean()
print("Sep 2005 Mean Low Price:", Sep2005_mean)
Sep2005.plot(x='Date', y='Low', title='AMD Low Prices in September 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2005=df.loc[(df['Date'] >= '2005-10-01') & (df['Date'] < '2005-10-31')]
print(Oct2005)
Oct2005_mean=Oct2005['Low'].mean()
print("Oct 2005 Mean Low Price:", Oct2005_mean)
Oct2005.plot(x='Date', y='Low', title='AMD Low Prices in October 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2005=df.loc[(df['Date'] >= '2005-11-01') & (df['Date'] < '2005-11-30')]
print(Nov2005)
Nov2005_mean=Nov2005['Low'].mean()
print("Nov 2005 Mean Low Price:", Nov2005_mean)
Nov2005.plot(x='Date', y='Low', title='AMD Low Prices in November 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2005=df.loc[(df['Date'] >= '2005-12-01') & (df['Date'] < '2005-12-31')]
print(Dec2005)
Dec2005_mean=Dec2005['Low'].mean()
print("Dec 2005 Mean Low Price:", Dec2005_mean)
Dec2005.plot(x='Date', y='Low', title='AMD Low Prices in December 2005')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2006=df.loc[(df['Date'] >= '2006-01-01') & (df['Date'] < '2006-01-31')]
print(Jan2006)
Jan2006_mean=Jan2006['Low'].mean()
print("Jan 2006 Mean Low Price:", Jan2006_mean)
Jan2006.plot(x='Date', y='Low', title='AMD Low Prices in January 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2006=df.loc[(df['Date'] >= '2006-02-01') & (df['Date'] < '2006-02-28')]
print(Feb2006)
Feb2006_mean=Feb2006['Low'].mean()
print("Feb 2006 Mean Low Price:", Feb2006_mean)
Feb2006.plot(x='Date', y='Low', title='AMD Low Prices in February 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2006=df.loc[(df['Date'] >= '2006-03-01') & (df['Date'] < '2006-03-31')]
print(Mar2006)
Mar2006_mean=Mar2006['Low'].mean()
print("Mar 2006 Mean Low Price:", Mar2006_mean)
Mar2006.plot(x='Date', y='Low', title='AMD Low Prices in March 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2006=df.loc[(df['Date'] >= '2006-04-01') & (df['Date'] < '2006-04-30')]
print(Apr2006)
Apr2006_mean=Apr2006['Low'].mean()
print("Apr 2006 Mean Low Price:", Apr2006_mean)
Apr2006.plot(x='Date', y='Low', title='AMD Low Prices in April 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2006=df.loc[(df['Date'] >= '2006-05-01') & (df['Date'] < '2006-05-31')]
print(May2006)
May2006_mean=May2006['Low'].mean()
print("May 2006 Mean Low Price:", May2006_mean)
May2006.plot(x='Date', y='Low', title='AMD Low Prices in May 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2006=df.loc[(df['Date'] >= '2006-06-01') & (df['Date'] < '2006-06-30')]
print(Jun2006)
Jun2006_mean=Jun2006['Low'].mean()
print("Jun 2006 Mean Low Price:", Jun2006_mean)
Jun2006.plot(x='Date', y='Low', title='AMD Low Prices in June 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2006=df.loc[(df['Date'] >= '2006-07-01') & (df['Date'] < '2006-07-31')]
print(Jul2006)
Jul2006_mean=Jul2006['Low'].mean()
print("Jul 2006 Mean Low Price:", Jul2006_mean)
Jul2006.plot(x='Date', y='Low', title='AMD Low Prices in July 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2006=df.loc[(df['Date'] >= '2006-08-01') & (df['Date'] < '2006-08-31')]
print(Aug2006)
Aug2006_mean=Aug2006['Low'].mean()
print("Aug 2006 Mean Low Price:", Aug2006_mean)
Aug2006.plot(x='Date', y='Low', title='AMD Low Prices in August 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2006=df.loc[(df['Date'] >= '2006-09-01') & (df['Date'] < '2006-09-30')]
print(Sep2006)
Sep2006_mean=Sep2006['Low'].mean()
print("Sep 2006 Mean Low Price:", Sep2006_mean)
Sep2006.plot(x='Date', y='Low', title='AMD Low Prices in September 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2006=df.loc[(df['Date'] >= '2006-10-01') & (df['Date'] < '2006-10-31')]
print(Oct2006)
Oct2006_mean=Oct2006['Low'].mean()
print("Oct 2006 Mean Low Price:", Oct2006_mean)
Oct2006.plot(x='Date', y='Low', title='AMD Low Prices in October 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2006=df.loc[(df['Date'] >= '2006-11-01') & (df['Date'] < '2006-11-30')]
print(Nov2006)
Nov2006_mean=Nov2006['Low'].mean()
print("Nov 2006 Mean Low Price:", Nov2006_mean)
Nov2006.plot(x='Date', y='Low', title='AMD Low Prices in November 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2006=df.loc[(df['Date'] >= '2006-12-01') & (df['Date'] < '2006-12-31')]
print(Dec2006)
Dec2006_mean=Dec2006['Low'].mean()
print("Dec 2006 Mean Low Price:", Dec2006_mean)
Dec2006.plot(x='Date', y='Low', title='AMD Low Prices in December 2006')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2007=df.loc[(df['Date'] >= '2007-01-01') & (df['Date'] < '2007-01-31')]
print(Jan2007)
Jan2007_mean=Jan2007['Low'].mean()
print("Jan 2007 Mean Low Price:", Jan2007_mean)
Jan2007.plot(x='Date', y='Low', title='AMD Low Prices in January 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2007=df.loc[(df['Date'] >= '2007-02-01') & (df['Date'] < '2007-02-28')]
print(Feb2007)
Feb2007_mean=Feb2007['Low'].mean()
print("Feb 2007 Mean Low Price:", Feb2007_mean)
Feb2007.plot(x='Date', y='Low', title='AMD Low Prices in February 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2007=df.loc[(df['Date'] >= '2007-03-01') & (df['Date'] < '2007-03-31')]
print(Mar2007)
Mar2007_mean=Mar2007['Low'].mean()
print("Mar 2007 Mean Low Price:", Mar2007_mean)
Mar2007.plot(x='Date', y='Low', title='AMD Low Prices in March 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2007=df.loc[(df['Date'] >= '2007-04-01') & (df['Date'] < '2007-04-30')]
print(Apr2007)
Apr2007_mean=Apr2007['Low'].mean()
print("Apr 2007 Mean Low Price:", Apr2007_mean)
Apr2007.plot(x='Date', y='Low', title='AMD Low Prices in April 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2007=df.loc[(df['Date'] >= '2007-05-01') & (df['Date'] < '2007-05-31')]
print(May2007)
May2007_mean=May2007['Low'].mean()
print("May 2007 Mean Low Price:", May2007_mean)
May2007.plot(x='Date', y='Low', title='AMD Low Prices in May 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2007=df.loc[(df['Date'] >= '2007-06-01') & (df['Date'] < '2007-06-30')]
print(Jun2007)
Jun2007_mean=Jun2007['Low'].mean()
print("Jun 2007 Mean Low Price:", Jun2007_mean)
Jun2007.plot(x='Date', y='Low', title='AMD Low Prices in June 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2007=df.loc[(df['Date'] >= '2007-07-01') & (df['Date'] < '2007-07-31')]
print(Jul2007)
Jul2007_mean=Jul2007['Low'].mean()
print("Jul 2007 Mean Low Price:", Jul2007_mean)
Jul2007.plot(x='Date', y='Low', title='AMD Low Prices in July 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2007=df.loc[(df['Date'] >= '2007-08-01') & (df['Date'] < '2007-08-31')]
print(Aug2007)
Aug2007_mean=Aug2007['Low'].mean()
print("Aug 2007 Mean Low Price:", Aug2007_mean)
Aug2007.plot(x='Date', y='Low', title='AMD Low Prices in August 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2007=df.loc[(df['Date'] >= '2007-09-01') & (df['Date'] < '2007-09-30')]
print(Sep2007)
Sep2007_mean=Jan2007['Low'].mean()
print("Sep 2007 Mean Low Price:", Sep2007_mean)
Sep2007.plot(x='Date', y='Low', title='AMD Low Prices in September 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2007=df.loc[(df['Date'] >= '2007-10-01') & (df['Date'] < '2007-10-31')]
print(Oct2007)
Oct2007_mean=Oct2007['Low'].mean()
print("Oct 2007 Mean Low Price:", Oct2007_mean)
Oct2007.plot(x='Date', y='Low', title='AMD Low Prices in October 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2007=df.loc[(df['Date'] >= '2007-11-01') & (df['Date'] < '2007-11-30')]
print(Nov2007)
Nov2007_mean=Nov2007['Low'].mean()
print("Nov 2007 Mean Low Price:", Nov2007_mean)
Nov2007.plot(x='Date', y='Low', title='AMD Low Prices in November 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2007=df.loc[(df['Date'] >= '2007-12-01') & (df['Date'] < '2007-12-31')]
print(Dec2007)
Dec2007_mean=Dec2007['Low'].mean()
print("Dec 2007 Mean Low Price:", Dec2007_mean)
Dec2007.plot(x='Date', y='Low', title='AMD Low Prices in December 2007')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2008=df.loc[(df['Date'] >= '2008-01-01') & (df['Date'] < '2008-01-31')]
print(Jan2008)
Jan2008_mean=Jan2008['Low'].mean()
print("Jan 2008 Mean Low Price:", Jan2008_mean)
Jan2008.plot(x='Date', y='Low', title='AMD Low Prices in January 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2008=df.loc[(df['Date'] >= '2008-02-01') & (df['Date'] < '2008-02-29')]
print(Feb2008)
Feb2008_mean=Feb2008['Low'].mean()
print("Feb 2008 Mean Low Price:", Feb2008_mean)
Feb2008.plot(x='Date', y='Low', title='AMD Low Prices in February 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2008=df.loc[(df['Date'] >= '2008-03-01') & (df['Date'] < '2008-03-31')]
print(Mar2008)
Mar2008_mean=Mar2008['Low'].mean()
print("Mar 2008 Mean Low Price:", Mar2008_mean)
Mar2008.plot(x='Date', y='Low', title='AMD Low Prices in March 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2008=df.loc[(df['Date'] >= '2008-04-01') & (df['Date'] < '2008-04-30')]
print(Apr2008)
Apr2008_mean=Apr2008['Low'].mean()
print("Apr 2008 Mean Low Price:", Apr2008_mean)
Apr2008.plot(x='Date', y='Low', title='AMD Low Prices in April 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2008=df.loc[(df['Date'] >= '2008-05-01') & (df['Date'] < '2008-05-31')]
print(May2008)
May2008_mean=May2008['Low'].mean()
print("May 2008 Mean Low Price:", May2008_mean)
May2008.plot(x='Date', y='Low', title='AMD Low Prices in May 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2008=df.loc[(df['Date'] >= '2008-06-01') & (df['Date'] < '2008-06-30')]
print(Jun2008)
Jun2008_mean=Jun2008['Low'].mean()
print("Jun 2008 Mean Low Price:", Jun2008_mean)
Jun2008.plot(x='Date', y='Low', title='AMD Low Prices in June 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2008=df.loc[(df['Date'] >= '2008-07-01') & (df['Date'] < '2008-07-31')]
print(Jul2008)
Jul2008_mean=Jul2008['Low'].mean()
print("Jul 2008 Mean Low Price:", Jul2008_mean)
Jul2008.plot(x='Date', y='Low', title='AMD Low Prices in July 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2008=df.loc[(df['Date'] >= '2008-08-01') & (df['Date'] < '2008-08-31')]
print(Aug2008)
Aug2008_mean=Aug2008['Low'].mean()
print("Aug 2008 Mean Low Price:", Aug2008_mean)
Aug2008.plot(x='Date', y='Low', title='AMD Low Prices in August 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2008=df.loc[(df['Date'] >= '2008-09-01') & (df['Date'] < '2008-09-30')]
print(Sep2008)
Sep2008_mean=Sep2008['Low'].mean()
print("Sep 2008 Mean Low Price:", Sep2008_mean)
Sep2008.plot(x='Date', y='Low', title='AMD Low Prices in September 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2008=df.loc[(df['Date'] >= '2008-10-01') & (df['Date'] < '2008-10-31')]
print(Oct2008)
Oct2008_mean=Oct2008['Low'].mean()
print("Oct 2008 Mean Low Price:", Oct2008_mean)
Oct2008.plot(x='Date', y='Low', title='AMD Low Prices in October 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2008=df.loc[(df['Date'] >= '2008-11-01') & (df['Date'] < '2008-11-30')]
print(Nov2008)
Nov2008_mean=Nov2008['Low'].mean()
print("Nov 2008 Mean Low Price:", Nov2008_mean)
Nov2008.plot(x='Date', y='Low', title='AMD Low Prices in November 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2008=df.loc[(df['Date'] >= '2008-12-01') & (df['Date'] < '2008-12-31')]
print(Dec2008)
Dec2008_mean=Dec2008['Low'].mean()
print("Dec 2008 Mean Low Price:", Dec2008_mean)
Dec2008.plot(x='Date', y='Low', title='AMD Low Prices in December 2008')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2009=df.loc[(df['Date'] >= '2009-01-01') & (df['Date'] < '2009-01-31')]
print(Jan2009)
Jan2009_mean=Jan2009['Low'].mean()
print("Jan 2009 Mean Low Price:", Jan2009_mean)
Jan2009.plot(x='Date', y='Low', title='AMD Low Prices in January 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2009=df.loc[(df['Date'] >= '2009-02-01') & (df['Date'] < '2009-02-28')]
print(Feb2009)
Feb2009_mean=Feb2009['Low'].mean()
print("Feb 2009 Mean Low Price:", Feb2009_mean)
Feb2009.plot(x='Date', y='Low', title='AMD Low Prices in February 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2009=df.loc[(df['Date'] >= '2009-03-01') & (df['Date'] < '2009-03-31')]
print(Mar2009)
Mar2009_mean=Mar2009['Low'].mean()
print("Mar 2009 Mean Low Price:", Mar2009_mean)
Mar2009.plot(x='Date', y='Low', title='AMD Low Prices in March 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2009=df.loc[(df['Date'] >= '2009-04-01') & (df['Date'] < '2009-04-30')]
print(Apr2009)
Apr2009_mean=Apr2009['Low'].mean()
print("Apr 2009 Mean Low Price:", Apr2009_mean)
Apr2009.plot(x='Date', y='Low', title='AMD Low Prices in April 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2009=df.loc[(df['Date'] >= '2009-05-01') & (df['Date'] < '2009-05-31')]
print(May2009)
May2009_mean=May2009['Low'].mean()
print("May 2009 Mean Low Price:", May2009_mean)
May2009.plot(x='Date', y='Low', title='AMD Low Prices in May 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2009=df.loc[(df['Date'] >= '2009-06-01') & (df['Date'] < '2009-06-30')]
print(Jun2009)
Jun2009_mean=Jun2009['Low'].mean()
print("Jun 2009 Mean Low Price:", Jun2009_mean)
Jun2009.plot(x='Date', y='Low', title='AMD Low Prices in June 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2009=df.loc[(df['Date'] >= '2009-07-01') & (df['Date'] < '2009-07-31')]
print(Jul2009)
Jul2009_mean=Jul2009['Low'].mean()
print("Jul 2009 Mean Low Price:", Jul2009_mean)
Jul2009.plot(x='Date', y='Low', title='AMD Low Prices in July 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2009=df.loc[(df['Date'] >= '2009-08-01') & (df['Date'] < '2009-08-31')]
print(Aug2009)
Aug2009_mean=Aug2009['Low'].mean()
print("Aug 2009 Mean Low Price:", Aug2009_mean)
Aug2009.plot(x='Date', y='Low', title='AMD Low Prices in August 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2009=df.loc[(df['Date'] >= '2009-09-01') & (df['Date'] < '2009-09-30')]
print(Sep2009)
Sep2009_mean=Sep2009['Low'].mean()
print("Sep 2009 Mean Low Price:", Sep2009_mean)
Sep2009.plot(x='Date', y='Low', title='AMD Low Prices in September 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2009=df.loc[(df['Date'] >= '2009-10-01') & (df['Date'] < '2009-10-31')]
print(Oct2009)
Oct2009_mean=Oct2009['Low'].mean()
print("Oct 2009 Mean Low Price:", Oct2009_mean)
Oct2009.plot(x='Date', y='Low', title='AMD Low Prices in October 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2009=df.loc[(df['Date'] >= '2009-11-01') & (df['Date'] < '2009-11-30')]
print(Nov2009)
Nov2009_mean=Nov2009['Low'].mean()
print("Nov 2009 Mean Low Price:", Nov2009_mean)
Nov2009.plot(x='Date', y='Low', title='AMD Low Prices in November 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2009=df.loc[(df['Date'] >= '2009-12-01') & (df['Date'] < '2009-12-31')]
print(Dec2009)
Dec2009_mean=Dec2009['Low'].mean()
print("Dec 2009 Mean Low Price:", Dec2009_mean)
Dec2009.plot(x='Date', y='Low', title='AMD Low Prices in December 2009')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2010=df.loc[(df['Date'] >= '2010-01-01') & (df['Date'] < '2010-01-31')]
print(Jan2010)
Jan2010_mean=Jan2010['Low'].mean()
print("Jan 2010 Mean Low Price:", Jan2010_mean)
Jan2010.plot(x='Date', y='Low', title='AMD Low Prices in January 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2010=df.loc[(df['Date'] >= '2010-02-01') & (df['Date'] < '2010-02-28')]
print(Feb2010)
Feb2010_mean=Feb2010['Low'].mean()
print("Feb 2010 Mean Low Price:", Feb2010_mean)
Feb2010.plot(x='Date', y='Low', title='AMD Low Prices in February 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2010=df.loc[(df['Date'] >= '2010-03-01') & (df['Date'] < '2010-03-31')]
print(Mar2010)
Mar2010_mean=Mar2010['Low'].mean()
print("Mar 2010 Mean Low Price:", Mar2010_mean)
Mar2010.plot(x='Date', y='Low', title='AMD Low Prices in March 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2010=df.loc[(df['Date'] >= '2010-04-01') & (df['Date'] < '2010-04-30')]
print(Apr2010)
Apr2010_mean=Apr2010['Low'].mean()
print("Apr 2010 Mean Low Price:", Apr2010_mean)
Apr2010.plot(x='Date', y='Low', title='AMD Low Prices in April 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2010=df.loc[(df['Date'] >= '2010-05-01') & (df['Date'] < '2010-05-31')]
print(May2010)
May2010_mean=May2010['Low'].mean()
print("May 2010 Mean Low Price:", May2010_mean)
May2010.plot(x='Date', y='Low', title='AMD Low Prices in May 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2010=df.loc[(df['Date'] >= '2010-06-01') & (df['Date'] < '2010-06-30')]
print(Jun2010)
Jun2010_mean=Jun2010['Low'].mean()
print("Jun 2010 Mean Low Price:", Jun2010_mean)
Jun2010.plot(x='Date', y='Low', title='AMD Low Prices in June 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2010=df.loc[(df['Date'] >= '2010-07-01') & (df['Date'] < '2010-07-31')]
print(Jul2010)
Jul2010_mean=Jul2010['Low'].mean()
print("Jul 2010 Mean Low Price:", Jul2010_mean)
Jul2010.plot(x='Date', y='Low', title='AMD Low Prices in July 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2010=df.loc[(df['Date'] >= '2010-08-01') & (df['Date'] < '2010-08-31')]
print(Aug2010)
Aug2010_mean=Aug2010['Low'].mean()
print("Aug 2010 Mean Low Price:", Aug2010_mean)
Aug2010.plot(x='Date', y='Low', title='AMD Low Prices in August 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2010=df.loc[(df['Date'] >= '2010-09-01') & (df['Date'] < '2010-09-30')]
print(Sep2010)
Sep2010_mean=Sep2010['Low'].mean()
print("Sep 2010 Mean Low Price:", Sep2010_mean)
Sep2010.plot(x='Date', y='Low', title='AMD Low Prices in September 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2010=df.loc[(df['Date'] >= '2010-10-01') & (df['Date'] < '2010-10-31')]
print(Oct2010)
Oct2010_mean=Oct2010['Low'].mean()
print("Oct 2010 Mean Low Price:", Oct2010_mean)
Oct2010.plot(x='Date', y='Low', title='AMD Low Prices in October 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2010=df.loc[(df['Date'] >= '2010-11-01') & (df['Date'] < '2010-11-30')]
print(Nov2010)
Nov2010_mean=Nov2010['Low'].mean()
print("Nov 2010 Mean Low Price:", Nov2010_mean)
Nov2010.plot(x='Date', y='Low', title='AMD Low Prices in November 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2010=df.loc[(df['Date'] >= '2010-12-01') & (df['Date'] < '2010-12-31')]
print(Dec2010)
Dec2010_mean=Dec2010['Low'].mean()
print("Dec 2010 Mean Low Price:", Dec2010_mean)
Dec2010.plot(x='Date', y='Low', title='AMD Low Prices in December 2010')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2011=df.loc[(df['Date'] >= '2011-01-01') & (df['Date'] < '2011-01-31')]
print(Jan2011)
Jan2011_mean=Jan2011['Low'].mean()
print("Jan 2011 Mean Low Price:", Jan2011_mean)
Jan2011.plot(x='Date', y='Low', title='AMD Low Prices in January 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2011=df.loc[(df['Date'] >= '2011-02-01') & (df['Date'] < '2011-02-28')]
print(Feb2011)
Feb2011_mean=Feb2011['Low'].mean()
print("Feb 2011 Mean Low Price:", Feb2011_mean)
Feb2011.plot(x='Date', y='Low', title='AMD Low Prices in February 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2011=df.loc[(df['Date'] >= '2011-03-01') & (df['Date'] < '2011-03-31')]
print(Mar2011)
Mar2011_mean=Mar2011['Low'].mean()
print("Mar 2011 Mean Low Price:", Mar2011_mean)
Mar2011.plot(x='Date', y='Low', title='AMD Low Prices in March 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2011=df.loc[(df['Date'] >= '2011-04-01') & (df['Date'] < '2011-04-30')]
print(Apr2011)
Apr2011_mean=Apr2011['Low'].mean()
print("Apr 2011 Mean Low Price:", Apr2011_mean)
Apr2011.plot(x='Date', y='Low', title='AMD Low Prices in April 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2011=df.loc[(df['Date'] >= '2011-05-01') & (df['Date'] < '2011-05-31')]
print(May2011)
May2011_mean=May2011['Low'].mean()
print("May 2011 Mean Low Price:", May2011_mean)
May2011.plot(x='Date', y='Low', title='AMD Low Prices in May 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2011=df.loc[(df['Date'] >= '2011-06-01') & (df['Date'] < '2011-06-30')]
print(Jun2011)
Jun2011_mean=Jun2011['Low'].mean()
print("Jun 2011 Mean Low Price:", Jun2011_mean)
Jun2011.plot(x='Date', y='Low', title='AMD Low Prices in June 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2011=df.loc[(df['Date'] >= '2011-07-01') & (df['Date'] < '2011-07-31')]
print(Jul2011)
Jul2011_mean=Jul2011['Low'].mean()
print("Jul 2011 Mean Low Price:", Jul2011_mean)
Jul2011.plot(x='Date', y='Low', title='AMD Low Prices in July 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2011=df.loc[(df['Date'] >= '2011-08-01') & (df['Date'] < '2011-08-31')]
print(Aug2011)
Aug2011_mean=Aug2011['Low'].mean()
print("Aug 2011 Mean Low Price:", Aug2011_mean)
Aug2011.plot(x='Date', y='Low', title='AMD Low Prices in August 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2011=df.loc[(df['Date'] >= '2011-09-01') & (df['Date'] < '2011-09-30')]
print(Sep2011)
Sep2011_mean=Sep2011['Low'].mean()
print("Sep 2011 Mean Low Price:", Sep2011_mean)
Sep2011.plot(x='Date', y='Low', title='AMD Low Prices in September 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2011=df.loc[(df['Date'] >= '2011-10-01') & (df['Date'] < '2011-10-31')]
print(Oct2011)
Oct2011_mean=Oct2011['Low'].mean()
print("Oct 2011 Mean Low Price:", Oct2011_mean)
Oct2011.plot(x='Date', y='Low', title='AMD Low Prices in October 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2011=df.loc[(df['Date'] >= '2011-11-01') & (df['Date'] < '2011-11-30')]
print(Nov2011)
Nov2011_mean=Nov2011['Low'].mean()
print("Nov 2011 Mean Low Price:", Nov2011_mean)
Nov2011.plot(x='Date', y='Low', title='AMD Low Prices in November 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2011=df.loc[(df['Date'] >= '2011-12-01') & (df['Date'] < '2011-12-31')]
print(Dec2011)
Dec2011_mean=Dec2011['Low'].mean()
print("Dec 2011 Mean Low Price:", Dec2011_mean)
Dec2011.plot(x='Date', y='Low', title='AMD Low Prices in December 2011')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2012=df.loc[(df['Date'] >= '2012-01-01') & (df['Date'] < '2012-01-31')]
print(Jan2012)
Jan2012_mean=Jan2012['Low'].mean()
print("Jan 2012 Mean Low Price:", Jan2012_mean)
Jan2012.plot(x='Date', y='Low', title='AMD Low Prices in January 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2012=df.loc[(df['Date'] >= '2012-02-01') & (df['Date'] < '2012-02-29')]
print(Feb2012)
Feb2012_mean=Feb2012['Low'].mean()
print("Feb 2012 Mean Low Price:", Feb2012_mean)
Feb2012.plot(x='Date', y='Low', title='AMD Low Prices in February 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2012=df.loc[(df['Date'] >= '2012-03-01') & (df['Date'] < '2012-03-31')]
print(Mar2012)
Mar2012_mean=Mar2012['Low'].mean()
print("Mar 2012 Mean Low Price:", Mar2012_mean)
Mar2012.plot(x='Date', y='Low', title='AMD Low Prices in March 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2012=df.loc[(df['Date'] >= '2012-04-01') & (df['Date'] < '2012-04-30')]
print(Apr2012)
Apr2012_mean=Apr2012['Low'].mean()
print("Apr 2012 Mean Low Price:", Apr2012_mean)
Apr2012.plot(x='Date', y='Low', title='AMD Low Prices in April 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2012=df.loc[(df['Date'] >= '2012-05-01') & (df['Date'] < '2012-05-31')]
print(May2012)
May2012_mean=May2012['Low'].mean()
print("May 2012 Mean Low Price:", May2012_mean)
May2012.plot(x='Date', y='Low', title='AMD Low Prices in May 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2012=df.loc[(df['Date'] >= '2012-06-01') & (df['Date'] < '2012-06-30')]
print(Jun2012)
Jun2012_mean=Jun2012['Low'].mean()
print("Jun 2012 Mean Low Price:", Jun2012_mean)
Jun2012.plot(x='Date', y='Low', title='AMD Low Prices in June 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2012=df.loc[(df['Date'] >= '2012-07-01') & (df['Date'] < '2012-07-31')]
print(Jul2012)
Jul2012_mean=Jul2012['Low'].mean()
print("Jul 2012 Mean Low Price:", Jul2012_mean)
Jul2012.plot(x='Date', y='Low', title='AMD Low Prices in July 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2012=df.loc[(df['Date'] >= '2012-08-01') & (df['Date'] < '2012-08-31')]
print(Aug2012)
Aug2012_mean=Aug2012['Low'].mean()
print("Aug 2012 Mean Low Price:", Aug2012_mean)
Aug2012.plot(x='Date', y='Low', title='AMD Low Prices in August 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2012=df.loc[(df['Date'] >= '2012-09-01') & (df['Date'] < '2012-09-30')]
print(Sep2012)
Sep2012_mean=Sep2012['Low'].mean()
print("Sep 2012 Mean Low Price:", Sep2012_mean)
Sep2012.plot(x='Date', y='Low', title='AMD Low Prices in September 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2012=df.loc[(df['Date'] >= '2012-10-01') & (df['Date'] < '2012-10-31')]
print(Oct2012)
Oct2012_mean=Oct2012['Low'].mean()
print("Oct 2012 Mean Low Price:", Oct2012_mean)
Oct2012.plot(x='Date', y='Low', title='AMD Low Prices in October 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2012=df.loc[(df['Date'] >= '2012-11-01') & (df['Date'] < '2012-11-30')]
print(Nov2012)
Nov2012_mean=Nov2012['Low'].mean()
print("Nov 2012 Mean Low Price:", Nov2012_mean)
Nov2012.plot(x='Date', y='Low', title='AMD Low Prices in November 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2012=df.loc[(df['Date'] >= '2012-12-01') & (df['Date'] < '2012-12-31')]
print(Dec2012)
Dec2012_mean=Dec2012['Low'].mean()
print("Dec 2012 Mean Low Price:", Dec2012_mean)
Dec2012.plot(x='Date', y='Low', title='AMD Low Prices in December 2012')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2013=df.loc[(df['Date'] >= '2013-01-01') & (df['Date'] < '2013-01-31')]
print(Jan2013)
Jan2013_mean=Jan2013['Low'].mean()
print("Jan 2013 Mean Low Price:", Jan2013_mean)
Jan2013.plot(x='Date', y='Low', title='AMD Low Prices in January 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2013=df.loc[(df['Date'] >= '2013-02-01') & (df['Date'] < '2013-02-28')]
print(Feb2013)
Feb2013_mean=Feb2013['Low'].mean()
print("Feb 2013 Mean Low Price:", Feb2013_mean)
Feb2013.plot(x='Date', y='Low', title='AMD Low Prices in February 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2013=df.loc[(df['Date'] >= '2013-03-01') & (df['Date'] < '2013-03-31')]
print(Mar2013)
Mar2013_mean=Mar2013['Low'].mean()
print("Mar 2013 Mean Low Price:", Mar2013_mean)
Mar2013.plot(x='Date', y='Low', title='AMD Low Prices in March 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2013=df.loc[(df['Date'] >= '2013-04-01') & (df['Date'] < '2013-04-30')]
print(Apr2013)
Apr2013_mean=Apr2013['Low'].mean()
print("Apr 2013 Mean Low Price:", Apr2013_mean)
Apr2013.plot(x='Date', y='Low', title='AMD Low Prices in April 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2013=df.loc[(df['Date'] >= '2013-05-01') & (df['Date'] < '2013-05-31')]
print(May2013)
May2013_mean=May2013['Low'].mean()
print("May 2013 Mean Low Price:", May2013_mean)
May2013.plot(x='Date', y='Low', title='AMD Low Prices in May 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2013=df.loc[(df['Date'] >= '2013-06-01') & (df['Date'] < '2013-06-30')]
print(Jun2013)
Jun2013_mean=Jun2013['Low'].mean()
print("Jun 2013 Mean Low Price:", Jun2013_mean)
Jun2013.plot(x='Date', y='Low', title='AMD Low Prices in June 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2013=df.loc[(df['Date'] >= '2013-07-01') & (df['Date'] < '2013-07-31')]
print(Jul2013)
Jul2013_mean=Jul2013['Low'].mean()
print("Jul 2013 Mean Low Price:", Jul2013_mean)
Jul2013.plot(x='Date', y='Low', title='AMD Low Prices in July 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2013=df.loc[(df['Date'] >= '2013-08-01') & (df['Date'] < '2013-08-31')]
print(Aug2013)
Aug2013_mean=Aug2013['Low'].mean()
print("Aug 2013 Mean Low Price:", Aug2013_mean)
Aug2013.plot(x='Date', y='Low', title='AMD Low Prices in August 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2013=df.loc[(df['Date'] >= '2013-09-01') & (df['Date'] < '2013-09-30')]
print(Sep2013)
Sep2013_mean=Sep2013['Low'].mean()
print("Sep 2013 Mean Low Price:", Sep2013_mean)
Sep2013.plot(x='Date', y='Low', title='AMD Low Prices in September 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2013=df.loc[(df['Date'] >= '2013-10-01') & (df['Date'] < '2013-10-31')]
print(Oct2013)
Oct2013_mean=Oct2013['Low'].mean()
print("Oct 2013 Mean Low Price:", Oct2013_mean)
Oct2013.plot(x='Date', y='Low', title='AMD Low Prices in October 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2013=df.loc[(df['Date'] >= '2013-11-01') & (df['Date'] < '2013-11-30')]
print(Nov2013)
Nov2013_mean=Nov2013['Low'].mean()
print("Nov 2013 Mean Low Price:", Nov2013_mean)
Nov2013.plot(x='Date', y='Low', title='AMD Low Prices in November 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2013=df.loc[(df['Date'] >= '2013-12-01') & (df['Date'] < '2013-12-31')]
print(Dec2013)
Dec2013_mean=Dec2013['Low'].mean()
print("Dec 2013 Mean Low Price:", Dec2013_mean)
Dec2013.plot(x='Date', y='Low', title='AMD Low Prices in December 2013')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2014=df.loc[(df['Date'] >= '2014-01-01') & (df['Date'] < '2014-01-31')]
print(Jan2014)
Jan2014_mean=Jan2014['Low'].mean()
print("Jan 2014 Mean Low Price:", Jan2014_mean)
Jan2014.plot(x='Date', y='Low', title='AMD Low Prices in January 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2014=df.loc[(df['Date'] >= '2014-02-01') & (df['Date'] < '2014-02-28')]
print(Feb2014)
Feb2014_mean=Feb2014['Low'].mean()
print("Feb 2014 Mean Low Price:", Feb2014_mean)
Feb2014.plot(x='Date', y='Low', title='AMD Low Prices in February 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2014=df.loc[(df['Date'] >= '2014-03-01') & (df['Date'] < '2014-03-31')]
print(Mar2014)
Mar2014_mean=Mar2014['Low'].mean()
print("Mar 2014 Mean Low Price:", Mar2014_mean)
Mar2014.plot(x='Date', y='Low', title='AMD Low Prices in March 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2014=df.loc[(df['Date'] >= '2014-04-01') & (df['Date'] < '2014-04-30')]
print(Apr2014)
Apr2014_mean=Apr2014['Low'].mean()
print("Apr 2014 Mean Low Price:", Apr2014_mean)
Apr2014.plot(x='Date', y='Low', title='AMD Low Prices in April 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2014=df.loc[(df['Date'] >= '2014-05-01') & (df['Date'] < '2014-05-31')]
print(May2014)
May2014_mean=May2014['Low'].mean()
print("May 2014 Mean Low Price:", May2014_mean)
May2014.plot(x='Date', y='Low', title='AMD Low Prices in May 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2014=df.loc[(df['Date'] >= '2014-06-01') & (df['Date'] < '2014-06-30')]
print(Jun2014)
Jun2014_mean=Jun2014['Low'].mean()
print("Jun 2014 Mean Low Price:", Jun2014_mean)
Jun2014.plot(x='Date', y='Low', title='AMD Low Prices in June 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2014=df.loc[(df['Date'] >= '2014-07-01') & (df['Date'] < '2014-07-31')]
print(Jul2014)
Jul2014_mean=Jul2014['Low'].mean()
print("Jul 2014 Mean Low Price:", Jul2014_mean)
Jul2014.plot(x='Date', y='Low', title='AMD Low Prices in July 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2014=df.loc[(df['Date'] >= '2014-08-01') & (df['Date'] < '2014-08-31')]
print(Aug2014)
Aug2014_mean=Aug2014['Low'].mean()
print("Aug 2014 Mean Low Price:", Aug2014_mean)
Aug2014.plot(x='Date', y='Low', title='AMD Low Prices in August 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2014=df.loc[(df['Date'] >= '2014-09-01') & (df['Date'] < '2014-09-30')]
print(Sep2014)
Sep2014_mean=Sep2014['Low'].mean()
print("Sep 2014 Mean Low Price:", Sep2014_mean)
Sep2014.plot(x='Date', y='Low', title='AMD Low Prices in September 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2014=df.loc[(df['Date'] >= '2014-10-01') & (df['Date'] < '2014-10-31')]
print(Oct2014)
Oct2014_mean=Oct2014['Low'].mean()
print("Oct 2014 Mean Low Price:", Oct2014_mean)
Oct2014.plot(x='Date', y='Low', title='AMD Low Prices in October 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2014=df.loc[(df['Date'] >= '2014-11-01') & (df['Date'] < '2014-11-30')]
print(Nov2014)
Nov2014_mean=Nov2014['Low'].mean()
print("Nov 2014 Mean Low Price:", Nov2014_mean)
Nov2014.plot(x='Date', y='Low', title='AMD Low Prices in November 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2014=df.loc[(df['Date'] >= '2014-12-01') & (df['Date'] < '2014-12-31')]
print(Dec2014)
Dec2014_mean=Dec2014['Low'].mean()
print("Dec 2014 Mean Low Price:", Dec2014_mean)
Dec2014.plot(x='Date', y='Low', title='AMD Low Prices in December 2014')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2015=df.loc[(df['Date'] >= '2015-01-01') & (df['Date'] < '2015-01-31')]
print(Jan2015)
Jan2015_mean=Jan2015['Low'].mean()
print("Jan 2015 Mean Low Price:", Jan2015_mean)
Jan2015.plot(x='Date', y='Low', title='AMD Low Prices in January 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2015=df.loc[(df['Date'] >= '2015-02-01') & (df['Date'] < '2015-02-28')]
print(Feb2015)
Feb2015_mean=Feb2015['Low'].mean()
print("Feb 2015 Mean Low Price:", Feb2015_mean)
Feb2015.plot(x='Date', y='Low', title='AMD Low Prices in February 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2015=df.loc[(df['Date'] >= '2015-03-01') & (df['Date'] < '2015-03-31')]
print(Mar2015)
Mar2015_mean=Mar2015['Low'].mean()
print("Mar 2015 Mean Low Price:", Mar2015_mean)
Mar2015.plot(x='Date', y='Low', title='AMD Low Prices in March 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2015=df.loc[(df['Date'] >= '2015-04-01') & (df['Date'] < '2015-04-30')]
print(Apr2015)
Apr2015_mean=Apr2015['Low'].mean()
print("Apr 2015 Mean Low Price:", Apr2015_mean)
Apr2015.plot(x='Date', y='Low', title='AMD Low Prices in April 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2015=df.loc[(df['Date'] >= '2015-05-01') & (df['Date'] < '2015-05-31')]
print(May2015)
May2015_mean=May2015['Low'].mean()
print("May 2015 Mean Low Price:", May2015_mean)
May2015.plot(x='Date', y='Low', title='AMD Low Prices in May 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2015=df.loc[(df['Date'] >= '2015-06-01') & (df['Date'] < '2015-06-30')]
print(Jun2015)
Jun2015_mean=Jun2015['Low'].mean()
print("Jun 2015 Mean Low Price:", Jun2015_mean)
Jun2015.plot(x='Date', y='Low', title='AMD Low Prices in June 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2015=df.loc[(df['Date'] >= '2015-07-01') & (df['Date'] < '2015-07-31')]
print(Jul2015)
Jul2015_mean=Jul2015['Low'].mean()
print("Jul 2015 Mean Low Price:", Jul2015_mean)
Jul2015.plot(x='Date', y='Low', title='AMD Low Prices in July 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2015=df.loc[(df['Date'] >= '2015-08-01') & (df['Date'] < '2015-08-31')]
print(Aug2015)
Aug2015_mean=Aug2015['Low'].mean()
print("Aug 2015 Mean Low Price:", Aug2015_mean)
Aug2015.plot(x='Date', y='Low', title='AMD Low Prices in August 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2015=df.loc[(df['Date'] >= '2015-09-01') & (df['Date'] < '2015-09-31')]
print(Sep2015)
Sep2015_mean=Sep2015['Low'].mean()
print("Sep 2015 Mean Low Price:", Sep2015_mean)
Sep2015.plot(x='Date', y='Low', title='AMD Low Prices in September 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2015=df.loc[(df['Date'] >= '2015-10-01') & (df['Date'] < '2015-10-31')]
print(Oct2015)
Oct2015_mean=Oct2015['Low'].mean()
print("Oct 2015 Mean Low Price:", Oct2015_mean)
Oct2015.plot(x='Date', y='Low', title='AMD Low Prices in October 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2015=df.loc[(df['Date'] >= '2015-11-01') & (df['Date'] < '2015-11-30')]
print(Nov2015)
Nov2015_mean=Nov2015['Low'].mean()
print("Nov 2015 Mean Low Price:", Nov2015_mean)
Nov2015.plot(x='Date', y='Low', title='AMD Low Prices in November 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2015=df.loc[(df['Date'] >= '2015-12-01') & (df['Date'] < '2015-12-31')]
print(Dec2015)
Dec2015_mean=Dec2015['Low'].mean()
print("Dec 2015 Mean Low Price:", Dec2015_mean)
Dec2015.plot(x='Date', y='Low', title='AMD Low Prices in December 2015')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2016=df.loc[(df['Date'] >= '2016-01-01') & (df['Date'] < '2016-01-31')]
print(Jan2016)
Jan2016_mean=Jan2016['Low'].mean()
print("Jan 2016 Mean Low Price:", Jan2016_mean)
Jan2016.plot(x='Date', y='Low', title='AMD Low Prices in January 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2016=df.loc[(df['Date'] >= '2016-02-01') & (df['Date'] < '2016-02-29')]
print(Feb2016)
Feb2016_mean=Feb2016['Low'].mean()
print("Feb 2016 Mean Low Price:", Feb2016_mean)
Feb2016.plot(x='Date', y='Low', title='AMD Low Prices in February 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2016=df.loc[(df['Date'] >= '2016-03-01') & (df['Date'] < '2016-03-31')]
print(Mar2016)
Mar2016_mean=Mar2016['Low'].mean()
print("Mar 2016 Mean Low Price:", Mar2016_mean)
Mar2016.plot(x='Date', y='Low', title='AMD Low Prices in March 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2016=df.loc[(df['Date'] >= '2016-04-01') & (df['Date'] < '2016-04-30')]
print(Apr2016)
Apr2016_mean=Apr2016['Low'].mean()
print("Apr 2016 Mean Low Price:", Apr2016_mean)
Apr2016.plot(x='Date', y='Low', title='AMD Low Prices in April 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2016=df.loc[(df['Date'] >= '2016-05-01') & (df['Date'] < '2016-05-31')]
print(May2016)
May2016_mean=May2016['Low'].mean()
print("May 2016 Mean Low Price:", May2016_mean)
May2016.plot(x='Date', y='Low', title='AMD Low Prices in May 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2016=df.loc[(df['Date'] >= '2016-06-01') & (df['Date'] < '2016-06-30')]
print(Jun2016)
Jun2016_mean=Jun2016['Low'].mean()
print("Jun 2016 Mean Low Price:", Jun2016_mean)
Jun2016.plot(x='Date', y='Low', title='AMD Low Prices in June 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2016=df.loc[(df['Date'] >= '2016-07-01') & (df['Date'] < '2016-07-31')]
print(Jul2016)
Jul2016_mean=Jul2016['Low'].mean()
print("Jul 2016 Mean Low Price:", Jul2016_mean)
Jul2016.plot(x='Date', y='Low', title='AMD Low Prices in July 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2016=df.loc[(df['Date'] >= '2016-08-01') & (df['Date'] < '2016-08-31')]
print(Aug2016)
Aug2016_mean=Aug2016['Low'].mean()
print("Aug 2016 Mean Low Price:", Aug2016_mean)
Aug2016.plot(x='Date', y='Low', title='AMD Low Prices in August 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2016=df.loc[(df['Date'] >= '2016-09-01') & (df['Date'] < '2016-09-30')]
print(Sep2016)
Sep2016_mean=Sep2016['Low'].mean()
print("Sep 2016 Mean Low Price:", Sep2016_mean)
Sep2016.plot(x='Date', y='Low', title='AMD Low Prices in September 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2016=df.loc[(df['Date'] >= '2016-10-01') & (df['Date'] < '2016-10-31')]
print(Oct2016)
Oct2016_mean=Oct2016['Low'].mean()
print("Oct 2016 Mean Low Price:", Oct2016_mean)
Oct2016.plot(x='Date', y='Low', title='AMD Low Prices in October 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2016=df.loc[(df['Date'] >= '2016-11-01') & (df['Date'] < '2016-11-30')]
print(Nov2016)
Nov2016_mean=Nov2016['Low'].mean()
print("Nov 2016 Mean Low Price:", Nov2016_mean)
Nov2016.plot(x='Date', y='Low', title='AMD Low Prices in November 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2016=df.loc[(df['Date'] >= '2016-12-01') & (df['Date'] < '2016-12-31')]
print(Dec2016)
Dec2016_mean=Dec2016['Low'].mean()
print("Dec 2016 Mean Low Price:", Dec2016_mean)
Dec2016.plot(x='Date', y='Low', title='AMD Low Prices in December 2016')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2017=df.loc[(df['Date'] >= '2017-01-01') & (df['Date'] < '2017-01-31')]
print(Jan2017)
Jan2017_mean=Jan2017['Low'].mean()
print("Jan 2017 Mean Low Price:", Jan2017_mean)
Jan2017.plot(x='Date', y='Low', title='AMD Low Prices in January 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2017=df.loc[(df['Date'] >= '2017-02-01') & (df['Date'] < '2017-02-28')]
print(Feb2017)
Feb2017_mean=Feb2017['Low'].mean()
print("Feb 2017 Mean Low Price:", Feb2017_mean)
Feb2017.plot(x='Date', y='Low', title='AMD Low Prices in February 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2017=df.loc[(df['Date'] >= '2017-03-01') & (df['Date'] < '2017-03-31')]
print(Mar2017)
Mar2017_mean=Mar2017['Low'].mean()
print("Mar 2017 Mean Low Price:", Mar2017_mean)
Mar2017.plot(x='Date', y='Low', title='AMD Low Prices in March 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2017=df.loc[(df['Date'] >= '2017-04-01') & (df['Date'] < '2017-04-30')]
print(Apr2017)
Apr2017_mean=Apr2017['Low'].mean()
print("Apr 2017 Mean Low Price:", Apr2017_mean)
Apr2017.plot(x='Date', y='Low', title='AMD Low Prices in April 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2017=df.loc[(df['Date'] >= '2017-05-01') & (df['Date'] < '2017-05-31')]
print(May2017)
May2017_mean=May2017['Low'].mean()
print("May 2017 Mean Low Price:", May2017_mean)
May2017.plot(x='Date', y='Low', title='AMD Low Prices in May 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2017=df.loc[(df['Date'] >= '2017-06-01') & (df['Date'] < '2017-06-30')]
print(Jun2017)
Jun2017_mean=Jun2017['Low'].mean()
print("Jun 2017 Mean Low Price:", Jun2017_mean)
Jun2017.plot(x='Date', y='Low', title='AMD Low Prices in June 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2017=df.loc[(df['Date'] >= '2017-07-01') & (df['Date'] < '2017-07-31')]
print(Jul2017)
Jul2017_mean=Jul2017['Low'].mean()
print("Jul 2017 Mean Low Price:", Jul2017_mean)
Jul2017.plot(x='Date', y='Low', title='AMD Low Prices in July 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2017=df.loc[(df['Date'] >= '2017-08-01') & (df['Date'] < '2017-08-31')]
print(Aug2017)
Aug2017_mean=Aug2017['Low'].mean()
print("Aug 2017 Mean Low Price:", Aug2017_mean)
Aug2017.plot(x='Date', y='Low', title='AMD Low Prices in August 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2017=df.loc[(df['Date'] >= '2017-09-01') & (df['Date'] < '2017-09-30')]
print(Sep2017)
Sep2017_mean=Sep2017['Low'].mean()
print("Sep 2017 Mean Low Price:", Sep2017_mean)
Sep2017.plot(x='Date', y='Low', title='AMD Low Prices in September 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2017=df.loc[(df['Date'] >= '2017-10-01') & (df['Date'] < '2017-10-31')]
print(Oct2017)
Oct2017_mean=Oct2017['Low'].mean()
print("Oct 2017 Mean Low Price:", Oct2017_mean)
Oct2017.plot(x='Date', y='Low', title='AMD Low Prices in October 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2017=df.loc[(df['Date'] >= '2017-11-01') & (df['Date'] < '2017-11-30')]
print(Nov2017)
Nov2017_mean=Nov2017['Low'].mean()
print("Nov 2017 Mean Low Price:", Nov2017_mean)
Nov2017.plot(x='Date', y='Low', title='AMD Low Prices in November 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2017=df.loc[(df['Date'] >= '2017-12-01') & (df['Date'] < '2017-12-31')]
print(Dec2017)
Dec2017_mean=Dec2017['Low'].mean()
print("Dec 2017 Mean Low Price:", Dec2017_mean)
Dec2017.plot(x='Date', y='Low', title='AMD Low Prices in December 2017')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2018=df.loc[(df['Date'] >= '2018-01-01') & (df['Date'] < '2018-01-31')]
print(Jan2018)
Jan2018_mean=Jan2018['Low'].mean()
print("Jan 2018 Mean Low Price:", Jan2018_mean)
Jan2018.plot(x='Date', y='Low', title='AMD Low Prices in January 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2018=df.loc[(df['Date'] >= '2018-02-01') & (df['Date'] < '2018-02-28')]
print(Feb2018)
Feb2018_mean=Feb2018['Low'].mean()
print("Feb 2018 Mean Low Price:", Feb2018_mean)
Feb2018.plot(x='Date', y='Low', title='AMD Low Prices in February 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2018=df.loc[(df['Date'] >= '2018-03-01') & (df['Date'] < '2018-03-31')]
print(Mar2018)
Mar2018_mean=Mar2018['Low'].mean()
print("Mar 2018 Mean Low Price:", Mar2018_mean)
Mar2018.plot(x='Date', y='Low', title='AMD Low Prices in March 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2018=df.loc[(df['Date'] >= '2018-04-01') & (df['Date'] < '2018-04-30')]
print(Apr2018)
Apr2018_mean=Apr2018['Low'].mean()
print("Apr 2018 Mean Low Price:", Apr2018_mean)
Apr2018.plot(x='Date', y='Low', title='AMD Low Prices in April 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2018=df.loc[(df['Date'] >= '2018-05-01') & (df['Date'] < '2018-05-31')]
print(May2018)
May2018_mean=May2018['Low'].mean()
print("May 2018 Mean Low Price:", May2018_mean)
May2018.plot(x='Date', y='Low', title='AMD Low Prices in May 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2018=df.loc[(df['Date'] >= '2018-06-01') & (df['Date'] < '2018-06-30')]
print(Jun2018)
Jun2018_mean=Jun2018['Low'].mean()
print("Jun 2018 Mean Low Price:", Jun2018_mean)
Jun2018.plot(x='Date', y='Low', title='AMD Low Prices in June 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2018=df.loc[(df['Date'] >= '2018-07-01') & (df['Date'] < '2018-07-31')]
print(Jul2018)
Jul2018_mean=Jul2018['Low'].mean()
print("Jul 2018 Mean Low Price:", Jul2018_mean)
Jul2018.plot(x='Date', y='Low', title='AMD Low Prices in July 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2018=df.loc[(df['Date'] >= '2018-08-01') & (df['Date'] < '2018-08-31')]
print(Aug2018)
Aug2018_mean=Aug2018['Low'].mean()
print("Aug 2018 Mean Low Price:", Aug2018_mean)
Aug2018.plot(x='Date', y='Low', title='AMD Low Prices in August 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2018=df.loc[(df['Date'] >= '2018-09-01') & (df['Date'] < '2018-09-30')]
print(Sep2018)
Sep2018_mean=Sep2018['Low'].mean()
print("Sep 2018 Mean Low Price:", Sep2018_mean)
Sep2018.plot(x='Date', y='Low', title='AMD Low Prices in September 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2018=df.loc[(df['Date'] >= '2018-10-01') & (df['Date'] < '2018-10-31')]
print(Oct2018)
Oct2018_mean=Oct2018['Low'].mean()
print("Oct 2018 Mean Low Price:", Oct2018_mean)
Oct2018.plot(x='Date', y='Low', title='AMD Low Prices in October 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2018=df.loc[(df['Date'] >= '2018-11-01') & (df['Date'] < '2018-11-30')]
print(Nov2018)
Nov2018_mean=Nov2018['Low'].mean()
print("Nov 2018 Mean Low Price:", Nov2018_mean)
Nov2018.plot(x='Date', y='Low', title='AMD Low Prices in November 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2018=df.loc[(df['Date'] >= '2018-12-01') & (df['Date'] < '2018-12-31')]
print(Dec2018)
Dec2018_mean=Dec2018['Low'].mean()
print("Dec 2018 Mean Low Price:", Dec2018_mean)
Dec2018.plot(x='Date', y='Low', title='AMD Low Prices in December 2018')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2019=df.loc[(df['Date'] >= '2019-01-01') & (df['Date'] < '2019-01-31')]
print(Jan2019)
Jan2019_mean=Jan2019['Low'].mean()
print("Jan 2019 Mean Low Price:", Jan2019_mean)
Jan2019.plot(x='Date', y='Low', title='AMD Low Prices in January 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2019=df.loc[(df['Date'] >= '2019-02-01') & (df['Date'] < '2019-02-28')]
print(Feb2019)
Feb2019_mean=Feb2019['Low'].mean()
print("Feb 2019 Mean Low Price:", Feb2019_mean)
Feb2019.plot(x='Date', y='Low', title='AMD Low Prices in February 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2019=df.loc[(df['Date'] >= '2019-03-01') & (df['Date'] < '2019-03-31')]
print(Mar2019)
Mar2019_mean=Mar2019['Low'].mean()
print("Mar 2019 Mean Low Price:", Mar2019_mean)
Mar2019.plot(x='Date', y='Low', title='AMD Low Prices in March 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2019=df.loc[(df['Date'] >= '2019-04-01') & (df['Date'] < '2019-04-30')]
print(Apr2019)
Apr2019_mean=Apr2019['Low'].mean()
print("Apr 2019 Mean Low Price:", Apr2019_mean)
Apr2019.plot(x='Date', y='Low', title='AMD Low Prices in April 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2019=df.loc[(df['Date'] >= '2019-05-01') & (df['Date'] < '2019-05-31')]
print(May2019)
May2019_mean=May2019['Low'].mean()
print("May 2019 Mean Low Price:", May2019_mean)
May2019.plot(x='Date', y='Low', title='AMD Low Prices in May 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2019=df.loc[(df['Date'] >= '2019-06-01') & (df['Date'] < '2019-06-30')]
print(Jun2019)
Jun2019_mean=Jun2019['Low'].mean()
print("Jun 2019 Mean Low Price:", Jun2019_mean)
Jun2019.plot(x='Date', y='Low', title='AMD Low Prices in June 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2019=df.loc[(df['Date'] >= '2019-07-01') & (df['Date'] < '2019-07-31')]
print(Jul2019)
Jul2019_mean=Jul2019['Low'].mean()
print("Jul 2019 Mean Low Price:", Jul2019_mean)
Jul2019.plot(x='Date', y='Low', title='AMD Low Prices in July 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2019=df.loc[(df['Date'] >= '2019-08-01') & (df['Date'] < '2019-08-31')]
print(Aug2019)
Aug2019_mean=Aug2019['Low'].mean()
print("Aug 2019 Mean Low Price:", Aug2019_mean)
Aug2019.plot(x='Date', y='Low', title='AMD Low Prices in August 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2019=df.loc[(df['Date'] >= '2019-09-01') & (df['Date'] < '2019-09-30')]
print(Sep2019)
Sep2019_mean=Sep2019['Low'].mean()
print("Sep 2019 Mean Low Price:", Sep2019_mean)
Sep2019.plot(x='Date', y='Low', title='AMD Low Prices in September 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2019=df.loc[(df['Date'] >= '2019-10-01') & (df['Date'] < '2019-10-31')]
print(Oct2019)
Oct2019_mean=Oct2019['Low'].mean()
print("Oct 2019 Mean Low Price:", Oct2019_mean)
Oct2019.plot(x='Date', y='Low', title='AMD Low Prices in October 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2019=df.loc[(df['Date'] >= '2019-11-01') & (df['Date'] < '2019-11-30')]
print(Nov2019)
Nov2019_mean=Nov2019['Low'].mean()
print("Nov 2019 Mean Low Price:", Nov2019_mean)
Nov2019.plot(x='Date', y='Low', title='AMD Low Prices in November 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2019=df.loc[(df['Date'] >= '2019-12-01') & (df['Date'] < '2019-12-31')]
print(Dec2019)
Dec2019_mean=Dec2019['Low'].mean()
print("Dec 2019 Mean Low Price:", Dec2019_mean)
Dec2019.plot(x='Date', y='Low', title='AMD Low Prices in December 2019')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2020=df.loc[(df['Date'] >= '2020-01-01') & (df['Date'] < '2020-01-31')]
print(Jan2020)
Jan2020_mean=Jan2020['Low'].mean()
print("Jan 2020 Mean Low Price:", Jan2020_mean)
Jan2020.plot(x='Date', y='Low', title='AMD Low Prices in January 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2020=df.loc[(df['Date'] >= '2020-02-01') & (df['Date'] < '2020-02-29')]
print(Feb2020)
Feb2020_mean=Feb2020['Low'].mean()
print("Feb 2020 Mean Low Price:", Feb2020_mean)
Feb2020.plot(x='Date', y='Low', title='AMD Low Prices in February 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2020=df.loc[(df['Date'] >= '2020-03-01') & (df['Date'] < '2020-03-31')]
print(Mar2020)
Mar2020_mean=Mar2020['Low'].mean()
print("Mar 2020 Mean Low Price:", Mar2020_mean)
Mar2020.plot(x='Date', y='Low', title='AMD Low Prices in March 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2020=df.loc[(df['Date'] >= '2020-04-01') & (df['Date'] < '2020-04-30')]
print(Apr2020)
Apr2020_mean=Apr2020['Low'].mean()
print("Apr 2020 Mean Low Price:", Apr2020_mean)
Apr2020.plot(x='Date', y='Low', title='AMD Low Prices in April 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2020=df.loc[(df['Date'] >= '2020-05-01') & (df['Date'] < '2020-05-31')]
print(May2020)
May2020_mean=May2020['Low'].mean()
print("May 2020 Mean Low Price:", May2020_mean)
May2020.plot(x='Date', y='Low', title='AMD Low Prices in May 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2020=df.loc[(df['Date'] >= '2020-06-01') & (df['Date'] < '2020-06-30')]
print(Jun2020)
Jun2020_mean=Jun2020['Low'].mean()
print("Jun 2020 Mean Low Price:", Jun2020_mean)
Jun2020.plot(x='Date', y='Low', title='AMD Low Prices in June 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2020=df.loc[(df['Date'] >= '2020-07-01') & (df['Date'] < '2020-07-31')]
print(Jul2020)
Jul2020_mean=Jul2020['Low'].mean()
print("Jul 2020 Mean Low Price:", Jul2020_mean)
Jul2020.plot(x='Date', y='Low', title='AMD Low Prices in July 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2020=df.loc[(df['Date'] >= '2020-08-01') & (df['Date'] < '2020-08-31')]
print(Aug2020)
Aug2020_mean=Aug2020['Low'].mean()
print("Aug 2020 Mean Low Price:", Aug2020_mean)
Aug2020.plot(x='Date', y='Low', title='AMD Low Prices in August 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2020=df.loc[(df['Date'] >= '2020-09-01') & (df['Date'] < '2020-09-30')]
print(Sep2020)
Sep2020_mean=Sep2020['Low'].mean()
print("Sep 2020 Mean Low Price:", Sep2020_mean)
Sep2020.plot(x='Date', y='Low', title='AMD Low Prices in September 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2020=df.loc[(df['Date'] >= '2020-10-01') & (df['Date'] < '2020-10-31')]
print(Oct2020)
Oct2020_mean=Oct2020['Low'].mean()
print("Oct 2020 Mean Low Price:", Oct2020_mean)
Oct2020.plot(x='Date', y='Low', title='AMD Low Prices in October 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2020=df.loc[(df['Date'] >= '2020-11-01') & (df['Date'] < '2020-11-30')]
print(Nov2020)
Nov2020_mean=Nov2020['Low'].mean()
print("Nov 2020 Mean Low Price:", Nov2020_mean)
Nov2020.plot(x='Date', y='Low', title='AMD Low Prices in November 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2020=df.loc[(df['Date'] >= '2020-12-01') & (df['Date'] < '2020-12-31')]
print(Dec2020)
Dec2020_mean=Dec2020['Low'].mean()
print("Dec 2020 Mean Low Price:", Dec2020_mean)
Dec2020.plot(x='Date', y='Low', title='AMD Low Prices in December 2020')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2021=df.loc[(df['Date'] >= '2021-01-01') & (df['Date'] < '2021-01-31')]
print(Jan2021)
Jan2021_mean=Jan2021['Low'].mean()
print("Jan 2021 Mean Low Price:", Jan2021_mean)
Jan2021.plot(x='Date', y='Low', title='AMD Low Prices in January 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2021=df.loc[(df['Date'] >= '2021-02-01') & (df['Date'] < '2021-02-28')]
print(Feb2021)
Feb2021_mean=Feb2021['Low'].mean()
print("Feb 2021 Mean Low Price:", Feb2021_mean)
Feb2021.plot(x='Date', y='Low', title='AMD Low Prices in February 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2021=df.loc[(df['Date'] >= '2021-03-01') & (df['Date'] < '2021-03-31')]
print(Mar2021)
Mar2021_mean=Mar2021['Low'].mean()
print("Mar 2021 Mean Low Price:", Mar2021_mean)
Mar2021.plot(x='Date', y='Low', title='AMD Low Prices in March 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2021=df.loc[(df['Date'] >= '2021-04-01') & (df['Date'] < '2021-04-30')]
print(Apr2021)
Apr2021_mean=Apr2021['Low'].mean()
print("Apr 2021 Mean Low Price:", Apr2021_mean)
Apr2021.plot(x='Date', y='Low', title='AMD Low Prices in April 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2021=df.loc[(df['Date'] >= '2021-05-01') & (df['Date'] < '2021-05-31')]
print(May2021)
May2021_mean=May2021['Low'].mean()
print("May 2021 Mean Low Price:", May2021_mean)
May2021.plot(x='Date', y='Low', title='AMD Low Prices in May 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2021=df.loc[(df['Date'] >= '2021-06-01') & (df['Date'] < '2021-06-30')]
print(Jun2021)
Jun2021_mean=Jun2021['Low'].mean()
print("Jun 2021 Mean Low Price:", Jun2021_mean)
Jun2021.plot(x='Date', y='Low', title='AMD Low Prices in June 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2021=df.loc[(df['Date'] >= '2021-07-01') & (df['Date'] < '2021-07-31')]
print(Jul2021)
Jul2021_mean=Jul2021['Low'].mean()
print("Jul 2021 Mean Low Price:", Jul2021_mean)
Jul2021.plot(x='Date', y='Low', title='AMD Low Prices in July 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2021=df.loc[(df['Date'] >= '2021-08-01') & (df['Date'] < '2021-08-31')]
print(Aug2021)
Aug2021_mean=Aug2021['Low'].mean()
print("Aug 2021 Mean Low Price:", Aug2021_mean)
Aug2021.plot(x='Date', y='Low', title='AMD Low Prices in August 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2021=df.loc[(df['Date'] >= '2021-09-01') & (df['Date'] < '2021-09-30')]
print(Sep2021)
Sep2021_mean=Sep2021['Low'].mean()
print("Sep 2021 Mean Low Price:", Sep2021_mean)
Sep2021.plot(x='Date', y='Low', title='AMD Low Prices in September 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2021=df.loc[(df['Date'] >= '2021-10-01') & (df['Date'] < '2021-10-31')]
print(Oct2021)
Oct2021_mean=Oct2021['Low'].mean()
print("Oct 2021 Mean Low Price:", Oct2021_mean)
Oct2021.plot(x='Date', y='Low', title='AMD Low Prices in October 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2021=df.loc[(df['Date'] >= '2021-11-01') & (df['Date'] < '2021-11-30')]
print(Nov2021)
Nov2021_mean=Nov2021['Low'].mean()
print("Nov 2021 Mean Low Price:", Nov2021_mean)
Nov2021.plot(x='Date', y='Low', title='AMD Low Prices in November 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2021=df.loc[(df['Date'] >= '2021-12-01') & (df['Date'] < '2021-12-31')]
print(Dec2021)
Dec2021_mean=Dec2021['Low'].mean()
print("Dec 2021 Mean Low Price:", Dec2021_mean)
Dec2021.plot(x='Date', y='Low', title='AMD Low Prices in December 2021')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2022=df.loc[(df['Date'] >= '2022-01-01') & (df['Date'] < '2022-01-31')]
print(Jan2022)
Jan2022_mean=Jan2022['Low'].mean()
print("Jan 2022 Mean Low Price:", Jan2022_mean)
Jan2022.plot(x='Date', y='Low', title='AMD Low Prices in January 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2022=df.loc[(df['Date'] >= '2022-02-01') & (df['Date'] < '2022-02-28')]
print(Feb2022)
Feb2022_mean=Feb2022['Low'].mean()
print("Feb 2022 Mean Low Price:", Feb2022_mean)
Feb2022.plot(x='Date', y='Low', title='AMD Low Prices in February 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2022=df.loc[(df['Date'] >= '2022-03-01') & (df['Date'] < '2022-03-31')]
print(Mar2022)
Mar2022_mean=Mar2022['Low'].mean()
print("Mar 2022 Mean Low Price:", Mar2022_mean)
Mar2022.plot(x='Date', y='Low', title='AMD Low Prices in March 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2022=df.loc[(df['Date'] >= '2022-04-01') & (df['Date'] < '2022-04-30')]
print(Apr2022)
Apr2022_mean=Apr2022['Low'].mean()
print("Apr 2022 Mean Low Price:", Apr2022_mean)
Apr2022.plot(x='Date', y='Low', title='AMD Low Prices in April 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2022=df.loc[(df['Date'] >= '2022-05-01') & (df['Date'] < '2022-05-31')]
print(May2022)
May2022_mean=May2022['Low'].mean()
print("May 2022 Mean Low Price:", May2022_mean)
May2022.plot(x='Date', y='Low', title='AMD Low Prices in May 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2022=df.loc[(df['Date'] >= '2022-06-01') & (df['Date'] < '2022-06-30')]
print(Jun2022)
Jun2022_mean=Jun2022['Low'].mean()
print("Jun 2022 Mean Low Price:", Jun2022_mean)
Jun2022.plot(x='Date', y='Low', title='AMD Low Prices in June 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2022=df.loc[(df['Date'] >= '2022-07-01') & (df['Date'] < '2022-07-31')]
print(Jul2022)
Jul2022_mean=Jul2022['Low'].mean()
print("Jul 2022 Mean Low Price:", Jul2022_mean)
Jul2022.plot(x='Date', y='Low', title='AMD Low Prices in July 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2022=df.loc[(df['Date'] >= '2022-08-01') & (df['Date'] < '2022-08-31')]
print(Aug2022)
Aug2022_mean=Aug2022['Low'].mean()
print("Aug 2022 Mean Low Price:", Aug2022_mean)
Aug2022.plot(x='Date', y='Low', title='AMD Low Prices in August 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2022=df.loc[(df['Date'] >= '2022-09-01') & (df['Date'] < '2022-09-30')]
print(Sep2022)
Sep2022_mean=Sep2022['Low'].mean()
print("Sep 2022 Mean Low Price:", Sep2022_mean)
Sep2022.plot(x='Date', y='Low', title='AMD Low Prices in September 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2022=df.loc[(df['Date'] >= '2022-10-01') & (df['Date'] < '2022-10-31')]
print(Oct2022)
Oct2022_mean=Oct2022['Low'].mean()
print("Oct 2022 Mean Low Price:", Oct2022_mean)
Oct2022.plot(x='Date', y='Low', title='AMD Low Prices in October 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2022=df.loc[(df['Date'] >= '2022-11-01') & (df['Date'] < '2022-11-30')]
print(Nov2022)
Nov2022_mean=Nov2022['Low'].mean()
print("Nov 2022 Mean Low Price:", Nov2022_mean)
Nov2022.plot(x='Date', y='Low', title='AMD Low Prices in November 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2022=df.loc[(df['Date'] >= '2022-12-01') & (df['Date'] < '2022-12-31')]
print(Dec2022)
Dec2022_mean=Dec2022['Low'].mean()
print("Dec 2022 Mean Low Price:", Dec2022_mean)
Dec2022.plot(x='Date', y='Low', title='AMD Low Prices in December 2022')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2023=df.loc[(df['Date'] >= '2023-01-01') & (df['Date'] < '2023-01-31')]
print(Jan2023)
Jan2023_mean=Jan2023['Low'].mean()
print("Jan 2023 Mean Low Price:", Jan2023_mean)
Jan2023.plot(x='Date', y='Low', title='AMD Low Prices in January 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2023=df.loc[(df['Date'] >= '2023-02-01') & (df['Date'] < '2023-02-28')]
print(Feb2023)
Feb2023_mean=Feb2023['Low'].mean()
print("Feb 2023 Mean Low Price:", Feb2023_mean)
Feb2023.plot(x='Date', y='Low', title='AMD Low Prices in February 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2023=df.loc[(df['Date'] >= '2023-03-01') & (df['Date'] < '2023-03-31')]
print(Mar2023)
Mar2023_mean=Mar2023['Low'].mean()
print("Mar 2023 Mean Low Price:", Mar2023_mean)
Mar2023.plot(x='Date', y='Low', title='AMD Low Prices in March 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2023=df.loc[(df['Date'] >= '2023-04-01') & (df['Date'] < '2023-04-30')]
print(Apr2023)
Apr2023_mean=Apr2023['Low'].mean()
print("Apr 2023 Mean Low Price:", Apr2023_mean)
Apr2023.plot(x='Date', y='Low', title='AMD Low Prices in April 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2023=df.loc[(df['Date'] >= '2023-05-01') & (df['Date'] < '2023-05-31')]
print(May2023)
May2023_mean=May2023['Low'].mean()
print("May 2023 Mean Low Price:", May2023_mean)
May2023.plot(x='Date', y='Low', title='AMD Low Prices in May 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2023=df.loc[(df['Date'] >= '2023-06-01') & (df['Date'] < '2023-06-30')]
print(Jun2023)
Jun2023_mean=Jun2023['Low'].mean()
print("Jun 2023 Mean Low Price:", Jun2023_mean)
Jun2023.plot(x='Date', y='Low', title='AMD Low Prices in June 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2023=df.loc[(df['Date'] >= '2023-07-01') & (df['Date'] < '2023-07-31')]
print(Jul2023)
Jul2023_mean=Jul2023['Low'].mean()
print("Jul 2023 Mean Low Price:", Jul2023_mean)
Jul2023.plot(x='Date', y='Low', title='AMD Low Prices in July 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2023=df.loc[(df['Date'] >= '2023-08-01') & (df['Date'] < '2023-08-31')]
print(Aug2023)
Aug2023_mean=Aug2023['Low'].mean()
print("Aug 2023 Mean Low Price:", Aug2023_mean)
Aug2023.plot(x='Date', y='Low', title='AMD Low Prices in August 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2023=df.loc[(df['Date'] >= '2023-09-01') & (df['Date'] < '2023-09-30')]
print(Sep2023)
Sep2023_mean=Sep2023['Low'].mean()
print("Sep 2023 Mean Low Price:", Sep2023_mean)
Sep2023.plot(x='Date', y='Low', title='AMD Low Prices in September 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2023=df.loc[(df['Date'] >= '2023-10-01') & (df['Date'] < '2023-10-31')]
print(Oct2023)
Oct2023_mean=Oct2023['Low'].mean()
print("Oct 2023 Mean Low Price:", Oct2023_mean)
Oct2023.plot(x='Date', y='Low', title='AMD Low Prices in October 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2023=df.loc[(df['Date'] >= '2023-11-01') & (df['Date'] < '2023-11-30')]
print(Nov2023)
Nov2023_mean=Nov2023['Low'].mean()
print("Nov 2023 Mean Low Price:", Nov2023_mean)
Nov2023.plot(x='Date', y='Low', title='AMD Low Prices in November 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2023=df.loc[(df['Date'] >= '2023-12-01') & (df['Date'] < '2023-12-31')]
print(Dec2023)
Dec2023_mean=Dec2023['Low'].mean()
print("Dec 2023 Mean Low Price:", Dec2023_mean)
Dec2023.plot(x='Date', y='Low', title='AMD Low Prices in December 2023')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2024=df.loc[(df['Date'] >= '2024-01-01') & (df['Date'] < '2024-01-31')]
print(Jan2024)
Jan2024_mean=Jan2024['Low'].mean()
print("Jan 2024 Mean Low Price:", Jan2024_mean)
Jan2024.plot(x='Date', y='Low', title='AMD Low Prices in January 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2024=df.loc[(df['Date'] >= '2024-02-01') & (df['Date'] < '2024-02-29')]
print(Feb2024)
Feb2024_mean=Feb2024['Low'].mean()
print("Feb 2024 Mean Low Price:", Feb2024_mean)
Feb2024.plot(x='Date', y='Low', title='AMD Low Prices in February 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2024=df.loc[(df['Date'] >= '2024-03-01') & (df['Date'] < '2024-03-31')]
print(Mar2024)
Mar2024_mean=Mar2024['Low'].mean()
print("Mar 2024 Mean Low Price:", Mar2024_mean)
Mar2024.plot(x='Date', y='Low', title='AMD Low Prices in March 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2024=df.loc[(df['Date'] >= '2024-04-01') & (df['Date'] < '2024-04-30')]
print(Apr2024)
Apr2024_mean=Apr2024['Low'].mean()
print("Apr 2024 Mean Low Price:", Apr2024_mean)
Apr2024.plot(x='Date', y='Low', title='AMD Low Prices in April 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2024=df.loc[(df['Date'] >= '2024-05-01') & (df['Date'] < '2024-05-31')]
print(May2024)
May2024_mean=May2024['Low'].mean()
print("May 2024 Mean Low Price:", May2024_mean)
May2024.plot(x='Date', y='Low', title='AMD Low Prices in May 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2024=df.loc[(df['Date'] >= '2024-06-01') & (df['Date'] < '2024-06-30')]
print(Jun2024)
Jun2024_mean=Jun2024['Low'].mean()
print("Jun 2024 Mean Low Price:", Jun2024_mean)
Jun2024.plot(x='Date', y='Low', title='AMD Low Prices in June 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2024=df.loc[(df['Date'] >= '2024-07-01') & (df['Date'] < '2024-07-31')]
print(Jul2024)
Jul2024_mean=Jul2024['Low'].mean()
print("Jul 2024 Mean Low Price:", Jul2024_mean)
Jul2024.plot(x='Date', y='Low', title='AMD Low Prices in July 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2024=df.loc[(df['Date'] >= '2024-08-01') & (df['Date'] < '2024-08-31')]
print(Aug2024)
Aug2024_mean=Aug2024['Low'].mean()
print("Aug 2024 Mean Low Price:", Aug2024_mean)
Aug2024.plot(x='Date', y='Low', title='AMD Low Prices in August 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2024=df.loc[(df['Date'] >= '2024-09-01') & (df['Date'] < '2024-09-30')]
print(Sep2024)
Sep2024_mean=Sep2024['Low'].mean()
print("Sep 2024 Mean Low Price:", Sep2024_mean)
Sep2024.plot(x='Date', y='Low', title='AMD Low Prices in September 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2024=df.loc[(df['Date'] >= '2024-10-01') & (df['Date'] < '2024-10-31')]
print(Oct2024)
Oct2024_mean=Oct2024['Low'].mean()
print("Oct 2024 Mean Low Price:", Oct2024_mean)
Oct2024.plot(x='Date', y='Low', title='AMD Low Prices in October 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2024=df.loc[(df['Date'] >= '2024-11-01') & (df['Date'] < '2024-11-30')]
print(Nov2024)
Nov2024_mean=Nov2024['Low'].mean()
print("Nov 2024 Mean Low Price:", Nov2024_mean)
Nov2024.plot(x='Date', y='Low', title='AMD Low Prices in November 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2024=df.loc[(df['Date'] >= '2024-12-01') & (df['Date'] < '2024-12-31')]
print(Dec2024)
Dec2024_mean=Dec2024['Low'].mean()
print("Dec 2024 Mean Low Price:", Dec2024_mean)
Dec2024.plot(x='Date', y='Low', title='AMD Low Prices in December 2024')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2025=df.loc[(df['Date'] >= '2025-01-01') & (df['Date'] < '2025-01-31')]
print(Jan2025)
Jan2025_mean=Jan2025['Low'].mean()
print("Jan 2025 Mean Low Price:", Jan2025_mean)
Jan2025.plot(x='Date', y='Low', title='AMD Low Prices in January 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2025=df.loc[(df['Date'] >= '2025-02-01') & (df['Date'] < '2025-02-28')]
print(Feb2025)
Feb2025_mean=Feb2025['Low'].mean()
print("Feb 2025 Mean Low Price:", Feb2025_mean)
Feb2025.plot(x='Date', y='Low', title='AMD Low Prices in February 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2025=df.loc[(df['Date'] >= '2025-03-01') & (df['Date'] < '2025-03-31')]
print(Mar2025)
Mar2025_mean=Mar2025['Low'].mean()
print("Mar 2025 Mean Low Price:", Mar2025_mean)
Mar2025.plot(x='Date', y='Low', title='AMD Low Prices in March 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2025=df.loc[(df['Date'] >= '2025-04-01') & (df['Date'] < '2025-04-30')]
print(Apr2025)
Apr2025_mean=Apr2025['Low'].mean()
print("Apr 2025 Mean Low Price:", Apr2025_mean)
Apr2025.plot(x='Date', y='Low', title='AMD Low Prices in April 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2025=df.loc[(df['Date'] >= '2025-05-01') & (df['Date'] < '2025-05-31')]
print(May2025)
May2025_mean=May2025['Low'].mean()
print("May 2025 Mean Low Price:", May2025_mean)
May2025.plot(x='Date', y='Low', title='AMD Low Prices in May 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2025=df.loc[(df['Date'] >= '2025-06-01') & (df['Date'] < '2025-06-30')]
print(Jun2025)
Jun2025_mean=Jun2025['Low'].mean()
print("Jun 2025 Mean Low Price:", Jun2025_mean)
Jun2025.plot(x='Date', y='Low', title='AMD Low Prices in June 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2025=df.loc[(df['Date'] >= '2025-07-01') & (df['Date'] < '2025-07-31')]
print(Jul2025)
Jul2025_mean=Jul2025['Low'].mean()
print("Jul 2025 Mean Low Price:", Jul2025_mean)
Jul2025.plot(x='Date', y='Low', title='AMD Low Prices in July 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2025=df.loc[(df['Date'] >= '2025-08-01') & (df['Date'] < '2025-08-31')]
print(Aug2025)
Aug2025_mean=Aug2025['Low'].mean()
print("Aug 2025 Mean Low Price:", Aug2025_mean)
Aug2025.plot(x='Date', y='Low', title='AMD Low Prices in August 2025')
plt.xlabel('Date')
plt.ylabel('Low Price')

plt.show()

#Monthwise Volume mentioned below

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1992=df.loc[(df['Date'] >= '1992-02-01') & (df['Date'] < '1992-02-29')]
print(Feb1992)
Feb1992_mean=Feb1992['Volume'].mean()
print("Feb 1992 Mean Volume:", Feb1992_mean)
Feb1992.plot(x='Date', y='Volume', title='AMD Volume in February 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1992=df.loc[(df['Date'] >= '1992-03-01') & (df['Date'] < '1992-03-31')]
print(Mar1992)
Mar1992_mean=Mar1992['Volume'].mean()
print("Mar 1992 Mean Volume:", Mar1992_mean)
Mar1992.plot(x='Date', y='Volume', title='AMD Volume in March 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1992=df.loc[(df['Date'] >= '1992-04-01') & (df['Date'] < '1992-04-30')]
print(Apr1992)
Apr1992_mean=Apr1992['Volume'].mean()
print("Apr 1992 Mean Volume:", Apr1992_mean)
Apr1992.plot(x='Date', y='Volume', title='AMD Volume in April 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1992=df.loc[(df['Date'] >= '1992-05-01') & (df['Date'] < '1992-05-31')]
print(May1992)
May1992_mean=May1992['Volume'].mean()
print("May 1992 Mean Volume:", May1992_mean)
May1992.plot(x='Date', y='Volume', title='AMD Volume in May 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1992=df.loc[(df['Date'] >= '1992-06-01') & (df['Date'] < '1992-06-30')]
print(Jun1992)
Jun1992_mean=Jun1992['Volume'].mean()
print("Jun 1992 Mean Volume:", Jun1992_mean)
Jun1992.plot(x='Date', y='Volume', title='AMD Volume in June 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1992=df.loc[(df['Date'] >= '1992-07-01') & (df['Date'] < '1992-07-31')]
print(Jul1992)
Jul1992_mean=Jul1992['Volume'].mean()
print("Jul 1992 Mean Volume:", Jul1992_mean)
Jul1992.plot(x='Date', y='Volume', title='AMD Volume in July 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1992=df.loc[(df['Date'] >= '1992-08-01') & (df['Date'] < '1992-08-31')]
print(Aug1992)
Aug1992_mean=Aug1992['Volume'].mean()
print("Aug 1992 Mean Volume:", Aug1992_mean)
Aug1992.plot(x='Date', y='Volume', title='AMD Volume in August 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1992=df.loc[(df['Date'] >= '1992-09-01') & (df['Date'] < '1992-09-30')]
print(Sep1992)
Sep1992_mean=Sep1992['Volume'].mean()
print("Sep 1992 Mean Volume:", Sep1992_mean)
Sep1992.plot(x='Date', y='Volume', title='AMD Volume in September 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1992=df.loc[(df['Date'] >= '1992-10-01') & (df['Date'] < '1992-10-31')]
print(Oct1992)
Oct1992_mean=Oct1992['Volume'].mean()
print("Oct 1992 Mean Volume:", Oct1992_mean)
Oct1992.plot(x='Date', y='Volume', title='AMD Volume in October 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1992=df.loc[(df['Date'] >= '1992-11-01') & (df['Date'] < '1992-11-30')]
print(Nov1992)
Nov1992_mean=Nov1992['Volume'].mean()
print("Nov 1992 Mean Volume:", Nov1992_mean)
Nov1992.plot(x='Date', y='Volume', title='AMD Volume in November 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1992=df.loc[(df['Date'] >= '1992-12-01') & (df['Date'] < '1992-12-31')]
print(Dec1992)
Dec1992_mean=Dec1992['Volume'].mean()
print("Dec 1992 Mean Volume:", Dec1992_mean)
Dec1992.plot(x='Date', y='Volume', title='AMD Volume in December 1992')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1993=df.loc[(df['Date'] >= '1993-01-01') & (df['Date'] < '1993-01-31')]
print(Jan1993)
Jan1993_mean=Jan1993['Volume'].mean()
print("Jan 1993 Mean Volume:", Jan1993_mean)
Jan1993.plot(x='Date', y='Volume', title='AMD Volume in January 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1993=df.loc[(df['Date'] >= '1993-02-01') & (df['Date'] < '1993-02-28')]
print(Feb1993)
Feb1993_mean=Feb1993['Volume'].mean()
print("Feb 1993 Mean Volume:", Feb1993_mean)
Feb1993.plot(x='Date', y='Volume', title='AMD Volume in February 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1993=df.loc[(df['Date'] >= '1993-03-01') & (df['Date'] < '1993-03-31')]
print(Mar1993)
Mar1993_mean=Mar1993['Volume'].mean()
print("Mar 1993 Mean Volume:", Mar1993_mean)
Mar1993.plot(x='Date', y='Volume', title='AMD Volume in March 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1993=df.loc[(df['Date'] >= '1993-04-01') & (df['Date'] < '1993-04-30')]
print(Apr1993)
Apr1993_mean=Apr1993['Volume'].mean()
print("Apr 1993 Mean Volume:", Apr1993_mean)
Apr1993.plot(x='Date', y='Volume', title='AMD Volume in April 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1993=df.loc[(df['Date'] >= '1993-05-01') & (df['Date'] < '1993-05-31')]
print(May1993)
May1993_mean=May1993['Volume'].mean()
print("May 1993 Mean Volume:", May1993_mean)
May1993.plot(x='Date', y='Volume', title='AMD Volume in May 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1993=df.loc[(df['Date'] >= '1993-06-01') & (df['Date'] < '1993-06-30')]
print(Jun1993)
Jun1993_mean=Jun1993['Volume'].mean()
print("Jun 1993 Mean Volume:", Jun1993_mean)
Jun1993.plot(x='Date', y='Volume', title='AMD Volume in June 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1993=df.loc[(df['Date'] >= '1993-07-01') & (df['Date'] < '1993-07-31')]
print(Jul1993)
Jul1993_mean=Jul1993['Volume'].mean()
print("Jul 1993 Mean Volume:", Jul1993_mean)
Jul1993.plot(x='Date', y='Volume', title='AMD Volume in July 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1993=df.loc[(df['Date'] >= '1993-08-01') & (df['Date'] < '1993-08-31')]
print(Aug1993)
Aug1993_mean=Aug1993['Volume'].mean()
print("Aug 1993 Mean Volume:", Aug1993_mean)
Aug1993.plot(x='Date', y='Volume', title='AMD Volume in August 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1993=df.loc[(df['Date'] >= '1993-09-01') & (df['Date'] < '1993-09-30')]
print(Sep1993)
Sep1993_mean=Sep1993['Volume'].mean()
print("Sep 1993 Mean Volume:", Sep1993_mean)
Sep1993.plot(x='Date', y='Volume', title='AMD Volume in September 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1993=df.loc[(df['Date'] >= '1993-10-01') & (df['Date'] < '1993-10-31')]
print(Oct1993)
Oct1993_mean=Oct1993['Volume'].mean()
print("Oct 1993 Mean Volume:", Oct1993_mean)
Oct1993.plot(x='Date', y='Volume', title='AMD Volume in October 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1993=df.loc[(df['Date'] >= '1993-11-01') & (df['Date'] < '1993-11-30')]
print(Nov1993)
Nov1993_mean=Nov1993['Volume'].mean()
print("Nov 1993 Mean Volume:", Nov1993_mean)
Nov1993.plot(x='Date', y='Volume', title='AMD Volume in November 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1993=df.loc[(df['Date'] >= '1993-12-01') & (df['Date'] < '1993-12-31')]
print(Dec1993)
Dec1993_mean=Dec1993['Volume'].mean()
print("Dec 1993 Mean Volume:", Dec1993_mean)
Dec1993.plot(x='Date', y='Volume', title='AMD Volume in December 1993')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1994=df.loc[(df['Date'] >= '1994-01-01') & (df['Date'] < '1994-01-31')]
print(Jan1994)
Jan1994_mean=Jan1994['Volume'].mean()
print("Jan 1994 Mean Volume:", Jan1994_mean)
Jan1994.plot(x='Date', y='Volume', title='AMD Volume in January 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1994=df.loc[(df['Date'] >= '1994-02-01') & (df['Date'] < '1994-02-28')]
print(Feb1994)
Feb1994_mean=Feb1994['Volume'].mean()
print("Feb 1994 Mean Volume:", Feb1994_mean)
Feb1994.plot(x='Date', y='Volume', title='AMD Volume in February 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1994=df.loc[(df['Date'] >= '1994-03-01') & (df['Date'] < '1994-03-31')]
print(Mar1994)
Mar1994_mean=Mar1994['Volume'].mean()
print("Mar 1994 Mean Volume:", Mar1994_mean)
Mar1994.plot(x='Date', y='Volume', title='AMD Volume in March 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1994=df.loc[(df['Date'] >= '1994-04-01') & (df['Date'] < '1994-04-30')]
print(Apr1994)
Apr1994_mean=Apr1994['Volume'].mean()
print("Apr 1994 Mean Volume:", Apr1994_mean)
Apr1994.plot(x='Date', y='Volume', title='AMD Volume in April 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1994=df.loc[(df['Date'] >= '1994-05-01') & (df['Date'] < '1994-05-31')]
print(May1994)
May1994_mean=May1994['Volume'].mean()
print("May 1994 Mean Volume:", May1994_mean)
May1994.plot(x='Date', y='Volume', title='AMD Volume in May 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1994=df.loc[(df['Date'] >= '1994-06-01') & (df['Date'] < '1994-06-30')]
print(Jun1994)
Jun1994_mean=Jun1994['Volume'].mean()
print("Jun 1994 Mean Volume:", Jun1994_mean)
Jun1994.plot(x='Date', y='Volume', title='AMD Volume in June 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1994=df.loc[(df['Date'] >= '1994-07-01') & (df['Date'] < '1994-07-31')]
print(Jul1994)
Jul1994_mean=Jul1994['Volume'].mean()
print("Jul 1994 Mean Volume:", Jul1994_mean)
Jul1994.plot(x='Date', y='Volume', title='AMD Volume in July 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1994=df.loc[(df['Date'] >= '1994-08-01') & (df['Date'] < '1994-08-31')]
print(Aug1994)
Aug1994_mean=Aug1994['Volume'].mean()
print("Aug 1994 Mean Volume:", Aug1994_mean)
Aug1994.plot(x='Date', y='Volume', title='AMD Volume in August 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1994=df.loc[(df['Date'] >= '1994-09-01') & (df['Date'] < '1994-09-30')]
print(Sep1994)
Sep1994_mean=Sep1994['Volume'].mean()
print("Sep 1994 Mean Volume:", Sep1994_mean)
Sep1994.plot(x='Date', y='Volume', title='AMD Volume in September 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1994=df.loc[(df['Date'] >= '1994-10-01') & (df['Date'] < '1994-10-31')]
print(Oct1994)
Oct1994_mean=Oct1994['Volume'].mean()
print("Oct 1994 Mean Volume:", Oct1994_mean)
Oct1994.plot(x='Date', y='Volume', title='AMD Volume in October 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1994=df.loc[(df['Date'] >= '1994-11-01') & (df['Date'] < '1994-11-30')]
print(Nov1994)
Nov1994_mean=Nov1994['Volume'].mean()
print("Nov 1994 Mean Volume:", Nov1994_mean)
Nov1994.plot(x='Date', y='Volume', title='AMD Volume in November 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1994=df.loc[(df['Date'] >= '1994-12-01') & (df['Date'] < '1994-12-31')]
print(Dec1994)
Dec1994_mean=Dec1994['Volume'].mean()
print("Dec 1994 Mean Volume:", Dec1994_mean)
Dec1994.plot(x='Date', y='Volume', title='AMD Volume in December 1994')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1995=df.loc[(df['Date'] >= '1995-01-01') & (df['Date'] < '1995-01-31')]
print(Jan1995)
Jan1995_mean=Jan1995['Volume'].mean()
print("Jan 1995 Mean Volume:", Jan1995_mean)
Jan1995.plot(x='Date', y='Volume', title='AMD Volume in January 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1995=df.loc[(df['Date'] >= '1995-02-01') & (df['Date'] < '1995-02-28')]
print(Feb1995)
Feb1995_mean=Feb1995['Volume'].mean()
print("Feb 1995 Mean Volume:", Feb1995_mean)
Feb1995.plot(x='Date', y='Volume', title='AMD Volume in February 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1995=df.loc[(df['Date'] >= '1995-03-01') & (df['Date'] < '1995-03-31')]
print(Mar1995)
Mar1995_mean=Mar1995['Volume'].mean()
print("Mar 1995 Mean Volume:", Mar1995_mean)
Mar1995.plot(x='Date', y='Volume', title='AMD Volume in March 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1995=df.loc[(df['Date'] >= '1995-04-01') & (df['Date'] < '1995-04-30')]
print(Apr1995)
Apr1995_mean=Apr1995['Volume'].mean()
print("Apr 1995 Mean Volume:", Apr1995_mean)
Apr1995.plot(x='Date', y='Volume', title='AMD Volume in April 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1995=df.loc[(df['Date'] >= '1995-05-01') & (df['Date'] < '1995-05-31')]
print(May1995)
May1995_mean=May1995['Volume'].mean()
print("May 1995 Mean Volume:", May1995_mean)
May1995.plot(x='Date', y='Volume', title='AMD Volume in May 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1995=df.loc[(df['Date'] >= '1995-06-01') & (df['Date'] < '1995-06-30')]
print(Jun1995)
Jun1995_mean=Jun1995['Volume'].mean()
print("Jun 1995 Mean Volume:", Jun1995_mean)
Jun1995.plot(x='Date', y='Volume', title='AMD Volume in June 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1995=df.loc[(df['Date'] >= '1995-07-01') & (df['Date'] < '1995-07-31')]
print(Jul1995)
Jul1995_mean=Jul1995['Volume'].mean()
print("Jul 1995 Mean Volume:", Jul1995_mean)
Jul1995.plot(x='Date', y='Volume', title='AMD Volume in July 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1995=df.loc[(df['Date'] >= '1995-08-01') & (df['Date'] < '1995-08-31')]
print(Aug1995)
Aug1995_mean=Jan1995['Volume'].mean()
print("Aug 1995 Mean Volume:", Aug1995_mean)
Aug1995.plot(x='Date', y='Volume', title='AMD Volume in August 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1995=df.loc[(df['Date'] >= '1995-09-01') & (df['Date'] < '1995-09-30')]
print(Sep1995)
Sep1995_mean=Sep1995['Volume'].mean()
print("Sep 1995 Mean Volume:", Sep1995_mean)
Sep1995.plot(x='Date', y='Volume', title='AMD Volume in September 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1995=df.loc[(df['Date'] >= '1995-10-01') & (df['Date'] < '1995-10-31')]
print(Oct1995)
Oct1995_mean=Oct1995['Volume'].mean()
print("Oct 1995 Mean Volume:", Oct1995_mean)
Oct1995.plot(x='Date', y='Volume', title='AMD Volume in October 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1995=df.loc[(df['Date'] >= '1995-11-01') & (df['Date'] < '1995-11-30')]
print(Nov1995)
Nov1995_mean=Nov1995['Volume'].mean()
print("Nov 1995 Mean Volume:", Nov1995_mean)
Nov1995.plot(x='Date', y='Volume', title='AMD Volume in November 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1995=df.loc[(df['Date'] >= '1995-12-01') & (df['Date'] < '1995-12-31')]
print(Dec1995)
Dec1995_mean=Dec1995['Volume'].mean()
print("Dec 1995 Mean Volume:", Dec1995_mean)
Dec1995.plot(x='Date', y='Volume', title='AMD Volume in December 1995')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1996=df.loc[(df['Date'] >= '1996-01-01') & (df['Date'] < '1996-01-31')]
print(Jan1996)
Jan1996_mean=Jan1996['Volume'].mean()
print("Jan 1996 Mean Volume:", Jan1996_mean)
Jan1996.plot(x='Date', y='Volume', title='AMD Volume in January 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1996=df.loc[(df['Date'] >= '1996-02-01') & (df['Date'] < '1996-02-29')]
print(Feb1996)
Feb1996_mean=Feb1996['Volume'].mean()
print("Feb 1996 Mean Volume:", Feb1996_mean)
Feb1996.plot(x='Date', y='Volume', title='AMD Volume in February 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1996=df.loc[(df['Date'] >= '1996-03-01') & (df['Date'] < '1996-03-31')]
print(Mar1996)
Mar1996_mean=Mar1996['Volume'].mean()
print("Mar 1996 Mean Volume:", Mar1996_mean)
Mar1996.plot(x='Date', y='Volume', title='AMD Volume in March 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1996=df.loc[(df['Date'] >= '1996-04-01') & (df['Date'] < '1996-04-30')]
print(Apr1996)
Apr1996_mean=Apr1996['Volume'].mean()
print("Apr 1996 Mean Volume:", Apr1996_mean)
Apr1996.plot(x='Date', y='Volume', title='AMD Volume in April 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1996=df.loc[(df['Date'] >= '1996-05-01') & (df['Date'] < '1996-05-31')]
print(May1996)
May1996_mean=May1996['Volume'].mean()
print("May 1996 Mean Volume:", May1996_mean)
May1996.plot(x='Date', y='Volume', title='AMD Volume in May 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1996=df.loc[(df['Date'] >= '1996-06-01') & (df['Date'] < '1996-06-30')]
print(Jun1996)
Jun1996_mean=Jun1996['Volume'].mean()
print("Jun 1996 Mean Volume:", Jun1996_mean)
Jun1996.plot(x='Date', y='Volume', title='AMD Volume in June 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1996=df.loc[(df['Date'] >= '1996-07-01') & (df['Date'] < '1996-07-31')]
print(Jul1996)
Jul1996_mean=Jul1996['Volume'].mean()
print("Jul 1996 Mean Volume:", Jul1996_mean)
Jul1996.plot(x='Date', y='Volume', title='AMD Volume in July 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1996=df.loc[(df['Date'] >= '1996-08-01') & (df['Date'] < '1996-08-31')]
print(Aug1996)
Aug1996_mean=Aug1996['Volume'].mean()
print("Aug 1996 Mean Volume:", Aug1996_mean)
Aug1996.plot(x='Date', y='Volume', title='AMD Volume in August 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1996=df.loc[(df['Date'] >= '1996-09-01') & (df['Date'] < '1996-09-30')]
print(Sep1996)
Sep1996_mean=Sep1996['Volume'].mean()
print("Sep 1996 Mean Volume:", Sep1996_mean)
Sep1996.plot(x='Date', y='Volume', title='AMD Volume in September 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1996=df.loc[(df['Date'] >= '1996-10-01') & (df['Date'] < '1996-10-31')]
print(Oct1996)
Oct1996_mean=Oct1996['Volume'].mean()
print("Oct 1996 Mean Volume:", Oct1996_mean)
Oct1996.plot(x='Date', y='Volume', title='AMD Volume in October 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1996=df.loc[(df['Date'] >= '1996-11-01') & (df['Date'] < '1996-11-30')]
print(Nov1996)
Nov1996_mean=Nov1996['Volume'].mean()
print("Nov 1996 Mean Volume:", Nov1996_mean)
Nov1996.plot(x='Date', y='Volume', title='AMD Volume in November 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1996=df.loc[(df['Date'] >= '1996-12-01') & (df['Date'] < '1996-12-31')]
print(Dec1996)
Dec1996_mean=Dec1996['Volume'].mean()
print("Dec 1996 Mean Volume:", Dec1996_mean)
Dec1996.plot(x='Date', y='Volume', title='AMD Volume in December 1996')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1997=df.loc[(df['Date'] >= '1997-01-01') & (df['Date'] < '1997-01-31')]
print(Jan1997)
Jan1997_mean=Jan1997['Volume'].mean()
print("Jan 1997 Mean Volume:", Jan1997_mean)
Jan1997.plot(x='Date', y='Volume', title='AMD Volume in January 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1997=df.loc[(df['Date'] >= '1997-02-01') & (df['Date'] < '1997-02-28')]
print(Feb1997)
Feb1997_mean=Feb1997['Volume'].mean()
print("Feb 1997 Mean Volume:", Feb1997_mean)
Feb1997.plot(x='Date', y='Volume', title='AMD Volume in February 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1997=df.loc[(df['Date'] >= '1997-03-01') & (df['Date'] < '1997-03-31')]
print(Mar1997)
Mar1997_mean=Mar1997['Volume'].mean()
print("Mar 1997 Mean Volume:", Mar1997_mean)
Mar1997.plot(x='Date', y='Volume', title='AMD Volume in March 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1997=df.loc[(df['Date'] >= '1997-04-01') & (df['Date'] < '1997-04-30')]
print(Apr1997)
Apr1997_mean=Apr1997['Volume'].mean()
print("Apr 1997 Mean Volume:", Apr1997_mean)
Apr1997.plot(x='Date', y='Volume', title='AMD Volume in April 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1997=df.loc[(df['Date'] >= '1997-05-01') & (df['Date'] < '1997-05-31')]
print(May1997)
May1997_mean=May1997['Volume'].mean()
print("May 1997 Mean Volume:", May1997_mean)
May1997.plot(x='Date', y='Volume', title='AMD Volume in May 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1997=df.loc[(df['Date'] >= '1997-06-01') & (df['Date'] < '1997-06-30')]
print(Jun1997)
Jun1997_mean=Jun1997['Volume'].mean()
print("Jun 1997 Mean Volume:", Jun1997_mean)
Jun1997.plot(x='Date', y='Volume', title='AMD Volume in June 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1997=df.loc[(df['Date'] >= '1997-07-01') & (df['Date'] < '1997-07-31')]
print(Jul1997)
Jul1997_mean=Jul1997['Volume'].mean()
print("Jul 1997 Mean Volume:", Jul1997_mean)
Jul1997.plot(x='Date', y='Volume', title='AMD Volume in July 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1997=df.loc[(df['Date'] >= '1997-08-01') & (df['Date'] < '1997-08-31')]
print(Aug1997)
Aug1997_mean=Aug1997['Volume'].mean()
print("Aug 1997 Mean Volume:", Aug1997_mean)
Aug1997.plot(x='Date', y='Volume', title='AMD Volume in August 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1997=df.loc[(df['Date'] >= '1997-09-01') & (df['Date'] < '1997-09-30')]
print(Sep1997)
Sep1997_mean=Sep1997['Volume'].mean()
print("Sep 1997 Mean Volume:", Sep1997_mean)
Sep1997.plot(x='Date', y='Volume', title='AMD Volume in September 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1997=df.loc[(df['Date'] >= '1997-10-01') & (df['Date'] < '1997-10-31')]
print(Oct1997)
Oct1997_mean=Oct1997['Volume'].mean()
print("Oct 1997 Mean Volume:", Oct1997_mean)
Oct1997.plot(x='Date', y='Volume', title='AMD Volume in October 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1997=df.loc[(df['Date'] >= '1997-11-01') & (df['Date'] < '1997-11-30')]
print(Nov1997)
Nov1997_mean=Nov1997['Volume'].mean()
print("Nov 1997 Mean Volume:", Nov1997_mean)
Nov1997.plot(x='Date', y='Volume', title='AMD Volume in November 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1997=df.loc[(df['Date'] >= '1997-12-01') & (df['Date'] < '1997-12-31')]
print(Dec1997)
Dec1997_mean=Dec1997['Volume'].mean()
print("Dec 1997 Mean Volume:", Dec1997_mean)
Dec1997.plot(x='Date', y='Volume', title='AMD Volume in December 1997')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1998=df.loc[(df['Date'] >= '1998-01-01') & (df['Date'] < '1998-01-31')]
print(Jan1998)
Jan1998_mean=Jan1998['Volume'].mean()
print("Jan 1998 Mean Volume:", Jan1998_mean)
Jan1998.plot(x='Date', y='Volume', title='AMD Volume in January 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1998=df.loc[(df['Date'] >= '1998-02-01') & (df['Date'] < '1998-02-28')]
print(Feb1998)
Feb1998_mean=Feb1998['Volume'].mean()
print("Feb 1998 Mean Volume:", Feb1998_mean)
Feb1998.plot(x='Date', y='Volume', title='AMD Volume in February 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1998=df.loc[(df['Date'] >= '1998-03-01') & (df['Date'] < '1998-03-31')]
print(Mar1998)
Mar1998_mean=Mar1998['Volume'].mean()
print("Mar 1998 Mean Volume:", Mar1998_mean)
Mar1998.plot(x='Date', y='Volume', title='AMD Volume in March 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1998=df.loc[(df['Date'] >= '1998-04-01') & (df['Date'] < '1998-04-30')]
print(Apr1998)
Apr1998_mean=Apr1998['Volume'].mean()
print("Apr 1998 Mean Volume:", Apr1998_mean)
Apr1998.plot(x='Date', y='Volume', title='AMD Volume in April 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1998=df.loc[(df['Date'] >= '1998-05-01') & (df['Date'] < '1998-05-31')]
print(May1998)
May1998_mean=May1998['Volume'].mean()
print("May 1998 Mean Volume:", May1998_mean)
May1998.plot(x='Date', y='Volume', title='AMD Volume in May 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1998=df.loc[(df['Date'] >= '1998-06-01') & (df['Date'] < '1998-06-30')]
print(Jun1998)
Jun1998_mean=Jun1998['Volume'].mean()
print("Jun 1998 Mean Volume:", Jun1998_mean)
Jun1998.plot(x='Date', y='Volume', title='AMD Volume in June 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1998=df.loc[(df['Date'] >= '1998-07-01') & (df['Date'] < '1998-07-31')]
print(Jul1998)
Jul1998_mean=Jul1998['Volume'].mean()
print("Jul 1998 Mean Volume:", Jul1998_mean)
Jul1998.plot(x='Date', y='Volume', title='AMD Volume in July 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1998=df.loc[(df['Date'] >= '1998-08-01') & (df['Date'] < '1998-08-31')]
print(Aug1998)
Aug1998_mean=Aug1998['Volume'].mean()
print("Aug 1998 Mean Volume:", Aug1998_mean)
Aug1998.plot(x='Date', y='Volume', title='AMD Volume in August 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1998=df.loc[(df['Date'] >= '1998-09-01') & (df['Date'] < '1998-09-30')]
print(Sep1998)
Sep1998_mean=Sep1998['Volume'].mean()
print("Sep 1998 Mean Volume:", Sep1998_mean)
Sep1998.plot(x='Date', y='Volume', title='AMD Volume in September 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1998=df.loc[(df['Date'] >= '1998-10-01') & (df['Date'] < '1998-10-31')]
print(Oct1998)
Oct1998_mean=Oct1998['Volume'].mean()
print("Oct 1998 Mean Volume:", Oct1998_mean)
Oct1998.plot(x='Date', y='Volume', title='AMD Volume in October 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1998=df.loc[(df['Date'] >= '1998-11-01') & (df['Date'] < '1998-11-30')]
print(Nov1998)
Nov1998_mean=Nov1998['Volume'].mean()
print("Nov 1998 Mean Volume:", Nov1998_mean)
Nov1998.plot(x='Date', y='Volume', title='AMD Volume in November 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1998=df.loc[(df['Date'] >= '1998-12-01') & (df['Date'] < '1998-12-31')]
print(Dec1998)
Dec1998_mean=Dec1998['Volume'].mean()
print("Dec 1998 Mean Volume:", Dec1998_mean)
Dec1998.plot(x='Date', y='Volume', title='AMD Volume in December 1998')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan1999=df.loc[(df['Date'] >= '1999-01-01') & (df['Date'] < '1999-01-31')]
print(Jan1999)
Jan1999_mean=Jan1999['Volume'].mean()
print("Jan 1999 Mean Volume:", Jan1999_mean)
Jan1999.plot(x='Date', y='Volume', title='AMD Volume in January 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb1999=df.loc[(df['Date'] >= '1999-02-01') & (df['Date'] < '1999-02-28')]
print(Feb1999)
Feb1999_mean=Feb1999['Volume'].mean()
print("Feb 1999 Mean Volume:", Feb1999_mean)
Feb1999.plot(x='Date', y='Volume', title='AMD Volume in February 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar1999=df.loc[(df['Date'] >= '1999-03-01') & (df['Date'] < '1999-03-31')]
print(Mar1999)
Mar1999_mean=Mar1999['Volume'].mean()
print("Mar 1999 Mean Volume:", Mar1999_mean)
Mar1999.plot(x='Date', y='Volume', title='AMD Volume in March 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr1999=df.loc[(df['Date'] >= '1999-04-01') & (df['Date'] < '1999-04-30')]
print(Apr1999)
Apr1999_mean=Apr1999['Volume'].mean()
print("Apr 1999 Mean Volume:", Apr1999_mean)
Apr1999.plot(x='Date', y='Volume', title='AMD Volume in April 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May1999=df.loc[(df['Date'] >= '1999-05-01') & (df['Date'] < '1999-05-31')]
print(May1999)
May1999_mean=May1999['Volume'].mean()
print("May 1999 Mean Volume:", May1999_mean)
May1999.plot(x='Date', y='Volume', title='AMD Volume in May 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun1999=df.loc[(df['Date'] >= '1999-06-01') & (df['Date'] < '1999-06-30')]
print(Jun1999)
Jun1999_mean=Jun1999['Volume'].mean()
print("Jun 1999 Mean Volume:", Jun1999_mean)
Jun1999.plot(x='Date', y='Volume', title='AMD Volume in June 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul1999=df.loc[(df['Date'] >= '1999-07-01') & (df['Date'] < '1999-07-31')]
print(Jul1999)
Jul1999_mean=Jul1999['Volume'].mean()
print("Jul 1999 Mean Volume:", Jul1999_mean)
Jul1999.plot(x='Date', y='Volume', title='AMD Volume in July 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug1999=df.loc[(df['Date'] >= '1999-08-01') & (df['Date'] < '1999-08-31')]
print(Aug1999)
Aug1999_mean=Aug1999['Volume'].mean()
print("Aug 1999 Mean Volume:", Aug1999_mean)
Aug1999.plot(x='Date', y='Volume', title='AMD Volume in August 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep1999=df.loc[(df['Date'] >= '1999-09-01') & (df['Date'] < '1999-09-30')]
print(Sep1999)
Sep1999_mean=Sep1999['Volume'].mean()
print("Sep 1999 Mean Volume:", Sep1999_mean)
Sep1999.plot(x='Date', y='Volume', title='AMD Volume in September 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct1999=df.loc[(df['Date'] >= '1999-10-01') & (df['Date'] < '1999-10-31')]
print(Oct1999)
Oct1999_mean=Oct1999['Volume'].mean()
print("Oct 1999 Mean Volume:", Oct1999_mean)
Oct1999.plot(x='Date', y='Volume', title='AMD Volume in October 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov1999=df.loc[(df['Date'] >= '1999-11-01') & (df['Date'] < '1999-11-30')]
print(Nov1999)
Nov1999_mean=Nov1999['Volume'].mean()
print("Nov 1999 Mean Volume:", Nov1999_mean)
Nov1999.plot(x='Date', y='Volume', title='AMD Volume in November 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec1999=df.loc[(df['Date'] >= '1999-12-01') & (df['Date'] < '1999-12-31')]
print(Dec1999)
Dec1999_mean=Dec1999['Volume'].mean()
print("Dec 1999 Mean Volume:", Dec1999_mean)
Dec1999.plot(x='Date', y='Volume', title='AMD Volume in December 1999')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2000=df.loc[(df['Date'] >= '2000-01-01') & (df['Date'] < '2000-01-31')]
print(Jan2000)
Jan2000_mean=Jan2000['Volume'].mean()
print("Jan 2000 Mean Volume:", Jan2000_mean)
Jan2000.plot(x='Date', y='Volume', title='AMD Volume in January 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2000=df.loc[(df['Date'] >= '2000-02-01') & (df['Date'] < '2000-02-29')]
print(Feb2000)
Feb2000_mean=Feb2000['Volume'].mean()
print("Feb 2000 Mean Volume:", Feb2000_mean)
Feb2000.plot(x='Date', y='Volume', title='AMD Volume in February 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2000=df.loc[(df['Date'] >= '2000-03-01') & (df['Date'] < '2000-03-31')]
print(Mar2000)
Mar2000_mean=Mar2000['Volume'].mean()
print("Mar 2000 Mean Volume:", Mar2000_mean)
Mar2000.plot(x='Date', y='Volume', title='AMD Volume in March 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2000=df.loc[(df['Date'] >= '2000-04-01') & (df['Date'] < '2000-04-30')]
print(Apr2000)
Apr2000_mean=Apr2000['Volume'].mean()
print("Apr 2000 Mean Volume:", Apr2000_mean)
Apr2000.plot(x='Date', y='Volume', title='AMD Volume in April 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2000=df.loc[(df['Date'] >= '2000-05-01') & (df['Date'] < '2000-05-31')]
print(May2000)
May2000_mean=May2000['Volume'].mean()
print("May 2000 Mean Volume:", May2000_mean)
May2000.plot(x='Date', y='Volume', title='AMD Volume in May 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2000=df.loc[(df['Date'] >= '2000-06-01') & (df['Date'] < '2000-06-30')]
print(Jun2000)
Jun2000_mean=Jun2000['Volume'].mean()
print("Jun 2000 Mean Volume:", Jun2000_mean)
Jun2000.plot(x='Date', y='Volume', title='AMD Volume in June 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2000=df.loc[(df['Date'] >= '2000-07-01') & (df['Date'] < '2000-07-31')]
print(Jul2000)
Jul2000_mean=Jul2000['Volume'].mean()
print("Jul 2000 Mean Volume:", Jul2000_mean)
Jul2000.plot(x='Date', y='Volume', title='AMD Volume in July 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2000=df.loc[(df['Date'] >= '2000-08-01') & (df['Date'] < '2000-08-31')]
print(Aug2000)
Aug2000_mean=Aug2000['Volume'].mean()
print("Aug 2000 Mean Volume:", Aug2000_mean)
Aug2000.plot(x='Date', y='Volume', title='AMD Volume in August 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2000=df.loc[(df['Date'] >= '2000-09-01') & (df['Date'] < '2000-09-30')]
print(Sep2000)
Sep2000_mean=Sep2000['Volume'].mean()
print("Sep 2000 Mean Volume:", Sep2000_mean)
Sep2000.plot(x='Date', y='Volume', title='AMD Volume in September 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2000=df.loc[(df['Date'] >= '2000-10-01') & (df['Date'] < '2000-10-31')]
print(Oct2000)
Oct2000_mean=Oct2000['Volume'].mean()
print("Oct 2000 Mean Volume:", Oct2000_mean)
Oct2000.plot(x='Date', y='Volume', title='AMD Volume in October 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2000=df.loc[(df['Date'] >= '2000-11-01') & (df['Date'] < '2000-11-30')]
print(Nov2000)
Nov2000_mean=Nov2000['Volume'].mean()
print("Nov 2000 Mean Volume:", Nov2000_mean)
Nov2000.plot(x='Date', y='Volume', title='AMD Volume in November 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2000=df.loc[(df['Date'] >= '2000-12-01') & (df['Date'] < '2000-12-31')]
print(Dec2000)
Dec2000_mean=Dec2000['Volume'].mean()
print("Dec 2000 Mean Volume:", Dec2000_mean)
Dec2000.plot(x='Date', y='Volume', title='AMD Volume in December 2000')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2001=df.loc[(df['Date'] >= '2001-01-01') & (df['Date'] < '2001-01-31')]
print(Jan2001)
Jan2001_mean=Jan2001['Volume'].mean()
print("Jan 2001 Mean Volume:", Jan2001_mean)
Jan2001.plot(x='Date', y='Volume', title='AMD Volume in January 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2001=df.loc[(df['Date'] >= '2001-02-01') & (df['Date'] < '2001-02-28')]
print(Feb2001)
Feb2001_mean=Feb2001['Volume'].mean()
print("Feb 2001 Mean Volume:", Feb2001_mean)
Feb2001.plot(x='Date', y='Volume', title='AMD Volume in February 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2001=df.loc[(df['Date'] >= '2001-03-01') & (df['Date'] < '2001-03-31')]
print(Mar2001)
Mar2001_mean=Mar2001['Volume'].mean()
print("Mar 2001 Mean Volume:", Mar2001_mean)
Mar2001.plot(x='Date', y='Volume', title='AMD Volume in March 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2001=df.loc[(df['Date'] >= '2001-04-01') & (df['Date'] < '2001-04-30')]
print(Apr2001)
Apr2001_mean=Apr2001['Volume'].mean()
print("Apr 2001 Mean Volume:", Apr2001_mean)
Apr2001.plot(x='Date', y='Volume', title='AMD Volume in April 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2001=df.loc[(df['Date'] >= '2001-05-01') & (df['Date'] < '2001-05-31')]
print(May2001)
May2001_mean=May2001['Volume'].mean()
print("May 2001 Mean Volume:", May2001_mean)
May2001.plot(x='Date', y='Volume', title='AMD Volume in May 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2001=df.loc[(df['Date'] >= '2001-06-01') & (df['Date'] < '2001-06-30')]
print(Jun2001)
Jun2001_mean=Jun2001['Volume'].mean()
print("Jun 2001 Mean Volume:", Jun2001_mean)
Jun2001.plot(x='Date', y='Volume', title='AMD Volume in June 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2001=df.loc[(df['Date'] >= '2001-07-01') & (df['Date'] < '2001-07-31')]
print(Jul2001)
Jul2001_mean=Jul2001['Volume'].mean()
print("Jul 2001 Mean Volume:", Jul2001_mean)
Jul2001.plot(x='Date', y='Volume', title='AMD Volume in July 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2001=df.loc[(df['Date'] >= '2001-08-01') & (df['Date'] < '2001-08-31')]
print(Aug2001)
Aug2001_mean=Aug2001['Volume'].mean()
print("Aug 2001 Mean Volume:", Aug2001_mean)
Aug2001.plot(x='Date', y='Volume', title='AMD Volume in August 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2001=df.loc[(df['Date'] >= '2001-09-01') & (df['Date'] < '2001-09-30')]
print(Sep2001)
Sep2001_mean=Sep2001['Volume'].mean()
print("Sep 2001 Mean Volume:", Sep2001_mean)
Sep2001.plot(x='Date', y='Volume', title='AMD Volume in September 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2001=df.loc[(df['Date'] >= '2001-10-01') & (df['Date'] < '2001-10-31')]
print(Oct2001)
Oct2001_mean=Oct2001['Volume'].mean()
print("Oct 2001 Mean Volume:", Oct2001_mean)
Oct2001.plot(x='Date', y='Volume', title='AMD Volume in October 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2001=df.loc[(df['Date'] >= '2001-11-01') & (df['Date'] < '2001-11-30')]
print(Nov2001)
Nov2001_mean=Nov2001['Volume'].mean()
print("Nov 2001 Mean Volume:", Nov2001_mean)
Nov2001.plot(x='Date', y='Volume', title='AMD Volume in November 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2001=df.loc[(df['Date'] >= '2001-12-01') & (df['Date'] < '2001-12-31')]
print(Dec2001)
Dec2001_mean=Dec2001['Volume'].mean()
print("Dec 2001 Mean Volume:", Dec2001_mean)
Dec2001.plot(x='Date', y='Volume', title='AMD Volume in December 2001')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2002=df.loc[(df['Date'] >= '2002-01-01') & (df['Date'] < '2002-01-31')]
print(Jan2002)
Jan2002_mean=Jan2002['Volume'].mean()
print("Jan 2002 Mean Volume:", Jan2002_mean)
Jan2002.plot(x='Date', y='Volume', title='AMD Volume in January 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2002=df.loc[(df['Date'] >= '2002-02-01') & (df['Date'] < '2002-02-28')]
print(Feb2002)
Feb2002_mean=Feb2002['Volume'].mean()
print("Feb 2002 Mean Volume:", Feb2002_mean)
Feb2002.plot(x='Date', y='Volume', title='AMD Volume in February 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2002=df.loc[(df['Date'] >= '2002-03-01') & (df['Date'] < '2002-03-31')]
print(Mar2002)
Mar2002_mean=Mar2002['Volume'].mean()
print("Mar 2002 Mean Volume:", Mar2002_mean)
Mar2002.plot(x='Date', y='Volume', title='AMD Volume in March 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2002=df.loc[(df['Date'] >= '2002-04-01') & (df['Date'] < '2002-04-30')]
print(Apr2002)
Apr2002_mean=Apr2002['Volume'].mean()
print("Apr 2002 Mean Volume:", Apr2002_mean)
Apr2002.plot(x='Date', y='Volume', title='AMD Volume in April 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2002=df.loc[(df['Date'] >= '2002-05-01') & (df['Date'] < '2002-05-31')]
print(May2002)
May2002_mean=May2002['Volume'].mean()
print("May 2002 Mean Volume:", May2002_mean)
May2002.plot(x='Date', y='Volume', title='AMD Volume in May 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2002=df.loc[(df['Date'] >= '2002-06-01') & (df['Date'] < '2002-06-30')]
print(Jun2002)
Jun2002_mean=Jun2002['Volume'].mean()
print("Jun 2002 Mean Volume:", Jun2002_mean)
Jun2002.plot(x='Date', y='Volume', title='AMD Volume in June 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2002=df.loc[(df['Date'] >= '2002-07-01') & (df['Date'] < '2002-07-31')]
print(Jul2002)
Jul2002_mean=Jul2002['Volume'].mean()
print("Jul 2002 Mean Volume:", Jul2002_mean)
Jul2002.plot(x='Date', y='Volume', title='AMD Volume in July 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2002=df.loc[(df['Date'] >= '2002-08-01') & (df['Date'] < '2002-08-31')]
print(Aug2002)
Aug2002_mean=Aug2002['Volume'].mean()
print("Aug 2002 Mean Volume:", Aug2002_mean)
Aug2002.plot(x='Date', y='Volume', title='AMD Volume in August 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2002=df.loc[(df['Date'] >= '2002-09-01') & (df['Date'] < '2002-09-30')]
print(Sep2002)
Sep2002_mean=Sep2002['Volume'].mean()
print("Sep 2002 Mean Volume:", Sep2002_mean)
Sep2002.plot(x='Date', y='Volume', title='AMD Volume in September 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2002=df.loc[(df['Date'] >= '2002-10-01') & (df['Date'] < '2002-10-31')]
print(Oct2002)
Oct2002_mean=Oct2002['Volume'].mean()
print("Oct 2002 Mean Volume:", Oct2002_mean)
Oct2002.plot(x='Date', y='Volume', title='AMD Volume in October 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2002=df.loc[(df['Date'] >= '2002-11-01') & (df['Date'] < '2002-11-30')]
print(Nov2002)
Nov2002_mean=Nov2002['Volume'].mean()
print("Nov 2002 Mean Volume:", Nov2002_mean)
Nov2002.plot(x='Date', y='Volume', title='AMD Volume in November 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2002=df.loc[(df['Date'] >= '2002-12-01') & (df['Date'] < '2002-12-31')]
print(Dec2002)
Dec2002_mean=Dec2002['Volume'].mean()
print("Dec 2002 Mean Volume:", Dec2002_mean)
Dec2002.plot(x='Date', y='Volume', title='AMD Volume in December 2002')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2003=df.loc[(df['Date'] >= '2003-01-01') & (df['Date'] < '2003-01-31')]
print(Jan2003)
Jan2003_mean=Jan2003['Volume'].mean()
print("Jan 2003 Mean Volume:", Jan2003_mean)
Jan2003.plot(x='Date', y='Volume', title='AMD Volume in January 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2003=df.loc[(df['Date'] >= '2003-02-01') & (df['Date'] < '2003-02-28')]
print(Feb2003)
Feb2003_mean=Feb2003['Volume'].mean()
print("Feb 2003 Mean Volume:", Feb2003_mean)
Feb2003.plot(x='Date', y='Volume', title='AMD Volume in February 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2003=df.loc[(df['Date'] >= '2003-03-01') & (df['Date'] < '2003-03-31')]
print(Mar2003)
Mar2003_mean=Mar2003['Volume'].mean()
print("Mar 2003 Mean Volume:", Mar2003_mean)
Mar2003.plot(x='Date', y='Volume', title='AMD Volume in March 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2003=df.loc[(df['Date'] >= '2003-04-01') & (df['Date'] < '2003-04-30')]
print(Apr2003)
Apr2003_mean=Apr2003['Volume'].mean()
print("Apr 2003 Mean Volume:", Apr2003_mean)
Apr2003.plot(x='Date', y='Volume', title='AMD Volume in April 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2003=df.loc[(df['Date'] >= '2003-05-01') & (df['Date'] < '2003-05-31')]
print(May2003)
May2003_mean=May2003['Volume'].mean()
print("May 2003 Mean Volume:", May2003_mean)
May2003.plot(x='Date', y='Volume', title='AMD Volume in May 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2003=df.loc[(df['Date'] >= '2003-06-01') & (df['Date'] < '2003-06-30')]
print(Jun2003)
Jun2003_mean=Jun2003['Volume'].mean()
print("Jun 2003 Mean Volume:", Jun2003_mean)
Jun2003.plot(x='Date', y='Volume', title='AMD Volume in June 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2003=df.loc[(df['Date'] >= '2003-07-01') & (df['Date'] < '2003-07-31')]
print(Jul2003)
Jul2003_mean=Jul2003['Volume'].mean()
print("Jul 2003 Mean Volume:", Jul2003_mean)
Jul2003.plot(x='Date', y='Volume', title='AMD Volume in July 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2003=df.loc[(df['Date'] >= '2003-08-01') & (df['Date'] < '2003-08-31')]
print(Aug2003)
Aug2003_mean=Aug2003['Volume'].mean()
print("Aug 2003 Mean Volume:", Aug2003_mean)
Aug2003.plot(x='Date', y='Volume', title='AMD Volume in August 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2003=df.loc[(df['Date'] >= '2003-09-01') & (df['Date'] < '2003-09-30')]
print(Sep2003)
Sep2003_mean=Sep2003['Volume'].mean()
print("Sep 2003 Mean Volume:", Sep2003_mean)
Sep2003.plot(x='Date', y='Volume', title='AMD Volume in September 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2003=df.loc[(df['Date'] >= '2003-10-01') & (df['Date'] < '2003-10-31')]
print(Oct2003)
Oct2003_mean=Oct2003['Volume'].mean()
print("Oct 2003 Mean Volume:", Oct2003_mean)
Oct2003.plot(x='Date', y='Volume', title='AMD Volume in October 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2003=df.loc[(df['Date'] >= '2003-11-01') & (df['Date'] < '2003-11-30')]
print(Nov2003)
Nov2003_mean=Nov2003['Volume'].mean()
print("Nov 2003 Mean Volume:", Nov2003_mean)
Nov2003.plot(x='Date', y='Volume', title='AMD Volume in November 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2003=df.loc[(df['Date'] >= '2003-12-01') & (df['Date'] < '2003-12-31')]
print(Dec2003)
Dec2003_mean=Dec2003['Volume'].mean()
print("Dec 2003 Mean Volume:", Dec2003_mean)
Dec2003.plot(x='Date', y='Volume', title='AMD Volume in December 2003')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2004=df.loc[(df['Date'] >= '2004-01-01') & (df['Date'] < '2004-01-31')]
print(Jan2004)
Jan2004_mean=Jan2004['Volume'].mean()
print("Jan 2004 Mean Volume:", Jan2004_mean)
Jan2004.plot(x='Date', y='Volume', title='AMD Volume in January 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2004=df.loc[(df['Date'] >= '2004-02-01') & (df['Date'] < '2004-02-29')]
print(Feb2004)
Feb2004_mean=Feb2004['Volume'].mean()
print("Feb 2004 Mean Volume:", Feb2004_mean)
Feb2004.plot(x='Date', y='Volume', title='AMD Volume in February 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2004=df.loc[(df['Date'] >= '2004-03-01') & (df['Date'] < '2004-03-31')]
print(Mar2004)
Mar2004_mean=Mar2004['Volume'].mean()
print("Mar 2004 Mean Volume:", Mar2004_mean)
Mar2004.plot(x='Date', y='Volume', title='AMD Volume in March 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2004=df.loc[(df['Date'] >= '2004-04-01') & (df['Date'] < '2004-04-30')]
print(Apr2004)
Apr2004_mean=Apr2004['Volume'].mean()
print("Apr 2004 Mean Volume:", Apr2004_mean)
Apr2004.plot(x='Date', y='Volume', title='AMD Volume in April 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2004=df.loc[(df['Date'] >= '2004-05-01') & (df['Date'] < '2004-05-31')]
print(May2004)
May2004_mean=May2004['Volume'].mean()
print("May 2004 Mean Volume:", May2004_mean)
May2004.plot(x='Date', y='Volume', title='AMD Volume in May 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2004=df.loc[(df['Date'] >= '2004-06-01') & (df['Date'] < '2004-06-30')]
print(Jun2004)
Jun2004_mean=Jun2004['Volume'].mean()
print("Jun 2004 Mean Volume:", Jun2004_mean)
Jun2004.plot(x='Date', y='Volume', title='AMD Volume in June 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2004=df.loc[(df['Date'] >= '2004-07-01') & (df['Date'] < '2004-07-31')]
print(Jul2004)
Jul2004_mean=Jul2004['Volume'].mean()
print("Jul 2004 Mean Volume:", Jul2004_mean)
Jul2004.plot(x='Date', y='Volume', title='AMD Volume in July 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2004=df.loc[(df['Date'] >= '2004-08-01') & (df['Date'] < '2004-08-31')]
print(Aug2004)
Aug2004_mean=Aug2004['Volume'].mean()
print("Aug 2004 Mean Volume:", Aug2004_mean)
Aug2004.plot(x='Date', y='Volume', title='AMD Volume in August 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2004=df.loc[(df['Date'] >= '2004-09-01') & (df['Date'] < '2004-09-30')]
print(Sep2004)
Sep2004_mean=Sep2004['Volume'].mean()
print("Sep 2004 Mean Volume:", Sep2004_mean)
Sep2004.plot(x='Date', y='Volume', title='AMD Volume in September 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2004=df.loc[(df['Date'] >= '2004-10-01') & (df['Date'] < '2004-10-31')]
print(Oct2004)
Oct2004_mean=Oct2004['Volume'].mean()
print("Oct 2004 Mean Volume:", Oct2004_mean)
Oct2004.plot(x='Date', y='Volume', title='AMD Volume in October 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2004=df.loc[(df['Date'] >= '2004-11-01') & (df['Date'] < '2004-11-30')]
print(Nov2004)
Nov2004_mean=Nov2004['Volume'].mean()
print("Nov 2004 Mean Volume:", Nov2004_mean)
Nov2004.plot(x='Date', y='Volume', title='AMD Volume in November 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2004=df.loc[(df['Date'] >= '2004-12-01') & (df['Date'] < '2004-12-31')]
print(Dec2004)
Dec2004_mean=Dec2004['Volume'].mean()
print("Dec 2004 Mean Volume:", Dec2004_mean)
Dec2004.plot(x='Date', y='Volume', title='AMD Volume in December 2004')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2005=df.loc[(df['Date'] >= '2005-01-01') & (df['Date'] < '2005-01-31')]
print(Jan2005)
Jan2005_mean=Jan2005['Volume'].mean()
print("Jan 2005 Mean Volume:", Jan2005_mean)
Jan2005.plot(x='Date', y='Volume', title='AMD Volume in January 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2005=df.loc[(df['Date'] >= '2005-02-01') & (df['Date'] < '2005-02-28')]
print(Feb2005)
Feb2005_mean=Feb2005['Volume'].mean()
print("Feb 2005 Mean Volume:", Feb2005_mean)
Feb2005.plot(x='Date', y='Volume', title='AMD Volume in February 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2005=df.loc[(df['Date'] >= '2005-03-01') & (df['Date'] < '2005-03-31')]
print(Mar2005)
Mar2005_mean=Mar2005['Volume'].mean()
print("Mar 2005 Mean Volume:", Mar2005_mean)
Mar2005.plot(x='Date', y='Volume', title='AMD Volume in March 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2005=df.loc[(df['Date'] >= '2005-04-01') & (df['Date'] < '2005-04-30')]
print(Apr2005)
Apr2005_mean=Apr2005['Volume'].mean()
print("Apr 2005 Mean Volume:", Apr2005_mean)
Apr2005.plot(x='Date', y='Volume', title='AMD Volume in April 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2005=df.loc[(df['Date'] >= '2005-05-01') & (df['Date'] < '2005-05-31')]
print(May2005)
May2005_mean=May2005['Volume'].mean()
print("May 2005 Mean Volume:", May2005_mean)
May2005.plot(x='Date', y='Volume', title='AMD Volume in May 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2005=df.loc[(df['Date'] >= '2005-06-01') & (df['Date'] < '2005-06-30')]
print(Jun2005)
Jun2005_mean=Jun2005['Volume'].mean()
print("Jun 2005 Mean Volume:", Jun2005_mean)
Jun2005.plot(x='Date', y='Volume', title='AMD Volume in June 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2005=df.loc[(df['Date'] >= '2005-07-01') & (df['Date'] < '2005-07-31')]
print(Jul2005)
Jul2005_mean=Jul2005['Volume'].mean()
print("Jul 2005 Mean Volume:", Jul2005_mean)
Jul2005.plot(x='Date', y='Volume', title='AMD Volume in July 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2005=df.loc[(df['Date'] >= '2005-08-01') & (df['Date'] < '2005-08-31')]
print(Aug2005)
Aug2005_mean=Aug2005['Volume'].mean()
print("Aug 2005 Mean Volume:", Aug2005_mean)
Aug2005.plot(x='Date', y='Volume', title='AMD Volume in August 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2005=df.loc[(df['Date'] >= '2005-09-01') & (df['Date'] < '2005-09-30')]
print(Sep2005)
Sep2005_mean=Sep2005['Volume'].mean()
print("Sep 2005 Mean Volume:", Sep2005_mean)
Sep2005.plot(x='Date', y='Volume', title='AMD Volume in September 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2005=df.loc[(df['Date'] >= '2005-10-01') & (df['Date'] < '2005-10-31')]
print(Oct2005)
Oct2005_mean=Oct2005['Volume'].mean()
print("Oct 2005 Mean Volume:", Oct2005_mean)
Oct2005.plot(x='Date', y='Volume', title='AMD Volume in October 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2005=df.loc[(df['Date'] >= '2005-11-01') & (df['Date'] < '2005-11-30')]
print(Nov2005)
Nov2005_mean=Nov2005['Volume'].mean()
print("Nov 2005 Mean Volume:", Nov2005_mean)
Nov2005.plot(x='Date', y='Volume', title='AMD Volume in November 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2005=df.loc[(df['Date'] >= '2005-12-01') & (df['Date'] < '2005-12-31')]
print(Dec2005)
Dec2005_mean=Dec2005['Volume'].mean()
print("Dec 2005 Mean Volume:", Dec2005_mean)
Dec2005.plot(x='Date', y='Volume', title='AMD Volume in December 2005')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2006=df.loc[(df['Date'] >= '2006-01-01') & (df['Date'] < '2006-01-31')]
print(Jan2006)
Jan2006_mean=Jan2006['Volume'].mean()
print("Jan 2006 Mean Volume:", Jan2006_mean)
Jan2006.plot(x='Date', y='Volume', title='AMD Volume in January 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2006=df.loc[(df['Date'] >= '2006-02-01') & (df['Date'] < '2006-02-28')]
print(Feb2006)
Feb2006_mean=Feb2006['Volume'].mean()
print("Feb 2006 Mean Volume:", Feb2006_mean)
Feb2006.plot(x='Date', y='Volume', title='AMD Volume in February 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2006=df.loc[(df['Date'] >= '2006-03-01') & (df['Date'] < '2006-03-31')]
print(Mar2006)
Mar2006_mean=Mar2006['Volume'].mean()
print("Mar 2006 Mean Volume:", Mar2006_mean)
Mar2006.plot(x='Date', y='Volume', title='AMD Volume in March 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2006=df.loc[(df['Date'] >= '2006-04-01') & (df['Date'] < '2006-04-30')]
print(Apr2006)
Apr2006_mean=Apr2006['Volume'].mean()
print("Apr 2006 Mean Volume:", Apr2006_mean)
Apr2006.plot(x='Date', y='Volume', title='AMD Volume in April 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2006=df.loc[(df['Date'] >= '2006-05-01') & (df['Date'] < '2006-05-31')]
print(May2006)
May2006_mean=May2006['Volume'].mean()
print("May 2006 Mean Volume:", May2006_mean)
May2006.plot(x='Date', y='Volume', title='AMD Volume in May 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2006=df.loc[(df['Date'] >= '2006-06-01') & (df['Date'] < '2006-06-30')]
print(Jun2006)
Jun2006_mean=Jun2006['Volume'].mean()
print("Jun 2006 Mean Volume:", Jun2006_mean)
Jun2006.plot(x='Date', y='Volume', title='AMD Volume in June 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2006=df.loc[(df['Date'] >= '2006-07-01') & (df['Date'] < '2006-07-31')]
print(Jul2006)
Jul2006_mean=Jul2006['Volume'].mean()
print("Jul 2006 Mean Volume:", Jul2006_mean)
Jul2006.plot(x='Date', y='Volume', title='AMD Volume in July 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2006=df.loc[(df['Date'] >= '2006-08-01') & (df['Date'] < '2006-08-31')]
print(Aug2006)
Aug2006_mean=Aug2006['Volume'].mean()
print("Aug 2006 Mean Volume:", Aug2006_mean)
Aug2006.plot(x='Date', y='Volume', title='AMD Volume in August 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2006=df.loc[(df['Date'] >= '2006-09-01') & (df['Date'] < '2006-09-30')]
print(Sep2006)
Sep2006_mean=Sep2006['Volume'].mean()
print("Sep 2006 Mean Volume:", Sep2006_mean)
Sep2006.plot(x='Date', y='Volume', title='AMD Volume in September 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2006=df.loc[(df['Date'] >= '2006-10-01') & (df['Date'] < '2006-10-31')]
print(Oct2006)
Oct2006_mean=Oct2006['Volume'].mean()
print("Oct 2006 Mean Volume:", Oct2006_mean)
Oct2006.plot(x='Date', y='Volume', title='AMD Volume in October 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2006=df.loc[(df['Date'] >= '2006-11-01') & (df['Date'] < '2006-11-30')]
print(Nov2006)
Nov2006_mean=Nov2006['Volume'].mean()
print("Nov 2006 Mean Volume:", Nov2006_mean)
Nov2006.plot(x='Date', y='Volume', title='AMD Volume in November 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2006=df.loc[(df['Date'] >= '2006-12-01') & (df['Date'] < '2006-12-31')]
print(Dec2006)
Dec2006_mean=Dec2006['Volume'].mean()
print("Dec 2006 Mean Volume:", Dec2006_mean)
Dec2006.plot(x='Date', y='Volume', title='AMD Volume in December 2006')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2007=df.loc[(df['Date'] >= '2007-01-01') & (df['Date'] < '2007-01-31')]
print(Jan2007)
Jan2007_mean=Jan2007['Volume'].mean()
print("Jan 2007 Mean Volume:", Jan2007_mean)
Jan2007.plot(x='Date', y='Volume', title='AMD Volume in January 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2007=df.loc[(df['Date'] >= '2007-02-01') & (df['Date'] < '2007-02-28')]
print(Feb2007)
Feb2007_mean=Feb2007['Volume'].mean()
print("Feb 2007 Mean Volume:", Feb2007_mean)
Feb2007.plot(x='Date', y='Volume', title='AMD Volume in February 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2007=df.loc[(df['Date'] >= '2007-03-01') & (df['Date'] < '2007-03-31')]
print(Mar2007)
Mar2007_mean=Mar2007['Volume'].mean()
print("Mar 2007 Mean Volume:", Mar2007_mean)
Mar2007.plot(x='Date', y='Volume', title='AMD Volume in March 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2007=df.loc[(df['Date'] >= '2007-04-01') & (df['Date'] < '2007-04-30')]
print(Apr2007)
Apr2007_mean=Apr2007['Volume'].mean()
print("Apr 2007 Mean Volume:", Apr2007_mean)
Apr2007.plot(x='Date', y='Volume', title='AMD Volume in April 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2007=df.loc[(df['Date'] >= '2007-05-01') & (df['Date'] < '2007-05-31')]
print(May2007)
May2007_mean=May2007['Volume'].mean()
print("May 2007 Mean Volume:", May2007_mean)
May2007.plot(x='Date', y='Volume', title='AMD Volume in May 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2007=df.loc[(df['Date'] >= '2007-06-01') & (df['Date'] < '2007-06-30')]
print(Jun2007)
Jun2007_mean=Jun2007['Volume'].mean()
print("Jun 2007 Mean Volume:", Jun2007_mean)
Jun2007.plot(x='Date', y='Volume', title='AMD Volume in June 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2007=df.loc[(df['Date'] >= '2007-07-01') & (df['Date'] < '2007-07-31')]
print(Jul2007)
Jul2007_mean=Jul2007['Volume'].mean()
print("Jul 2007 Mean Volume:", Jul2007_mean)
Jul2007.plot(x='Date', y='Volume', title='AMD Volume in July 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2007=df.loc[(df['Date'] >= '2007-08-01') & (df['Date'] < '2007-08-31')]
print(Aug2007)
Aug2007_mean=Aug2007['Volume'].mean()
print("Aug 2007 Mean Volume:", Aug2007_mean)
Aug2007.plot(x='Date', y='Volume', title='AMD Volume in August 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2007=df.loc[(df['Date'] >= '2007-09-01') & (df['Date'] < '2007-09-30')]
print(Sep2007)
Sep2007_mean=Sep2007['Volume'].mean()
print("Sep 2007 Mean Volume:", Sep2007_mean)
Sep2007.plot(x='Date', y='Volume', title='AMD Volume in September 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2007=df.loc[(df['Date'] >= '2007-10-01') & (df['Date'] < '2007-10-31')]
print(Oct2007)
Oct2007_mean=Oct2007['Volume'].mean()
print("Oct 2007 Mean Volume:", Oct2007_mean)
Oct2007.plot(x='Date', y='Volume', title='AMD Volume in October 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2007=df.loc[(df['Date'] >= '2007-11-01') & (df['Date'] < '2007-11-30')]
print(Nov2007)
Nov2007_mean=Nov2007['Volume'].mean()
print("Nov 2007 Mean Volume:", Nov2007_mean)
Nov2007.plot(x='Date', y='Volume', title='AMD Volume in November 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2007=df.loc[(df['Date'] >= '2007-12-01') & (df['Date'] < '2007-12-31')]
print(Dec2007)
Dec2007_mean=Dec2007['Volume'].mean()
print("Dec 2007 Mean Volume:", Dec2007_mean)
Dec2007.plot(x='Date', y='Volume', title='AMD Volume in December 2007')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2008=df.loc[(df['Date'] >= '2008-01-01') & (df['Date'] < '2008-01-31')]
print(Jan2008)
Jan2008_mean=Jan2008['Volume'].mean()
print("Jan 2008 Mean Volume:", Jan2008_mean)
Jan2008.plot(x='Date', y='Volume', title='AMD Volume in January 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2008=df.loc[(df['Date'] >= '2008-02-01') & (df['Date'] < '2008-02-29')]
print(Feb2008)
Feb2008_mean=Feb2008['Volume'].mean()
print("Feb 2008 Mean Volume:", Feb2008_mean)
Feb2008.plot(x='Date', y='Volume', title='AMD Volume in February 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2008=df.loc[(df['Date'] >= '2008-03-01') & (df['Date'] < '2008-03-31')]
print(Mar2008)
Mar2008_mean=Mar2008['Volume'].mean()
print("Mar 2008 Mean Volume:", Mar2008_mean)
Mar2008.plot(x='Date', y='Volume', title='AMD Volume in March 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2008=df.loc[(df['Date'] >= '2008-04-01') & (df['Date'] < '2008-04-30')]
print(Apr2008)
Apr2008_mean=Apr2008['Volume'].mean()
print("Apr 2008 Mean Volume:", Apr2008_mean)
Apr2008.plot(x='Date', y='Volume', title='AMD Volume in April 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2008=df.loc[(df['Date'] >= '2008-05-01') & (df['Date'] < '2008-05-31')]
print(May2008)
May2008_mean=May2008['Volume'].mean()
print("May 2008 Mean Volume:", May2008_mean)
May2008.plot(x='Date', y='Volume', title='AMD Volume in May 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2008=df.loc[(df['Date'] >= '2008-06-01') & (df['Date'] < '2008-06-30')]
print(Jun2008)
Jun2008_mean=Jun2008['Volume'].mean()
print("Jun 2008 Mean Volume:", Jun2008_mean)
Jun2008.plot(x='Date', y='Volume', title='AMD Volume in June 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2008=df.loc[(df['Date'] >= '2008-07-01') & (df['Date'] < '2008-07-31')]
print(Jul2008)
Jul2008_mean=Jul2008['Volume'].mean()
print("Jul 2008 Mean Volume:", Jul2008_mean)
Jul2008.plot(x='Date', y='Volume', title='AMD Volume in July 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2008=df.loc[(df['Date'] >= '2008-08-01') & (df['Date'] < '2008-08-31')]
print(Aug2008)
Aug2008_mean=Aug2008['Volume'].mean()
print("Aug 2008 Mean Volume:", Aug2008_mean)
Aug2008.plot(x='Date', y='Volume', title='AMD Volume in August 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2008=df.loc[(df['Date'] >= '2008-09-01') & (df['Date'] < '2008-09-30')]
print(Sep2008)
Sep2008_mean=Sep2008['Volume'].mean()
print("Sep 2008 Mean Volume:", Sep2008_mean)
Sep2008.plot(x='Date', y='Volume', title='AMD Volume in September 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2008=df.loc[(df['Date'] >= '2008-10-01') & (df['Date'] < '2008-10-31')]
print(Oct2008)
Oct2008_mean=Oct2008['Volume'].mean()
print("Oct 2008 Mean Volume:", Oct2008_mean)
Oct2008.plot(x='Date', y='Volume', title='AMD Volume in October 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2008=df.loc[(df['Date'] >= '2008-11-01') & (df['Date'] < '2008-11-30')]
print(Nov2008)
Nov2008_mean=Nov2008['Volume'].mean()
print("Nov 2008 Mean Volume:", Nov2008_mean)
Nov2008.plot(x='Date', y='Volume', title='AMD Volume in November 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2008=df.loc[(df['Date'] >= '2008-12-01') & (df['Date'] < '2008-12-31')]
print(Dec2008)
Dec2008_mean=Dec2008['Volume'].mean()
print("Dec 2008 Mean Volume:", Dec2008_mean)
Dec2008.plot(x='Date', y='Volume', title='AMD Volume in December 2008')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2009=df.loc[(df['Date'] >= '2009-01-01') & (df['Date'] < '2009-01-31')]
print(Jan2009)
Jan2009_mean=Jan2009['Volume'].mean()
print("Jan 2009 Mean Volume:", Jan2009_mean)
Jan2009.plot(x='Date', y='Volume', title='AMD Volume in January 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2009=df.loc[(df['Date'] >= '2009-02-01') & (df['Date'] < '2009-02-28')]
print(Feb2009)
Feb2009_mean=Feb2009['Volume'].mean()
print("Feb 2009 Mean Volume:", Feb2009_mean)
Feb2009.plot(x='Date', y='Volume', title='AMD Volume in February 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2009=df.loc[(df['Date'] >= '2009-03-01') & (df['Date'] < '2009-03-31')]
print(Mar2009)
Mar2009_mean=Mar2009['Volume'].mean()
print("Mar 2009 Mean Volume:", Mar2009_mean)
Mar2009.plot(x='Date', y='Volume', title='AMD Volume in March 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2009=df.loc[(df['Date'] >= '2009-04-01') & (df['Date'] < '2009-04-30')]
print(Apr2009)
Apr2009_mean=Apr2009['Volume'].mean()
print("Apr 2009 Mean Volume:", Apr2009_mean)
Apr2009.plot(x='Date', y='Volume', title='AMD Volume in April 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2009=df.loc[(df['Date'] >= '2009-05-01') & (df['Date'] < '2009-05-31')]
print(May2009)
May2009_mean=May2009['Volume'].mean()
print("May 2009 Mean Volume:", May2009_mean)
May2009.plot(x='Date', y='Volume', title='AMD Volume in May 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2009=df.loc[(df['Date'] >= '2009-06-01') & (df['Date'] < '2009-06-30')]
print(Jun2009)
Jun2009_mean=Jun2009['Volume'].mean()
print("Jun 2009 Mean Volume:", Jun2009_mean)
Jun2009.plot(x='Date', y='Volume', title='AMD Volume in June 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2009=df.loc[(df['Date'] >= '2009-07-01') & (df['Date'] < '2009-07-31')]
print(Jul2009)
Jul2009_mean=Jul2009['Volume'].mean()
print("Jul 2009 Mean Volume:", Jul2009_mean)
Jul2009.plot(x='Date', y='Volume', title='AMD Volume in July 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2009=df.loc[(df['Date'] >= '2009-08-01') & (df['Date'] < '2009-08-31')]
print(Aug2009)
Aug2009_mean=Aug2009['Volume'].mean()
print("Aug 2009 Mean Volume:", Aug2009_mean)
Aug2009.plot(x='Date', y='Volume', title='AMD Volume in August 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2009=df.loc[(df['Date'] >= '2009-09-01') & (df['Date'] < '2009-09-30')]
print(Sep2009)
Sep2009_mean=Sep2009['Volume'].mean()
print("Sep 2009 Mean Volume:", Sep2009_mean)
Sep2009.plot(x='Date', y='Volume', title='AMD Volume in September 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2009=df.loc[(df['Date'] >= '2009-10-01') & (df['Date'] < '2009-10-31')]
print(Oct2009)
Oct2009_mean=Oct2009['Volume'].mean()
print("Oct 2009 Mean Volume:", Oct2009_mean)
Oct2009.plot(x='Date', y='Volume', title='AMD Volume in October 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2009=df.loc[(df['Date'] >= '2009-11-01') & (df['Date'] < '2009-11-30')]
print(Nov2009)
Nov2009_mean=Nov2009['Volume'].mean()
print("Nov 2009 Mean Volume:", Nov2009_mean)
Nov2009.plot(x='Date', y='Volume', title='AMD Volume in November 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2009=df.loc[(df['Date'] >= '2009-12-01') & (df['Date'] < '2009-12-31')]
print(Dec2009)
Dec2009_mean=Dec2009['Volume'].mean()
print("Dec 2009 Mean Volume:", Dec2009_mean)
Dec2009.plot(x='Date', y='Volume', title='AMD Volume in December 2009')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2010=df.loc[(df['Date'] >= '2010-01-01') & (df['Date'] < '2010-01-31')]
print(Jan2010)
Jan2010_mean=Jan2010['Volume'].mean()
print("Jan 2010 Mean Volume:", Jan2010_mean)
Jan2010.plot(x='Date', y='Volume', title='AMD Volume in January 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2010=df.loc[(df['Date'] >= '2010-02-01') & (df['Date'] < '2010-02-28')]
print(Feb2010)
Feb2010_mean=Feb2010['Volume'].mean()
print("Feb 2010 Mean Volume:", Feb2010_mean)
Feb2010.plot(x='Date', y='Volume', title='AMD Volume in February 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2010=df.loc[(df['Date'] >= '2010-03-01') & (df['Date'] < '2010-03-31')]
print(Mar2010)
Mar2010_mean=Mar2010['Volume'].mean()
print("Mar 2010 Mean Volume:", Mar2010_mean)
Mar2010.plot(x='Date', y='Volume', title='AMD Volume in March 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2010=df.loc[(df['Date'] >= '2010-04-01') & (df['Date'] < '2010-04-30')]
print(Apr2010)
Apr2010_mean=Apr2010['Volume'].mean()
print("Apr 2010 Mean Volume:", Apr2010_mean)
Apr2010.plot(x='Date', y='Volume', title='AMD Volume in April 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2010=df.loc[(df['Date'] >= '2010-05-01') & (df['Date'] < '2010-05-31')]
print(May2010)
May2010_mean=May2010['Volume'].mean()
print("May 2010 Mean Volume:", May2010_mean)
May2010.plot(x='Date', y='Volume', title='AMD Volume in May 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2010=df.loc[(df['Date'] >= '2010-06-01') & (df['Date'] < '2010-06-30')]
print(Jun2010)
Jun2010_mean=Jun2010['Volume'].mean()
print("Jun 2010 Mean Volume:", Jun2010_mean)
Jun2010.plot(x='Date', y='Volume', title='AMD Volume in June 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2010=df.loc[(df['Date'] >= '2010-07-01') & (df['Date'] < '2010-07-31')]
print(Jul2010)
Jul2010_mean=Jul2010['Volume'].mean()
print("Jul 2010 Mean Volume:", Jul2010_mean)
Jul2010.plot(x='Date', y='Volume', title='AMD Volume in July 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2010=df.loc[(df['Date'] >= '2010-08-01') & (df['Date'] < '2010-08-31')]
print(Aug2010)
Aug2010_mean=Aug2010['Volume'].mean()
print("Aug 2010 Mean Volume:", Aug2010_mean)
Aug2010.plot(x='Date', y='Volume', title='AMD Volume in August 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2010=df.loc[(df['Date'] >= '2010-09-01') & (df['Date'] < '2010-09-30')]
print(Sep2010)
Sep2010_mean=Sep2010['Volume'].mean()
print("Sep 2010 Mean Volume:", Sep2010_mean)
Sep2010.plot(x='Date', y='Volume', title='AMD Volume in September 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2010=df.loc[(df['Date'] >= '2010-10-01') & (df['Date'] < '2010-10-31')]
print(Oct2010)
Oct2010_mean=Oct2010['Volume'].mean()
print("Oct 2010 Mean Volume:", Oct2010_mean)
Oct2010.plot(x='Date', y='Volume', title='AMD Volume in October 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2010=df.loc[(df['Date'] >= '2010-11-01') & (df['Date'] < '2010-11-30')]
print(Nov2010)
Nov2010_mean=Nov2010['Volume'].mean()
print("Nov 2010 Mean Volume:", Nov2010_mean)
Nov2010.plot(x='Date', y='Volume', title='AMD Volume in November 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2010=df.loc[(df['Date'] >= '2010-12-01') & (df['Date'] < '2010-12-31')]
print(Dec2010)
Dec2010_mean=Dec2010['Volume'].mean()
print("Dec 2010 Mean Volume:", Dec2010_mean)
Dec2010.plot(x='Date', y='Volume', title='AMD Volume in December 2010')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2011=df.loc[(df['Date'] >= '2011-01-01') & (df['Date'] < '2011-01-31')]
print(Jan2011)
Jan2011_mean=Jan2011['Volume'].mean()
print("Jan 2011 Mean Volume:", Jan2011_mean)
Jan2011.plot(x='Date', y='Volume', title='AMD Volume in January 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2011=df.loc[(df['Date'] >= '2011-02-01') & (df['Date'] < '2011-02-28')]
print(Feb2011)
Feb2011_mean=Feb2011['Volume'].mean()
print("Feb 2011 Mean Volume:", Feb2011_mean)
Feb2011.plot(x='Date', y='Volume', title='AMD Volume in February 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2011=df.loc[(df['Date'] >= '2011-03-01') & (df['Date'] < '2011-03-31')]
print(Mar2011)
Mar2011_mean=Mar2011['Volume'].mean()
print("Mar 2011 Mean Volume:", Mar2011_mean)
Mar2011.plot(x='Date', y='Volume', title='AMD Volume in March 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2011=df.loc[(df['Date'] >= '2011-04-01') & (df['Date'] < '2011-04-30')]
print(Apr2011)
Apr2011_mean=Apr2011['Volume'].mean()
print("Apr 2011 Mean Volume:", Apr2011_mean)
Apr2011.plot(x='Date', y='Volume', title='AMD Volume in April 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2011=df.loc[(df['Date'] >= '2011-05-01') & (df['Date'] < '2011-05-31')]
print(May2011)
May2011_mean=May2011['Volume'].mean()
print("May 2011 Mean Volume:", May2011_mean)
May2011.plot(x='Date', y='Volume', title='AMD Volume in May 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2011=df.loc[(df['Date'] >= '2011-06-01') & (df['Date'] < '2011-06-30')]
print(Jun2011)
Jun2011_mean=Jun2011['Volume'].mean()
print("Jun 2011 Mean Volume:", Jun2011_mean)
Jun2011.plot(x='Date', y='Volume', title='AMD Volume in June 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2011=df.loc[(df['Date'] >= '2011-07-01') & (df['Date'] < '2011-07-31')]
print(Jul2011)
Jul2011_mean=Jul2011['Volume'].mean()
print("Jul 2011 Mean Volume:", Jul2011_mean)
Jul2011.plot(x='Date', y='Volume', title='AMD Volume in July 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2011=df.loc[(df['Date'] >= '2011-08-01') & (df['Date'] < '2011-08-31')]
print(Aug2011)
Aug2011_mean=Aug2011['Volume'].mean()
print("Aug 2011 Mean Volume:", Aug2011_mean)
Aug2011.plot(x='Date', y='Volume', title='AMD Volume in August 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2011=df.loc[(df['Date'] >= '2011-09-01') & (df['Date'] < '2011-09-30')]
print(Sep2011)
Sep2011_mean=Sep2011['Volume'].mean()
print("Sep 2011 Mean Volume:", Sep2011_mean)
Sep2011.plot(x='Date', y='Volume', title='AMD Volume in September 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2011=df.loc[(df['Date'] >= '2011-10-01') & (df['Date'] < '2011-10-31')]
print(Oct2011)
Oct2011_mean=Oct2011['Volume'].mean()
print("Oct 2011 Mean Volume:", Oct2011_mean)
Oct2011.plot(x='Date', y='Volume', title='AMD Volume in October 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2011=df.loc[(df['Date'] >= '2011-11-01') & (df['Date'] < '2011-11-30')]
print(Nov2011)
Nov2011_mean=Nov2011['Volume'].mean()
print("Nov 2011 Mean Volume:", Nov2011_mean)
Nov2011.plot(x='Date', y='Volume', title='AMD Volume in November 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2011=df.loc[(df['Date'] >= '2011-12-01') & (df['Date'] < '2011-12-31')]
print(Dec2011)
Dec2011_mean=Dec2011['Volume'].mean()
print("Dec 2011 Mean Volume:", Dec2011_mean)
Dec2011.plot(x='Date', y='Volume', title='AMD Volume in December 2011')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2012=df.loc[(df['Date'] >= '2012-01-01') & (df['Date'] < '2012-01-31')]
print(Jan2012)
Jan2012_mean=Jan2012['Volume'].mean()
print("Jan 2012 Mean Volume:", Jan2012_mean)
Jan2012.plot(x='Date', y='Volume', title='AMD Volume in January 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2012=df.loc[(df['Date'] >= '2012-02-01') & (df['Date'] < '2012-02-29')]
print(Feb2012)
Feb2012_mean=Feb2012['Volume'].mean()
print("Feb 2012 Mean Volume:", Feb2012_mean)
Feb2012.plot(x='Date', y='Volume', title='AMD Volume in February 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2012=df.loc[(df['Date'] >= '2012-03-01') & (df['Date'] < '2012-03-31')]
print(Mar2012)
Mar2012_mean=Mar2012['Volume'].mean()
print("Mar 2012 Mean Volume:", Mar2012_mean)
Mar2012.plot(x='Date', y='Volume', title='AMD Volume in March 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2012=df.loc[(df['Date'] >= '2012-04-01') & (df['Date'] < '2012-04-30')]
print(Apr2012)
Apr2012_mean=Apr2012['Volume'].mean()
print("Apr 2012 Mean Volume:", Apr2012_mean)
Apr2012.plot(x='Date', y='Volume', title='AMD Volume in April 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2012=df.loc[(df['Date'] >= '2012-05-01') & (df['Date'] < '2012-05-31')]
print(May2012)
May2012_mean=May2012['Volume'].mean()
print("May 2012 Mean Volume:", May2012_mean)
May2012.plot(x='Date', y='Volume', title='AMD Volume in May 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2012=df.loc[(df['Date'] >= '2012-06-01') & (df['Date'] < '2012-06-30')]
print(Jun2012)
Jun2012_mean=Jun2012['Volume'].mean()
print("Jun 2012 Mean Volume:", Jun2012_mean)
Jun2012.plot(x='Date', y='Volume', title='AMD Volume in June 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2012=df.loc[(df['Date'] >= '2012-07-01') & (df['Date'] < '2012-07-31')]
print(Jul2012)
Jul2012_mean=Jul2012['Volume'].mean()
print("Jul 2012 Mean Volume:", Jul2012_mean)
Jul2012.plot(x='Date', y='Volume', title='AMD Volume in July 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2012=df.loc[(df['Date'] >= '2012-08-01') & (df['Date'] < '2012-08-31')]
print(Aug2012)
Aug2012_mean=Aug2012['Volume'].mean()
print("Aug 2012 Mean Volume:", Aug2012_mean)
Aug2012.plot(x='Date', y='Volume', title='AMD Volume in August 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2012=df.loc[(df['Date'] >= '2012-09-01') & (df['Date'] < '2012-09-30')]
print(Sep2012)
Sep2012_mean=Sep2012['Volume'].mean()
print("Sep 2012 Mean Volume:", Sep2012_mean)
Sep2012.plot(x='Date', y='Volume', title='AMD Volume in September 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2012=df.loc[(df['Date'] >= '2012-10-01') & (df['Date'] < '2012-10-31')]
print(Oct2012)
Oct2012_mean=Oct2012['Volume'].mean()
print("Oct 2012 Mean Volume:", Oct2012_mean)
Oct2012.plot(x='Date', y='Volume', title='AMD Volume in October 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2012=df.loc[(df['Date'] >= '2012-11-01') & (df['Date'] < '2012-11-30')]
print(Nov2012)
Nov2012_mean=Nov2012['Volume'].mean()
print("Nov 2012 Mean Volume:", Nov2012_mean)
Nov2012.plot(x='Date', y='Volume', title='AMD Volume in November 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2012=df.loc[(df['Date'] >= '2012-12-01') & (df['Date'] < '2012-12-31')]
print(Dec2012)
Dec2012_mean=Dec2012['Volume'].mean()
print("Dec 2012 Mean Volume:", Dec2012_mean)
Dec2012.plot(x='Date', y='Volume', title='AMD Volume in December 2012')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2013=df.loc[(df['Date'] >= '2013-01-01') & (df['Date'] < '2013-01-31')]
print(Jan2013)
Jan2013_mean=Jan2013['Volume'].mean()
print("Jan 2013 Mean Volume:", Jan2013_mean)
Jan2013.plot(x='Date', y='Volume', title='AMD Volume in January 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2013=df.loc[(df['Date'] >= '2013-02-01') & (df['Date'] < '2013-02-28')]
print(Feb2013)
Feb2013_mean=Feb2013['Volume'].mean()
print("Feb 2013 Mean Volume:", Feb2013_mean)
Feb2013.plot(x='Date', y='Volume', title='AMD Volume in February 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2013=df.loc[(df['Date'] >= '2013-03-01') & (df['Date'] < '2013-03-31')]
print(Mar2013)
Mar2013_mean=Mar2013['Volume'].mean()
print("Mar 2013 Mean Volume:", Mar2013_mean)
Mar2013.plot(x='Date', y='Volume', title='AMD Volume in March 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2013=df.loc[(df['Date'] >= '2013-04-01') & (df['Date'] < '2013-04-30')]
print(Apr2013)
Apr2013_mean=Apr2013['Volume'].mean()
print("Apr 2013 Mean Volume:", Apr2013_mean)
Apr2013.plot(x='Date', y='Volume', title='AMD Volume in April 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2013=df.loc[(df['Date'] >= '2013-05-01') & (df['Date'] < '2013-05-31')]
print(May2013)
May2013_mean=May2013['Volume'].mean()
print("May 2013 Mean Volume:", May2013_mean)
May2013.plot(x='Date', y='Volume', title='AMD Volume in May 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2013=df.loc[(df['Date'] >= '2013-06-01') & (df['Date'] < '2013-06-30')]
print(Jun2013)
Jun2013_mean=Jun2013['Volume'].mean()
print("Jun 2013 Mean Volume:", Jun2013_mean)
Jun2013.plot(x='Date', y='Volume', title='AMD Volume in June 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2013=df.loc[(df['Date'] >= '2013-07-01') & (df['Date'] < '2013-07-31')]
print(Jul2013)
Jul2013_mean=Jul2013['Volume'].mean()
print("Jul 2013 Mean Volume:", Jul2013_mean)
Jul2013.plot(x='Date', y='Volume', title='AMD Volume in July 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2013=df.loc[(df['Date'] >= '2013-08-01') & (df['Date'] < '2013-08-31')]
print(Aug2013)
Aug2013_mean=Aug2013['Volume'].mean()
print("Aug 2013 Mean Volume:", Aug2013_mean)
Aug2013.plot(x='Date', y='Volume', title='AMD Volume in August 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2013=df.loc[(df['Date'] >= '2013-09-01') & (df['Date'] < '2013-09-30')]
print(Sep2013)
Sep2013_mean=Sep2013['Volume'].mean()
print("Sep 2013 Mean Volume:", Sep2013_mean)
Sep2013.plot(x='Date', y='Volume', title='AMD Volume in September 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2013=df.loc[(df['Date'] >= '2013-10-01') & (df['Date'] < '2013-10-31')]
print(Oct2013)
Oct2013_mean=Oct2013['Volume'].mean()
print("Oct 2013 Mean Volume:", Oct2013_mean)
Oct2013.plot(x='Date', y='Volume', title='AMD Volume in October 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2013=df.loc[(df['Date'] >= '2013-11-01') & (df['Date'] < '2013-11-30')]
print(Nov2013)
Nov2013_mean=Nov2013['Volume'].mean()
print("Nov 2013 Mean Volume:", Nov2013_mean)
Nov2013.plot(x='Date', y='Volume', title='AMD Volume in November 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2013=df.loc[(df['Date'] >= '2013-12-01') & (df['Date'] < '2013-12-31')]
print(Dec2013)
Dec2013_mean=Dec2013['Volume'].mean()
print("Dec 2013 Mean Volume:", Dec2013_mean)
Dec2013.plot(x='Date', y='Volume', title='AMD Volume in December 2013')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2014=df.loc[(df['Date'] >= '2014-01-01') & (df['Date'] < '2014-01-31')]
print(Jan2014)
Jan2014_mean=Jan2014['Volume'].mean()
print("Jan 2014 Mean Volume:", Jan2014_mean)
Jan2014.plot(x='Date', y='Volume', title='AMD Volume in January 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2014=df.loc[(df['Date'] >= '2014-02-01') & (df['Date'] < '2014-02-28')]
print(Feb2014)
Feb2014_mean=Feb2014['Volume'].mean()
print("Feb 2014 Mean Volume:", Feb2014_mean)
Feb2014.plot(x='Date', y='Volume', title='AMD Volume in February 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2014=df.loc[(df['Date'] >= '2014-03-01') & (df['Date'] < '2014-03-31')]
print(Mar2014)
Mar2014_mean=Mar2014['Volume'].mean()
print("Mar 2014 Mean Volume:", Mar2014_mean)
Mar2014.plot(x='Date', y='Volume', title='AMD Volume in March 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2014=df.loc[(df['Date'] >= '2014-04-01') & (df['Date'] < '2014-04-30')]
print(Apr2014)
Apr2014_mean=Apr2014['Volume'].mean()
print("Apr 2014 Mean Volume:", Apr2014_mean)
Apr2014.plot(x='Date', y='Volume', title='AMD Volume in April 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2014=df.loc[(df['Date'] >= '2014-05-01') & (df['Date'] < '2014-05-31')]
print(May2014)
May2014_mean=May2014['Volume'].mean()
print("May 2014 Mean Volume:", May2014_mean)
May2014.plot(x='Date', y='Volume', title='AMD Volume in May 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2014=df.loc[(df['Date'] >= '2014-06-01') & (df['Date'] < '2014-06-30')]
print(Jun2014)
Jun2014_mean=Jun2014['Volume'].mean()
print("Jun 2014 Mean Volume:", Jun2014_mean)
Jun2014.plot(x='Date', y='Volume', title='AMD Volume in June 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2014=df.loc[(df['Date'] >= '2014-07-01') & (df['Date'] < '2014-07-31')]
print(Jul2014)
Jul2014_mean=Jul2014['Volume'].mean()
print("Jul 2014 Mean Volume:", Jul2014_mean)
Jul2014.plot(x='Date', y='Volume', title='AMD Volume in July 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2014=df.loc[(df['Date'] >= '2014-08-01') & (df['Date'] < '2014-08-31')]
print(Aug2014)
Aug2014_mean=Aug2014['Volume'].mean()
print("Aug 2014 Mean Volume:", Aug2014_mean)
Aug2014.plot(x='Date', y='Volume', title='AMD Volume in August 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2014=df.loc[(df['Date'] >= '2014-09-01') & (df['Date'] < '2014-09-30')]
print(Sep2014)
Sep2014_mean=Sep2014['Volume'].mean()
print("Sep 2014 Mean Volume:", Sep2014_mean)
Sep2014.plot(x='Date', y='Volume', title='AMD Volume in September 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2014=df.loc[(df['Date'] >= '2014-10-01') & (df['Date'] < '2014-10-31')]
print(Oct2014)
Oct2014_mean=Oct2014['Volume'].mean()
print("Oct 2014 Mean Volume:", Oct2014_mean)
Oct2014.plot(x='Date', y='Volume', title='AMD Volume in October 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2014=df.loc[(df['Date'] >= '2014-11-01') & (df['Date'] < '2014-11-30')]
print(Nov2014)
Nov2014_mean=Nov2014['Volume'].mean()
print("Nov 2014 Mean Volume:", Nov2014_mean)
Nov2014.plot(x='Date', y='Volume', title='AMD Volume in November 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2014=df.loc[(df['Date'] >= '2014-12-01') & (df['Date'] < '2014-12-31')]
print(Dec2014)
Dec2014_mean=Dec2014['Volume'].mean()
print("Dec 2014 Mean Volume:", Dec2014_mean)
Dec2014.plot(x='Date', y='Volume', title='AMD Volume in December 2014')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2015=df.loc[(df['Date'] >= '2015-01-01') & (df['Date'] < '2015-01-31')]
print(Jan2015)
Jan2015_mean=Jan2015['Volume'].mean()
print("Jan 2015 Mean Volume:", Jan2015_mean)
Jan2015.plot(x='Date', y='Volume', title='AMD Volume in January 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2015=df.loc[(df['Date'] >= '2015-02-01') & (df['Date'] < '2015-02-28')]
print(Feb2015)
Feb2015_mean=Feb2015['Volume'].mean()
print("Feb 2015 Mean Volume:", Feb2015_mean)
Feb2015.plot(x='Date', y='Volume', title='AMD Volume in February 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2015=df.loc[(df['Date'] >= '2015-03-01') & (df['Date'] < '2015-03-31')]
print(Mar2015)
Mar2015_mean=Mar2015['Volume'].mean()
print("Mar 2015 Mean Volume:", Mar2015_mean)
Mar2015.plot(x='Date', y='Volume', title='AMD Volume in March 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2015=df.loc[(df['Date'] >= '2015-04-01') & (df['Date'] < '2015-04-30')]
print(Apr2015)
Apr2015_mean=Apr2015['Volume'].mean()
print("Apr 2015 Mean Volume:", Apr2015_mean)
Apr2015.plot(x='Date', y='Volume', title='AMD Volume in April 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2015=df.loc[(df['Date'] >= '2015-05-01') & (df['Date'] < '2015-05-31')]
print(May2015)
May2015_mean=May2015['Volume'].mean()
print("May 2015 Mean Volume:", May2015_mean)
May2015.plot(x='Date', y='Volume', title='AMD Volume in May 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2015=df.loc[(df['Date'] >= '2015-06-01') & (df['Date'] < '2015-06-30')]
print(Jun2015)
Jun2015_mean=Jun2015['Volume'].mean()
print("Jun 2015 Mean Volume:", Jun2015_mean)
Jun2015.plot(x='Date', y='Volume', title='AMD Volume in June 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2015=df.loc[(df['Date'] >= '2015-07-01') & (df['Date'] < '2015-07-31')]
print(Jul2015)
Jul2015_mean=Jul2015['Volume'].mean()
print("Jul 2015 Mean Volume:", Jul2015_mean)
Jul2015.plot(x='Date', y='Volume', title='AMD Volume in July 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2015=df.loc[(df['Date'] >= '2015-08-01') & (df['Date'] < '2015-08-31')]
print(Aug2015)
Aug2015_mean=Aug2015['Volume'].mean()
print("Aug 2015 Mean Volume:", Aug2015_mean)
Aug2015.plot(x='Date', y='Volume', title='AMD Volume in August 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2015=df.loc[(df['Date'] >= '2015-09-01') & (df['Date'] < '2015-09-30')]
print(Sep2015)
Sep2015_mean=Sep2015['Volume'].mean()
print("Sep 2015 Mean Volume:", Sep2015_mean)
Sep2015.plot(x='Date', y='Volume', title='AMD Volume in September 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2015=df.loc[(df['Date'] >= '2015-10-01') & (df['Date'] < '2015-10-31')]
print(Oct2015)
Oct2015_mean=Oct2015['Volume'].mean()
print("Oct 2015 Mean Volume:", Oct2015_mean)
Oct2015.plot(x='Date', y='Volume', title='AMD Volume in October 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2015=df.loc[(df['Date'] >= '2015-11-01') & (df['Date'] < '2015-11-30')]
print(Nov2015)
Nov2015_mean=Nov2015['Volume'].mean()
print("Nov 2015 Mean Volume:", Nov2015_mean)
Nov2015.plot(x='Date', y='Volume', title='AMD Volume in November 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2015=df.loc[(df['Date'] >= '2015-12-01') & (df['Date'] < '2015-12-31')]
print(Dec2015)
Dec2015_mean=Dec2015['Volume'].mean()
print("Dec 2015 Mean Volume:", Dec2015_mean)
Dec2015.plot(x='Date', y='Volume', title='AMD Volume in December 2015')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2016=df.loc[(df['Date'] >= '2016-01-01') & (df['Date'] < '2016-01-31')]
print(Jan2016)
Jan2016_mean=Jan2016['Volume'].mean()
print("Jan 2016 Mean Volume:", Jan2016_mean)
Jan2016.plot(x='Date', y='Volume', title='AMD Volume in January 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2016=df.loc[(df['Date'] >= '2016-02-01') & (df['Date'] < '2016-02-29')]
print(Feb2016)
Feb2016_mean=Feb2016['Volume'].mean()
print("Feb 2016 Mean Volume:", Feb2016_mean)
Feb2016.plot(x='Date', y='Volume', title='AMD Volume in February 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2016=df.loc[(df['Date'] >= '2016-03-01') & (df['Date'] < '2016-03-31')]
print(Mar2016)
Mar2016_mean=Mar2016['Volume'].mean()
print("Mar 2016 Mean Volume:", Mar2016_mean)
Mar2016.plot(x='Date', y='Volume', title='AMD Volume in March 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2016=df.loc[(df['Date'] >= '2016-04-01') & (df['Date'] < '2016-04-30')]
print(Apr2016)
Apr2016_mean=Apr2016['Volume'].mean()
print("Apr 2016 Mean Volume:", Apr2016_mean)
Apr2016.plot(x='Date', y='Volume', title='AMD Volume in April 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2016=df.loc[(df['Date'] >= '2016-05-01') & (df['Date'] < '2016-05-31')]
print(May2016)
May2016_mean=May2016['Volume'].mean()
print("May 2016 Mean Volume:", May2016_mean)
May2016.plot(x='Date', y='Volume', title='AMD Volume in May 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2016=df.loc[(df['Date'] >= '2016-06-01') & (df['Date'] < '2016-06-30')]
print(Jun2016)
Jun2016_mean=Jun2016['Volume'].mean()
print("Jun 2016 Mean Volume:", Jun2016_mean)
Jun2016.plot(x='Date', y='Volume', title='AMD Volume in June 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2016=df.loc[(df['Date'] >= '2016-07-01') & (df['Date'] < '2016-07-31')]
print(Jul2016)
Jul2016_mean=Jul2016['Volume'].mean()
print("Jul 2016 Mean Volume:", Jul2016_mean)
Jul2016.plot(x='Date', y='Volume', title='AMD Volume in July 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2016=df.loc[(df['Date'] >= '2016-08-01') & (df['Date'] < '2016-08-31')]
print(Aug2016)
Aug2016_mean=Aug2016['Volume'].mean()
print("Aug 2016 Mean Volume:", Aug2016_mean)
Aug2016.plot(x='Date', y='Volume', title='AMD Volume in August 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2016=df.loc[(df['Date'] >= '2016-09-01') & (df['Date'] < '2016-09-30')]
print(Sep2016)
Sep2016_mean=Sep2016['Volume'].mean()
print("Sep 2016 Mean Volume:", Sep2016_mean)
Sep2016.plot(x='Date', y='Volume', title='AMD Volume in September 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2016=df.loc[(df['Date'] >= '2016-10-01') & (df['Date'] < '2016-10-31')]
print(Oct2016)
Oct2016_mean=Oct2016['Volume'].mean()
print("Oct 2016 Mean Volume:", Oct2016_mean)
Oct2016.plot(x='Date', y='Volume', title='AMD Volume in October 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2016=df.loc[(df['Date'] >= '2016-11-01') & (df['Date'] < '2016-11-30')]
print(Nov2016)
Nov2016_mean=Nov2016['Volume'].mean()
print("Nov 2016 Mean Volume:", Nov2016_mean)
Nov2016.plot(x='Date', y='Volume', title='AMD Volume in November 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2016=df.loc[(df['Date'] >= '2016-12-01') & (df['Date'] < '2016-12-31')]
print(Dec2016)
Dec2016_mean=Dec2016['Volume'].mean()
print("Dec 2016 Mean Volume:", Dec2016_mean)
Dec2016.plot(x='Date', y='Volume', title='AMD Volume in December 2016')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2017=df.loc[(df['Date'] >= '2017-01-01') & (df['Date'] < '2017-01-31')]
print(Jan2017)
Jan2017_mean=Jan2017['Volume'].mean()
print("Jan 2017 Mean Volume:", Jan2017_mean)
Jan2017.plot(x='Date', y='Volume', title='AMD Volume in January 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2017=df.loc[(df['Date'] >= '2017-02-01') & (df['Date'] < '2017-02-28')]
print(Feb2017)
Feb2017_mean=Feb2017['Volume'].mean()
print("Feb 2017 Mean Volume:", Feb2017_mean)
Feb2017.plot(x='Date', y='Volume', title='AMD Volume in February 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2017=df.loc[(df['Date'] >= '2017-03-01') & (df['Date'] < '2017-03-31')]
print(Mar2017)
Mar2017_mean=Mar2017['Volume'].mean()
print("Mar 2017 Mean Volume:", Mar2017_mean)
Mar2017.plot(x='Date', y='Volume', title='AMD Volume in March 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2017=df.loc[(df['Date'] >= '2017-04-01') & (df['Date'] < '2017-04-30')]
print(Apr2017)
Apr2017_mean=Apr2017['Volume'].mean()
print("Apr 2017 Mean Volume:", Apr2017_mean)
Apr2017.plot(x='Date', y='Volume', title='AMD Volume in April 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2017=df.loc[(df['Date'] >= '2017-05-01') & (df['Date'] < '2017-05-31')]
print(May2017)
May2017_mean=May2017['Volume'].mean()
print("May 2017 Mean Volume:", May2017_mean)
May2017.plot(x='Date', y='Volume', title='AMD Volume in May 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2017=df.loc[(df['Date'] >= '2017-06-01') & (df['Date'] < '2017-06-30')]
print(Jun2017)
Jun2017_mean=Jun2017['Volume'].mean()
print("Jun 2017 Mean Volume:", Jun2017_mean)
Jun2017.plot(x='Date', y='Volume', title='AMD Volume in June 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2017=df.loc[(df['Date'] >= '2017-07-01') & (df['Date'] < '2017-07-31')]
print(Jul2017)
Jul2017_mean=Jul2017['Volume'].mean()
print("Jul 2017 Mean Volume:", Jul2017_mean)
Jul2017.plot(x='Date', y='Volume', title='AMD Volume in July 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2017=df.loc[(df['Date'] >= '2017-08-01') & (df['Date'] < '2017-08-31')]
print(Aug2017)
Aug2017_mean=Aug2017['Volume'].mean()
print("Aug 2017 Mean Volume:", Aug2017_mean)
Aug2017.plot(x='Date', y='Volume', title='AMD Volume in August 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2017=df.loc[(df['Date'] >= '2017-09-01') & (df['Date'] < '2017-09-30')]
print(Sep2017)
Sep2017_mean=Sep2017['Volume'].mean()
print("Sep 2017 Mean Volume:", Sep2017_mean)
Sep2017.plot(x='Date', y='Volume', title='AMD Volume in September 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2017=df.loc[(df['Date'] >= '2017-10-01') & (df['Date'] < '2017-10-31')]
print(Oct2017)
Oct2017_mean=Oct2017['Volume'].mean()
print("Oct 2017 Mean Volume:", Oct2017_mean)
Oct2017.plot(x='Date', y='Volume', title='AMD Volume in October 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2017=df.loc[(df['Date'] >= '2017-11-01') & (df['Date'] < '2017-11-30')]
print(Nov2017)
Nov2017_mean=Nov2017['Volume'].mean()
print("Nov 2017 Mean Volume:", Nov2017_mean)
Nov2017.plot(x='Date', y='Volume', title='AMD Volume in November 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2017=df.loc[(df['Date'] >= '2017-12-01') & (df['Date'] < '2017-12-31')]
print(Dec2017)
Dec2017_mean=Dec2017['Volume'].mean()
print("Dec 2017 Mean Volume:", Dec2017_mean)
Dec2017.plot(x='Date', y='Volume', title='AMD Volume in December 2017')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2018=df.loc[(df['Date'] >= '2018-01-01') & (df['Date'] < '2018-01-31')]
print(Jan2018)
Jan2018_mean=Jan2018['Volume'].mean()
print("Jan 2018 Mean Volume:", Jan2018_mean)
Jan2018.plot(x='Date', y='Volume', title='AMD Volume in January 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2018=df.loc[(df['Date'] >= '2018-02-01') & (df['Date'] < '2018-02-28')]
print(Feb2018)
Feb2018_mean=Feb2018['Volume'].mean()
print("Feb 2018 Mean Volume:", Feb2018_mean)
Feb2018.plot(x='Date', y='Volume', title='AMD Volume in February 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2018=df.loc[(df['Date'] >= '2018-03-01') & (df['Date'] < '2018-03-31')]
print(Mar2018)
Mar2018_mean=Mar2018['Volume'].mean()
print("Mar 2018 Mean Volume:", Mar2018_mean)
Mar2018.plot(x='Date', y='Volume', title='AMD Volume in March 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2018=df.loc[(df['Date'] >= '2018-04-01') & (df['Date'] < '2018-04-30')]
print(Apr2018)
Apr2018_mean=Apr2018['Volume'].mean()
print("Apr 2018 Mean Volume:", Apr2018_mean)
Apr2018.plot(x='Date', y='Volume', title='AMD Volume in April 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2018=df.loc[(df['Date'] >= '2018-05-01') & (df['Date'] < '2018-05-31')]
print(May2018)
May2018_mean=May2018['Volume'].mean()
print("May 2018 Mean Volume:", May2018_mean)
May2018.plot(x='Date', y='Volume', title='AMD Volume in May 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2018=df.loc[(df['Date'] >= '2018-06-01') & (df['Date'] < '2018-06-30')]
print(Jun2018)
Jun2018_mean=Jun2018['Volume'].mean()
print("Jun 2018 Mean Volume:", Jun2018_mean)
Jun2018.plot(x='Date', y='Volume', title='AMD Volume in June 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2018=df.loc[(df['Date'] >= '2018-07-01') & (df['Date'] < '2018-07-31')]
print(Jul2018)
Jul2018_mean=Jul2018['Volume'].mean()
print("Jul 2018 Mean Volume:", Jul2018_mean)
Jul2018.plot(x='Date', y='Volume', title='AMD Volume in July 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2018=df.loc[(df['Date'] >= '2018-08-01') & (df['Date'] < '2018-08-31')]
print(Aug2018)
Aug2018_mean=Aug2018['Volume'].mean()
print("Aug 2018 Mean Volume:", Aug2018_mean)
Aug2018.plot(x='Date', y='Volume', title='AMD Volume in August 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2018=df.loc[(df['Date'] >= '2018-09-01') & (df['Date'] < '2018-09-30')]
print(Sep2018)
Sep2018_mean=Sep2018['Volume'].mean()
print("Sep 2018 Mean Volume:", Sep2018_mean)
Sep2018.plot(x='Date', y='Volume', title='AMD Volume in September 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2018=df.loc[(df['Date'] >= '2018-10-01') & (df['Date'] < '2018-10-31')]
print(Oct2018)
Oct2018_mean=Oct2018['Volume'].mean()
print("Oct 2018 Mean Volume:", Oct2018_mean)
Oct2018.plot(x='Date', y='Volume', title='AMD Volume in October 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2018=df.loc[(df['Date'] >= '2018-11-01') & (df['Date'] < '2018-11-30')]
print(Nov2018)
Nov2018_mean=Nov2018['Volume'].mean()
print("Nov 2018 Mean Volume:", Nov2018_mean)
Nov2018.plot(x='Date', y='Volume', title='AMD Volume in November 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2018=df.loc[(df['Date'] >= '2018-12-01') & (df['Date'] < '2018-12-31')]
print(Dec2018)
Dec2018_mean=Dec2018['Volume'].mean()
print("Dec 2018 Mean Volume:", Dec2018_mean)
Dec2018.plot(x='Date', y='Volume', title='AMD Volume in December 2018')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2019=df.loc[(df['Date'] >= '2019-01-01') & (df['Date'] < '2019-01-31')]
print(Jan2019)
Jan2019_mean=Jan2019['Volume'].mean()
print("Jan 2019 Mean Volume:", Jan2019_mean)
Jan2019.plot(x='Date', y='Volume', title='AMD Volume in January 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2019=df.loc[(df['Date'] >= '2019-02-01') & (df['Date'] < '2019-02-28')]
print(Feb2019)
Feb2019_mean=Feb2019['Volume'].mean()
print("Feb 2019 Mean Volume:", Feb2019_mean)
Feb2019.plot(x='Date', y='Volume', title='AMD Volume in February 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2019=df.loc[(df['Date'] >= '2019-03-01') & (df['Date'] < '2019-03-31')]
print(Mar2019)
Mar2019_mean=Mar2019['Volume'].mean()
print("Mar 2019 Mean Volume:", Mar2019_mean)
Mar2019.plot(x='Date', y='Volume', title='AMD Volume in March 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2019=df.loc[(df['Date'] >= '2019-04-01') & (df['Date'] < '2019-04-30')]
print(Apr2019)
Apr2019_mean=Apr2019['Volume'].mean()
print("Apr 2019 Mean Volume:", Apr2019_mean)
Apr2019.plot(x='Date', y='Volume', title='AMD Volume in April 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2019=df.loc[(df['Date'] >= '2019-05-01') & (df['Date'] < '2019-05-31')]
print(May2019)
May2019_mean=May2019['Volume'].mean()
print("May 2019 Mean Volume:", May2019_mean)
May2019.plot(x='Date', y='Volume', title='AMD Volume in May 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2019=df.loc[(df['Date'] >= '2019-06-01') & (df['Date'] < '2019-06-30')]
print(Jun2019)
Jun2019_mean=Jun2019['Volume'].mean()
print("Jun 2019 Mean Volume:", Jun2019_mean)
Jun2019.plot(x='Date', y='Volume', title='AMD Volume in June 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2019=df.loc[(df['Date'] >= '2019-07-01') & (df['Date'] < '2019-07-31')]
print(Jul2019)
Jul2019_mean=Jul2019['Volume'].mean()
print("Jul 2019 Mean Volume:", Jul2019_mean)
Jul2019.plot(x='Date', y='Volume', title='AMD Volume in July 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2019=df.loc[(df['Date'] >= '2019-08-01') & (df['Date'] < '2019-08-31')]
print(Aug2019)
Aug2019_mean=Aug2019['Volume'].mean()
print("Aug 2019 Mean Volume:", Aug2019_mean)
Aug2019.plot(x='Date', y='Volume', title='AMD Volume in August 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2019=df.loc[(df['Date'] >= '2019-09-01') & (df['Date'] < '2019-09-30')]
print(Sep2019)
Sep2019_mean=Sep2019['Volume'].mean()
print("Sep 2019 Mean Volume:", Sep2019_mean)
Sep2019.plot(x='Date', y='Volume', title='AMD Volume in September 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2019=df.loc[(df['Date'] >= '2019-10-01') & (df['Date'] < '2019-10-31')]
print(Oct2019)
Oct2019_mean=Oct2019['Volume'].mean()
print("Oct 2019 Mean Volume:", Oct2019_mean)
Oct2019.plot(x='Date', y='Volume', title='AMD Volume in October 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2019=df.loc[(df['Date'] >= '2019-11-01') & (df['Date'] < '2019-11-30')]
print(Nov2019)
Nov2019_mean=Nov2019['Volume'].mean()
print("Nov 2019 Mean Volume:", Nov2019_mean)
Nov2019.plot(x='Date', y='Volume', title='AMD Volume in November 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2019=df.loc[(df['Date'] >= '2019-12-01') & (df['Date'] < '2019-12-31')]
print(Dec2019)
Dec2019_mean=Dec2019['Volume'].mean()
print("Dec 2019 Mean Volume:", Dec2019_mean)
Dec2019.plot(x='Date', y='Volume', title='AMD Volume in December 2019')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2020=df.loc[(df['Date'] >= '2020-01-01') & (df['Date'] < '2020-01-31')]
print(Jan2020)
Jan2020_mean=Jan2020['Volume'].mean()
print("Jan 2020 Mean Volume:", Jan2020_mean)
Jan2020.plot(x='Date', y='Volume', title='AMD Volume in January 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2020=df.loc[(df['Date'] >= '2020-02-01') & (df['Date'] < '2020-02-29')]
print(Feb2020)
Feb2020_mean=Feb2020['Volume'].mean()
print("Feb 2020 Mean Volume:", Feb2020_mean)
Feb2020.plot(x='Date', y='Volume', title='AMD Volume in February 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2020=df.loc[(df['Date'] >= '2020-03-01') & (df['Date'] < '2020-03-31')]
print(Mar2020)
Mar2020_mean=Mar2020['Volume'].mean()
print("Mar 2020 Mean Volume:", Mar2020_mean)
Mar2020.plot(x='Date', y='Volume', title='AMD Volume in March 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2020=df.loc[(df['Date'] >= '2020-04-01') & (df['Date'] < '2020-04-30')]
print(Apr2020)
Apr2020_mean=Apr2020['Volume'].mean()
print("Apr 2020 Mean Volume:", Apr2020_mean)
Apr2020.plot(x='Date', y='Volume', title='AMD Volume in April 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2020=df.loc[(df['Date'] >= '2020-05-01') & (df['Date'] < '2020-05-31')]
print(May2020)
May2020_mean=May2020['Volume'].mean()
print("May 2020 Mean Volume:", May2020_mean)
May2020.plot(x='Date', y='Volume', title='AMD Volume in May 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2020=df.loc[(df['Date'] >= '2020-06-01') & (df['Date'] < '2020-06-30')]
print(Jun2020)
Jun2020_mean=Jun2020['Volume'].mean()
print("Jun 2020 Mean Volume:", Jun2020_mean)
Jun2020.plot(x='Date', y='Volume', title='AMD Volume in June 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2020=df.loc[(df['Date'] >= '2020-07-01') & (df['Date'] < '2020-07-31')]
print(Jul2020)
Jul2020_mean=Jul2020['Volume'].mean()
print("Jul 2020 Mean Volume:", Jul2020_mean)
Jul2020.plot(x='Date', y='Volume', title='AMD Volume in July 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2020=df.loc[(df['Date'] >= '2020-08-01') & (df['Date'] < '2020-08-31')]
print(Aug2020)
Aug2020_mean=Aug2020['Volume'].mean()
print("Aug 2020 Mean Volume:", Aug2020_mean)
Aug2020.plot(x='Date', y='Volume', title='AMD Volume in August 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2020=df.loc[(df['Date'] >= '2020-09-01') & (df['Date'] < '2020-09-30')]
print(Sep2020)
Sep2020_mean=Sep2020['Volume'].mean()
print("Sep 2020 Mean Volume:", Sep2020_mean)
Sep2020.plot(x='Date', y='Volume', title='AMD Volume in September 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2020=df.loc[(df['Date'] >= '2020-10-01') & (df['Date'] < '2020-10-31')]
print(Oct2020)
Oct2020_mean=Oct2020['Volume'].mean()
print("Oct 2020 Mean Volume:", Oct2020_mean)
Oct2020.plot(x='Date', y='Volume', title='AMD Volume in October 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2020=df.loc[(df['Date'] >= '2020-11-01') & (df['Date'] < '2020-11-30')]
print(Nov2020)
Nov2020_mean=Nov2020['Volume'].mean()
print("Nov 2020 Mean Volume:", Nov2020_mean)
Nov2020.plot(x='Date', y='Volume', title='AMD Volume in November 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2020=df.loc[(df['Date'] >= '2020-12-01') & (df['Date'] < '2020-12-31')]
print(Dec2020)
Dec2020_mean=Dec2020['Volume'].mean()
print("Dec 2020 Mean Volume:", Dec2020_mean)
Dec2020.plot(x='Date', y='Volume', title='AMD Volume in December 2020')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2021=df.loc[(df['Date'] >= '2021-01-01') & (df['Date'] < '2021-01-31')]
print(Jan2021)
Jan2021_mean=Jan2021['Volume'].mean()
print("Jan 2021 Mean Volume:", Jan2021_mean)
Jan2021.plot(x='Date', y='Volume', title='AMD Volume in January 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2021=df.loc[(df['Date'] >= '2021-02-01') & (df['Date'] < '2021-02-28')]
print(Feb2021)
Feb2021_mean=Feb2021['Volume'].mean()
print("Feb 2021 Mean Volume:", Feb2021_mean)
Feb2021.plot(x='Date', y='Volume', title='AMD Volume in February 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2021=df.loc[(df['Date'] >= '2021-03-01') & (df['Date'] < '2021-03-31')]
print(Mar2021)
Mar2021_mean=Mar2021['Volume'].mean()
print("Mar 2021 Mean Volume:", Mar2021_mean)
Mar2021.plot(x='Date', y='Volume', title='AMD Volume in March 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2021=df.loc[(df['Date'] >= '2021-04-01') & (df['Date'] < '2021-04-30')]
print(Apr2021)
Apr2021_mean=Apr2021['Volume'].mean()
print("Apr 2021 Mean Volume:", Apr2021_mean)
Apr2021.plot(x='Date', y='Volume', title='AMD Volume in April 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2021=df.loc[(df['Date'] >= '2021-05-01') & (df['Date'] < '2021-05-31')]
print(May2021)
May2021_mean=May2021['Volume'].mean()
print("May 2021 Mean Volume:", May2021_mean)
May2021.plot(x='Date', y='Volume', title='AMD Volume in May 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2021=df.loc[(df['Date'] >= '2021-06-01') & (df['Date'] < '2021-06-30')]
print(Jun2021)
Jun2021_mean=Jun2021['Volume'].mean()
print("Jun 2021 Mean Volume:", Jun2021_mean)
Jun2021.plot(x='Date', y='Volume', title='AMD Volume in June 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2021=df.loc[(df['Date'] >= '2021-07-01') & (df['Date'] < '2021-07-31')]
print(Jul2021)
Jul2021_mean=Jul2021['Volume'].mean()
print("Jul 2021 Mean Volume:", Jul2021_mean)
Jul2021.plot(x='Date', y='Volume', title='AMD Volume in July 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2021=df.loc[(df['Date'] >= '2021-08-01') & (df['Date'] < '2021-08-31')]
print(Aug2021)
Aug2021_mean=Aug2021['Volume'].mean()
print("Aug 2021 Mean Volume:", Aug2021_mean)
Aug2021.plot(x='Date', y='Volume', title='AMD Volume in August 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2021=df.loc[(df['Date'] >= '2021-09-01') & (df['Date'] < '2021-09-30')]
print(Sep2021)
Sep2021_mean=Sep2021['Volume'].mean()
print("Sep 2021 Mean Volume:", Sep2021_mean)
Sep2021.plot(x='Date', y='Volume', title='AMD Volume in September 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2021=df.loc[(df['Date'] >= '2021-10-01') & (df['Date'] < '2021-10-31')]
print(Oct2021)
Oct2021_mean=Oct2021['Volume'].mean()
print("Oct 2021 Mean Volume:", Oct2021_mean)
Oct2021.plot(x='Date', y='Volume', title='AMD Volume in October 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2021=df.loc[(df['Date'] >= '2021-11-01') & (df['Date'] < '2021-11-30')]
print(Nov2021)
Nov2021_mean=Nov2021['Volume'].mean()
print("Nov 2021 Mean Volume:", Nov2021_mean)
Nov2021.plot(x='Date', y='Volume', title='AMD Volume in November 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2021=df.loc[(df['Date'] >= '2021-12-01') & (df['Date'] < '2021-12-31')]
print(Dec2021)
Dec2021_mean=Dec2021['Volume'].mean()
print("Dec 2021 Mean Volume:", Dec2021_mean)
Dec2021.plot(x='Date', y='Volume', title='AMD Volume in December 2021')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2022=df.loc[(df['Date'] >= '2022-01-01') & (df['Date'] < '2022-01-31')]
print(Jan2022)
Jan2022_mean=Jan2022['Volume'].mean()
print("Jan 2022 Mean Volume:", Jan2022_mean)
Jan2022.plot(x='Date', y='Volume', title='AMD Volume in January 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2022=df.loc[(df['Date'] >= '2022-02-01') & (df['Date'] < '2022-02-28')]
print(Feb2022)
Feb2022_mean=Feb2022['Volume'].mean()
print("Feb 2022 Mean Volume:", Feb2022_mean)
Feb2022.plot(x='Date', y='Volume', title='AMD Volume in February 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2022=df.loc[(df['Date'] >= '2022-03-01') & (df['Date'] < '2022-03-31')]
print(Mar2022)
Mar2022_mean=Mar2022['Volume'].mean()
print("Mar 2022 Mean Volume:", Mar2022_mean)
Mar2022.plot(x='Date', y='Volume', title='AMD Volume in March 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2022=df.loc[(df['Date'] >= '2022-04-01') & (df['Date'] < '2022-04-30')]
print(Apr2022)
Apr2022_mean=Apr2022['Volume'].mean()
print("Apr 2022 Mean Volume:", Apr2022_mean)
Apr2022.plot(x='Date', y='Volume', title='AMD Volume in April 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2022=df.loc[(df['Date'] >= '2022-05-01') & (df['Date'] < '2022-05-31')]
print(May2022)
May2022_mean=May2022['Volume'].mean()
print("May 2022 Mean Volume:", May2022_mean)
May2022.plot(x='Date', y='Volume', title='AMD Volume in May 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2022=df.loc[(df['Date'] >= '2022-06-01') & (df['Date'] < '2022-06-30')]
print(Jun2022)
Jun2022_mean=Jun2022['Volume'].mean()
print("Jun 2022 Mean Volume:", Jun2022_mean)
Jun2022.plot(x='Date', y='Volume', title='AMD Volume in June 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2022=df.loc[(df['Date'] >= '2022-07-01') & (df['Date'] < '2022-07-31')]
print(Jul2022)
Jul2022_mean=Jul2022['Volume'].mean()
print("Jul 2022 Mean Volume:", Jul2022_mean)
Jul2022.plot(x='Date', y='Volume', title='AMD Volume in July 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2022=df.loc[(df['Date'] >= '2022-08-01') & (df['Date'] < '2022-08-31')]
print(Aug2022)
Aug2022_mean=Aug2022['Volume'].mean()
print("Aug 2022 Mean Volume:", Aug2022_mean)
Aug2022.plot(x='Date', y='Volume', title='AMD Volume in August 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2022=df.loc[(df['Date'] >= '2022-09-01') & (df['Date'] < '2022-09-30')]
print(Sep2022)
Sep2022_mean=Sep2022['Volume'].mean()
print("Sep 2022 Mean Volume:", Sep2022_mean)
Sep2022.plot(x='Date', y='Volume', title='AMD Volume in September 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2022=df.loc[(df['Date'] >= '2022-10-01') & (df['Date'] < '2022-10-31')]
print(Oct2022)
Oct2022_mean=Oct2022['Volume'].mean()
print("Oct 2022 Mean Volume:", Oct2022_mean)
Oct2022.plot(x='Date', y='Volume', title='AMD Volume in October 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2022=df.loc[(df['Date'] >= '2022-11-01') & (df['Date'] < '2022-11-30')]
print(Nov2022)
Nov2022_mean=Nov2022['Volume'].mean()
print("Nov 2022 Mean Volume:", Nov2022_mean)
Nov2022.plot(x='Date', y='Volume', title='AMD Volume in November 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2022=df.loc[(df['Date'] >= '2022-12-01') & (df['Date'] < '2022-12-31')]
print(Dec2022)
Dec2022_mean=Dec2022['Volume'].mean()
print("Dec 2022 Mean Volume:", Dec2022_mean)
Dec2022.plot(x='Date', y='Volume', title='AMD Volume in December 2022')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2023=df.loc[(df['Date'] >= '2023-01-01') & (df['Date'] < '2023-01-31')]
print(Jan2023)
Jan2023_mean=Jan2023['Volume'].mean()
print("Jan 2023 Mean Volume:", Jan2023_mean)
Jan2023.plot(x='Date', y='Volume', title='AMD Volume in January 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2023=df.loc[(df['Date'] >= '2023-02-01') & (df['Date'] < '2023-02-28')]
print(Feb2023)
Feb2023_mean=Feb2023['Volume'].mean()
print("Feb 2023 Mean Volume:", Feb2023_mean)
Feb2023.plot(x='Date', y='Volume', title='AMD Volume in February 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2023=df.loc[(df['Date'] >= '2023-03-01') & (df['Date'] < '2023-03-31')]
print(Mar2023)
Mar2023_mean=Mar2023['Volume'].mean()
print("Mar 2023 Mean Volume:", Mar2023_mean)
Mar2023.plot(x='Date', y='Volume', title='AMD Volume in March 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2023=df.loc[(df['Date'] >= '2023-04-01') & (df['Date'] < '2023-04-30')]
print(Apr2023)
Apr2023_mean=Apr2023['Volume'].mean()
print("Apr 2023 Mean Volume:", Apr2023_mean)
Apr2023.plot(x='Date', y='Volume', title='AMD Volume in April 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2023=df.loc[(df['Date'] >= '2023-05-01') & (df['Date'] < '2023-05-31')]
print(May2023)
May2023_mean=May2023['Volume'].mean()
print("May 2023 Mean Volume:", May2023_mean)
May2023.plot(x='Date', y='Volume', title='AMD Volume in May 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2023=df.loc[(df['Date'] >= '2023-06-01') & (df['Date'] < '2023-06-30')]
print(Jun2023)
Jun2023_mean=Jun2023['Volume'].mean()
print("Jun 2023 Mean Volume:", Jun2023_mean)
Jun2023.plot(x='Date', y='Volume', title='AMD Volume in June 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2023=df.loc[(df['Date'] >= '2023-07-01') & (df['Date'] < '2023-07-31')]
print(Jul2023)
Jul2023_mean=Jul2023['Volume'].mean()
print("Jul 2023 Mean Volume:", Jul2023_mean)
Jul2023.plot(x='Date', y='Volume', title='AMD Volume in July 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2023=df.loc[(df['Date'] >= '2023-08-01') & (df['Date'] < '2023-08-31')]
print(Aug2023)
Aug2023_mean=Aug2023['Volume'].mean()
print("Aug 2023 Mean Volume:", Aug2023_mean)
Aug2023.plot(x='Date', y='Volume', title='AMD Volume in August 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2023=df.loc[(df['Date'] >= '2023-09-01') & (df['Date'] < '2023-09-30')]
print(Sep2023)
Sep2023_mean=Sep2023['Volume'].mean()
print("Sep 2023 Mean Volume:", Sep2023_mean)
Sep2023.plot(x='Date', y='Volume', title='AMD Volume in September 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2023=df.loc[(df['Date'] >= '2023-10-01') & (df['Date'] < '2023-10-31')]
print(Oct2023)
Oct2023_mean=Oct2023['Volume'].mean()
print("Oct 2023 Mean Volume:", Oct2023_mean)
Oct2023.plot(x='Date', y='Volume', title='AMD Volume in October 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2023=df.loc[(df['Date'] >= '2023-11-01') & (df['Date'] < '2023-11-30')]
print(Nov2023)
Nov2023_mean=Nov2023['Volume'].mean()
print("Nov 2023 Mean Volume:", Nov2023_mean)
Nov2023.plot(x='Date', y='Volume', title='AMD Volume in November 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2023=df.loc[(df['Date'] >= '2023-12-01') & (df['Date'] < '2023-12-31')]
print(Dec2023)
Dec2023_mean=Dec2023['Volume'].mean()
print("Dec 2023 Mean Volume:", Dec2023_mean)
Dec2023.plot(x='Date', y='Volume', title='AMD Volume in December 2023')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2024=df.loc[(df['Date'] >= '2024-01-01') & (df['Date'] < '2024-01-31')]
print(Jan2024)
Jan2024_mean=Jan2024['Volume'].mean()
print("Jan 2024 Mean Volume:", Jan2024_mean)
Jan2024.plot(x='Date', y='Volume', title='AMD Volume in January 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2024=df.loc[(df['Date'] >= '2024-02-01') & (df['Date'] < '2024-02-29')]
print(Feb2024)
Feb2024_mean=Feb2024['Volume'].mean()
print("Feb 2024 Mean Volume:", Feb2024_mean)
Feb2024.plot(x='Date', y='Volume', title='AMD Volume in February 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2024=df.loc[(df['Date'] >= '2024-03-01') & (df['Date'] < '2024-03-31')]
print(Mar2024)
Mar2024_mean=Mar2024['Volume'].mean()
print("Mar 2024 Mean Volume:", Mar2024_mean)
Mar2024.plot(x='Date', y='Volume', title='AMD Volume in March 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2024=df.loc[(df['Date'] >= '2024-04-01') & (df['Date'] < '2024-04-30')]
print(Apr2024)
Apr2024_mean=Apr2024['Volume'].mean()
print("Apr 2024 Mean Volume:", Apr2024_mean)
Apr2024.plot(x='Date', y='Volume', title='AMD Volume in April 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2024=df.loc[(df['Date'] >= '2024-05-01') & (df['Date'] < '2024-05-31')]
print(May2024)
May2024_mean=May2024['Volume'].mean()
print("May 2024 Mean Volume:", May2024_mean)
May2024.plot(x='Date', y='Volume', title='AMD Volume in May 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2024=df.loc[(df['Date'] >= '2024-06-01') & (df['Date'] < '2024-06-30')]
print(Jun2024)
Jun2024_mean=Jun2024['Volume'].mean()
print("Jun 2024 Mean Volume:", Jun2024_mean)
Jun2024.plot(x='Date', y='Volume', title='AMD Volume in June 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2024=df.loc[(df['Date'] >= '2024-07-01') & (df['Date'] < '2024-07-31')]
print(Jul2024)
Jul2024_mean=Jul2024['Volume'].mean()
print("Jul 2024 Mean Volume:", Jul2024_mean)
Jul2024.plot(x='Date', y='Volume', title='AMD Volume in July 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2024=df.loc[(df['Date'] >= '2024-08-01') & (df['Date'] < '2024-08-31')]
print(Aug2024)
Aug2024_mean=Aug2024['Volume'].mean()
print("Aug 2024 Mean Volume:", Aug2024_mean)
Aug2024.plot(x='Date', y='Volume', title='AMD Volume in August 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2024=df.loc[(df['Date'] >= '2024-09-01') & (df['Date'] < '2024-09-30')]
print(Sep2024)
Sep2024_mean=Sep2024['Volume'].mean()
print("Sep 2024 Mean Volume:", Sep2024_mean)
Sep2024.plot(x='Date', y='Volume', title='AMD Volume in September 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Oct2024=df.loc[(df['Date'] >= '2024-10-01') & (df['Date'] < '2024-10-31')]
print(Oct2024)
Oct2024_mean=Oct2024['Volume'].mean()
print("Oct 2024 Mean Volume:", Oct2024_mean)
Oct2024.plot(x='Date', y='Volume', title='AMD Volume in October 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Nov2024=df.loc[(df['Date'] >= '2024-11-01') & (df['Date'] < '2024-11-30')]
print(Nov2024)
Nov2024_mean=Nov2024['Volume'].mean()
print("Nov 2024 Mean Volume:", Nov2024_mean)
Nov2024.plot(x='Date', y='Volume', title='AMD Volume in November 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Dec2024=df.loc[(df['Date'] >= '2024-12-01') & (df['Date'] < '2024-12-31')]
print(Dec2024)
Dec2024_mean=Dec2024['Volume'].mean()
print("Dec 2024 Mean Volume:", Dec2024_mean)
Dec2024.plot(x='Date', y='Volume', title='AMD Volume in December 2024')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jan2025=df.loc[(df['Date'] >= '2025-01-01') & (df['Date'] < '2025-01-31')]
print(Jan2025)
Jan2025_mean=Jan2025['Volume'].mean()
print("Jan 2025 Mean Volume:", Jan2025_mean)
Jan2025.plot(x='Date', y='Volume', title='AMD Volume in January 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Feb2025=df.loc[(df['Date'] >= '2025-02-01') & (df['Date'] < '2025-02-28')]
print(Feb2025)
Feb2025_mean=Feb2025['Volume'].mean()
print("Feb 2025 Mean Volume:", Feb2025_mean)
Feb2025.plot(x='Date', y='Volume', title='AMD Volume in February 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Mar2025=df.loc[(df['Date'] >= '2025-03-01') & (df['Date'] < '2025-03-31')]
print(Mar2025)
Mar2025_mean=Mar2025['Volume'].mean()
print("Mar 2025 Mean Volume:", Mar2025_mean)
Mar2025.plot(x='Date', y='Volume', title='AMD Volume in March 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Apr2025=df.loc[(df['Date'] >= '2025-04-01') & (df['Date'] < '2025-04-30')]
print(Apr2025)
Apr2025_mean=Apr2025['Volume'].mean()
print("Apr 2025 Mean Volume:", Apr2025_mean)
Apr2025.plot(x='Date', y='Volume', title='AMD Volume in April 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

May2025=df.loc[(df['Date'] >= '2025-05-01') & (df['Date'] < '2025-05-31')]
print(May2025)
May2025_mean=May2025['Volume'].mean()
print("May 2025 Mean Volume:", May2025_mean)
May2025.plot(x='Date', y='Volume', title='AMD Volume in May 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jun2025=df.loc[(df['Date'] >= '2025-06-01') & (df['Date'] < '2025-06-30')]
print(Jun2025)
Jun2025_mean=Jun2025['Volume'].mean()
print("Jun 2025 Mean Volume:", Jun2025_mean)
Jun2025.plot(x='Date', y='Volume', title='AMD Volume in June 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Jul2025=df.loc[(df['Date'] >= '2025-07-01') & (df['Date'] < '2025-07-31')]
print(Jul2025)
Jul2025_mean=Jul2025['Volume'].mean()
print("Jul 2025 Mean Volume:", Jul2025_mean)
Jul2025.plot(x='Date', y='Volume', title='AMD Volume in July 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Aug2025=df.loc[(df['Date'] >= '2025-08-01') & (df['Date'] < '2025-08-31')]
print(Aug2025)
Aug2025_mean=Aug2025['Volume'].mean()
print("Aug 2025 Mean Volume:", Aug2025_mean)
Aug2025.plot(x='Date', y='Volume', title='AMD Volume in August 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])

Sep2025=df.loc[(df['Date'] >= '2025-09-01') & (df['Date'] < '2025-09-30')]
print(Sep2025)
Sep2025_mean=Sep2025['Volume'].mean()
print("Sep 2025 Mean Volume:", Sep2025_mean)
Sep2025.plot(x='Date', y='Volume', title='AMD Volume in September 2025')
plt.xlabel('Date')
plt.ylabel('Volume')

plt.show()

