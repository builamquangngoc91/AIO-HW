import streamlit as st

st.title('My project')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('AI Viet Nam')
st.caption('This is a caption')


st.divider()

st.markdown('# Heading 1')
st.markdown('[AI VIET NAM](https://aivietnam.ai/)')
st.markdown("""
    1. Machine Learning
    2. Deep Learning
""")
st.markdown(r'$ \sqrt{2x} $')

st.divider()

st.latex(r'\sqrt{2x}')

st.divider()

st.write('AI Viet Nam')
st.write("Heading 1")
st.write("[Google](https://www.google.com)")
st.write(r'$ \sqrt{2x} $')
st.write('1 + 1 = ', 2)

st.divider()
st.code("""
    import random
    value = random.randint(3, 10)
    print(value)
""")

def get_year():
    return '19'

with st.echo():
    st.write('This is a text')
    def get_name():
        return 'Thai'
    
    name = get_name()
    year = get_year()
    st.write(name, year)


st.divider()


st.logo('./source/logo.png')

st.image('./source/dogs.jpeg', caption='Funny dogs.')

st.audio('./source/audio.mp4')

st.video('./source/video.mp4')


st.divider()

def on_change():
    print('Changed')

agree = st.checkbox('I agree', on_change=on_change)
if agree:
    st.write('You agreed!')

color = st.radio('You Favorite Color', ['Yellow', 'Blue'], captions=['Vàng', 'Xanh'])
print(color)

status = st.selectbox('Your Contact', ['Email', 'Address'])
print(status)

options = st.multiselect('Colors:', ['Green', 'Yellow', 'Blue'])
print(options)

st.select_slider('Your Colors:', [0, 1, 2])

st.divider()

if st.button('Say Hello'):
    st.write('Hello')
else:
    st.write('Goodbye')

your_name = st.text_input('Your name:', value='Thai')
st.write('Your name:', your_name)

st.divider()

uploaded_files = st.file_uploader('Choose files:', accept_multiple_files=True)
for uploaded_file in uploaded_files:
    read_f = uploaded_file
    st.write("File Name:", uploaded_file.name)

st.divider()

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

with st.form("my form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('Name:')
    f_age = col2.text_input('Age:')

    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write(f'Name: {f_name}, Age: {f_age}')

st.divider()

# section

import random
value = random.randint(1, 10)
if 'key' not in st.session_state:
    st.session_state.key = value
    st.session_state.email = value
    st.session_state.password = value

st.write('Value:', st.session_state.key)
st.write('Email:', st.session_state)