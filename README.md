# 📘 Interactive STEM Learning Platform: Mathematics Module

Welcome to the **Interactive STEM Learning Platform** focused on Mathematics, specifically **Linear Functions**. This project is developed using **Google Colab** and Python with interactive widgets and visualizations to enhance conceptual understanding in a fun and engaging way.

---

## 🎯 Objective

This module aims to:
- Introduce the concept of **linear functions**.
- Allow learners to **interactively explore** the effect of changing slope and intercept on a graph.
- Reinforce understanding with a **built-in quiz**.

---

## 🧰 Technologies & Libraries Used

- **Google Colab** – for interactive and collaborative coding.
- **Python** – core programming language.
- **NumPy** – for efficient mathematical operations.
- **Matplotlib** – for plotting graphs.
- **ipywidgets** – for interactive sliders and buttons.
- **IPython.display** – for rendering rich content like Markdown.

---

## 🧠 Lesson Covered: Linear Functions

### 📖 What is a Linear Function?

A linear function is a function that can be written in the form:

\[
y = mx + b
\]

Where:
- \( m \) is the **slope** (rise over run)
- \( b \) is the **y-intercept** (where the line crosses the y-axis)

This lesson provides a **visual exploration** of how different values of slope and intercept affect the graph of a linear function.

---

## 🧪 Interactive Features

### 🎛 Real-Time Graph Plotting

You can change the slope and intercept using the sliders:

- **Slope Slider**: Adjust from -5 to 5 (step of 0.5)
- **Intercept Slider**: Adjust from -10 to 10 (step of 1)

As you move the sliders, the graph updates automatically to reflect:

- The **line equation** based on current values.
- A **matplotlib-rendered** graph showing the line and axes.

### ❓ Quiz Section

To reinforce learning, a simple multiple-choice quiz is included:

- **Question**: What is the slope of the line \( y = 3x + 2 \)?
- **Options**: "1", "2", "3", "5"
- Upon submission, the quiz provides **immediate feedback** indicating correct or incorrect answers.

---

## 🚀 How to Run This Notebook

1. Open the notebook in **Google Colab**.
2. Make sure you have the necessary libraries installed:

   Uncomment and run this cell if needed:
   ```python
   # !pip install ipywidgets matplotlib numpy
