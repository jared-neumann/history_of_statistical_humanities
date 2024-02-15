import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# define session states
st.session_state.shakespeare_data_1 = None
st.session_state.shakespeare_data_2 = None

# Load the data (you can replace this with your data loading code)
@st.cache_resource
def load_shakespeare_data():
    try:
        data_1 = pd.read_csv('data/Jevons_table_1.csv')
        data_2 = pd.read_csv('data/Jevons_table_2.csv', index_col=0)
    except:
        try:
            data_1 = pd.read_csv('streamlit/data/Jevons_table_1.csv')
            data_2 = pd.read_csv('streamlit/data/Jevons_table_2.csv', index_col=0)
        except:
            try:
                data_1 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/Jevons_table_1.csv')
                data_2 = pd.read_csv('https://raw.githubusercontent.com/jared-neumann/statistical-humanities-projects/main/data/Jevons_table_2.csv', index_col=0)
            except Exception as e:
                logging.error(f'Error loading Shakspearean literature data: {e}')
                st.error('Error loading Shakspearean literature data')
                return None, None
    return data_1, data_2

if not st.session_state.shakespeare_data_1 or not st.session_state.shakespeare_data_2:
    try:
        st.session_state.shakespeare_data_1, st.session_state.shakespeare_data_2 = load_shakespeare_data()
    except Exception as e:
        logging.error(f'Error loading Shakspearean literature data: {e}')
        st.error('Error loading Shakspearean literature data')

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

    title = """SHAKSPEAREAN LITERATURE"""
    byline = """<div style="text-align: justify;">William Stanley Jevons, Owens College, Manchester, March 5, 1864</div>"""
    paragraph_1 = """<div style="text-align: justify;">Two years ago I formed the following estimate of the number of publications containing or relating to the works of Shakspeare. As these works are universally allowed to be the best ornament of the English language, it seemed likely that the comparative degrees of attention bestowed upon them at different periods would afford some measure, or at least some imperfect indication, of the degree of good taste then prevailing. The results, perhaps, even in this respect are not valueless, but to the student of Shakspeare they may, at the present time especially, possess other points of interest.</div>"""
    info_table_1 = """<div style="text-align: justify;"><i>Number of Shakspearean Books published in each Period of Ten Years from 1591 to 1830 inclusive.</i></div>"""
    paragraph_2 = """<div style="text-align: justify;">The numbers in the above table were derived from a careful examination of that portion (filling two volumes) of the Great Catalogue of the British Museum which is under the heading "Shakspeare." The old or minor catalogues of the Museum were also compared, and some additions were made from Halliwell's "Shakspeariana," the "Bibliotheca Britannica" of Watts, the printed Catalogue of the Bodleian Library, the publishers' indexes, or other bibliographical works.</div>"""
    paragraph_3 = """<div style="text-align: justify;">Though these authorities are, doubtless, some of the best and most complete for the purpose, it is not to be supposed that the estimate pretends to anything like completeness. The numbers for the earlier years may be nearly complete, the earlier publications and every successive issue having been so carefully sought out and recorded. Within the last fifty or one hundred years the case is very different, and after 1830 the numbers were thought too uncertain for publication. It may be added, however, that the number of publications I have counted considerably exceeds those enumerated in Wilson's 'Shaksperiana,' which purported to give </i>all</i> Shakspearian publications up to its date (1827). The same might be said as regards Halliwell's later work of the same kind.</div>"""
    paragraph_4 = """<div style="text-align: justify;">As regards the foregoing table, it should be noted that the numbers of collected works include a few incomplete collections of plays. A poem or separate collection of poems was counted as equivalent to a separate play. The spurious plays are those entered as such in,the Museum Catalogue. Of foreign editions, or works relating to Shakspeare, 70 were enumerated up to 1830; but as it seemed obvious that even the National Library could not give a proper account of these, they were entirely omitted from the estimate. The books counted under the head of Commentaries consist of such works concerning Shakspeare or his writings as would be usually entered under the heading of Shakspeare in a good index. Yet the enumeration of commentaries is, I believe, far from complete; and of course the works which more or less refer to or bear upon Shakspeare are quite indefinite and much more numerous.</div>"""
    paragraph_5 = """<div style="text-align: justify;">Statements hazarded under conditions are apt to be repeated <i>simpliciter</i>; but the following numbers must not be taken for more than they are worth as approximations:—</div>"""
    info_table_2 = """<div style="text-align: justify;"><i>Approximate Number of English Shakspearian Publications</i>, 1591-1830.</div>"""
    paragraph_6 = """<div style="text-align: justify;">Of late years the publication of separate plays may have fallen off, but the complete editions or successive issues of the same editor's copy have become so numerous that an exact estimate could hardly be formed. The Great Exhibition of 1851 called forth at least eight complete editions; and, at the present moment, the Shakspearian press is probably more active than ever before. Between 1630 and 1880 I have counted nearly 300 English and 190 foreign publications, making our total lowest estimate 1,262. It would not be safe, however, to say that a Shakspeare Library could be complete under 2,000 separate works, making a good deal more than 2,000 volumes.</div>"""
    paragraph_7 = """<div style="text-align: justify;">I may point out a few facts which are confirmed or illustrated by the above numbers. The enumeration commences with the supposed quarto 'King John,' of 1591, but the 'Venus' of 1593 is the first true publication. After Shakspeare's death, in 1616, the republication of the plays or poems continued pretty frequent up to the breaking ont of the Great Rebellion. The number of plays, such as ' Locrine,' ' Mucedorus,' 'Sir John Oldcastle,' 'The London Prodigal,' 'The Puritan,' ' Yorkshire Tragedy,' 'Cromwell,' &c., falsely attributed to Shakspeare, is an indirect proof of the estimation in which he was then held. It is remarkable too that, up to 1640, the detached poems were more popular than they have ever since been. Some 26 issues of poems, chiefly the ' Venus' or the ' Lucrece,' took place up to 1640, since which date there have only been, up to 1830, some 12 issues of the poems, chiefly in the collected form, and for the sake of the sonnets. And in this, popular taste has not erred, for the 'Venus,' and ' Lucrece,' and many of the sonnets are hardly to be regarded as more than extravagant examples of powerful imagination and description.</div>"""
    paragraph_8 = """<div style="text-align: justify;">The distraction of the public attention by the Great Rebellion, and the Puritanical suppression of the theatres, put a complete stop to Shakspearian publications. The press teemed with sermons, theological or political tracts, or bulletins of news, the germ of our newspapers, but Shakepeare was forgotten or tabooed. So far as I have been able to discover, there was not a single Shakspearian publication between the octavo edition of the Sonnets in 1640, and a quarto copy of the Merchant of Venice in 1652. The only other publications of the ten years 1651-60, were Lear, and Othello, with the Lucrece, and the spurious Merry Devil of Edmonton, all in 1655. Even the Restoration and the re-opening of the theatres only produced the altered Bottom the Weaver, in 1661, and the spurious Birth of Merlin, in 1662. The third folio edition, indeed, appeared in 1663-4, but in the few next years we have only a re-issue of the false Mucedorus in 1668, and Davenant and Dryden's altered comedy of The Tempest in 1670.</div>"""
    paragraph_9 = """<div style="text-align: justify;">After 1673 the publications became a little more frequent and continuous, but most of the plays were subjected to vile improvements. They generally, too, appeared under new names, by which their best friends would hardly know them, such as 'The Comical Gallant' ('Merry Wives'), ' Universal Passion' ('Much Ado'), 'Love Betrayed' ('Twelfth Night'), 'Sanny the Scot,' and 'Cure for a Scold' ('Taming of the Shrew'), 'Love in a Forest, or a Modern Receipt' ('As You Like It'), and so on. This was the period when Shadwell, and Jevon, and Cibber and other like dramatists supplied the theatres with trash that still dilutes our libraries. It is of course to this almost total neglect or misappreciation of Shakspeare during the second half of the century in which he died that we must attribute our ignorance of his personal history.</div>"""
    paragraph_10 = """<div style="text-align: justify;">With the eighteenth century a new state of things gradually began. The critical study of Shakspeare took its rise with Rowe's Life and Works of the Poet in 1709 and 1710, and the successive issues of this edition, and of the subsequent well-known editions of Pope, Theobald, Hanmer, Warburton and Blair, show that the public taste was gradually rising from its debasement.</div>"""
    paragraph_11 = """<div style="text-align: justify;">Just about the middle of the century, again, a further new period began in the history of Shakspearian literature, which, after the manner of Dr. Whewell, we might call the Period of Commentaries. A few slight works of a commentatorial character had appeared some time before, beginning with Rymer's depreciatory essays in 1678, 1692-3, and Gildon's answer to them. With Johnson's 'Observations on the Tragedy of Macbeth' in 1745, and the warm discussions excited by Warburton's writings, properly commenced the new branch of critical literature which, in 1830, had added 280 volumes to our shelves.</div>"""
    paragraph_12 = """<div style="text-align: justify;">Garrick's acting from the year 1741, his Shakspeare Jubilee in 1769, Kemble's acting from 1783 to 1817, and even the fierce discussion concerning Ireland's forged 'Vortigern' in 1796, may be noted among the causes which have drawn attention to Shakspeare's excellencies, or swollen our Shakspearian literature. W. S. Jevons.</div>"""
    appendix = """<b><div style="text-align: justify;">APPENDIX A: Graphing the data</b></div>"""
    appendix_paragraph_1 = """<div style="text-align: justify;">The following is a graphical representation of the data in the first table.</div>"""

    st.title(title)
    st.markdown(byline, unsafe_allow_html=True)
    # add a line
    st.markdown('---')
    st.markdown(paragraph_1, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(info_table_1, unsafe_allow_html=True)
    st.dataframe(st.session_state.shakespeare_data_1)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_2, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_3, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_4, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_5, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(info_table_2, unsafe_allow_html=True)
    st.dataframe(st.session_state.shakespeare_data_2)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_6, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_7, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_8, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_9, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_10, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_11, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown(paragraph_12, unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('---')
    st.markdown(appendix, unsafe_allow_html=True)
    st.markdown(appendix_paragraph_1, unsafe_allow_html=True)

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
    ax.plot(decades, total, label='Total Publications', linestyle='--', color='black')
    ax.set_xlabel('Decades')
    # rotate the x-axis labels
    plt.xticks(rotation=90)
    ax.set_ylabel('Number of Publications')
    ax.set_title('Number of Shakspearean Books published in each Period of Ten Years from 1591 to 1830 inclusive')
    ax.legend()
    # subtler background
    ax.set_facecolor('whitesmoke')
    fig.patch.set_facecolor('whitesmoke')
    st.pyplot(fig)







