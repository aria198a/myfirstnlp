import streamlit as st
import ollama

def main():
    st.title("My First NLP")

    #設置用戶對話框
    user_input = st.text_area("您想問甚麼?","")

    #當使用者按下送出按鈕後處理
    if st.button("送出"):
        if user_input:
            #使用ollama模型，進行對話
            response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': user_input}])

            #回答
            st.text("回答:")
            st.write(response['message']['content'])
        else:
            st.warning("請輸入問題!")

if __name__ == "__main__":             
    main()   