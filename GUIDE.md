# Kynlos Python Packager User Guide

The Kynlos Python Packager is a tool designed to package Python projects into standalone executable files using PyInstaller. This guide provides instructions on how to use the packager effectively.

## Getting Started

1. **Installation**: Ensure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/).

2. **Download Packager**: Clone or download the Kynlos Python Packager from the repository.

3. **Install Dependencies**: Install the required dependencies by running `pip install -r requirements.txt` in the packager directory.

## Usage

### Command Line Interface (CLI)

To use the Kynlos Python Packager via the command line interface:

```bash
python packager.py [options]
```

Replace `[options]` with the desired parameters and flags outlined below.

### Wizard

Alternatively, you can use the interactive wizard to guide you through the packaging process:

```bash
python packager.py -w
```

Follow the prompts to configure your packaging settings.

## Parameters and Options

The Kynlos Python Packager supports various parameters and options to customize the packaging process. Here's a summary of the available options:

- `-w`, `--wizard`: Launches a wizard to guide you through the packaging process.
- `path`: Path to the Python project directory.
- `-d`, `--directory`: Flag to indicate if the path is a directory.
- `-o`, `--output-dir`: Output directory for the packaged executable.
- `-i`, `--include`: Additional files or directories to include in the package (format: `source_path:destination_path`).
- `-a`, `--pyinstaller-args`: Additional arguments to PyInstaller.
- `-n`, `--output-name`: Custom name for the output executable.
- `-c`, `--clean`: Clean build and dist directories before packaging.
- `--icon`: Icon file for the executable.
- `--hidden-imports`: Additional hidden imports.
- `--version`: Version information for the executable.
- `--binaries`: Additional binaries or data files to include.
- `--license`: Custom license file for the packaged executable.
- `--env-vars`: Environment variables for the packaged executable (comma-separated).
- `--python`: Custom Python interpreter to bundle with the executable.
- `--no-compress`: Disable compression of bundled files.
- `--hooks`: Additional PyInstaller hooks.
- `--bootloader`: Custom bootloader file.
- `--manifest`: Custom manifest file.
- `--splash`: Splash screen file.
- `--runtime-hooks`: Runtime hooks file.
- `--exe-format`: Specify whether to generate a single executable (`exe`) or a directory with bundled files (`directory`).
- `--system-path`: Additional paths to include in the system PATH environment variable.
- `--upx-level`: Specify the UPX compression level.
- `--eula`: End User License Agreement (EULA) file.
- `--spec-file`: Custom PyInstaller spec file.
- `--runtime-hook-spec`: Custom runtime hook specification.
- `--template`: Custom template directory for PyInstaller.
- `--compile-pyc`: Compile Python files into bytecode (.pyc) files.
- `--icon-mac`: Custom icon for the packaged executable on macOS.
- `--package-data`: Additional package data files.
- `--build-mode`: Specify whether to generate a debug or release build.
- `--custom-hooks`: Custom hooks directories.
- `--custom-upx`: Custom UPX binary.
- `--bundle-stdlib`: Bundle the standard library into the executable.
- `--exclude`: Custom exclusion patterns for file/directory inclusion.
- `--bootloader-conf`: Custom bootloader configuration file.
- `--verbose`: Enable verbose output during the packaging process.
- `--external-modules`: External Python modules.
- `--bundled-icon`: Custom icon for the bundled files on Windows.
- `--temp-dir`: Custom location for the PyInstaller temporary directory.
- `--upx-conf`: Custom UPX configuration file.
- `--resource-files`: Additional resource files.
- `--app-name`: Custom app name for macOS bundles.
- `--log-dir`: Custom output directory for logs.
- `--app-version`: Custom version number for the bundled application.
- `--additional-files`: Additional files to be included in the application bundle.
- `--user-hooks`: Custom path for user hooks.
- `--file-version`: Custom file version for the bundled executable.
- `--custom-library`: Custom library files.
- `--upx-path`: Custom path for UPX compression.
- `--no-confirm`: Skip confirmation prompts during packaging.
- `--custom-commands`: Additional custom commands for PyInstaller.
- `--freeze-imports`: Freeze imports and disable packing.
- `--clean-build`: Clean build directories before packaging.
- `--warn-project-version`: Enable warnings for project version mismatches.
- `--warn-no-version`: Enable warnings for missing version information.
- `--name`: Custom name for the packaged executable.

For a complete list of options and usage examples, refer to the [CLI usage](#using-command-line-interface-cli) section.

## Example

To package a Python project into a standalone executable with custom settings:

```bash
python packager.py my_project.py --icon my_icon.ico --output-dir dist --no-compress --verbose
```

This command packages the `my_project.py` script into a standalone executable with the specified options.

## Troubleshooting

If you encounter any issues or errors during the packaging process, refer to the [troubleshooting guide](#troubleshooting) in the documentation for possible solutions.

---

This user guide provides a brief overview of the Kynlos Python Packager and its usage. For more detailed instructions and advanced configurations, consult the documentation included with the packager.

If you have any further questions or need assistance, feel free to reach out to the packager's support team.

Happy packaging!

