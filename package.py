import argparse
import subprocess
import os
import platform

def package_project(
    selected_path, is_directory, output_dir=None, include=None, pyinstaller_args=None,
    output_name=None, clean=False, icon=None, hidden_imports=None, version=None,
    binaries=None, license=None, env_vars=None, python=None, compress=True, hooks=None,
    bootloader=None, manifest=None, splash=None, runtime_hooks=None, exe_format='exe',
    system_path=None, upx_level=None, eula=None, spec_file=None, runtime_hook_spec=None,
    template=None, compile_pyc=False, icon_mac=None, package_data=None, build_mode=None,
    custom_hooks=None, custom_upx=None, bundle_stdlib=False, exclude=None,
    bootloader_conf=None, verbose=False, external_modules=None, bundled_icon=None,
    temp_dir=None, upx_conf=None, resource_files=None, app_name=None, log_dir=None,
    app_version=None, additional_files=None, user_hooks=None, file_version=None,
    custom_library=None, upx_path=None, no_confirm=False, custom_commands=None,
    freeze_imports=None, clean_build=None, warn_project_version=None,
    warn_no_version=None, name=None
):
    """
    Package a Python project into an executable using PyInstaller.

    Parameters:
        selected_path (str): Path to the Python project directory or script file.
        is_directory (bool): Indicates whether the provided path is a directory.
        output_dir (str, optional): Output directory for the packaged executable.
        include (str, optional): Additional files or directories to include in the package.
        pyinstaller_args (str, optional): Additional arguments to PyInstaller.
        output_name (str, optional): Custom name for the output executable.
        clean (bool, optional): Clean build and dist directories before packaging.
        icon (str, optional): Icon file for the executable.
        hidden_imports (str, optional): Additional hidden imports.
        version (str, optional): Version information for the executable.
        binaries (str, optional): Additional binaries or data files to include.
        license (str, optional): Custom license file for the packaged executable.
        env_vars (str, optional): Environment variables for the packaged executable.
        python (str, optional): Custom Python interpreter to bundle with the executable.
        compress (bool, optional): Enable compression of bundled files.
        hooks (str, optional): Additional PyInstaller hooks.
        bootloader (str, optional): Custom bootloader file.
        manifest (str, optional): Custom manifest file.
        splash (str, optional): Splash screen file.
        runtime_hooks (str, optional): Runtime hooks file.
        exe_format (str, optional): Specify whether to generate a single executable ('exe') or a directory with bundled files ('directory').
        system_path (str, optional): Additional paths to include in the system PATH environment variable.
        upx_level (int, optional): Specify the UPX compression level.
        eula (str, optional): End User License Agreement (EULA) file.
        spec_file (str, optional): Custom PyInstaller spec file.
        runtime_hook_spec (str, optional): Custom runtime hook specification.
        template (str, optional): Custom template directory for PyInstaller.
        compile_pyc (bool, optional): Compile Python files into bytecode (.pyc) files.
        icon_mac (str, optional): Custom icon for the packaged executable on macOS.
        package_data (str, optional): Additional package data files.
        build_mode (str, optional): Specify whether to generate a debug or release build.
        custom_hooks (str, optional): Custom hooks directories.
        custom_upx (str, optional): Custom UPX binary.
        bundle_stdlib (bool, optional): Bundle the standard library into the executable.
        exclude (str, optional): Custom exclusion patterns for file/directory inclusion.
        bootloader_conf (str, optional): Custom bootloader configuration file.
        verbose (bool, optional): Enable verbose output during the packaging process.
        external_modules (str, optional): External Python modules.
        bundled_icon (str, optional): Custom icon for the bundled files on Windows.
        temp_dir (str, optional): Custom location for the PyInstaller temporary directory.
        upx_conf (str, optional): Custom UPX configuration file.
        resource_files (str, optional): Additional resource files.
        app_name (str, optional): Custom app name for macOS bundles.
        log_dir (str, optional): Custom output directory for logs.
        app_version (str, optional): Custom version number for the bundled application.
        additional_files (str, optional): Additional files to be included in the application bundle.
        user_hooks (str, optional): Custom path for user hooks.
        file_version (str, optional): Custom file version for the bundled executable.
        custom_library (str, optional): Custom library files.
        upx_path (str, optional): Custom path for UPX compression.
        no_confirm (bool, optional): Skip confirmation prompts during packaging.
        custom_commands (str, optional): Additional custom commands for PyInstaller.
        freeze_imports (bool, optional): Freeze imports and disable packing.
        clean_build (bool, optional): Clean build directories before packaging.
        warn_project_version (bool, optional): Enable warnings for project version mismatches.
        warn_no_version (bool, optional): Enable warnings for missing version information.
        name (str, optional): Custom name for the packaged executable.
    """
    try:
        # Construct PyInstaller command based on platform
        pyinstaller_command = ["pyinstaller"]
        if platform.system() == 'Windows':
            if exe_format == 'exe':
                pyinstaller_command.append("--onefile")
            else:
                pyinstaller_command.append("--onedir")
        elif platform.system() == 'Darwin':  # macOS
            pyinstaller_command.append("--onefile")
            pyinstaller_command.append("--osx-bundle-identifier=com.example.app")
            pyinstaller_command.append("--osx-bundle-name=AppName")
        elif platform.system() == 'Linux':
            if exe_format == 'exe':
                pyinstaller_command.append("--onefile")
            else:
                pyinstaller_command.append("--onedir")
            pyinstaller_command.append("--linux-bundle-name=AppName")

        # Append optional arguments to PyInstaller command
        if output_dir:
            pyinstaller_command.extend(["--distpath", output_dir])
        if include:
            pyinstaller_command.extend(["--add-data", include])
        if pyinstaller_args:
            pyinstaller_command.extend(pyinstaller_args.split())
        if output_name:
            pyinstaller_command.extend(["--name", output_name])
        if clean:
            pyinstaller_command.append("--clean")
        if icon:
            pyinstaller_command.extend(["--icon", icon])
        if hidden_imports:
            pyinstaller_command.extend(["--hidden-import", hidden_imports])
        if version:
            pyinstaller_command.extend(["--version-file", version])
        if binaries:
            pyinstaller_command.extend(["--add-binary", binaries])
        if license:
            pyinstaller_command.extend(["--license", license])
        if env_vars:
            for var in env_vars.split(','):
                pyinstaller_command.extend(["--set-env", var])
        if python:
            pyinstaller_command.extend(["--python", python])
        if not compress:
            pyinstaller_command.append("--noupx")
        if hooks:
            pyinstaller_command.extend(["--additional-hooks-dir", hooks])
        if bootloader:
            pyinstaller_command.extend(["--bootloader-path", bootloader])
        if manifest:
            pyinstaller_command.extend(["--manifest", manifest])
        if splash:
            pyinstaller_command.extend(["--splash", splash])
        if runtime_hooks:
            pyinstaller_command.extend(["--runtime-hook", runtime_hooks])
        if system_path:
            pyinstaller_command.extend(["--paths", system_path])
        if upx_level:
            pyinstaller_command.extend(["--upx", f"--upx-level={upx_level}"])
        if eula:
            pyinstaller_command.extend(["--eula", eula])
        if spec_file:
            pyinstaller_command.extend(["--specpath", spec_file])
        if runtime_hook_spec:
            pyinstaller_command.extend(["--runtime-hook-spec", runtime_hook_spec])
        if template:
            pyinstaller_command.extend(["--template", template])
        if compile_pyc:
            pyinstaller_command.append("--compile")
        if icon_mac:
            pyinstaller_command.extend(["--osx-bundle-icon", icon_mac])
        if package_data:
            pyinstaller_command.extend(["--package-data", package_data])
        if build_mode:
            pyinstaller_command.extend(["--mode", build_mode])
        if custom_hooks:
            pyinstaller_command.extend(["--hooks-path", custom_hooks])
        if custom_upx:
            pyinstaller_command.extend(["--upx-dir", custom_upx])
        #if bundle_stdlib:
            #pyinstaller_command.append("--no-strippython")
        if exclude:
            pyinstaller_command.extend(["--exclude", exclude])
        if bootloader_conf:
            pyinstaller_command.extend(["--bootloader-conf", bootloader_conf])
        if verbose:
            pyinstaller_command.append("--log-level=DEBUG")
        if external_modules:
            pyinstaller_command.extend(["--ext-module", external_modules])
        if bundled_icon:
            pyinstaller_command.extend(["--icon", bundled_icon])
        if temp_dir:
            pyinstaller_command.extend(["--workpath", temp_dir])
        if upx_conf:
            pyinstaller_command.extend(["--upx-conf", upx_conf])
        if resource_files:
            pyinstaller_command.extend(["--resource", resource_files])
        if app_name:
            pyinstaller_command.extend(["--appname", app_name])
        if log_dir:
            pyinstaller_command.extend(["--logfile", log_dir])
        if app_version:
            pyinstaller_command.extend(["--version", app_version])
        if additional_files:
            pyinstaller_command.extend(["--add-data", additional_files])
        if user_hooks:
            pyinstaller_command.extend(["--user-hooks", user_hooks])
        if file_version:
            pyinstaller_command.extend(["--file-version", file_version])
        if custom_library:
            pyinstaller_command.extend(["--custom-library", custom_library])
        if upx_path:
            pyinstaller_command.extend(["--upx-path", upx_path])

        if custom_commands:
            pyinstaller_command.extend(custom_commands.split())

        if freeze_imports:
            pyinstaller_command.append("--no-packing")

        if clean_build:
            pyinstaller_command.append("--clean-build")

        if warn_project_version:
            pyinstaller_command.append("--warn-project")

        if warn_no_version:
            pyinstaller_command.append("--warn-no-version")

        if name:
            pyinstaller_command.extend(["--name", name])

        # Execute PyInstaller command
        if is_directory:
            pyinstaller_command.append(selected_path)
        else:
            file_directory = os.path.dirname(selected_path)
            pyinstaller_command.extend(["--name", os.path.basename(selected_path).split(".")[0], selected_path])
            os.chdir(file_directory)

        if no_confirm:
            pyinstaller_command.append("--noconfirm")

        subprocess.run(pyinstaller_command)
        print("Project packaged successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def wizard():
    """
    Launches a wizard to guide through the process of packaging a Python project into an executable.
    """
    print("Welcome to Kynlos Python Packager Wizard!")
    print("This wizard will guide you through the process of packaging your Python project into a standalone executable.")
    selected_path = input("Enter the path to your Python script or directory: ")
    is_directory = input("Is the provided path a directory? (y/n): ").lower() == 'y'
    output_dir = input("Enter the output directory for the packaged executable (optional, press Enter to skip): ")
    include = input("Enter additional files or directories to include in the package (optional, format: source_path:destination_path, press Enter to skip): ")
    pyinstaller_args = input("Enter additional arguments for PyInstaller (optional, press Enter to skip): ")
    output_name = input("Enter a custom name for the output executable (optional, press Enter to skip): ")
    clean = input("Do you want to clean build and dist directories before packaging? (y/n): ").lower() == 'y'
    icon = input("Enter the path to the icon file for the executable (optional, press Enter to skip): ")
    hidden_imports = input("Enter additional hidden imports (optional, press Enter to skip): ")
    version = input("Enter version information for the executable (optional, press Enter to skip): ")
    binaries = input("Enter additional binaries or data files to include (optional, press Enter to skip): ")
    license = input("Enter the path to a custom license file for the packaged executable (optional, press Enter to skip): ")
    env_vars = input("Enter environment variables for the packaged executable (optional, format: var1=value1,var2=value2, press Enter to skip): ")
    python = input("Enter the path to a custom Python interpreter to bundle with the executable (optional, press Enter to skip): ")
    compress = input("Do you want to enable compression of bundled files? (y/n): ").lower() == 'y'
    hooks = input("Enter additional PyInstaller hooks (optional, press Enter to skip): ")
    bootloader = input("Enter the path to a custom bootloader file (optional, press Enter to skip): ")
    manifest = input("Enter the path to a custom manifest file (optional, press Enter to skip): ")
    splash = input("Enter the path to a splash screen file (optional, press Enter to skip): ")
    runtime_hooks = input("Enter the path to a runtime hooks file (optional, press Enter to skip): ")
    exe_format = input("Specify whether to generate a single executable ('exe') or a directory with bundled files ('directory'): ")
    system_path = input("Enter additional paths to include in the system PATH environment variable (optional, press Enter to skip): ")
    upx_level = input("Enter the UPX compression level (0-9, optional, press Enter to skip): ")
    eula = input("Enter the path to an End User License Agreement (EULA) file (optional, press Enter to skip): ")
    spec_file = input("Enter the path to a custom PyInstaller spec file (optional, press Enter to skip): ")
    runtime_hook_spec = input("Enter the path to a custom runtime hook specification (optional, press Enter to skip): ")
    template = input("Enter the path to a custom template directory for PyInstaller (optional, press Enter to skip): ")
    compile_pyc = input("Do you want to compile Python files into bytecode (.pyc) files? (y/n): ").lower() == 'y'
    icon_mac = input("Enter the path to a custom icon for the packaged executable on macOS (optional, press Enter to skip): ")
    package_data = input("Enter additional package data files (optional, press Enter to skip): ")
    build_mode = input("Specify whether to generate a debug or release build (optional, press Enter to skip): ")
    custom_hooks = input("Enter custom hooks directories (optional, press Enter to skip): ")
    custom_upx = input("Enter the path to a custom UPX binary (optional, press Enter to skip): ")
    bundle_stdlib = input("Do you want to bundle the standard library into the executable? (y/n): ").lower() == 'y'
    exclude = input("Enter custom exclusion patterns for file/directory inclusion (optional, press Enter to skip): ")
    bootloader_conf = input("Enter the path to a custom bootloader configuration file (optional, press Enter to skip): ")
    verbose = input("Do you want to enable verbose output during the packaging process? (y/n): ").lower() == 'y'
    external_modules = input("Enter external Python modules (optional, press Enter to skip): ")
    bundled_icon = input("Enter the path to a custom icon for the bundled files on Windows (optional, press Enter to skip): ")
    temp_dir = input("Enter a custom location for the PyInstaller temporary directory (optional, press Enter to skip): ")
    upx_conf = input("Enter the path to a custom UPX configuration file (optional, press Enter to skip): ")
    resource_files = input("Enter additional resource files (optional, press Enter to skip): ")
    app_name = input("Enter a custom app name for macOS bundles (optional, press Enter to skip): ")
    log_dir = input("Enter a custom output directory for logs (optional, press Enter to skip): ")
    app_version = input("Enter a custom version number for the bundled application (optional, press Enter to skip): ")
    additional_files = input("Enter additional files to be included in the application bundle (optional, press Enter to skip): ")
    user_hooks = input("Enter a custom path for user hooks (optional, press Enter to skip): ")
    file_version = input("Enter a custom file version for the bundled executable (optional, press Enter to skip): ")
    custom_library = input("Enter custom library files (optional, press Enter to skip): ")
    upx_path = input("Enter a custom path for UPX compression (optional, press Enter to skip): ")
    no_confirm = input("Do you want to skip confirmation prompts during packaging? (y/n): ").lower() == 'y'
    custom_commands = input("Enter additional custom commands for PyInstaller (optional, press Enter to skip): ")
    freeze_imports = input("Do you want to freeze imports and disable packing? (y/n): ").lower() == 'y'
    clean_build = input("Do you want to clean build directories before packaging? (y/n): ").lower() == 'y'
    warn_project_version = input("Do you want to enable warnings for project version mismatches? (y/n): ").lower() == 'y'
    warn_no_version = input("Do you want to enable warnings for missing version information? (y/n): ").lower() == 'y'
    name = input("Enter a custom name for the packaged executable (optional, press Enter to skip): ")

    package_project(
        selected_path, is_directory, output_dir, include, pyinstaller_args, output_name, clean, icon, hidden_imports,
        version, binaries, license, env_vars, python, compress, hooks, bootloader, manifest, splash, runtime_hooks,
        exe_format, system_path, upx_level, eula, spec_file, runtime_hook_spec, template, compile_pyc, icon_mac,
        package_data, build_mode, custom_hooks, custom_upx, bundle_stdlib, exclude, bootloader_conf, verbose,
        external_modules, bundled_icon, temp_dir, upx_conf, resource_files, app_name, log_dir, app_version,
        additional_files, user_hooks, file_version, custom_library, upx_path, no_confirm, custom_commands,
        freeze_imports, clean_build, warn_project_version, warn_no_version, name
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kynlos Python Packager")
    parser.add_argument("-w", "--wizard", action="store_true", help="Run the packaging process using a wizard")
    parser.add_argument('path', nargs='?', default=None, help='Path to the project or script to package')
    parser.add_argument("-d", "--directory", action="store_true", help="Flag to indicate if the path is a directory")
    parser.add_argument("-o", "--output-dir", help="Output directory for the packaged executable")
    parser.add_argument("-i", "--include", help="Additional files or directories to include in the package (format: source_path:destination_path)")
    parser.add_argument("-a", "--pyinstaller-args", help="Additional arguments to PyInstaller")
    parser.add_argument("-n", "--output-name", help="Custom name for the output executable")
    parser.add_argument("-c", "--clean", action="store_true", help="Clean build and dist directories before packaging")
    parser.add_argument("--icon", help="Icon file for the executable")
    parser.add_argument("--hidden-imports", help="Additional hidden imports")
    parser.add_argument("--version", help="Version information for the executable")
    parser.add_argument("--binaries", help="Additional binaries or data files to include")
    parser.add_argument("--license", help="Custom license file for the packaged executable")
    parser.add_argument("--env-vars", help="Environment variables for the packaged executable (comma-separated)")
    parser.add_argument("--python", help="Custom Python interpreter to bundle with the executable")
    parser.add_argument("--no-compress", dest="compress", action="store_false", help="Disable compression of bundled files")
    parser.add_argument("--hooks", help="Additional PyInstaller hooks")
    parser.add_argument("--bootloader", help="Custom bootloader file")
    parser.add_argument("--manifest", help="Custom manifest file")
    parser.add_argument("--splash", help="Splash screen file")
    parser.add_argument("--runtime-hooks", help="Runtime hooks file")
    parser.add_argument("--exe-format", choices=['exe', 'directory'], default='exe', help="Specify whether to generate a single executable ('exe') or a directory with bundled files ('directory')")
    parser.add_argument("--system-path", help="Additional paths to include in the system PATH environment variable")
    parser.add_argument("--upx-level", type=int, choices=range(0, 10), help="Specify the UPX compression level")
    parser.add_argument("--eula", help="End User License Agreement (EULA) file")
    parser.add_argument("--spec-file", help="Custom PyInstaller spec file")
    parser.add_argument("--runtime-hook-spec", help="Custom runtime hook specification")
    parser.add_argument("--template", help="Custom template directory for PyInstaller")
    parser.add_argument("--compile-pyc", action="store_true", help="Compile Python files into bytecode (.pyc) files")
    parser.add_argument("--icon-mac", help="Custom icon for the packaged executable on macOS")
    parser.add_argument("--package-data", help="Additional package data files")
    parser.add_argument("--build-mode", help="Specify whether to generate a debug or release build")
    parser.add_argument("--custom-hooks", help="Custom hooks directories")
    parser.add_argument("--custom-upx", help="Custom UPX binary")
    parser.add_argument("--bundle-stdlib", action="store_true", help="Bundle the standard library into the executable")
    parser.add_argument("--exclude", help="Custom exclusion patterns for file/directory inclusion")
    parser.add_argument("--bootloader-conf", help="Custom bootloader configuration file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output during the packaging process")
    parser.add_argument("--external-modules", help="External Python modules")
    parser.add_argument("--bundled-icon", help="Custom icon for the bundled files on Windows")
    parser.add_argument("--temp-dir", help="Custom location for the PyInstaller temporary directory")
    parser.add_argument("--upx-conf", help="Custom UPX configuration file")
    parser.add_argument("--resource-files", help="Additional resource files")
    parser.add_argument("--app-name", help="Custom app name for macOS bundles")
    parser.add_argument("--log-dir", help="Custom output directory for logs")
    parser.add_argument("--app-version", help="Custom version number for the bundled application")
    parser.add_argument("--additional-files", help="Additional files to be included in the application bundle")
    parser.add_argument("--user-hooks", help="Custom path for user hooks")
    parser.add_argument("--file-version", help="Custom file version for the bundled executable")
    parser.add_argument("--custom-library", help="Custom library files")
    parser.add_argument("--upx-path", help="Custom path for UPX compression")
    parser.add_argument("--no-confirm", action="store_true", help="Skip confirmation prompts during packaging")
    parser.add_argument("--custom-commands", help="Additional custom commands for PyInstaller")
    parser.add_argument("--freeze-imports", action="store_true", help="Freeze imports and disable packing")
    parser.add_argument("--clean-build", action="store_true", help="Clean build directories before packaging")
    parser.add_argument("--warn-project-version", action="store_true", help="Enable warnings for project version mismatches")
    parser.add_argument("--warn-no-version", action="store_true", help="Enable warnings for missing version information")
    parser.add_argument("--name", help="Custom name for the packaged executable")
    
    args = parser.parse_args()

    if args.wizard:
        # Run the wizard without requiring the path
        wizard()
    else:
        if args.path is None:
            parser.error("the following arguments are required: path")
        else:
            # Proceed with the normal packaging process using args.path
            package_project(
                args.path, args.directory, args.output_dir, args.include, args.pyinstaller_args, args.output_name,
                args.clean, args.icon, args.hidden_imports, args.version, args.binaries, args.license, args.env_vars,
                args.python, args.compress, args.hooks, args.bootloader, args.manifest, args.splash, args.runtime_hooks,
                args.exe_format, args.system_path, args.upx_level, args.eula, args.spec_file, args.runtime_hook_spec,
                args.template, args.compile_pyc, args.icon_mac, args.package_data, args.build_mode, args.custom_hooks,
                args.custom_upx, args.bundle_stdlib, args.exclude, args.bootloader_conf, args.verbose,
                args.external_modules, args.bundled_icon, args.temp_dir, args.upx_conf, args.resource_files, args.app_name,
                args.log_dir, args.app_version, args.additional_files, args.user_hooks, args.file_version,
                args.custom_library, args.upx_path, args.no_confirm, args.custom_commands, args.freeze_imports,
                args.clean_build, args.warn_project_version, args.warn_no_version, args.name
            )
