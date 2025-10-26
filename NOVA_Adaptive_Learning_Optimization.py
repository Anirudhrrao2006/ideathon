# NOVA - Adaptive Learning Optimization Simulation
# Developed as a baseline model for engagement optimization and pre-post learning analytics.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def nova_learning_simulation(num_students=10, random_seed=42):
    np.random.seed(random_seed)
    students = [f"Student_{i+1}" for i in range(num_students)]

    # Step 1: Input Parameters (E, A, F, R, V)
    E = np.random.uniform(10, 40, num_students)   # Engagement time (minutes)
    A = np.random.uniform(0.4, 0.9, num_students) # Accuracy (%)
    F = np.random.randint(5, 20, num_students)    # Interaction frequency
    R = np.random.uniform(2, 5, num_students)     # Reflection depth (1-5)
    V = np.random.randint(1, 10, num_students)    # Voice interaction count

    # Step 2: Deterministic Optimization Function
    # Learning Gain (L) = α1*E + α2*A + α3*F + α4*R + α5*V
    alpha = [0.25, 0.35, 0.15, 0.15, 0.10]  # Coefficients for each input
    L = alpha[0]*E + alpha[1]*A*100 + alpha[2]*F + alpha[3]*R + alpha[4]*V

    # Step 3: Adaptive Decision (Advance or Reinforce)
    threshold = np.mean(L)
    performance = ["Advance" if score >= threshold else "Reinforce" for score in L]

    # Step 4: Pre and Post Learning Assessment Simulation
    pre_scores = np.random.uniform(40, 60, num_students)
    post_scores = pre_scores + (L / np.max(L)) * 40  # Post gain proportional to learning gain

    # Step 5: Data Summary
    data = pd.DataFrame({
        "Student": students,
        "Engagement(E)": E.round(2),
        "Accuracy(A)%": (A*100).round(1),
        "Frequency(F)": F,
        "Reflection(R)": R.round(2),
        "Voice(V)": V,
        "Learning_Gain(L)": L.round(2),
        "Performance": performance,
        "Pre_Score": pre_scores.round(1),
        "Post_Score": post_scores.round(1),
        "Improvement(%)": ((post_scores - pre_scores)/pre_scores*100).round(1)
    })

    print("=== NOVA Adaptive Learning Optimization Simulation ===")
    print(data.to_string(index=False))

    # Step 6: Visualization of Learning Improvement
    plt.figure(figsize=(10,5))
    plt.bar(students, data["Improvement(%)"], color="royalblue")
    plt.title("Simulated Learning Improvement Across Students", fontsize=14)
    plt.ylabel("Improvement (%)")
    plt.xlabel("Student ID")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return data

if __name__ == "__main__":
    nova_learning_simulation()
