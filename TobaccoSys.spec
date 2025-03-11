# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 在顶部导入新增
from PyInstaller.utils.hooks import collect_submodules
import os
import django  # 新增django导入

# 在Analysis部分补充两个关键依赖
a = Analysis(
    ['c:\\Users\\75241\\Desktop\\AI_烟草出入库\\main.py'],
    pathex=['c:\\Users\\75241\\Desktop\\AI_烟草出入库'],
    binaries=[],
    datas=[
        ('inventory/templates/**', 'inventory/templates'),
        ('inventory/static/**', 'inventory/static'),
        ('db.sqlite3', '.'),
        ('config/settings.py', 'config'),
        (os.path.join(django.__path__[0], 'contrib/admin/templates/**'), 'django/contrib/admin/templates'),
        (os.path.join(django.__path__[0], 'contrib/admin/static/**'), 'django/contrib/admin/static')
    ],
    hiddenimports=[
        # 添加过滤条件排除gis模块
        *collect_submodules('django.contrib', filter=lambda name: 'gis' not in name),
        *collect_submodules('django.template'),
        'django.core.management',
        'django.core.cache'
    ],
    hookspath=['.'],
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
    name='TobaccoSys',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir='.',
    console=True,
)

# 移除底部所有额外配置
