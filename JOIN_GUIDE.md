# Joining DataFrames with Pandas

This guide explains how to join several CSV, Excel, or JSON files with pandas. The interactive example in **join_project.py** reads each file into a DataFrame, then joins the DataFrames using matching key columns.

For a quick overview of the whole repository and its other pandas examples, see the [main README](README.md).

## The Core Loop

~~~python
result = dfs[0]

for i in range(1, len(dfs)):
    result = pd.merge(
        result,
        dfs[i],
        on=key_columns,
        how=how_map[join_choice]
    )
~~~

## How It Works

1. **dfs** is a list that holds all the DataFrames.
2. Python list positions start at **0**, so **dfs[0]** is the first DataFrame.
3. **result = dfs[0]** starts the result with the first DataFrame.
4. **range(1, len(dfs))** loops through the remaining DataFrames. It starts at **1** because the first DataFrame is already in **result**.
5. **pd.merge()** joins the current result with the next DataFrame, **dfs[i]**.
6. The joined table is saved back into **result**. The next loop uses this updated result.
7. When the loop ends, **result** contains the final joined table.

## Join Flow

~~~mermaid
flowchart TD
    A[Read the first file] --> B[Set result to the first DataFrame]
    B --> C{More DataFrames?}
    C -- Yes --> D[Choose matching key columns]
    D --> E[Merge result with the next DataFrame]
    E --> C
    C -- No --> F[Show the final joined DataFrame]
~~~

## Join Columns

The **on=key_columns** option tells pandas which column or columns to match between DataFrames. When you use **on=**, the key column names must be the same in every DataFrame.

For one key column:

~~~python
key_columns = ["student_id"]
~~~

For more than one key column:

~~~python
key_columns = ["student_id", "class"]
~~~

With multiple keys, pandas matches rows only when all key values match.

## Join Types

The **how** option selects which rows to keep:

| Choice | Join type | What it keeps |
| --- | --- | --- |
| **1** | **inner** | Rows with matching keys in both tables |
| **2** | **left** | Every row from the current result |
| **3** | **right** | Every row from the next DataFrame |
| **4** | **outer** | Rows from both tables, including rows without a match |
| **5** | **cross** | Every possible row combination between the two tables |

## Example

First DataFrame:

| student_id | name |
| --- | --- |
| 1 | Asha |
| 2 | Rafi |

Second DataFrame:

| student_id | mark |
| --- | --- |
| 1 | 85 |
| 2 | 92 |

With **key_columns = ["student_id"]** and an inner join, the result is:

| student_id | name | mark |
| --- | --- | --- |
| 1 | Asha | 85 |
| 2 | Rafi | 92 |

## Important Notes

- Provide at least one DataFrame.
- Every DataFrame must contain each key column listed in **key_columns**.
- When using **on=key_columns**, key column names must be the same in every DataFrame.
- Check that the key column names and join choice are correct.
- A cross join does not use key columns.
