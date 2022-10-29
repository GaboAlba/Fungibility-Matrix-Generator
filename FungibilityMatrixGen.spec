# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['TkGUI.py'],
    pathex=[],
    binaries=[],
    datas=[('Intel-logo-2022.png', 'icon'), ('Intel-logo-2022.ico', 'icon')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FungibilityMatrixGen',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\gfalbaro\\OneDrive - Intel Corporation\\Documents\\GitHub\\MyProjects\\Python\\Fungibility_Matrix_Generator\\Intel-logo-2022.png'],
)
