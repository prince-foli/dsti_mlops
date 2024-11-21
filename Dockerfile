# Use latest miniconda image as parent
# miniconda is python + conda installer
FROM continuumio/miniconda3

# Meta-data
LABEL maintainer="Prince Foli Acouetey <prince-foli.acouetey@edu.dsti.institute>" \
      description="Docker Pytest Workflow #2: Pytest\
      Setting environment to conduct test."

# Set the working directory to /app
WORKDIR /app

# Install the required libraries
RUN conda install pytest -y && \
    conda clean -y --all

# Copy the current directory contents into the container at /app
COPY . .

# Create mountpoint
VOLUME /app

# Run pytest when container launches
CMD ["pytest"]