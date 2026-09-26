# Join DataFrames with Pandas

This guide explains how to join several CSV, Excel, or JSON files with pandas. Each file is read into a DataFrame, and the DataFrames are joined one at a time using one or more matching columns.

## Join Code

```python
result = dfs[0]

for i in range(1, len(dfs)):
    result = pd.merge(
        result,
        dfs[i],
        on=key_columns,
        how=how_map[join_choice]
    )
```

## How It Works

1. `dfs` is a list that holds all the DataFrames.
2. Python list positions start at `0`, so `dfs[0]` is the first DataFrame.
3. `result = dfs[0]` starts the result with the first DataFrame.
4. `range(1, len(dfs))` loops through the remaining DataFrames. It starts at `1` because the first DataFrame is already in `result`.
5. `pd.merge()` joins the current result with the next DataFrame, `dfs[i]`.
6. The joined table is saved back into `result`. The next loop uses this updated result.
7. When the loop ends, `result` contains the final joined table.

## Join Flow

```mermaid
flowchart LR
    A["First DataFrame: dfs[0]"] --> B["Save as result"]
    B --> C["Join with dfs[1]"]
    C --> D["Update result"]
    D --> E["Join with dfs[2]"]
    E --> F["Final result"]
```

## Join Columns

`on=key_columns` tells pandas which column or columns to match between the DataFrames.

```python
key_columns = ["student_id"]
```

Every DataFrame must have a column with the same name, such as `student_id`. You can use more than one key column:

```python
key_columns = ["student_id", "class"]
```

When there is more than one key, pandas matches rows where all key values match.

## Join Types

`how=how_map[join_choice]` selects the join type. For example, if `join_choice` is `"1"`, `how_map[join_choice]` is `"inner"`.

| Choice | Join type | What it keeps |
| --- | --- | --- |
| `1` | `inner` | Rows with matching keys in both tables |
| `2` | `left` | Every row from the current result |
| `3` | `right` | Every row from the next DataFrame |
| `4` | `outer` | Rows from both tables, including rows without a match |

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

With `key_columns = ["student_id"]` and an inner join, the result is:

| student_id | name | mark |
| --- | --- | --- |
| 1 | Asha | 85 |
| 2 | Rafi | 92 |

## Important Notes

- `dfs` must contain at least one DataFrame.
- Every DataFrame must have each key column listed in `key_columns`.
- When using `on=key_columns`, key column names must be the same in every DataFrame.
- Check that the key column names and join choice are correct.
