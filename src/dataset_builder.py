from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.config import (
    TEST_SIZE,
    RANDOM_STATE,
)


class DatasetBuilder:

    def __init__(self, dataframe, feature_columns, target_column):

        self.df = dataframe.copy()

        self.feature_columns = feature_columns

        self.target_column = target_column

    ############################################################

    def prepare(self):

        X = self.df[self.feature_columns]

        y = self.df[self.target_column]

        return X, y

    ############################################################

    def split(
        self,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    ):

        X, y = self.prepare()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state
        )

        return X_train, X_test, y_train, y_test

    ############################################################

    def scale(self):

        X_train, X_test, y_train, y_test = self.split()

        scaler = StandardScaler()

        X_train_scaled = scaler.fit_transform(X_train)

        X_test_scaled = scaler.transform(X_test)

        return (
            X_train_scaled,
            X_test_scaled,
            y_train,
            y_test,
            scaler
        )