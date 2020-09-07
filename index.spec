# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['index.py'],
             pathex=['D:\\SOFT\\python\\projects\\6'],
             binaries=[('D:\\SOFT\\python\\projects\\6\\icon.ico', '.'), ('D:\\SOFT\\python\\projects\\6\\style.dll', '.')],
             datas=[('D:\\SOFT\\python\\projects\\6\\VLC', 'VLC/'), ('D:\\SOFT\\python\\projects\\6\\VLC', '.'), ('D:\\SOFT\\python\\projects\\6\\bklsn', 'bklsn/'), ('D:\\SOFT\\python\\projects\\6\\downloads', 'downloads/'), ('D:\\SOFT\\python\\projects\\6\\images', 'images/'), ('D:\\SOFT\\python\\projects\\6\\play_check', 'play_check/')],
             hiddenimports=['python-vlc'],
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
          name='index',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='index')
