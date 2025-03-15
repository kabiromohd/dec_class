# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy and install application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY data_process_db.py ./

# Expose port 8501
EXPOSE 8501

# Set the container's entrypoint to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "data_process_db.py"]
