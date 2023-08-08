# Command Line Chatbot with OpenAI API

Based on script from: [Gynvael Coldwind's amazing blog](https://gynvael.coldwind.pl/?lang=en&id=771)

This repository contains a simple Python script that utilizes the OpenAI API to create a command line chatbot. The script takes a system command and its arguments as input, interacts with the GPT-3.5 Turbo model to generate a description of the command, and then prints the generated description.

## Prerequisites

Before using this script, you need to have the following:

- **Python**: Make sure you have Python installed on your system.
- **OpenAI API Key**: You need an OpenAI API key to authenticate your requests to the GPT-3.5 Turbo model.

## Usage

1. Export your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY=your-api-key

2. Run the script with the desired command and its arguments:

   ```bash
   python howto.py <system> <arguments>

   Replace `<system>` with the name of the command and `<arguments>` with the arguments you want to pass to the command.

## Example

For instance, if you want to get a description of the `ls` command, you can run:
  ```console
  python howto.py powershell list files in current directory
  ```

The script will interact with the GPT-3.5 Turbo model to generate a description of the `ls` command and its usage.

## Output

The script will print the generated command.

## Notes

- The script uses the GPT-3.5 Turbo model to generate descriptions. You can experiment with other models by modifying the `model` parameter in the script.
- The generated description may not always be accurate or up-to-date. It's important to verify the information provided.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize and extend this script to suit your needs. If you have any questions or suggestions, please feel free to create an issue or pull request in the repository.


