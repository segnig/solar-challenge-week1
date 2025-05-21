import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import load_data, compute_summary

# Page settings
st.set_page_config(page_title="Solar Insights Dashboard", layout="wide", initial_sidebar_state="expanded")
st.title("☀️ Cross-Country Solar Energy Comparison")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("🔧 Filter Options")
metrics = st.sidebar.multiselect(
    "Select Solar Metrics to Display:",
    options=["GHI", "DNI", "DHI"],
    default=["GHI", "DNI", "DHI"]
)

# Conditional check
if not metrics:
    st.warning("Please select at least one metric to visualize.")
    st.stop()

# Boxplots
st.subheader("📦 Boxplots of Solar Metrics")
fig, axes = plt.subplots(1, len(metrics), figsize=(6 * len(metrics), 5))
if len(metrics) == 1:
    axes = [axes]  # Make it iterable

for i, metric in enumerate(metrics):
    sns.boxplot(data=df, x='country', y=metric, ax=axes[i], palette="Set2")
    axes[i].set_title(f"{metric} by Country")
    axes[i].set_xlabel("")
    axes[i].set_ylabel(metric)

st.pyplot(fig)

# Summary Statistics Table
st.subheader("📋 Summary Statistics Table")
summary = compute_summary(df)
st.dataframe(summary.style.format(precision=2))

# Bar Chart
st.subheader("📊 Average GHI by Country")
avg_ghi = df.groupby("country")["GHI"].mean().sort_values()
st.bar_chart(avg_ghi)

# Key Observations
st.markdown("### 🔍 Key Observations")
st.markdown("""
- 🌍 **Togo** has the highest **average GHI**, indicating strong solar potential.
- 🌩️ **Benin** shows **lowest median values** and **highest variability**, suggesting inconsistencies in solar availability.
- ⚡ **Sierra Leone** shows a **moderate** but stable GHI range.
""")
# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Segni Girma")