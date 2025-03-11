from PyInstaller.utils.hooks import collect_submodules

hiddenimports = [
    *collect_submodules('django.contrib.admin'),
    *collect_submodules('django.contrib.auth'),
    *collect_submodules('django.template.loaders')
]