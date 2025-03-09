import streamlit as st

st.set_page_config(page_title="Text Analyzer", layout="wide")
st.title("Text Analyzer")
st.write("Enter a paragraph to analyze its properties")

# User input
text_input = st.text_area("Enter your text here:", height=200)

st.subheader("Search and Replace")
search_word = st.text_input("Enter word to search:")
replace_word = st.text_input("Enter word to replace with:")

# Validate input
if st.button("Analyze Text"):
    if not text_input.strip():
        st.error("Please enter some text to analyze.")
    else:
        # Create columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Basic Statistics")
            
            # Word count
            words = text_input.split()
            word_count = len(words)
            
            # Character count
            char_count = len(text_input)
            
            vowels = "aeiouAEIOU"
            vowel_count = sum(1 for char in text_input if char in vowels)
            
            word_count_str = str(word_count)
            char_count_str = str(char_count)
            vowel_count_str = str(vowel_count)
            
            st.info(f"Word Count: {word_count_str}")
            st.info(f"Character Count: {char_count_str}")
            st.info(f"Vowel Count: {vowel_count_str}")
            if word_count > 0:
                avg_word_length = char_count / word_count
                st.info(f"Average Word Length: {avg_word_length:.2f} characters")
        with col2:
            st.subheader("Text Transformations")
            st.write("**Uppercase Version:**")
            st.code(text_input.upper())
            
            st.write("**Lowercase Version:**")
            st.code(text_input.lower())
            st.subheader("Search and Replace Results")
            if search_word:
                occurrences = text_input.lower().count(search_word.lower())
                
                if occurrences > 0:
                    st.write(f"Found {occurrences} occurrence(s) of '{search_word}'")
                    if replace_word:
                        modified_text = text_input.replace(search_word, replace_word)
                        st.write("**Modified Text:**")
                        st.code(modified_text)
                        st.success(f"Replaced all occurrences of '{search_word}' with '{replace_word}'")
                    else:
                        st.info("Enter a replacement word to see the modified text")
                else:
                    st.warning(f"No occurrences of '{search_word}' found in the text")
            else:
                st.info("Enter a search word to find and replace text")
st.markdown("---")
st.write("This text analyzer helps you understand the properties of your text including word count, character count, and more.")
st.write("Made By Mussawir Sohail ")
