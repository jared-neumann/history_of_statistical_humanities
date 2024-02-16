import streamlit as st
import pandas as pd
import io
import base64
import os
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# define session states
st.session_state.shakespeare_data_1 = None
st.session_state.shakespeare_data_2 = None
st.session_state.shakespeare_markdown = None

st.session_state.mendenhall_data_1 = None
st.session_state.mendenhall_data_2 = None
st.session_state.mendenhall_markdown = None

# Load the data (you can replace this with your data loading code)
@st.cache_resource
def load_shakespeare_data():
    try:
        data_1 = pd.read_csv('data/jevons_table_1.csv')
        data_2 = pd.read_csv('data/jevons_table_2.csv', index_col=0)
        # read txt file for shakespeare_markdown
        shakespeare_markdown = open('text_copy/jevons_shakspearian_literature.txt', 'r').read() 
    except:
        logging.error('Could not load local data, trying from the Streamlit directory')
        logging.info('Current directory: ' + os.getcwd())
        try:
            data_1 = pd.read_csv('streamlit/data/jevons_table_1.csv')
            data_2 = pd.read_csv('streamlit/data/jevons_table_2.csv', index_col=0)
            # read txt file for data_3
            shakespeare_markdown = open('streamlit/text_copy/jevons_shakspearian_literature.txt', 'r').read()
        except:
            logging.error('Could not load data from the Streamlit directory, trying from the GitHub repository')
            try:
                data_1 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/jevons_table_1.csv')
                data_2 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/jevons_table_2.csv', index_col=0)
                # read txt file for data_3
                shakespeare_markdown = open('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/text_copy/jevons_shakspearian_literature.txt', 'r').read()
            except Exception as e:
                logging.error(f'Error loading Shakspearian literature data: {e}')
                st.error('Error loading Shakspearian literature data')
                return None, None
    return data_1, data_2, shakespeare_markdown

if not st.session_state.shakespeare_data_1 or not st.session_state.shakespeare_data_2 or not st.session_state.shakespeare_markdown:
    try:
        st.session_state.shakespeare_data_1, st.session_state.shakespeare_data_2, st.session_state.shakespeare_markdown = load_shakespeare_data()
    except Exception as e:
        logging.error(f'Error loading Shakspearian literature data: {e}')
        st.error('Error loading Shakspearian literature data')

@st.cache_resource
def load_mendenhall_data():
    try:
        data_1 = pd.read_csv('data/mendenhall_table_1.csv')
        data_2 = pd.read_csv('data/oliver_twist_word_lengths.csv')
        mendenhall_markdown = open('text_copy/mendenhall_characteristic_curves.txt', 'r').read()
    except:
        try:
            data_1 = pd.read_csv('streamlit/data/mendenhall_table_1.csv')
            data_2 = pd.read_csv('streamlit/data/oliver_twist_word_lengths.csv')
            mendenhall_markdown = open('streamlit/text_copy/mendenhall_characteristic_curves.txt', 'r').read()
        except:
            try:
                data_1 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/mendenhall_table_1.csv')
                data_2 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/oliver_twist_word_lengths.csv')
                mendenhall_markdown = open('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/text_copy/mendenhall_characteristic_curves.txt', 'r').read()
            except Exception as e:
                logging.error(f'Error loading Mendenhall data: {e}')
                st.error('Error loading Mendenhall data')
                return None
    return data_1, data_2, mendenhall_markdown

if not st.session_state.mendenhall_data_1 or not st.session_state.menenhall_data_2 or not st.session_state.mendenhall_markdown:
    try:
        st.session_state.mendenhall_data_1, st.session_state.mendenhall_data_2, st.session_state.mendenhall_markdown = load_mendenhall_data()
    except Exception as e:
        logging.error(f'Error loading Mendenhall data: {e}')
        st.error('Error loading Mendenhall data')

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

def make_mendenhall_figure_1():

    data = st.session_state.mendenhall_data_1

    plt.figure(figsize=(12, 5)) # set figure size
    plt.plot(data["number_of_letters"], data["number_of_words"], label="Original", color="whitesmoke") # plot original
    plt.grid(True) # add grid

    plt.xticks(range(1, 17)) # set x-axis range
    plt.xlim(1, 16) # align 1 with the first tick
    plt.xticks(list(plt.xticks()[0]) + [16]) # relabel last tick as 16

    plt.ylim(0, 300) # set y-axis range
    plt.yticks(list(plt.yticks()[0])[1:-1]) # don't show first or last tick

    # make background completely transparent
    plt.gca().patch.set_alpha(0.0) # set background of plot area to transparent
    plt.gcf().patch.set_alpha(0.0) # set background of figure to transparent

    # set font color for x and y axis labels
    plt.gca().xaxis.label.set_color('lightgray')
    plt.gca().yaxis.label.set_color('lightgray')

    # set font color for x and y axis ticks
    plt.gca().tick_params(axis='x', colors='gray')
    plt.gca().tick_params(axis='y', colors='gray')

    # set font color for spines
    plt.gca().spines['bottom'].set_color('lightgray')
    plt.gca().spines['top'].set_color('lightgray')
    plt.gca().spines['right'].set_color('lightgray')
    plt.gca().spines['left'].set_color('lightgray')

    
    return plt

def make_mendenhall_figure_2():

    data = st.session_state.mendenhall_data_2

    # plot the data
    fig, ax = plt.subplots()

    # line styles
    linestyles = [
        ('dashdot', '-.'),
        ('dashed', '--'),
        
        ('dotted', ':'),
        ('solid', '-'),
        ('densely dotted', (0, (1, 1)))
    ]

    # only keep columns labeled with 'Set '
    data = data.filter(like='Set ', axis=1)

    for i in range(5):
        linestyle = linestyles[i]
        ax.plot(data.index, data.iloc[:, i], label=f'Word length {i+1}', linestyle=linestyle[1], color='whitesmoke')

    # add a grid
    ax.grid(True)

    # modify x-ticks so that 1 is the first tick and 16 is the last tick
    ax.set_xticks(range(1, 17))
    ax.set_xlim(1, 16)

    # modify y range to 0-300, but don't show 0 or 300
    ax.set_ylim(0, 300)
    ax.set_yticks(range(50, 300, 50))

    # modify figure size so that the grid is square
    fig.set_size_inches(12, 5)

    # make background completely transparent
    ax.patch.set_alpha(0.0)
    fig.patch.set_alpha(0.0)

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

    return fig, ax

# Sidebar content
st.sidebar.title('Navigation')
page_selection = st.sidebar.radio("Choose a project page", ["Home", "Jevons, Shakspearian literature (1864)", "Mendenhall, Characteristic curves (1887)"])

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
elif page_selection == "Jevons, Shakspearian literature (1864)":

    # the markdown text is split into header, body, and appendices
    # with each paragraph separated by a newline
    # and [FIGURE] indicating where a figure should go
    header, body, appendices = split_markdown_text(st.session_state.shakespeare_markdown)

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

elif page_selection == "Mendenhall, Characteristic curves (1887)":

    # the markdown text is split into header, body, and appendices
    # with each paragraph separated by a newline
    # and [FIGURE] indicating where a figure should go
    header, body, appendices = split_markdown_text(st.session_state.mendenhall_markdown)

    # Header
    for line in header:
        st.markdown(line, unsafe_allow_html=True)

    st.markdown('---', unsafe_allow_html=True)

    # Body
    for line in body:
        if '[FIGURE_1]' in line:
            # make and display the figure
            fig = make_mendenhall_figure_1()
            st.pyplot(fig)
        elif '[TABLE_1]' in line:
            # write dataframe from data_1
            data_1 = st.session_state.mendenhall_data_1
            # get a list of headers to make the index
            header_index = list(data_1.columns)
            # transpose the dataframe to look like a table
            data_1 = data_1.T
            # set the index to the list of headers
            data_1.index = header_index

            # make a markdown table with just the data and no headers
            values_data_1 = data_1.values.tolist()
            index_data_1 = data_1.index.tolist()
            
            data_1 = '<table>'

            for i, row in enumerate(values_data_1):
                data_1 += '<tr>'
                data_1 += f'<td>{index_data_1[i]}</td>'
                for value in row:
                    data_1 += f'<td>{value}</td>'
                data_1 += '</tr>'
            data_1 += '</table>'

            # center it as markdown
            centered_data_1 = f'<center>{data_1}</center>'
            st.markdown(centered_data_1, unsafe_allow_html=True)
        elif '[FIGURE_2]' in line:
            # make and display the figure
            fig, ax = make_mendenhall_figure_2()
            st.pyplot(fig)
        else:
            st.markdown(line, unsafe_allow_html=True)

    st.markdown('---', unsafe_allow_html=True)

    # Appendices
    for line in appendices:
        st.markdown(line, unsafe_allow_html=True)

else:
    st.error('Page not found')
    






