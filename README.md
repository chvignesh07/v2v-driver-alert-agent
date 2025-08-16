# v2v-driver-alert-agent
An AI agent prototype for V2V communication and driver alerts.
## Overview
This project is an AI agent prototype designed to improve road safety by processing Vehicle-to-Vehicle (V2V) messages. The agent acts as an intelligent co-pilot, analyzing real-time data to provide timely and context-aware alerts to the driver.

## Features
- **Data Perception:** Processes dynamic sensor data including distance to obstacles, vehicle speed, and unstructured text messages about road hazards.
- **Contextual Planning:** Uses a multi-layered decision model to choose from a range of actions (e.g., `REDUCE SPEED`, `BRAKE HARD`, `MAINTAIN CAUTION`).
- **Unit Consistency:** The agent's logic is calibrated to ensure consistent unit usage (km/h and mph).
- **AI-Powered Development:** A core part of the development process involved using prompt engineering with Gemini AI Pro to accelerate code generation and refinement.

## How to Run the Prototype
To run this prototype, you will need Python 3 installed.
1. Save the `simple_v2v_agent.py` file to your local machine.
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the script using the following command:
   `python3 simple_v2v_agent.py`
4. Press `Ctrl + C` in the terminal to stop the simulation.

## Outputs

*An attached file in this repository provides the full, raw terminal output.*

---
_This project was completed as part of a capstone program. The code is a functional prototype and not intended for production use._
