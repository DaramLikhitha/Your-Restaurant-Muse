
# Restaurant Name and Menu Generator

This Streamlit-based project generates a restaurant name and menu items based on the selected cuisine using Large Language Models (LLMs) and the LangChain framework with sequential chains.

## Overview

The application leverages advanced natural language processing capabilities to create unique restaurant names and corresponding menu items. By selecting a specific cuisine, users can receive tailored suggestions for their restaurant concepts.

## Features

- **Cuisine Selection**: Choose from a variety of cuisines to generate a themed restaurant name and menu.
- **Restaurant Name Generation**: Get a unique and creative name for your restaurant based on the selected cuisine.
- **Menu Item Generation**: Receive a list of menu items that align with the chosen cuisine.
- **Sequential Chains**: Utilize the power of LangChain to ensure coherent and contextually accurate generation of names and menus.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/DaramLikhitha/Your-Restaurant-Muse.git
    cd "Your-Restaurant-Muse/restaurant recommendation"
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the Streamlit app, run the following command in your terminal:
```sh
streamlit run restaurant.py
```

Once the app is running, follow these steps:

1. **Select Cuisine**: Choose your preferred cuisine from the dropdown menu.
2. **Generate Name and Menu**: Click on the 'Generate' button to receive a restaurant name and a list of menu items.

## Project Structure

- `restaurant.py`: The main application file containing the Streamlit app code.
- `res_langchain.py`: Defines the sequential chains using LangChain for generating names and menus.
- `requirements.txt`: A list of Python packages required to run the application.
- `README.md`: Project documentation.

## Dependencies

- **Streamlit**: For building the interactive web application.
- **LangChain**: Framework for building applications with LLMs.
- **OpenAI**: API for accessing advanced language models.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## Acknowledgements

- Special thanks to the developers of Streamlit and LangChain for their powerful tools.
- Thanks to OpenAI for providing the language models that make this project possible.

