# Git Directory Pusher

## Description

Git Directory Pusher is a Python application with a custom GUI that allows you to push the contents of a local directory to a GitHub repository. This tool is designed to simplify the process of initializing a Git repository, adding files, and pushing changes to GitHub. It includes a modern GUI created with CustomTkinter and provides easy-to-follow instructions and feedback during the process.

## Features

- **GUI Interface**: User-friendly interface built with CustomTkinter.
- **Directory Selection**: Easily choose the directory you want to push to GitHub.
- **Repository Management**: Automatically initializes the repository and manages remote settings.
- **Commit and Push**: Adds all files, commits changes, and pushes to the specified repository.
- **Error Handling**: Displays error messages and copies them to the clipboard if something goes wrong.
- **Credits**: Includes credits to Germanized for contributions.

## Installation

1. **Clone the Repository**

git clone https://github.com/Germanized/Github-Gui-Pusher.git
or just click "code" then the "download zip"


2. ## Installing ReQ

### Requirements

The application requires the following Python packages:

- `gitpython` - For interacting with Git repositories.
- `pyperclip` - For copying error messages to the clipboard.
- `customtkinter` - For creating the modern GUI.


1. **Choose Directory**

Click on "Choose Directory" to select the local directory you want to push to GitHub.

2. **Enter Repository URL**

Provide the URL of your GitHub repository in the "Repository URL" field.

3. **Push to GitHub**

Click on "Push to GitHub" to begin the process. The application will initialize the repository, add files, commit changes, and push to the specified remote repository.

4. **View Status**

The status label will display the current status of the operation, including success or error messages.

## Troubleshooting

- **Error: Remote origin already exists**

This means that the remote `origin` is already set up for the repository. You may need to manually update or remove the remote if you encounter issues.

- **Error: Failed to push some refs**

Ensure that your local branch is up to date with the remote branch. You might need to pull changes from the remote repository before pushing.

## Credits

Germanized (me)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

