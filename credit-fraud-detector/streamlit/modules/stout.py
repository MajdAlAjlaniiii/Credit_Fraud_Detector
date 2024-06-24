import streamlit as st
import subprocess

def DisplayPipeExecution(pipe_tag):
    command = ['kedro', 'run', '--tags', pipe_tag]
    process = subprocess.Popen(command, cwd='../', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    placeholder = st.empty()
    with placeholder.container(height=250):
        while process.poll() is None:
            line = process.stdout.readline()
            if not line:
                continue
            st.write(line.strip())
