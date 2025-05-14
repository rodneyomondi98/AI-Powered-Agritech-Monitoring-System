# 📘 Interactive STEM Learning Platform: Mathematics Module  
**A Google Colab-based interactive learning tool for linear functions**  

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter" alt="Jupyter">
  <img src="https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab" alt="Colab">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</div>

## 🌟 Overview
An interactive mathematics module that teaches linear functions through:  
✅ **Dynamic visualizations** (real-time graphing)  
✅ **Hands-on experimentation** (adjustable parameters)  
✅ **Self-assessment quizzes** (instant feedback)  
✅ **Theory + Practice integration**  

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/repo/blob/main/notebook.ipynb)

## 🧮 Core Features
### 📊 Interactive Graphing Tool
```python
def plot_linear(slope, intercept):
    x = np.linspace(-10, 10, 100)
    plt.plot(x, slope*x + intercept)

    What is the slope in y = 4x + 1?  
A) 1  
B) 4  
C) x  
