**CardioRiskCalc: A Cardiovascular Risk Assessment Tool**

**Project Description:**

CardioRiskCalc is a desktop application developed using Python's Tkinter library to assist healthcare professionals in evaluating the cardiovascular risk of patients based on specific clinical parameters. This tool calculates a composite risk score (Krs) by analyzing five critical factors, providing tailored recommendations for therapy adjustments based on the calculated risk level.

**Key Features:**

1. **User-Friendly Interface:**
   - Clean and intuitive layout using Tkinter's `ttk` widgets.
   - Responsive design that adapts to various screen sizes.

2. **Input Parameters:**
   - **Spontaneous Aggregation (SA) in %**
   - **IAAK (Arachidonic Acid Induced Aggregation) in %**
   - **VT (Mean Platelet Volume) in fl/platelet**
   - **FG (Pharmacogenetic Testing) options:**
     - 2С19*17
     - 2С19*1
     - 2С19*2/2С19*3
   - **IAADF5 (Aggregation with ADP 50 µmol) in %**

3. **Risk Calculation Logic:**
   - Each input parameter is assigned a point value based on predefined ranges.
   - The points are aggregated to compute the Krs score.
   - Risk levels are categorized, and corresponding therapeutic recommendations are provided.

4. **Dynamic Results Display:**
   - Real-time calculation and display of the risk score and recommendations.
   - Use of `ScrolledText` for displaying results, ensuring readability for longer texts.

5. **Error Handling:**
   - Input validation to ensure numerical entries, with error messages for invalid inputs.

**How It Works:**

- The user inputs the values for SA, IAAK, VT, selects the FG option, and enters the IAADF5 value.
- Upon clicking the "Рассчитать" (Calculate) button, the application computes the total points and Krs score.
- Based on the Krs score, the application provides a recommendation:
  - **Low Risk (Krs < 2):** Target hypoaggregation achieved; no therapy adjustment needed.
  - **High Risk (2 ≤ Krs ≤ 2.8):** Target hypoaggregation not achieved; therapy adjustment recommended.
  - **Very High Risk (Krs > 2.8):** Immediate therapy adjustment required due to extremely high risk of recurrent vascular events.

**Usage:**

CardioRiskCalc is designed to support cardiologists and healthcare providers in making informed decisions regarding antiplatelet therapy adjustments, ensuring optimal patient outcomes through personalized risk assessment.

**Technology Stack:**

- **Programming Language:** Python
- **GUI Framework:** Tkinter
- **Widgets Used:** `ttk.Label`, `ttk.Entry`, `ttk.Combobox`, `ttk.Button`, `ScrolledText`

**Future Enhancements:**

- Integration with electronic health records (EHR) systems for seamless data input.
- Advanced data analytics and visualization for trend analysis.
- Multilingual support to cater to a global user base.

CardioRiskCalc aims to streamline the cardiovascular risk assessment process, providing accurate and actionable insights to healthcare professionals, ultimately contributing to better patient care and management.
