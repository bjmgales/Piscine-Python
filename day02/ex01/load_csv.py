import pandas as pd


def load(path: str) -> list:
    try:
        assert isinstance(path, str), "path parameter must be of str type"
        assert path.endswith('.csv'), "awaiting .csv file"
        dataset = pd.read_csv(path, encoding="utf-8")
        if dataset.empty:
            raise ValueError("file is empty.")
        row_len = len(dataset.columns)
        if any(row_len != len(row) for row in dataset.values):
            raise ValueError("irregular row lengths.")
        print("Loading dataset of dimensions:", dataset.shape)
        dataset.reset_index(drop=True, inplace=True)
        print(dataset.head(3))

    except Exception as err:
        print(type(err).__name__ + ':', err)
        return None
    return dataset
