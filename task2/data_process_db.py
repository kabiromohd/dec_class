import pandas as pd
from sqlalchemy import create_engine
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


def get_csv(uploaded_file: str) -> list:
    """Read uploaded file into a Dataframe

    Args:
        uploaded_file (str): Uploaded file from the UI

    Returns:
        list: A dataframe object and the name of the uploaded file
    """
    df = pd.read_csv(uploaded_file)

    file_name = uploaded_file.name
    file_name = file_name.split(".")[0]
    return df, file_name


def load_csv(db_connection, csv_data: pd.DataFrame, table_name: str):
    """Loads Dataframe into Postgres table

    Args:
        db_connection (obj): The database connection object
        csv_data (pd.DataFrame): The dataframe to be loaded
        table_name (str): The Postgres table to load into
    """
    with db_connection.begin() as connection:
        csv_data.to_sql(
            name=table_name, con=connection, if_exists="replace", index=False
        )


def read_table(db_connection) -> pd.DataFrame:
    """Read data from Postgres table

    Args:
        db_connection (obj): The database connection object

    Returns:
        pd.DataFrame: Dataframe
    """
    with db_connection.begin() as connection:
        df = pd.read_sql(sql=file_name, con=connection)
    return df


def streamlit_ui(df: pd.DataFrame):
    """Streamlit app to upload a csv file and display it's summary statistics

    Args:
        df (pd.DataFrame): _description_
    """
    st.write(df.head())
    st.write(df.describe())


if __name__ == "__main__":

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    st.set_page_config(page_title="Docker Practice Project",
                       page_icon=":bar_chart:")
    st.title("Docker Practice Project")

    uploaded_file = st.file_uploader("Upload a CSV file", "csv")
    # Check if a file has been uploaded before running the data processing
    if uploaded_file is not None:
        df, file_name = get_csv(uploaded_file)

        db_connection = create_engine(
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa: E501
        )
        load_csv(db_connection, df, file_name)
        read_data = read_table(db_connection)
        streamlit_ui(read_data)
