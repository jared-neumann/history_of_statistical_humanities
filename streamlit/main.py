import streamlit as st
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# define session states
st.session_state.shakespeare_data_1 = None
st.session_state.shakespeare_data_2 = None
st.session_state.shakespeare_data_3 = None

# Load the data (you can replace this with your data loading code)
@st.cache_resource
def load_shakespeare_data():
    try:
        data_1 = pd.read_csv('data/Jevons_table_1.csv')
        data_2 = pd.read_csv('data/Jevons_table_2.csv', index_col=0)
        # read txt file for data_3
        with open('text_copy/Jevons_Shakspearean_literature.txt', 'r') as file:
            data_3 = file.read()
    except:
        try:
            data_1 = pd.read_csv('streamlit/data/Jevons_table_1.csv')
            data_2 = pd.read_csv('streamlit/data/Jevons_table_2.csv', index_col=0)
            # read txt file for data_3
            with open('streamlit/text_copy/Jevons_Shakspearean_literature.txt', 'r') as file:
                data_3 = file.read()
        except:
            try:
                data_1 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/Jevons_table_1.csv')
                data_2 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/Jevons_table_2.csv', index_col=0)
                # read txt file for data_3
                with open('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/text_copy/Jevons_Shakspearean_literature.txt', 'r') as file:
                    data_3 = file.read()
            except Exception as e:
                logging.error(f'Error loading Shakspearean literature data: {e}')
                st.error('Error loading Shakspearean literature data')
                return None, None
    return data_1, data_2, data_3

if not st.session_state.shakespeare_data_1 or not st.session_state.shakespeare_data_2 or not st.session_state.shakespeare_data_3:
    try:
        st.session_state.shakespeare_data_1, st.session_state.shakespeare_data_2, st.session_state.shakespeare_data_3 = load_shakespeare_data()
    except Exception as e:
        logging.error(f'Error loading Shakspearean literature data: {e}')
        st.error('Error loading Shakspearean literature data')

# function to format markdown text
def split_markdown_text(text):
    # split by --- which indicates header/body/appendices
    split_text = text.split('---')
    header = split_text[0]
    body = split_text[1]
    appendices = split_text[2]

    # split each by newlines
    header = header.split('\n')
    body = body.split('\n')
    appendices = appendices.split('\n')

    # now, [FIGURE] indicates a place where a figure goes
    # so we render the chunks before and after the figure
    # to add the figure in the middle
    return header, body, appendices

def make_jevons_table_1():

    # Plot the data
    fig, ax = plt.subplots()
    decades = st.session_state.shakespeare_data_1['PERIODS_OF_10_YEARS']
    collected_works = st.session_state.shakespeare_data_1['COLLECTED_WORKS']
    separate_plays_or_poems = st.session_state.shakespeare_data_1['SEPARATE_PLAYS_OR_POEMS']
    altered_plays = st.session_state.shakespeare_data_1['ALTERED_PLAYS']
    spurious_plays = st.session_state.shakespeare_data_1['SPURIOUS_PLAYS']
    commentaries = st.session_state.shakespeare_data_1['COMMENTARIES']
    total = st.session_state.shakespeare_data_1['TOTAL_PUBLICATIONS']

    ax.plot(decades, collected_works, label='Collected Works')
    ax.plot(decades, separate_plays_or_poems, label='Separate Plays or Poems')
    ax.plot(decades, altered_plays, label='Altered Plays')
    ax.plot(decades, spurious_plays, label='Spurious Plays')
    ax.plot(decades, commentaries, label='Commentaries')
    # make the total a dashed line
    ax.plot(decades, total, label='Total Publications', linestyle='--', color='whitesmoke')
    ax.set_xlabel('Decades')
    # rotate the x-axis labels
    plt.xticks(rotation=90)
    ax.set_ylabel('Number of Publications')
    ax.legend()
    # subtler background
    ax.set_facecolor('whitesmoke')
    fig.patch.set_facecolor('whitesmoke')

    # make background completely transparent
    ax.patch.set_alpha(0.0)
    fig.patch.set_alpha(0.0)
    
    # make legend background transparent
    ax.legend().get_frame().set_alpha(0.0)

    # set font color for x and y axis labels
    ax.xaxis.label.set_color('lightgray')
    ax.yaxis.label.set_color('lightgray')

    # set font color for x and y axis ticks
    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')

    # set font color for spines
    ax.spines['bottom'].set_color('lightgray')
    ax.spines['top'].set_color('lightgray')
    ax.spines['right'].set_color('lightgray')
    ax.spines['left'].set_color('lightgray')

    # set font color for legend items
    for text in ax.get_legend().get_texts():
        text.set_color('lightgray')
    
    return fig, ax

# Sidebar content
st.sidebar.title('Navigation')
page_selection = st.sidebar.radio("Choose a project page", ["Home", "Jevons, Shakspearean literature (1864)"])

st.sidebar.title('About')
st.sidebar.info('Author: Jared Neumann')
st.sidebar.info('Email: antspiderbee@gmail.com')
st.sidebar.info('GitHub: jared-neumann')

# Home Page
if page_selection == "Home":
    st.title('Statistical humanities projects')
    st.header('Project overview')
    st.write('This project aims to find and present statistical humanities projects, especially early ones, for the following reasons:')
    st.write('1. To provide historical context for the development of the field of digital humanities.')
    st.write('2. To preserve the work of early statistical humanities projects.')
    st.write('3. To identify common strategies and important developments in the field.')

    st.header('Project goals')
    st.write('The goal of this project is to research, transcribe, present, and analyze early and/or toy statistical humanities projects. As research for additional projects wraps up, pages will be added to this site to present them.')

    st.header('About statistical humanities')
    st.write('Statistical humanities is a subfield of digital humanities that uses statistical methods to analyze humanities data. This can include text analysis, network analysis, and other methods. The field has been around for a long time, but has been called different things over the years.')

# Shakespearean Literature Page
elif page_selection == "Jevons, Shakspearean literature (1864)":

    # the markdown text is split into header, body, and appendices
    # with each paragraph separated by a newline
    # and [FIGURE] indicating where a figure should go
    header, body, appendices = split_markdown_text(st.session_state.shakespeare_data_3)

    # Header
    for line in header:
        st.markdown(line, unsafe_allow_html=True)

    st.markdown('---', unsafe_allow_html=True)

    # Body
    for line in body:
        if '[FIGURE_1]' in line:
            # write dataframe from data_1
            # center it
            col1, col2, col3 = st.columns([1, 20, 1])
            col1.write()
            col2.dataframe(st.session_state.shakespeare_data_1)
            col3.write()
        elif '[FIGURE_2]' in line:
            # write dataframe from data_2
            # center it
            col1, col2, col3 = st.columns([1, 20, 1])
            col1.write()
            col2.table(st.session_state.shakespeare_data_2)
            col3.write()      
        else:
            st.markdown(line, unsafe_allow_html=True)

    st.markdown('---', unsafe_allow_html=True)

    # Appendices
    for line in appendices:
        if '[FIGURE_3]' in line:
            # make and display the figure
            fig, ax = make_jevons_table_1()
            st.pyplot(fig)
        else:
            st.markdown(line, unsafe_allow_html=True)







