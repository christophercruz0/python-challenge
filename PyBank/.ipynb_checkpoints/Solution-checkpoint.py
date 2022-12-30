{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "a33497ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Finanacial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Total: $22564198\n",
      "Average Change: $-8311.11\n",
      "Greatest Increase in Profits: Aug-16 ($1862002)\n",
      "Greatest Decrease in Profits: Feb-14 ($-1825558)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd, numpy as np, csv \n",
    "\n",
    "bank = pd.read_csv(r'/Users/christophercruz/Downloads/Instructions 4/PyBank/Resources/budget_data.csv')\n",
    "bank['Profit/Losses Diff'] = bank['Profit/Losses'].diff()\n",
    "avg = bank['Profit/Losses Diff'].mean()\n",
    "avg = np.round(avg,decimals=2)\n",
    "mx, mn = bank[['Profit/Losses Diff']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].max()],bank[['Profit/Losses Diff']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].min()]\n",
    "mn, mx = mn.astype(int), mx.astype(int)\n",
    "dtmx ,dtmn = bank[['Date']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].max()],bank[['Date']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].min()]\n",
    "\n",
    "print(\"Finanacial Analysis\")\n",
    "print(\"----------------------------\")\n",
    "print(\"Total Months: \"+bank[\"Date\"].count().astype(str))\n",
    "print(\"Total: $\"+bank[\"Profit/Losses\"].sum().astype(str))\n",
    "print(\"Average Change: $\" + avg.astype(str))\n",
    "print(\"Greatest Increase in Profits: \"+dtmx.to_string(header=False,index=False)+' ($'+ mx.to_string(header=False,index=False)+')')\n",
    "print(\"Greatest Decrease in Profits: \"+dtmn.to_string(header=False,index=False)+' ($'+ mn.to_string(header=False,index=False)+')')\n",
    "\n",
    "\n",
    "file = open('Solution.csv','w')\n",
    "writer = csv.writer(file)\n",
    "writer.writerow([\"Finanacial Analysis\"])\n",
    "writer.writerow([\"----------------------------\"])\n",
    "writer.writerow([\"Total Months: \"+bank[\"Date\"].count().astype(str)])\n",
    "writer.writerow([\"Total: $\"+bank[\"Profit/Losses\"].sum().astype(str)])\n",
    "writer.writerow([\"Average Change: $\" + avg.astype(str)])\n",
    "writer.writerow([\"Greatest Increase in Profits: \"+dtmx.to_string(header=False,index=False)+' ($'+ mx.to_string(header=False,index=False)+')'])\n",
    "writer.writerow([\"Greatest Decrease in Profits: \"+dtmn.to_string(header=False,index=False)+' ($'+ mn.to_string(header=False,index=False)+')'])\n",
    "file.close()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "3c4b0de4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "22564198"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bank[\"Profit/Losses\"].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7fe0a6a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "86"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bank[\"Date\"].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "21324960",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Date  Profit/Losses  Profit/Losses Diff\n",
      "0   Jan-10        1088983                 NaN\n",
      "1   Feb-10        -354534          -1443517.0\n",
      "2   Mar-10         276622            631156.0\n",
      "3   Apr-10        -728133          -1004755.0\n",
      "4   May-10         852993           1581126.0\n",
      "..     ...            ...                 ...\n",
      "81  Oct-16        -729004          -1627245.0\n",
      "82  Nov-16        -112209            616795.0\n",
      "83  Dec-16         516313            628522.0\n",
      "84  Jan-17         607208             90895.0\n",
      "85  Feb-17         382539           -224669.0\n",
      "\n",
      "[86 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "bank['Profit/Losses Diff'] = bank['Profit/Losses'].diff()\n",
    "    \n",
    "print(bank)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "99af5352",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1862002.0"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bank['Profit/Losses Diff'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "f0f7830a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1825558.0"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "0d7b4176",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-8311.11\n"
     ]
    }
   ],
   "source": [
    "\n",
    "avg = bank['Profit/Losses Diff'].mean()\n",
    "avg = np.round(avg,decimals=2)\n",
    "print(avg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "af5aefed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date                     Aug-16\n",
       "Profit/Losses            951227\n",
       "Profit/Losses Diff    1862002.0\n",
       "Name: 79, dtype: object"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bank.loc[bank['Profit/Losses Diff'].idxmax()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "04e3bdc9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date             Aug-16\n",
       "Profit/Losses    951227\n",
       "Name: 79, dtype: object"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bank.iloc[bank['Profit/Losses Diff'].argmax(),0:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "1a9c9270",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Aug-16\n"
     ]
    }
   ],
   "source": [
    "dtmx = bank[['Date']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].max()]\n",
    "dtmn = bank[['Date']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].min()]\n",
    "\n",
    "print(dtmx.to_string(header=False,index=False))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "f0101979",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Aug-16 ($1862002)\n",
      "Aug-16 ($-1825558)\n"
     ]
    }
   ],
   "source": [
    "mx, mn = bank[['Profit/Losses Diff']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].max()],bank[['Profit/Losses Diff']][bank['Profit/Losses Diff']==bank['Profit/Losses Diff'].min()]\n",
    "mn, mx = mn.astype(int), mx.astype(int)\n",
    "\n",
    "print(dtmx.to_string(header=False,index=False)+' ($'+ mx.to_string(header=False,index=False)+')')\n",
    "print(dtmn.to_string(header=False,index=False)+' ($'+ mn.to_string(header=False,index=False)+')')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b58b224e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
