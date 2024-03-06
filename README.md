# Kynlos Python Packager

Kynlos Python Packager is a powerful tool crafted to streamline the process of packaging Python projects into standalone executables. Leveraging the capabilities of PyInstaller, this script empowers developers to bundle their Python applications and scripts into self-contained executables, eliminating the need for users to install Python or any dependencies.

## Key Features:

1. **Versatile Packaging Options:** Kynlos Python Packager offers both command-line interface (CLI) and wizard-based packaging options, catering to users with varying preferences and levels of expertise. Whether you prefer fine-grained control through the CLI or a guided experience with the wizard, Kynlos Python Packager has you covered.

2. **Extensive Customization:** With a plethora of customizable options, users can tailor the packaging process to their specific project requirements. From specifying additional files and directories to including custom icons and license files, the script provides flexibility to accommodate diverse project needs.

3. **Platform Agnostic:** Whether you're developing applications for Windows, macOS, or Linux, Kynlos Python Packager ensures cross-platform compatibility by generating executables that can run seamlessly on different operating systems. This enables developers to reach a wider audience without worrying about platform-specific issues.

4. **Automatic Dependency Resolution:** Kynlos Python Packager automatically resolves and bundles dependencies required by the packaged Python project, ensuring that the executable remains self-contained and portable. This simplifies distribution and deployment, as users no longer need to manually install dependencies.

5. **Comprehensive Documentation:** To facilitate ease of use, the script comes with comprehensive documentation that explains each parameter, option, and customization feature in detail. Whether you're a novice user or an experienced developer, the documentation serves as a valuable resource for understanding and harnessing the full potential of Kynlos Python Packager.

## Getting Started:

To begin using Kynlos Python Packager, simply clone the repository and follow the instructions provided in the README. Whether you're packaging a simple Python script or a complex application, the script's intuitive interface and extensive customization options make the packaging process a breeze.

# Usage

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


## Examples

To package a Python project into a standalone executable using the CLI:

```bash
python package.py "\path\to\my_project.py" --icon my_icon.ico --output-dir dist --no-compress --verbose
```

With more options:

```bash
python package.py -d "\path\to\my_project" \
    --output-dir dist \
    --no-compress \
    --verbose \
    --icon my_icon.ico \
    --hidden-imports pandas \
    --env-vars "KEY=VALUE,ANOTHER_KEY=ANOTHER_VALUE" \
    --additional-files "data_folder:data_folder" \
    --upx-level 9 \
    --custom-commands="--add-data 'resource_folder:resource_folder' --exclude '__pycache__'" \
    --name NAME \
    --custom-upx C:\path\to\custom_upx.exe \
    --bundle-stdlib \
    --clean-build \
    --warn-project-version \
    --warn-no-version \
    --app-version 1.0 \
    --file-version 1.0 \
    --no-confirm
```

(Single line)

```bash
python package.py -d "\path\to\my_project" --output-dir dist --no-compress --verbose --icon my_icon.ico --hidden-imports pandas --env-vars "KEY=VALUE,ANOTHER_KEY=ANOTHER_VALUE" --additional-files "data_folder:data_folder" --upx-level 9 --custom-commands="--add-data 'resource_folder:resource_folder' --exclude '__pycache__'" --name NAME --custom-upx C:\path\to\custom_upx.exe --bundle-stdlib --clean-build --warn-project-version --warn-no-version --app-version 1.0 --file-version 1.0 --no-confirm
```

This will package the my_project.py script into a standalone executable with the specified options.
