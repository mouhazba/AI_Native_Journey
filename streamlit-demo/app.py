import streamlit as st




def create_welcome_message(name, purpose):
    if name != "Mamadou":
        return "Hey, it's the awesome AI Director!"
    else:
        return f"Builders, I'm {name}! I'm here {purpose}"


st.set_page_config(page_title="Python Basics Assistant", page_icon="🐍")

st.title("🐍 Learn Python Basics with Streamlit")
st.write("This is your interactive assistant to help you learn Python step by step.")

# Menu de navigation
option = st.sidebar.selectbox("Choose a concept to learn:", [
    "Variables",
    "If Statements",
    "Data Types",
    "Mini Quiz"
])

# ----------------------------
# Section : Variables
if option == "Variables":
    st.header("📦 Python Variables")
    st.write("""
    A **variable** is like a box where you can store information.  
    In Python, you create a variable like this:
    """)
    st.code('name = "Mamadou"')
    st.write("You can use the variable later in your code:")
    st.code('print("Hello", name)')
    st.write("Hello, Mamadou")
    st.success("Try changing the values and see what happens!")

# ----------------------------
# Section : If Statements
elif option == "If Statements":
    st.header("🧠 If Statements")
    st.write("""
    An **if statement** lets you make decisions in your code.

    Example:
    """)
    st.code("""
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    """, language="python")

    st.write("👉 Python uses **indentation** (spaces) to define blocks.")

# ----------------------------
# Section : Data Types
elif option == "Data Types":
    st.header("🧪 Python Data Types")
    st.write("Python has different types of data:")
    st.markdown("""
    - `str` → Text (e.g., `"Hello"`)
    - `int` → Integer number (e.g., `10`)
    - `float` → Decimal number (e.g., `3.14`)
    - `bool` → Boolean (`True` or `False`)
    """)

    st.code("""
name = "Alice"   # str
age = 30         # int
height = 1.75    # float
is_student = False  # bool
""", language="python")

# ----------------------------
# Section : Mini Quiz
elif option == "Mini Quiz":
    st.header("🧩 Quick Quiz: Check Your Understanding")

    question = st.radio("What is the type of this value: `42`?", ["str", "int", "bool"], index=None, key="q1")

    if question is not None:
        if question == "int":
            st.success("✅ Correct!")
        else:
            st.error("❌ Try again. `42` is an integer.")
    else:
        st.info("🕵️ Please select an answer above.")

    question2 = st.radio("What does this return: `5 > 3`?", ["True", "False", "Error"], index=None, key="q2")

    if question2 is not None:
        if question2 == "True":
            st.success("✅ That's right!")
        else:
            st.error("❌ Nope. `5 > 3` means '5 is greater than 3' → True")
    else:
        st.info("🕵️ Please select an answer above.")


# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")


if st.button("Generate Welcome Message"):
    message = create_welcome_message('Mamadou', 'I am to become a biggest AI Director')
    st.success(message)