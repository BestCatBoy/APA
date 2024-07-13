; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{255E9875-8299-460C-8662-275EB50F36E3}
AppName=RIKOR APA
AppVersion=2.8.12
;AppVerName=RIKOR APA 2.8.12
AppPublisher=����������� ��������������� ������� ��. �.�. ��������
AppPublisherURL=https://arz.unn.ru/spo
AppSupportURL=https://arz.unn.ru/spo
AppUpdatesURL=https://arz.unn.ru/spo
DefaultDirName={pf}\RIKOR
DefaultGroupName=RIKOR APA
OutputDir=D:\Eclipse projects\APA 2.8.12\app\setup
OutputBaseFilename=APA.setup
SetupIconFile=D:\Eclipse projects\APA 2.8.12\images\rikor_ico.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Eclipse projects\APA 2.8.12\app\executable\run.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Eclipse projects\APA 2.8.12\app\executable\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\RIKOR APA"; Filename: "{app}\run.exe"
Name: "{commondesktop}\RIKOR APA"; Filename: "{app}\run.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\run.exe"; Description: "{cm:LaunchProgram,RIKOR APA}"; Flags: nowait postinstall skipifsilent

