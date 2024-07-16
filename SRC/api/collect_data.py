from actions import selectDataVar
from database import SessionLocal


def Collectdata():
    data = selectDataVar(db=SessionLocal())
    data.to_csv('./data_var.csv', index=False)


if __name__ == '__main__':
    Collectdata()
