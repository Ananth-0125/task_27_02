import streamlit as st

st.title("Simple Course Registration")

# Simple Course Data
courses = {
    "CSE101": {"name": "Python", "fee": 5000, "seats": 2},
    "ECE201": {"name": "Digital Circuits", "fee": 4000, "seats": 1}
}

# Initialize storage
if "registrations" not in st.session_state:
    st.session_state.registrations = []

if "seat_count" not in st.session_state:
    st.session_state.seat_count = {code: 0 for code in courses}


menu = st.sidebar.selectbox("Menu", ["Register", "View All", "Revenue"])


# ---------------- REGISTER ----------------
if menu == "Register":

    st.header("Register Student")

    name = st.text_input("Student Name")
    roll = st.number_input("Roll Number", min_value=1, step=1)
    course_code = st.selectbox("Select Course", list(courses.keys()))

    if st.button("Register"):
        if name == "":
            st.error("Enter Name")
        else:
            if st.session_state.seat_count[course_code] < courses[course_code]["seats"]:

                st.session_state.registrations.append({
                    "name": name,
                    "roll": roll,
                    "course": courses[course_code]["name"],
                    "fee": courses[course_code]["fee"]
                })

                st.session_state.seat_count[course_code] += 1

                st.success("Registered Successfully!")

            else:
                st.warning("No seats available!")


# ---------------- VIEW ALL ----------------
elif menu == "View All":

    st.header("All Registrations")

    if st.session_state.registrations:
        st.table(st.session_state.registrations)
    else:
        st.info("No students registered yet.")


# ---------------- REVENUE ----------------
elif menu == "Revenue":

    st.header("Total Revenue")

    total = sum(r["fee"] for r in st.session_state.registrations)

    st.success(f"Total Revenue: ₹{total}")