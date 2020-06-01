def packages():
    if 'google.colab' in sys.modules:
        !pip install pandas-profiling==2.*

    else:
        None

def train_test(data):
    from sklearn.model_selection import train_test_split
    import pandas as pd
    df = pd.read_csv(data)
    train, test = train_test_split(df, train_size=0.80, test_size=0.20)
    print("Train shape :",train.shape,"Test shape :" ,test.shape)
    return


