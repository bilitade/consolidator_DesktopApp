# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('output.csv', '.'),
        ('branches.json', '.'),
        ('branches.json', '.'),
        ('districts.json', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ConsolidatorApp',
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
    icon='./icon.ico',
    description='Card Embossing file ConsolidatorApp App, Use Full to automate card identification packing , reporting  and merging embossing file ',  
    company_name='Cooperative Bank of Oromia',  
    copyright='© 2024 Cooperative Bank of Oromia. All rights reserved.',  
)
