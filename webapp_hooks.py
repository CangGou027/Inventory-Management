from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = []
hiddenimports += collect_submodules('django.contrib.admin')
hiddenimports += collect_submodules('django.template.loaders')
datas = collect_data_files('django.contrib.admin')