from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://wmbcvvjiskfgau:e516ae997a2f8dfb1c29941e8fab818b76d17672865106f090328c7f5ad4d414@ec2-50-17-21-170.compute-1.amazonaws.com:5432/d3c33hv0lpcnck")
db = scoped_session(sessionmaker(bind=engine))


def main():
    fd = open("./initialize.sql", 'r')
    commands = fd.readlines()
    fd.close()

    for command in commands:
        db.execute(command)
        print(command, "Executed")
    db.commit()

if __name__ == "__main__":
    main()