import pathlib
from typing import List

from PIL import Image
import streamlit as st


def main():
    st.markdown("# Data visualization tool using Streamlit")

    st.title('My first app')

    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')

    st.sidebar.button('Hit me')
    st.checkbox('Check me out')
    st.radio('Radio', [1,2,3])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1,'2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.color_picker('Pick a color')

    # st.balloons()
    st.error('Error message')
    st.warning('Warning message')
    st.info('Info message')
    st.success('Success message')
    st.spinner()

    option = st.sidebar.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))
    st.sidebar.write('You selected:', option)

    test = st.sidebar.multiselect('Multiselect2', [1,2,3])
    st.sidebar.write('You selected:', test)


if __name__ == "__main__":
    main()