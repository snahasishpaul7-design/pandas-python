import pandas as pd


def read_any_file():

    while True:

        file_type = input(
            "Which file will you provide, CSV, Excel, or JSON?:- "
        ).lower().strip()

        path = input("Enter the file path:-").strip()

        try:

            if file_type == "csv":

                df = pd.read_csv(path, encoding="latin-1")

            elif file_type == "excel":

                df = pd.read_excel(path)

            elif file_type == "json":

                df = pd.read_json(path)

            else:

                print("Invalid file type. Please type csv, excel, or json.")

                continue

            print(df)

            return df

        except Exception as e:

            print(f"Error reading file: {e}")


def join_data():

    num_files = int(input("How many files do you want to join:-"))

    dfs = []

    for i in range(num_files):

        print(f"\nProvide file {i + 1}:")
        df = read_any_file()
        dfs.append(df)

    for i, df in enumerate(dfs):

        print(f"\nColumns in DataFrame {i + 1}:", list(df.columns))

    num_keys = int(input("\nHow many columns do you want to join on:-"))

    key_columns = []

    for j in range(num_keys):

        col = input(f"Enter key column {j + 1} name:-").strip()
        key_columns.append(col)

    print(
        "\npress 1 for inner join\n"
        "press 2 for left join\n"
        "press 3 for right join\n"
        "press 4 for outer join\n"
    )

    how_map = {
        "1": "inner",
        "2": "left",
        "3": "right",
        "4": "outer",
    }

    join_choice = input("Which join do you want to do:-").strip()

    if join_choice not in how_map:

        print("Invalid choice")

        return

    result = dfs[0]

    for i in range(1, len(dfs)):

        result = pd.merge(
            result, dfs[i],
            on=key_columns,
            how=how_map[join_choice]
        )

    print("\nJoined DataFrame:")
    print(result)

    return result


if __name__ == "__main__":

    join_data()
