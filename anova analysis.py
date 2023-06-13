import streamlit as st
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


def calculate_anova_table(df):
    # Menampilkan ANOVA analisis menggunakan statsmodels
    model = ols('Dependent ~ Independent', data=df).fit()
    anova_table = anova_lm(model)

    return anova_table

def main_title():
    st.title("ANOVA Analysis")

def data_input_section():
    dependent_input = st.text_area("Dependent Variable (comma-separated)", "")
    independent_input = st.text_area("Independent Variable (comma-separated)", "")
    return dependent_input, independent_input
    
def perform_anova(dependent, independent):
    # Mengkonversi data ke DataFrame
    df = pd.DataFrame({'Dependent': dependent, 'Independent': independent})

    # Menampilkan ANOVA analisis
    anova_table = calculate_anova_table(df)
    return anova_table

def display_results(anova_table, alpha):
    st.header("ANOVA Result")
    st.write("ANOVA Table:")
    st.dataframe(anova_table)

    f_value = anova_table['F'][0]
    p_value = anova_table['PR(>F)'][0]
    st.write("F-Value:", f_value)
    st.write("p-value:", p_value)

    if p_value < alpha :
        st.write("Decision: Reject H0")
    else:
        st.write("Decision: Fail to reject H0")

def main():
    main_title()
    dependent_input, independent_input = data_input_section()
    
    alpha = st.number_input("Enter alpha value:")
    
    if st.button("Perform ANOVA"):
        if dependent_input and independent_input:
            dependent = [float(x.strip()) for x in dependent_input.split(",")]
            independent = [float(x.strip()) for x in independent_input.split(",")]
            anova_table = perform_anova(dependent, independent)
            display_results(anova_table, alpha)
        else:
            st.error("Please enter data for both dependent and independent variables.")

if __name__ == "__main__":
    main()
