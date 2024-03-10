# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/pythonProjectCovid19/main.py'],
             pathex=['D:\\pythonProjectCovid19'],
             binaries=[],
             datas=[('D:/pythonProjectCovid19/gui.ui', '.'), ('D:/pythonProjectCovid19/app.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\pythonProjectCovid19\\app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
