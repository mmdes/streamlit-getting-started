import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
pre = left_column.button('Press me!')

if pre:
    print('o botão foi pressionado com sucesso!')


# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")