# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'audio/', 'audio' ),
         ( 'res/', 'res' )
         ]

a = Analysis(['game1.py'],
             pathex=['/home/harshish/Documents/GAMES/Surakshit Karo'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Surakshit_Karo',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='game_icon.ico')
