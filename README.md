# Kynlos Python Packager

This Python script provides functionality to package a Python project into a standalone executable using PyInstaller.

## Usage

### Using Command Line Interface (CLI)

```bash
python packager.py [-h] [-w] [path] [-d] [-o OUTPUT_DIR] [-i INCLUDE] [-a PYINSTALLER_ARGS]
                   [-n OUTPUT_NAME] [-c] [--icon ICON] [--hidden-imports HIDDEN_IMPORTS]
                   [--version VERSION] [--binaries BINARIES] [--license LICENSE]
                   [--env-vars ENV_VARS] [--python PYTHON] [--no-compress] [--hooks HOOKS]
                   [--bootloader BOOTLOADER] [--manifest MANIFEST] [--splash SPLASH]
                   [--runtime-hooks RUNTIME_HOOKS] [--exe-format {exe,directory}]
                   [--system-path SYSTEM_PATH] [--upx-level {0..9}] [--eula EULA]
                   [--spec-file SPEC_FILE] [--runtime-hook-spec RUNTIME_HOOK_SPEC]
                   [--template TEMPLATE] [--compile-pyc] [--icon-mac ICON_MAC]
                   [--package-data PACKAGE_DATA] [--build-mode BUILD_MODE]
                   [--custom-hooks CUSTOM_HOOKS] [--custom-upx CUSTOM_UPX]
                   [--bundle-stdlib] [--exclude EXCLUDE] [--bootloader-conf BOOTLOADER_CONF]
                   [--verbose] [--external-modules EXTERNAL_MODULES] [--bundled-icon BUNDLED_ICON]
                   [--temp-dir TEMP_DIR] [--upx-conf UPX_CONF] [--resource-files RESOURCE_FILES]
                   [--app-name APP_NAME] [--log-dir LOG_DIR] [--app-version APP_VERSION]
                   [--additional-files ADDITIONAL_FILES] [--user-hooks USER_HOOKS]
                   [--file-version FILE_VERSION] [--custom-library CUSTOM_LIBRARY] [--upx-path UPX_PATH]
                   [--no-confirm] [--custom-commands CUSTOM_COMMANDS] [--freeze-imports] [--clean-build]
                   [--warn-project-version] [--warn-no-version] [--name NAME]
```

### Using Wizard
```bash
python packager.py PATH -w
```

Follow the wizard prompts to guide you through the packaging process.

### Parameters

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


## Example

To package a Python project into a standalone executable using the CLI:

```bash
python packager.py "my_project.py" --icon my_icon.ico --output-dir dist --no-compress --verbose
```

This will package the my_project.py script into a standalone executable with the specified options.
