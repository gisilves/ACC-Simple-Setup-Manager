; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "ACC Simple Setup Manager"
#define MyAppVersion "0.1"
#define MyAppURL "https://github.com/gisilves/ACC-Simple-Setup-Manager"
#define MyAppExeName "acc_simple_setup_manager.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{8C2724C9-2AA0-42AA-B5D0-D0D4F4025915}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=C:\Users\gigi\Downloads\ACC\ACC-Simple-Setup-Manager\LICENSE
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputBaseFilename=acc_simple_setup_manager
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\gigi\Downloads\ACC\ACC-Simple-Setup-Manager\build\exe.win-amd64-3.9\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\gigi\Downloads\ACC\ACC-Simple-Setup-Manager\build\exe.win-amd64-3.9\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\gigi\Downloads\ACC\ACC-Simple-Setup-Manager\build\exe.win-amd64-3.9\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\gigi\Downloads\ACC\ACC-Simple-Setup-Manager\build\exe.win-amd64-3.9\python39.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\gigi\Downloads\ACC\ACC-Simple-Setup-Manager\build\exe.win-amd64-3.9\vcruntime140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\gigi\Downloads\ACC\ACC-Simple-Setup-Manager\icon.ico"; DestDir: "{app}"; Flags: ignoreversion

; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

