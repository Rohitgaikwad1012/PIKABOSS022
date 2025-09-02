import streamlit as st
import random
import datetime

# ------------------- SIDEBAR MENU -------------------
st.sidebar.title("֎ ℙ𝕀𝕂𝔸𝔹𝕆𝕊𝕊 ")

# (Your functions remain the same – DO NOT delete them)

# ------------------- CSS Styling -------------------
st.markdown("""
<style>
    div[data-testid="stSidebar"] .stRadio > label {font-weight:bold;}
    div[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label div[data-testid="stMarkdownContainer"] {
        background-color:#007BFF; color:white; padding:6px 10px; border-radius:8px; margin:2px 0;
    }
</style>
""", unsafe_allow_html=True)
def calculator_ui():
    st.header("🧮 Calculator")
    num1 = st.number_input("Num 1", value=0)
    num2 = st.number_input("Num 2", value=0)
    op = st.selectbox("Operation", ["+", "-", "*", "/", "%", "//"])
    if st.button("Calculate"):
        try:
            if op == "+":
                st.success(f"ANS: {num1 + num2}")
            elif op == "-":
                st.success(f"ANS: {num1 - num2}")
            elif op == "*":
                st.success(f"ANS: {num1 * num2}")
            elif op == "/":
                st.success(f"ANS: {num1 / num2}")
            elif op == "%":
                st.success(f"ANS: {num1 % num2}")
            elif op == "//":
                st.success(f"ANS: {num1 // num2}")
        except Exception as e:
            st.error(e)


def even_odd_ui():
    st.header("🔢 Even / Odd Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        num = st.number_input("Enter a number", value=0, step=1)
        if st.button("Check"):
            st.success(f"{num} is Even" if num % 2 == 0 else f"{num} is Odd")
        st.markdown('</div>', unsafe_allow_html=True)


def simple_interest_ui():
    st.header("💰 Simple Interest Calculator")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        p = st.number_input("Principal", value=0.0)
        r = st.number_input("Rate (%)", value=0.0)
        t = st.number_input("Time (years)", value=0.0)
        if st.button("Calculate SI"):
            SI = (p * r * t) / 100
            st.success(f"Simple Interest: {SI}")
        st.markdown('</div>', unsafe_allow_html=True)


def bmi_ui():
    st.header("💪 Body Mass Index (BMI)")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        weight = st.number_input("Weight (kg)", value=0)
        height_ft = st.number_input("Height (ft)", value=0.0)
        if st.button("📊 Check BMI"):
            height_m = height_ft * 0.3048
            BMI = weight / (height_m ** 2) if height_m > 0 else 0
            st.write(f"BMI: {BMI:.2f}")
            if 16.0 <= BMI <= 16.9:
                st.warning("🧍Moderate Underweight")
            elif 17.0 <= BMI <= 18.4:
                st.warning(" 🚶‍♂️ Mild Underweight")
            elif 18.5 <= BMI <= 24.9:
                st.success("💪Normal Weight")
            elif 25.0 <= BMI <=29.0:
                st.success("🧍‍♂️📈Overweight")
            elif BMI >= 30.0:
                st.error("⚠️ Alert! Obese")
        else:
            st.write("TRY AGAIN!")
        st.markdown('</div>', unsafe_allow_html=True)


def guess_number_with_friend_ui():
    st.header("🎯 Guess Number With Friend 🧑‍🤝‍🧑")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        secret_number = st.number_input(
            "Player 1: Enter secret number", min_value=1, max_value=10, step=1)
        guess = st.number_input("Player 2: Guess number",
                                min_value=1, max_value=10, step=1)
        if st.button("Check Guess"):
            st.success("Correct! ✅" if guess ==
                       secret_number else "  Wrong guess! ❌, try again.")
        st.markdown('</div>', unsafe_allow_html=True)


def range_function_ui():
    st.header("🔢 Range Function Printer")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        start = st.number_input("Start", value=0)
        end = st.number_input("End", value=10)
        if st.button("Print Range"):
            st.write(list(range(start, end+1)))
        st.markdown('</div>', unsafe_allow_html=True)


def reverse_ui():
    st.header("🔄 Reverse String")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        text = st.text_input("Enter string to reverse")
        if st.button("Reverse"):
            st.write(text[::-1])
        st.markdown('</div>', unsafe_allow_html=True)


def prime_checker_ui():
    st.header("🔢 Prime Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        num = st.number_input("Enter number", value=2, step=1)
        if st.button("Check Prime"):
            if num < 2:
                st.subheader(f"{num} is not prime")
            else:
                if(all(num % i != 0 for i in range(2, int(num**0.5)+1))):
                    st.subheader(f"{num} is prime number") 
                else :
                    st.subheader(f"{num} is not prime number ")
        else:
            st.write(" ")
        st.markdown('</div>', unsafe_allow_html=True)


def leap_year_ui():
    st.header("📅 Leap Year Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        year = st.number_input("Enter year", value=2025, step=1)
        if st.button("Check"):
            if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                st.subheader(f"{year} is a leap year") 
            else:
                st.subheader(f"{year} is not a leap year")
        st.markdown('</div>', unsafe_allow_html=True)
        



def guess_against_computer_ui():
    st.header(" 🤖 Guess Number Against Computer")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        guess = st.number_input(
            "Enter guess 1-10", min_value=1, max_value=10, step=1)
        comp_num = random.randint(1, 10)
        if st.button("Check"):
            st.write("computer checking..")
            
            if guess == comp_num:
                st.subheader(f"🎉 Correct! Computer number was {comp_num}")
            else :
                st.subheader(f"❌ Wrong! Computer number was {comp_num}")
        st.markdown('</div>', unsafe_allow_html=True)


def number_reverse_ui():
    st.header("🔢 Sum of Digits")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        num = st.number_input("Enter number", value=0, step=1)
        if st.button("Calculate"):
            total = sum(int(d) for d in str(num))
            st.success(f"Sum of digits: {total}")
        st.markdown('</div>', unsafe_allow_html=True)


def strong_password_ui():
    st.header("🔐 Strong Password Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        password = st.text_input("Enter password")
        special_chars = "@#!$&*"
        if st.button("Check"):
            if (len(password) > 8 and any(c.isupper() for c in password) and any(c.islower() for c in password)
                    and any(c.isdigit() for c in password) and any(c in special_chars for c in password)):
                st.subheader("STRONG PASSWORD ✅")
            else:
                st.write("Password must contain at least 8 characters, one uppercase, one lowercase, one digit, and one special character.")
                st.subheader("WEAK PASSWORD ❌")

        st.markdown('</div>', unsafe_allow_html=True)


def grocery_bill_ui():
    st.header("🛒 Grocery Store Bill Maker(Distount on items above 1000 )")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        item1 = st.number_input("Item 1 price")
        item2 = st.number_input("Item 2 price")
        item3 = st.number_input("Item 3 price")
        if st.button("Generate Bill"):
            total = item1 + item2 + item3
            avg = total / 3
            tax = avg * 0.05
            grand_total = total + tax
            discount = grand_total * 0.1 if grand_total > 1000 else 0
            grand_final = grand_total - discount

            st.header("----------RECEIPT----------")
            st.write(f"▪ Total :", int(total))
            st.write(f"▪ Tax :", int(tax))
            st.write(f"▪ Grand total :", int(grand_total))
            st.write(f"▪ Discount :", int((discount)))
            st.subheader(f"GRAND TOTAL : {int(grand_final)}₹")
            st.write(" THANK YOU!!")
        st.markdown('</div>', unsafe_allow_html=True)


def celsius_fahrenheit_ui():
    st.header("🌡️ Celsius ↔ Fahrenheit Converter")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        choice = st.radio("Conversion type", ["C to F", "F to C"])
        if choice == "C to F":
            c = st.number_input("Enter Celsius")
            if st.button("Convert to F"):
                st.success(f"{(c*9/5)+32:.2f} °F")
        else:
            f = st.number_input("Enter Fahrenheit")
            if st.button("Convert to C"):
                st.success(f"{(f-32)*5/9:.2f} °C")
        st.markdown('</div>', unsafe_allow_html=True)


def table_generator_ui():
    st.header("✖️ Multiplication Table")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        num = st.number_input("Enter number", value=1)
        if st.button("Generate Table"):
            for i in range(1, 11):
                st.write(f"{num} x {i} = {num*i}")
            st.write(" THANK YOU! ")
        st.markdown('</div>', unsafe_allow_html=True)


def area_ui():
    st.header("📐 Area & Perimeter Calculator")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        shape = st.selectbox(
            "Select Shape", ["Square", "Rectangle", "Circle", "Triangle"])
        if shape == "Square":
            s = st.number_input("Side")
            if st.button("Calculate Square"):
                st.write("Area:", s*s, "Perimeter:", 4*s)
        elif shape == "Rectangle":
            l = st.number_input("Length")
            b = st.number_input("Breadth")
            if st.button("Calculate Rectangle"):
                st.write("Area:", l*b, "Perimeter:", 2*(l+b))
        elif shape == "Circle":
            r = st.number_input("Radius")
            if st.button("Calculate Circle"):
                st.write("Area:", 3.14*r*r, "Circumference:", 2*3.14*r)
        elif shape == "Triangle":
            b = st.number_input("Base")
            p = st.number_input("Perpendicular")
            h = st.number_input("Hypotenuse")
            if st.button("Calculate Triangle"):
                st.write("Area:", 0.5*b*p, "Perimeter:", b+p+h)
        st.markdown('</div>', unsafe_allow_html=True)


def factorials_ui():
    st.header("‼️ Factorial Calculator")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        num = st.number_input("Enter number", value=0, step=1)
        if st.button("Calculate Factorial"):
            fact = 1
            for i in range(1, num+1):
                fact *= i
            st.success(f"Factorial: {fact}")
        st.markdown('</div>', unsafe_allow_html=True)


def birth_checker_ui():
    st.header("🎂 Age Calculator")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        by = st.number_input("Birth Year", value=2000, step=1)
        bm = st.number_input("Birth Month", value=1, step=1)
        bd = st.number_input("Birth Day", value=1, step=1)
        if st.button("Calculate Age"):
            today = datetime.date.today()
            birthdate = datetime.date(by, bm, bd)
            age = today.year - birthdate.year - \
                ((today.month, today.day) < (birthdate.month, birthdate.day))
            st.subheader(f"Age: {age} years")
        st.markdown('</div>', unsafe_allow_html=True)


def quizzes_ui():
    st.header("❓ Quiz")
    st.write(" ✅ CORRECT ANS +10 ")
    st.write(" ❌ WRONG ANS -5")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        score = 0
        ans1 = st.text_input("1. What is the keyword used to define a function in Python?")
        ans2 = st.text_input("2. What data type is returned by input() function in Python?")
        ans3 = st.text_input("3. Which keyword is used to exit a loop prematurely?")
        ans4 = st.text_input("4. What is the output of len(Python)?")
        ans5 = st.text_input("Which built-in function is used to find the maximum value in a list?")
        if st.button("Check Quiz"):
            score += 10 if ans1.lower() == "def " else -5
            score += 10 if ans2.lower() == "str" or ans1.lower()=="string" else -5
            score += 10 if ans3.lower() == "break" else -5
            score += 10 if ans4== "6" else -5
            score += 10 if ans5.lower()=="max" else -5
            st.write(f"Score: {score}/40")
        st.markdown('</div>', unsafe_allow_html=True)


def highest_number_ui():
    st.header("🔝 Highest Number Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        number1 = st.number_input("Number 1",value=0)
        number2 = st.number_input("Number 2",value=0)
        number3 = st.number_input("Number 3",value=0)
        if st.button("Check Highest"):
            st.success(f"{max("number1","number2","number3")} : {max(number1, number2, number3)}")
        st.markdown('</div>', unsafe_allow_html=True)


def smallest_number_ui():
    st.header("🔻 Smallest Number Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        number1 = st.number_input("Number 1",value=0)
        number2 = st.number_input("Number 2",value=0)
        number3 = st.number_input("Number 3",value=0)
        if st.button("Check Smallest"):
            st.success(f"{min("number1","number2","number3")} : {min(number1,number2,number3)}")
        st.markdown('</div>', unsafe_allow_html=True)


def check_result_ui():
    st.header("📝 Result Checker (Marks)")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        sub1 = st.number_input("Marks Subject 1", 0, 100)
        sub2 = st.number_input("Marks Subject 2", 0, 100)
        sub3 = st.number_input("Marks Subject 3", 0, 100)
        if st.button("Check Result"):
            total = sub1+sub2+sub3
            percentage = total/3
            st.write(f"Total: {total}/300")
            st.write(f"Percentage: {percentage:.2f}%")
            if percentage >= 50:
                st.subheader("Result: Pass ✅")
            else:
                st.subheader("Result fail ❌")


def basic_calendar_ui():
    st.header("📅 Basic Calendar")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        days = st.number_input("Days in Month", 28, 31)
        start_day = st.number_input("Starting Weekday (1=Mon,7=Sun)", 1, 7)
        if st.button("Show Calendar"):
            cal = [str("Mon") + str("Tue")+str("Wed")+str("Thu")+str("Fri")+str("Sat")+str("Sun")]
            st.write(" ".join(cal))
            blanks = "    " * (start_day-1)
            day_line = blanks
            for d in range(1, days+1):
                day_line += f"{d:3} "
                if (d + start_day - 1) % 7 == 0:
                    st.text(day_line)
                    day_line = ""
            if day_line:
                st.text(day_line)
        st.markdown('</div>', unsafe_allow_html=True)


def palindrome_ui():
    st.header("🔁 Palindrome Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        text = st.text_input("Enter text")
        if st.button("Check Palindrome"):
            clean_text = ''.join(e.lower() for e in text if e.isalnum())
            if clean_text == clean_text[::-1]:
                st.subheader(f"'{text}' is a palindrome ✅")
            else :
                st.subheader(f"'{text}' is not a palindrome ❌")
        st.markdown('</div>', unsafe_allow_html=True)


def expenses_ui():
    st.header("💸 Expenses Checker")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        exp1 = st.number_input("Expense 1")
        exp2 = st.number_input("Expense 2")
        exp3 = st.number_input("Expense 3")
        if st.button("Calculate Expenses"):
            total = exp1+exp2+exp3
            st.write(f"Total Expenses: {total}")
        st.markdown('</div>', unsafe_allow_html=True)


def sum_of_n_ui():
    st.header("🔢 Sum of N Natural Numbers")
    with st.container():
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        n = st.number_input("Enter N", 0)
        if st.button("Calculate Sum"):
            st.success(f"Sum of first {n} numbers : {n*(n+1)//2}")
        st.markdown('</div>', unsafe_allow_html=True)


def pro_voter_ui():
    st.header("🗳️ Voter Eligibility Checker")
    with st.container():
        age = st.number_input("Enter Age", 0)
        citizen = st.radio("Are you citizen of the country?", ["Yes", "No"])

        if st.button("Check Eligibility"):
            if age >= 18 and citizen == "Yes":
                st.success("✅ You are eligible to vote")
            else:
                st.error("❌ You are not eligible to vote")

    # st.header("🗳️ Voter Eligibility Checker")
    # with st.container():
    #     st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    #     age = st.number_input("Enter Age", 0)
    #     citizen = st.radio("Are you citizen of the country?", ["Yes", "No"])
    #     if st.button("Check Eligibility"):
    #         st.success(" are eligible to vote ✅ "if age >=18 and citizen == "Yes" else "You are not eligible to vote ❌")
    #     st.markdown('</div>', unsafe_allow_html=True)


def currency_converter_ui():
    st.header("💱 Currency Converter (INR ↔ USD/EUR)")
    with st.form("currency"):
        amount = st.number_input("Amount in INR", value=0.0)
        currency = st.selectbox("Convert to", ["USD", "EUR"])
        submit = st.form_submit_button("Convert")
        if submit:
            rates = {"USD": 0.012, "EUR": 0.011}  # Approx static rates
            converted = amount * rates[currency]
            st.success(f"{amount} INR = {converted:.2f} {currency}")

# ------------------- CATEGORIES -------------------
st.sidebar.subheader(" 𓃑 MENU")

# Show menu only if no tool is selected
if "selected_tool" not in st.session_state:
    st.session_state.selected_tool = None

if st.session_state.selected_tool is None:
    # Math Tools
    with st.sidebar.expander("➕ MATHS TOOLS ", expanded=True):
        math_tools = [
            None, "Calculator", "Even / Odd", "Simple Interest", "BMI", "Range Function",
            "Reverse String", "Prime Checker", "Leap Year", "Sum of Digits",
            "Multiplication Table", "Area Calculator", "Factorials", "Highest Number",
            "Smallest Number", "Sum of N"
        ]
        selected_math = st.radio("MATH", math_tools, index=0, format_func=lambda x: "" if x is None else x)

    # Games
    with st.sidebar.expander("🎮 GAMES"):
        game_tools = [None, "Guess Number with Friend", "Guess Against Computer", "Quiz", "Palindrome"]
        selected_game = st.radio("Games", game_tools, index=0, format_func=lambda x: "" if x is None else x)

    # Utilities
    with st.sidebar.expander(" 🧩 Multi-Tool"):
        utility_tools = [
            None, "Currency_Converter", "Strong Password", "Grocery Bill", "Celsius↔Fahrenheit",
            "Age Calculator", "Result Checker", "Basic Calendar", "Expenses", "Voter Eligibility"
        ]
        selected_utility = st.radio("Utilities", utility_tools, index=0, format_func=lambda x: "" if x is None else x)

    # EXIT Button
    if st.sidebar.button("❌ 𝐄𝐗𝐈𝐓"):
        st.success("👋 Thank you for using the app!")
        st.info("✨ Have a great day! Come back soon!")
        st.info(" 🔄 PRESS CTRL+R TO RESET ")
        st.warning("⚠️ Remember to save your work before closing.")
        st.stop()

    # Update selection in session state
    if selected_math:
        st.session_state.selected_tool = selected_math
    elif selected_game:
        st.session_state.selected_tool = selected_game
    elif selected_utility:
        st.session_state.selected_tool = selected_utility

# ------------------- FEATURE MAPPING -------------------
feature_mapping = {
    # Math
    "Calculator": calculator_ui,
    "Even / Odd": even_odd_ui,
    "Simple Interest": simple_interest_ui,
    "BMI": bmi_ui,
    "Range Function": range_function_ui,
    "Reverse String": reverse_ui,
    "Prime Checker": prime_checker_ui,
    "Leap Year": leap_year_ui,
    "Sum of Digits": number_reverse_ui,
    "Multiplication Table": table_generator_ui,
    "Area Calculator": area_ui,
    "Factorials": factorials_ui,
    "Highest Number": highest_number_ui,
    "Smallest Number": smallest_number_ui,
    "Sum of N": sum_of_n_ui,

    # Games
    "Guess Number with Friend": guess_number_with_friend_ui,
    "Guess Against Computer": guess_against_computer_ui,
    "Quiz": quizzes_ui,
    "Palindrome": palindrome_ui,

    # Utilities
    "Currency_Converter": currency_converter_ui,
    "Strong Password": strong_password_ui,
    "Grocery Bill": grocery_bill_ui,
    "Celsius↔Fahrenheit": celsius_fahrenheit_ui,
    "Age Calculator": birth_checker_ui,
    "Result Checker": check_result_ui,
    "Basic Calendar": basic_calendar_ui,
    "Expenses": expenses_ui,
    "Voter Eligibility": pro_voter_ui
}

# ------------------- RENDER SELECTED TOOL -------------------
if st.session_state.selected_tool:
    tool = st.session_state.selected_tool
    if tool in feature_mapping:
        st.markdown(f"### 🔹 {tool}")
        feature_mapping[tool]()  # Run the selected feature

    # ✅ Back to Menu button
    if st.button("⬅️ Back to Menu"):
        st.session_state.selected_tool = None
        st.rerun()
