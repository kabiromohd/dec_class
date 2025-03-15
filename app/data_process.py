import pandas as pd
import streamlit as st


def get_csv(uploaded_file: str) -> pd.DataFrame:
    """Read uploaded file into a Dataframe

    Args:
        uploaded_file (str): Uploaded file from the UI

    Returns:
        list: A dataframe object and the name of the uploaded file
    """
    df = pd.read_csv(uploaded_file)
    return df


def streamlit_ui(df: pd.DataFrame):
    """Streamlit app to upload a csv file and display it's summary statistics

    Args:
        df (pd.DataFrame): _description_
    """
    st.write(df.head())
    st.write(df.describe())


if __name__ == "__main__":

    st.set_page_config(page_title="Docker Practice Project",
                       page_icon=":bar_chart:")
    st.title("Docker Practice Project")

    uploaded_file = st.file_uploader("Upload a CSV file", "csv")
    # Check if a file has been uploaded before running the data processing
    if uploaded_file is not None:
        df = get_csv(uploaded_file)

        streamlit_ui(df)
