# pages/Interview.py
import streamlit as st
import json
import random

def run_interview():
    # Load question bank
    with open("question_bank.json", "r") as f:
        qbank = json.load(f)

    field = st.session_state.get("field")
    level = st.session_state.get("level")

    if not field or not level:
        st.error("Please select field and experience first.")
        return

    if "questions" not in st.session_state:
        pool = qbank[field][level]
        st.session_state.questions = random.sample(pool, 5)
        st.session_state.answers = [""] * 5
        st.session_state.idx = 0
        st.session_state.correct_count = 0

    idx = st.session_state.idx
    question = st.session_state.questions[idx]

    st.header(f"Question {idx+1} of 5")
    st.write(question)

    answer = st.text_area("Your Answer:", value=st.session_state.answers[idx], key=f"ans_{idx}")

    # Simple keyword check system
    keywords = {
        "Artificial Intelligence": {
            "supervised": ["label", "training", "input", "output"],
            "overfitting": ["train", "test", "generalize"],
            "neural network": ["layers", "neurons", "weights"],
            "cnn": ["convolution", "image"],
            "rnn": ["sequence", "time", "memory"],
        },
        "Web Development": {
            "html": ["tag", "markup"],
            "css": ["style", "design"],
            "api": ["connect", "data", "request"],
            "frontend": ["ui", "browser"],
            "backend": ["server", "database"],
        },
        "Game Development": {
            "engine": ["unity", "unreal", "framework"],
            "sprite": ["2d", "image"],
            "physics": ["gravity", "collision"],
            "3d": ["model", "render"],
            "ai": ["npc", "behavior"],
        }
    }

    def check_answer(ans, q):
        f = field
        for key, words in keywords.get(f, {}).items():
            if key in q.lower():
                for w in words:
                    if w in ans.lower():
                        return True
        return False

    # Button handling
    if idx < 4:
        if st.button("Next"):
            st.session_state.answers[idx] = answer
            if check_answer(answer, question):
                st.session_state.correct_count += 1
            st.session_state.idx += 1
            st.experimental_rerun()
    else:
        if st.button("Complete"):
            st.session_state.answers[idx] = answer
            if check_answer(answer, question):
                st.session_state.correct_count += 1

            st.subheader("Final Result")
            st.write(f"Total Correct: {st.session_state.correct_count}/5")

            if st.session_state.correct_count >= 3:
                st.success("✅ Congratulations! You're eligible.")
            else:
                st.error("❌ Sorry, try next time.")

            if st.button("Restart"):
                for k in ["questions", "answers", "idx", "correct_count"]:
                    if k in st.session_state:
                        del st.session_state[k]
                st.session_state.page = "field"
                st.experimental_rerun()
